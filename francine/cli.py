import click

from francine.repositories.tinydb import TinyDBRepository
from francine.services.task import TaskService

repository = TinyDBRepository()
service = TaskService(repository)


@click.group()
def cli():
    pass


@click.command()
@click.argument("description")
def add(description):
    service.add(description)
    click.echo(f"Task added: {description}")


@click.command()
def list():
    tasks = service.list()
    for number, task in enumerate(tasks):
        click.echo(f"{number} - {task.description}")


@click.command()
def complete():
    service.complete()
    click.echo("Task completed")


@click.command()
def flush():
    service.flush()
    click.echo("Old tasks flushed")


cli.add_command(add)
cli.add_command(list)
cli.add_command(complete)
cli.add_command(flush)

if __name__ == "__main__":
    cli()
