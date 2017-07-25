from rbh.containers import RunFrontendContainer
from rbh.docker import ContainerCommand


class FrontendContainerCommand(ContainerCommand):
    container_name = 'frontend'

    def create_dependecies(self):
        super().create_dependecies()
        self.run_before(RunFrontendContainer())


class FrontendBash(FrontendContainerCommand):
    command = 'bash'
