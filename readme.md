# 🧠 AI-Powered Web Change Monitor & Summarizer

A smart web monitoring tool that tracks changes in web content, detects updates using SHA256 hashing, alerts users via console, and generates summaries of changes using OpenAI API. This project showcases full-stack development with a Flask backend, PostgreSQL database, and a simple HTML frontend, built as a portfolio piece.

---

## ✨ Features

- Add multiple websites for monitoring via a web interface.
- Detects content changes using SHA256 hashing.
- Sends alerts to the console when changes are detected.
- Generates summaries of changes using a OpenAI API.
- Stores website data in PostgreSQL for persistence.
- Simple, clean frontend with a form and table for user interaction.

---

## 🛠️ Tech Stack

- **Backend**: Python, Flask  
- **Frontend**: HTML  
- **Libraries**:
  - `requests`, `hashlib`, `schedule` for monitoring and change detection
  - `BeautifulSoup`, `lxml` for web scraping
  - `psycopg2` for PostgreSQL integration
- **Database**: PostgreSQL  


---

## 📁 Project Structure

```
web-change-monitor/
├── app/
│   ├── monitor.py         # Handles website tracking & hashing
│   ├── summarizer.py      #  OpenAI API summarizer
│   ├── notifier.py        # Console alerts
│   └── utils.py           # Helper functions
├── templates/
│   └── index.html         # Frontend interface
├── main.py                # Entry point
├── requirements.txt       # Dependencies
├── .gitignore             # Git ignore file
└── README.md              # This file
```

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/web-change-monitor.git
cd web-change-monitor
```

### 2. Create a Virtual Environment and Install Dependencies

```bash
python -m venv venv
# On macOS/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate

pip install -r requirements.txt
```

### 3. Set Up PostgreSQL

- Install PostgreSQL and create a database named `webmonitor`:
```bash
createdb webmonitor
```

### 4. Set Environment Variables

**Option A: In terminal**
```bash
export DB_NAME=webmonitor
export DB_USER=your_postgres_user
export DB_PASSWORD=your_postgres_password
export DB_HOST=localhost
export DB_PORT=5432
export OPENAI_API_KEY=sk-api-key-1234567890
```

**Option B: Create a `.env` file**
```
DB_NAME=webmonitor
DB_USER=your_postgres_user
DB_PASSWORD=your_postgres_password
DB_HOST=localhost
DB_PORT=5432
OPENAI_API_KEY=sk-api-key-1234567890
```

### 5. Run the Application

```bash
python main.py
```

Open your browser and navigate to:  
📍 `http://localhost:5000`

---

## 🚀 Usage

- **Add Websites**: Enter a website URL (e.g., `https://example.com`) and click **"Add Website"**
- **Monitor Changes**: System checks every 60 seconds using SHA256 hashing
- **View Alerts**: Console shows changes + summary from  OpenAI API
- **View Monitored Sites**: Table shows URLs, current hash, and recent content

---

## 🔮 Future Improvements
- Add email alerts using SMTP
- Build interactive frontend with React
- Monitor specific HTML/DOM elements only
---