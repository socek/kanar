from rbh.cmd.app import BaseApplication
from rbh.containers import RunBackendContainer
from rbh.containers import RunFrontendContainer
from rbh.containers import RunNginxContainer


class ContainersApplication(BaseApplication):
    tasks = {
        'nginx': RunNginxContainer,
        'frontend': RunFrontendContainer,
        'backend': RunBackendContainer,
    }
    tasks_help = 'Start container'
