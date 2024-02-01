import click

from francine.repositories.tinydb import TinyDBRepository
from francine.services.task import TaskService

repository = TinyDBRepository()
service = TaskService(repository)


@click.group()
def francine():
    """Francine helps you to track your short daily goals on track"""
    pass


@click.command()
@click.argument("description")
def add(description):
    """# adds a task for your list (francine add "task")"""
    service.flush()
    service.add(description)
    click.echo(f"Task added: {description}")


@click.command()
def get():
    """# shows the current task"""
    task = service.get()
    click.echo(f"Task: {task.description}")


@click.command()
def list():
    """# show all your last 24 hours task"""
    service.flush()
    tasks = service.list()
    for number, task in enumerate(tasks):
        click.echo(f"{number} - {task.description}")


@click.command()
def complete():
    """# completes the current task"""
    service.complete()
    click.echo("Task completed")


francine.add_command(add)
francine.add_command(get)
francine.add_command(list)
francine.add_command(complete)

if __name__ == "__main__":
    francine()
