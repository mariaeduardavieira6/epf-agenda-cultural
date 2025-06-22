import uuid

class Event:
    def __init__(self, title, description, date, location, capacity, id = None):
        self.id = id or str(uuid.uuid4())
        self.title = title
        self.description = description
        self.date = date
        self.location = location
        self.capacity = capacity

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "date": self.date,
            "location": self.location,
            "capacity": self.capacity
        }
    
    @staticmethod
    def from_dict(data):
        return Event(
            id = data.get("id"),
            title = data.get("title"),
            description = data.get("description"),
            date = data.get("date"),
            location = data.get("location"),
            capacity = data.get("capacity")
        )