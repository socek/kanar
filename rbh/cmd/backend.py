from rbh.cmd.app import BaseApplication
from rbh.containers import BackendShell


class BackendApplication(BaseApplication):
    tasks = {
        'shell': BackendShell,
    }
    tasks_help = 'Commands'
