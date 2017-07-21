from baelfire.dependencies import AlwaysTrue
from baelfire.dependencies import FileChanged
from baelfire.dependencies import TaskRebuilded

from kbh.docker import ContainerBuilder
from kbh.docker import ContainerCommand
from kbh.docker import ContainerRunner


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

    def create_dependecies(self):
        self.build_if(TaskRebuilded(BackendContainerBuild()))
        self.build_if(AlwaysTrue())


class RunFrontendContainer(ContainerRunner):
    container_name = 'frontend'

    def create_dependecies(self):
        self.build_if(TaskRebuilded(FrontendContainerBuild()))
        self.build_if(AlwaysTrue())


class RunNginxContainer(ContainerRunner):
    container_name = 'nginx'

    def create_dependecies(self):
        self.build_if(TaskRebuilded(BackendContainerBuild()))
        self.build_if(TaskRebuilded(FrontendContainerBuild()))
        self.build_if(TaskRebuilded(NginxContainerBuild()))
        self.build_if(AlwaysTrue())


class BackendShell(ContainerCommand):
    container_name = 'backend'
    command = 'backend -t shell'
