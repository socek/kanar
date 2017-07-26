from baelfire.dependencies import FileChanged

from rbh.docker import ContainerBuilder
from rbh.docker import ContainerLogs
from rbh.docker import ContainerRunner


class BackendContainerBuild(ContainerBuilder):
    output_name = 'backend:dockerfile_flag'
    container_name = 'backend'

    def create_dependecies(self):
        super().create_dependecies()

        self.build_if(FileChanged('backend:requirements:dev'))
        self.build_if(FileChanged('backend:setuppy'))


class FrontendContainerBuild(ContainerBuilder):
    output_name = 'frontend:dockerfile_flag'
    container_name = 'frontend'

    def create_dependecies(self):
        super().create_dependecies()

        self.build_if(FileChanged('frontend:packages'))


class NginxContainerBuild(ContainerBuilder):
    output_name = 'nginx:dockerfile_flag'
    container_name = 'nginx'

    def create_dependecies(self):
        super().create_dependecies()

        self.build_if(FileChanged('nginx:conf'))


class RunBackendContainer(ContainerRunner):
    container_name = 'backend'
    image_name = 'rotarran_backend'

    def create_dependecies(self):
        super().create_dependecies()
        self.run_before(BackendContainerBuild())


class RunFrontendContainer(ContainerRunner):
    container_name = 'frontend'
    image_name = 'rotarran_frontend'

    def create_dependecies(self):
        super().create_dependecies()
        self.run_before(FrontendContainerBuild())


class RunNginxContainer(ContainerRunner):
    container_name = 'nginx'
    image_name = 'rotarran_nginx'

    def create_dependecies(self):
        super().create_dependecies()
        self.run_before(BackendContainerBuild())
        self.run_before(FrontendContainerBuild())
        self.run_before(NginxContainerBuild())


class NginxLogs(ContainerLogs):
    container_name = 'nginx'

    def create_dependecies(self):
        super().create_dependecies()
        self.run_before(RunNginxContainer())


class BackendLogs(ContainerLogs):
    container_name = 'backend'

    def create_dependecies(self):
        super().create_dependecies()
        self.run_before(RunBackendContainer())


class FrontendLogs(ContainerLogs):
    container_name = 'frontend'

    def create_dependecies(self):
        super().create_dependecies()
        self.run_before(RunFrontendContainer())
