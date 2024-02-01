from francine.models.task import Task
from francine.repositories.tinydb import TinyDBRepository


class TaskService:
    def __init__(self, repository: TinyDBRepository):
        self.repository = repository

    def add(self, description: str):
        task = Task(description)
        self.repository.add(task)

    def list(self):
        return self.repository.list()

    def complete(self):
        self.repository.remove()

    def flush(self):
        self.repository.flush()
