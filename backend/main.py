from flask import Flask
from routes.appointment_routes import app
import sqlite3

def initialize_db():
    conn = sqlite3.connect('appointments.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS appointments
                      (id INTEGER PRIMARY KEY AUTOINCREMENT,
                      title TEXT NOT NULL,
                      start_time TEXT NOT NULL,
                      end_time TEXT NOT NULL,
                      description TEXT,
                      google_calendar_event_id TEXT);''')
    conn.commit()
    conn.close()

if __name__ == '__main__':
    initialize_db()
    app.run(debug=True)