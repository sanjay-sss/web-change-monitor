from flask import Flask, render_template, request, jsonify
import psycopg2
from psycopg2 import pool
from app.monitor import check_website_changes
from app.notifier import send_console_alert
from app.summarizer import summarize_changes
import schedule
import time
import threading
import os

app = Flask(__name__)

# Initialize PostgreSQL connection pool
db_pool = psycopg2.pool.SimpleConnectionPool(
    1, 20,
    dbname=os.getenv("DB_NAME", "webmonitor"),
    user=os.getenv("DB_USER", "postgres"),
    password=os.getenv("DB_PASSWORD", "password"),
    host=os.getenv("DB_HOST", "localhost"),
    port=os.getenv("DB_PORT", "5432")
)

def init_db():
    conn = db_pool.getconn()
    try:
        with conn.cursor() as c:
            c.execute('''CREATE TABLE IF NOT EXISTS websites
                         (url TEXT PRIMARY KEY, hash TEXT, last_content TEXT)''')
            conn.commit()
    finally:
        db_pool.putconn(conn)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add', methods=['POST'])
def add_website():
    url = request.form.get('url')
    if not url:
        return jsonify({'error': 'URL is required'}), 400
    try:
        conn = db_pool.getconn()
        try:
            with conn.cursor() as c:
                c.execute("INSERT INTO websites (url, hash, last_content) VALUES (%s, %s, %s) ON CONFLICT (url) DO NOTHING",
                          (url, '', ''))
                conn.commit()
            return jsonify({'message': f'Added {url} for monitoring'})
        finally:
            db_pool.putconn(conn)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/websites', methods=['GET'])
def get_websites():
    try:
        conn = db_pool.getconn()
        try:
            with conn.cursor() as c:
                c.execute("SELECT url, hash, last_content FROM websites")
                websites = [{'url': row[0], 'hash': row[1], 'last_content': row[2]} for row in c.fetchall()]
            return jsonify(websites)
        finally:
            db_pool.putconn(conn)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

def run_monitor():
    schedule.every(60).seconds.do(check_and_notify)
    while True:
        schedule.run_pending()
        time.sleep(1)

def check_and_notify():
    conn = db_pool.getconn()
    try:
        with conn.cursor() as c:
            c.execute("SELECT url FROM websites")
            urls = [row[0] for row in c.fetchall()]
    finally:
        db_pool.putconn(conn)
    for url in urls:
        changes, new_hash, new_content = check_website_changes(url)
        if changes:
            summary = summarize_changes(changes)
            send_console_alert(url, summary)

if __name__ == '__main__':
    init_db()
    threading.Thread(target=run_monitor, daemon=True).start()
    app.run(debug=True)