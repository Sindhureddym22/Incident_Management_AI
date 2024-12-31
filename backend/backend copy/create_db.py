import sqlite3

# Create a new SQLite database (or connect to an existing one)
conn = sqlite3.connect('db/support_tickets.db')
cursor = conn.cursor()

# Create the tickets table
cursor.execute('''
CREATE TABLE IF NOT EXISTS tickets (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    query TEXT UNIQUE,
    response TEXT
)
''')

# Insert sample data
sample_data = [
    ("How do I reset my password?", "To reset your password, go to the login page and click on 'Forgot Password'. Follow the instructions sent to your email."),
    ("What is the status of my ticket?", "You can check the status of your ticket by logging into your account and navigating to the 'My Tickets' section."),
    ("How do I update my profile?", "To update your profile, log in to your account, go to 'Settings', and make the necessary changes."),
    ("How do I contact support?", "You can contact support by emailing support@example.com or by using the live chat feature on our website."),
    ("What are the system requirements?", "The system requirements are listed on our website under the 'Support' section."),
    ("Unable to login", "Please check your username and password. If you have forgotten your password, use the 'Forgot Password' link."),
    ("Application crashes on startup", "Try clearing the application cache and restarting your device. If the issue persists, reinstall the application."),
    ("Slow performance", "Ensure that your device meets the minimum system requirements and close any unnecessary applications running in the background.")
]

# Insert data into the tickets table
cursor.executemany('INSERT OR IGNORE INTO tickets (query, response) VALUES (?, ?)', sample_data)

# Commit changes and close the connection
conn.commit()
conn.close()