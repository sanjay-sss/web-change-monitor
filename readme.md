AI-Powered Web Change Monitor & Summarizer
A smart web monitoring tool that tracks changes in web content, detects updates using SHA256 hashing, and generates summaries of changes using OpenAI's API (mocked for demo). Built as a portfolio project to showcase full-stack development and integration with modern APIs.
Features

Add multiple websites for monitoring via a web interface.
Detects content changes using SHA256 hashing.
Sends alerts to the console when changes are detected.
Generates summaries of changes using OpenAI API (mock implementation for demo).
Stores website data in PostgreSQL.

Tech Stack

Backend: Python, Flask
Frontend: HTML
Libraries:
requests, hashlib, schedule
BeautifulSoup, lxml for web scraping
psycopg2 for PostgreSQL


Database: PostgreSQL

Setup Instructions

Clone the repository:git clone https://github.com/your-username/web-change-monitor.git
cd web-change-monitor


Create a virtual environment and install dependencies:python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt


Set up PostgreSQL:
Install PostgreSQL and create a database named webmonitor.
Update environment variables in a .env file or shell:export DB_NAME=webmonitor
export DB_USER=your_postgres_user
export DB_PASSWORD=your_postgres_password
export DB_HOST=localhost
export DB_PORT=5432
export OPENAI_API_KEY=your_openai_api_key




Run the application:python main.py


Open your browser and navigate to http://localhost:5000.

Usage

Enter a website URL in the input field and click "Add Website".
The system monitors added websites every 60 seconds for changes.
Changes are detected via SHA256 hash comparison and logged to the console with a summary.
View the list of monitored websites and their current hash/content preview in the table.

Project Structure
web-change-monitor/
├── app/
│   ├── monitor.py         # Handles website tracking & hashing
│   ├── summarizer.py      # Mock OpenAI API summarizer
│   ├── notifier.py        # Console alerts
│   └── utils.py           # Helper functions
├── templates/
│   └── index.html         # Frontend interface
├── main.py                # Entry point
├── requirements.txt       # Dependencies
├── README.md              # This file

Deployment

Render/Vercel: Update main.py to bind to 0.0.0.0 and the provided port (e.g., os.environ.get('PORT')).
Configure PostgreSQL on a cloud provider (e.g., Render's managed PostgreSQL).
Set environment variables for DB_* and OPENAI_API_KEY in the deployment platform.
For production, replace the mock OpenAI API call in summarizer.py with a real API request.

Future Improvements

Replace mock OpenAI API with a real implementation.
Add email notifications via SMTP.
Enhance frontend with React for better interactivity.
Support more advanced change detection (e.g., specific DOM elements).

License
MIT License
