from rbh.backend import BackendBash
from rbh.cmd.app import BaseApplication
from rbh.containers import BackendLogs
from rbh.containers import FrontendLogs
from rbh.containers import NginxLogs
from rbh.containers import RunBackendContainer
from rbh.containers import RunFrontendContainer
from rbh.containers import RunNginxContainer
from rbh.frontend import FrontendBash
from rbh.nginx import NginxBash


class ContainersApplication(BaseApplication):
    tasks = {
        'nginx': RunNginxContainer,
        'frontend': RunFrontendContainer,
        'backend': RunBackendContainer,
    }
    bashes = {
        'nginx': NginxBash,
        'frontend': FrontendBash,
        'backend': BackendBash,
    }
    logs = {
        'nginx': NginxLogs,
        'frontend': FrontendLogs,
        'backend': BackendLogs,
    }
    tasks_help = 'Start container'

    def _add_task_group(self):
        tasks = super()._add_task_group()

        tasks.add_argument(
            '-b',
            '--bash',
            dest='bash',
            help='Start bash under running container.',
            action="store_true",
        )

        tasks.add_argument(
            '-o',
            '--logs',
            dest='logs',
            help='Show logs of running container.',
            action="store_true",
        )

        return tasks

    def get_task(self, task, args):
        if args.bash:
            return self.bashes[task](self.core_cls())
        if args.logs:
            return self.logs[task](self.core_cls())
        else:
            return self.tasks[task](self.core_cls())
