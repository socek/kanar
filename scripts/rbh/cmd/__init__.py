from rbh.cmd.backend import BackendApplication
from rbh.cmd.containers import ContainersApplication


def containers():
    ContainersApplication().run()


def backend():
    BackendApplication().run()
