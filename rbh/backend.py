from rbh.containers import RunBackendContainer
from rbh.docker import ContainerCommand


class BackendContainerCommand(ContainerCommand):

    def create_dependecies(self):
        super().create_dependecies()
        self.run_before(RunBackendContainer())


class BackendShell(BackendContainerCommand):
    container_name = 'backend'
    command = 'backend -t shell'


class BackendPytest(BackendContainerCommand):
    show_command_errors = False
    container_name = 'backend'
    command = 'btest'
