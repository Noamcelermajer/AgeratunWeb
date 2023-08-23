from flask import Flask, jsonify
from datetime import datetime, timedelta
import sqlite3
import threading

app = Flask(__name__)
DB_NAME = "unavailable_dates.db"

def create_table():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS unavailable_dates (date_time TEXT UNIQUE)""")
    conn.commit()
    conn.close()

def add_unavailable_date(date_time):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("INSERT OR IGNORE INTO unavailable_dates (date_time) VALUES (?)", (date_time,))
    conn.commit()
    conn.close()

def remove_expired_dates():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM unavailable_dates WHERE date_time < datetime('now')")
    conn.commit()
    conn.close()

def get_unavailable_dates():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT date_time FROM unavailable_dates")
    dates = [row[0] for row in cursor.fetchall()]
    conn.close()
    return dates

def schedule_cleanup():
    threading.Timer(3600, schedule_cleanup).start()  # Run every hour
    remove_expired_dates()

@app.route('/fetch-unavailable-dates', methods=['GET'])
def fetch_unavailable_dates():
    dates = get_unavailable_dates()
    return jsonify(dates)

@app.route('/schedule-meeting', methods=['POST'])
def schedule_meeting():
    date_time = request.json['date_time']
    add_unavailable_date(date_time)
    return jsonify({'message': 'Meeting scheduled successfully!'})

if __name__ == '__main__':
    create_table()
    schedule_cleanup()
    app.run(debug=True, host='localhost', port=5000)
