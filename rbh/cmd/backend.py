from rbh.cmd.app import BaseApplication
from rbh.backend import BackendShell


class BackendApplication(BaseApplication):
    tasks = {
        'shell': BackendShell,
    }
    tasks_help = 'Commands'
