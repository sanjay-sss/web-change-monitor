import requests
import hashlib
from bs4 import BeautifulSoup
import psycopg2
from psycopg2 import pool
import os

# Reuse the same connection pool
db_pool = psycopg2.pool.SimpleConnectionPool(
    1, 20,
    dbname=os.getenv("DB_NAME", "webmonitor"),
    user=os.getenv("DB_USER", "postgres"),
    password=os.getenv("DB_PASSWORD", "password"),
    host=os.getenv("DB_HOST", "localhost"),
    port=os.getenv("DB_PORT", "5432")
)

def get_website_content(url):
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'lxml')
        return soup.get_text(strip=True)
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return None

def compute_hash(content):
    if content:
        return hashlib.sha256(content.encode('utf-8')).hexdigest()
    return ""

def check_website_changes(url):
    content = get_website_content(url)
    if not content:
        return None, None, None

    new_hash = compute_hash(content)
    conn = db_pool.getconn()
    try:
        with conn.cursor() as c:
            c.execute("SELECT hash, last_content FROM websites WHERE url = %s", (url,))
            result = c.fetchone()
            if result and result[0] == new_hash:
                return None, new_hash, content  # No changes
            else:
                changes = "New content detected" if not result else f"Content changed from: {result[1][:100]}... to: {content[:100]}..."
                c.execute("UPDATE websites SET hash = %s, last_content = %s WHERE url = %s",
                          (new_hash, content, url))
                conn.commit()
                return changes, new_hash, content
    finally:
        db_pool.putconn(conn)