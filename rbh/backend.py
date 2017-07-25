from rbh.containers import RunBackendContainer
from rbh.docker import ContainerCommand


class BackendContainerCommand(ContainerCommand):
    container_name = 'backend'

    def create_dependecies(self):
        super().create_dependecies()
        self.run_before(RunBackendContainer())


class BackendShell(BackendContainerCommand):
    command = 'backend -t shell'


class BackendPytest(BackendContainerCommand):
    show_command_errors = False
    command = 'btest'


class BackendAlembic(BackendContainerCommand):
    show_command_errors = False
    command = 'balembic'


class BackendBash(BackendContainerCommand):
    command = 'bash'
