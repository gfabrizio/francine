from datetime import datetime


class Task:
    def __init__(self, description: str, timestamp: datetime = datetime.now()):
        self.description = description
        self.timestamp = timestamp
