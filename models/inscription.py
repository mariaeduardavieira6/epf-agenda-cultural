class Inscription:
    def __init__(self, id, user_id, event_id):
        self.id = id
        self.user_id = user_id
        self.event_id = event_id

    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "event_id": self.event_id
        }