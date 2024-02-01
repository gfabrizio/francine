from datetime import datetime, timedelta

from tinydb import Query, TinyDB

from francine.config import get_db_path
from francine.models.task import Task
from francine.repositories.base import BaseRepostitory

db_path = get_db_path()


class TinyDBRepository(BaseRepostitory):
    def __init__(self):
        self.db = TinyDB(db_path)
        self.query = Query()

    def add(self, task: Task):
        self.db.insert(
            {"description": task.description, "timestamp": task.timestamp.isoformat()}
        )

    def list(self):
        return [
            Task(item["description"], datetime.fromisoformat(item["timestamp"]))
            for item in self.db.all()
        ]

    def get(self):
        return [
            Task(item["description"], datetime.fromisoformat(item["timestamp"]))
            for item in [self.db.all()[0]]
        ]

    def remove(self):
        doc_id = self.db.all()[0].doc_id
        self.db.remove(
            doc_ids=[
                doc_id,
            ]
        )
        return [
            Task(item["description"], datetime.fromisoformat(item["timestamp"]))
            for item in self.db.all()
        ]

    def flush(self):
        diff = datetime.now() - timedelta(days=1)
        self.db.remove(self.query.timestamp < diff.isoformat())
