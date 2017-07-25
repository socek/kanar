from docker import from_env

from baelfire.dependencies import Dependency


class ContainerIsNotRunning(Dependency):

    def __init__(self, image_name):
        super().__init__()
        self.image_name = image_name
        self.docker = from_env()

    def should_build(self):
        for container in self.docker.containers.list():
            if container.attrs['Config']['Image'] == self.image_name:
                return container.attrs['State']['Status'] != 'running'
        return True
