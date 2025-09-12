🛍️ MarketHub

MarketHub is a web-based marketplace built with Flask and SQLite.
It allows users to register, log in, browse items, purchase items, and manage owned items securely.

🚀 Features

User registration & login (with password hashing 🔐)

View available marketplace items

Buy & Sell items

Secure authentication using Flask-Login

Uses SQLite database (no setup needed)

🛠️ Tech Stack

Backend: Flask, Flask-WTF, Flask-SQLAlchemy, Flask-Bcrypt

Database: SQLite (instance/market.db)

Frontend: HTML, CSS, Jinja2 Templates

📂 Project Structure
MarketHub/
│── run.py              # Main entry point
│── market/             # Flask application (routes, models, forms)
│   ├── routes.py
│   ├── models.py
│   ├── forms.py
│   ├── templates/      # HTML templates
│── instance/
│   └── market.db       # SQLite database
│── requirements.txt    # Dependencies

🙌 Author

👩‍💻 Developed by Tanya Jhaveri
