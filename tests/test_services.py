from unittest.mock import Mock

import pytest

from francine.services.task import TaskService


@pytest.fixture
def mock():
    return Mock()


@pytest.fixture
def service(mock):
    return TaskService(mock)


def test_add_task(service, mock):
    service.add("Test")
    mock.add.assert_called_once()


def test_list_tasks(service, mock):
    service.list()
    mock.list.assert_called_once()


def test_complete_task(service, mock):
    service.complete()
    mock.remove.assert_called_once()


def test_flush_tasks(service, mock):
    service.flush()
    mock.flush.assert_called_once()
