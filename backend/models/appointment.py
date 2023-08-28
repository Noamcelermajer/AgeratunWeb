from datetime import datetime
APPOINTMENT_DURATION_MINUTES = 15  # Can be changed easily later

class Appointment:
    def __init__(self, id, title, start_time, end_time, description):
        self.id = id
        self.title = title
        self.start_time = start_time
        self.end_time = end_time
        self.description = description

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "start_time": self.start_time.isoformat(),
            "end_time": self.end_time.isoformat(),
            "description": self.description,
        }
