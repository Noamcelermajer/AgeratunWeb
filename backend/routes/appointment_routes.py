from flask import Flask, jsonify, request
from datetime import datetime,timedelta
from models.appointment import APPOINTMENT_DURATION_MINUTES
from models.appointment import Appointment
from google_calendar_helper import init_google_calendar_api, create_google_calendar_event,update_google_calendar_event, delete_google_calendar_event

app = Flask(__name__)
appointments = []
google_calendar_service = init_google_calendar_api()

@app.route("/appointments", methods=["GET"])
def get_appointments():
    return jsonify([a.to_dict() for a in appointments])

@app.route("/appointments", methods=["POST"])
def create_appointment():
    data = request.json
    start_time = datetime.fromisoformat(data["start_time"])
    end_time = start_time + timedelta(minutes=APPOINTMENT_DURATION_MINUTES)  # Automatically set end time

    new_appointment = Appointment(
        id=len(appointments) + 1,
        title=data["title"],
        start_time=start_time.isoformat(),
        end_time=end_time.isoformat(),
        description=data["description"]
    )

    google_calendar_event_id = create_google_calendar_event(google_calendar_service, new_appointment)
    new_appointment.google_calendar_event_id = google_calendar_event_id
    appointments.append(new_appointment)
    return jsonify(new_appointment.to_dict()), 201

@app.route("/appointments/<int:id>", methods=["PUT"])
def update_appointment(id):
    appointment = next((a for a in appointments if a.id == id), None)
    if appointment is None:
        return jsonify({"error": "Appointment not found"}), 404
    
    data = request.json
    appointment.title = data.get("title", appointment.title)
    appointment.start_time = datetime.fromisoformat(data.get("start_time", appointment.start_time.isoformat()))
    appointment.end_time = datetime.fromisoformat(data.get("end_time", appointment.end_time.isoformat()))
    appointment.description = data.get("description", appointment.description)
    
    update_google_calendar_event(google_calendar_service, appointment)
    
    return jsonify(appointment.to_dict())

@app.route("/appointments/<int:id>", methods=["DELETE"])
def delete_appointment(id):
    appointment = next((a for a in appointments if a.id == id), None)
    if appointment is None:
        return jsonify({"error": "Appointment not found"}), 404
    
    delete_google_calendar_event(google_calendar_service, appointment)
    
    global appointments
    appointments = [a for a in appointments if a.id != id]
    
    return jsonify({"result": "Appointment deleted"})
