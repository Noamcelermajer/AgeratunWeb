from google.oauth2 import service_account
from googleapiclient.discovery import build
import datetime

def init_google_calendar_api():
    credentials = service_account.Credentials.from_service_account_file(
        "path/to/credentials.json", 
        scopes=["https://www.googleapis.com/auth/calendar"]
    )
    return build("calendar", "v3", credentials=credentials)

def create_google_calendar_event(service, appointment):
    start_time = datetime.datetime.fromisoformat(appointment.start_time)
    end_time = datetime.datetime.fromisoformat(appointment.end_time)

    event = {
        "summary": appointment.title,
        "description": appointment.description,
        "start": {"dateTime": start_time, "timeZone": "UTC"},
        "end": {"dateTime": end_time, "timeZone": "UTC"},
    }

    created_event = service.events().insert(
        calendarId="primary", body=event
    ).execute()

    return created_event["id"]

# Add functions for updating and deleting Google Calendar events here
