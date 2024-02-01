from datetime import datetime, timedelta

import pytest

from francine.models.task import Task
from francine.repositories.tinydb import TinyDBRepository


@pytest.fixture
def repository():
    TinyDBRepository().db.truncate()
    return TinyDBRepository()


def test_add_task(repository):
    task = Task("Test Add")
    repository.add(task)
    assert len(repository.list()) == 1


def test_get_task(repository):
    task = Task("Test Get")
    repository.add(task)
    assert repository.get().description == "Test Get"


def test_flush_old_tasks(repository):
    old_task = Task("Old", datetime.now() - timedelta(days=2))
    new_task = Task("New")
    repository.add(old_task)
    repository.add(new_task)
    repository.flush()
    tasks = repository.list()
    assert len(tasks) == 1
    assert tasks[0].description == "New"


def test_remove_task(repository):
    repository.flush()
    task = Task("Test")
    repository.add(task)
    repository.remove()
    assert len(repository.list()) == 0
