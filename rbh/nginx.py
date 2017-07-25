from rbh.containers import RunNginxContainer
from rbh.docker import ContainerCommand


class NginxContainerCommand(ContainerCommand):
    container_name = 'nginx'

    def create_dependecies(self):
        super().create_dependecies()
        self.run_before(RunNginxContainer())


class NginxBash(NginxContainerCommand):
    command = 'bash'
