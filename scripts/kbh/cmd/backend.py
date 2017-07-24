from kbh.cmd.app import BaseApplication
from kbh.containers import BackendShell


class BackendApplication(BaseApplication):
    tasks = {
        'shell': BackendShell,
    }
    tasks_help = 'Commands'
