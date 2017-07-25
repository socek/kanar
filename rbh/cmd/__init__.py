from sys import argv

from rbh.backend import BackendAlembic
from rbh.backend import BackendPytest
from rbh.cmd.backend import BackendApplication
from rbh.cmd.containers import ContainersApplication
from rbh.core import KbhCore


def containers():
    ContainersApplication().run()


def backend():
    BackendApplication().run()


def pytest():
    BackendPytest(KbhCore()).run(argv[1:])


def alembic():
    BackendAlembic(KbhCore()).run(argv[1:])
