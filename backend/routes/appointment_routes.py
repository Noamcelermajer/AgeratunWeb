from flask import Flask, jsonify, request, make_response
from models.appointment import Appointment
from google_calendar_helper import init_google_calendar_api, create_google_calendar_event, update_google_calendar_event, delete_google_calendar_event
import sqlite3
from datetime import datetime, timedelta

app = Flask(__name__)
google_calendar_service = init_google_calendar_api()

def get_db():
    conn = sqlite3.connect('appointments.db')
    return conn

@app.route("/appointments", methods=["GET"])
def get_appointments():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM appointments")
    rows = cursor.fetchall()
    conn.close()

    appointments = [Appointment(*row).to_dict() for row in rows]
    return jsonify(appointments)

@app.route("/appointments", methods=["POST"])
def create_appointment():
    try:
        data = request.json
        start_time = datetime.fromisoformat(data["start_time"])
        end_time = start_time + timedelta(minutes=15)  # Automatically set end time based on your requirement

        new_appointment = Appointment(
            id=None,
            title=data["title"],
            start_time=start_time.isoformat(),
            end_time=end_time.isoformat(),
            description=data["description"]
        )

        google_calendar_event_id = create_google_calendar_event(google_calendar_service, new_appointment)
        new_appointment.google_calendar_event_id = google_calendar_event_id

        conn = get_db()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO appointments (title, start_time, end_time, description, google_calendar_event_id) VALUES (?, ?, ?, ?, ?)",
                       (new_appointment.title, new_appointment.start_time, new_appointment.end_time, new_appointment.description, new_appointment.google_calendar_event_id))
        conn.commit()
        conn.close()

        return jsonify(new_appointment.to_dict()), 201

    except Exception as e:
        return make_response(jsonify({"error": str(e)}), 400)

@app.route("/appointments/<int:id>", methods=["PUT"])
def update_appointment(id):
    try:
        data = request.json
        conn = get_db()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM appointments WHERE id=?", (id,))
        row = cursor.fetchone()

        if row is None:
            return make_response(jsonify({"error": "Appointment not found"}), 404)

        appointment = Appointment(*row)

        # Updating the appointment
        appointment.title = data.get("title", appointment.title)
        appointment.start_time = datetime.fromisoformat(data.get("start_time", appointment.start_time))
        appointment.end_time = datetime.fromisoformat(data.get("end_time", appointment.end_time))
        appointment.description = data.get("description", appointment.description)

        # Update Google Calendar Event
        update_google_calendar_event(google_calendar_service, appointment)

        # Update the database
        cursor.execute("UPDATE appointments SET title=?, start_time=?, end_time=?, description=? WHERE id=?",
                       (appointment.title, appointment.start_time, appointment.end_time, appointment.description, id))
        conn.commit()
        conn.close()

        return jsonify(appointment.to_dict())

    except Exception as e:
        return make_response(jsonify({"error": str(e)}), 400)

@app.route("/appointments/<int:id>", methods=["DELETE"])
def delete_appointment(id):
    try:
        conn = get_db()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM appointments WHERE id=?", (id,))
        row = cursor.fetchone()

        if row is None:
            return make_response(jsonify({"error": "Appointment not found"}), 404)

        appointment = Appointment(*row)

        # Delete Google Calendar Event
        delete_google_calendar_event(google_calendar_service, appointment)

        # Delete from the database
        cursor.execute("DELETE FROM appointments WHERE id=?", (id,))
        conn.commit()
        conn.close()

        return jsonify({"result": "Appointment deleted"})

    except Exception as e:
        return make_response(jsonify({"error": str(e)}), 400)
