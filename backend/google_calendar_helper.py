from google.oauth2 import service_account
from googleapiclient.discovery import build
import datetime

def init_google_calendar_api():
    credentials = service_account.Credentials.from_service_account_file(
        "credentials\\backcalendar-3c62b1ff5ffc.json", 
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

def update_google_calendar_event(service, appointment):
    event = service.events().get(calendarId='primary', eventId=appointment.google_calendar_event_id).execute()

    event['summary'] = appointment.title
    event['description'] = appointment.description
    event['start']['dateTime'] = appointment.start_time.isoformat()
    event['end']['dateTime'] = appointment.end_time.isoformat()

    updated_event = service.events().update(calendarId='primary', eventId=event['id'], body=event).execute()

    return updated_event["id"]

def delete_google_calendar_event(service, appointment):
    service.events().delete(calendarId='primary', eventId=appointment.google_calendar_event_id).execute()