from baelfire.dependencies import FileChanged
from baelfire.task.file import FileTask
from baelfire.task.process import SubprocessTask


class ContainerBuilder(FileTask, SubprocessTask):

    @property
    def dockerfile_key(self):
        return self.container_name + ':dockerfile'

    def create_dependecies(self):
        super().create_dependecies()
        self.build_if(FileChanged(self.dockerfile_key))

    def build(self):
        self.popen('docker-compose build {0}'.format(self.container_name))

        open(self.output, 'w').close()


class ContainerRunner(SubprocessTask):

    def build(self):
        self.popen('docker-compose up -d {0}'.format(self.container_name))
