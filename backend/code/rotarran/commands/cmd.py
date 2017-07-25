from sys import argv

from rotarran.commands.alembic import AlembicCommand
from rotarran.commands.app import BakendApplication
from rotarran.commands.core import BackendCore
from rotarran.commands.pytest import PyTest


def backend():
    BakendApplication().run()


def alembic():
    AlembicCommand(BackendCore()).run(argv[1:])


def pytest():
    PyTest(BackendCore()).run(argv[1:])
