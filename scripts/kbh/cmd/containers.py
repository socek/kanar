from kbh.cmd.app import BaseApplication
from kbh.containers import RunBackendContainer
from kbh.containers import RunFrontendContainer
from kbh.containers import RunNginxContainer


class ContainersApplication(BaseApplication):
    tasks = {
        'nginx': RunNginxContainer,
        'frontend': RunFrontendContainer,
        'backend': RunBackendContainer,
    }
    tasks_help = 'Start container'
