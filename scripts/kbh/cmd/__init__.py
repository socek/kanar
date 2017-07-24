from kbh.cmd.backend import BackendApplication
from kbh.cmd.containers import ContainersApplication


def containers():
    ContainersApplication().run()


def backend():
    BackendApplication().run()
