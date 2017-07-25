from baelfire.dependencies import AlwaysTrue
from baelfire.dependencies import FileChanged
from baelfire.task.file import FileTask
from baelfire.task.process import CommandError
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


class ContainerCommand(SubprocessTask):
    show_command_errors = True

    def create_dependecies(self):
        self.build_if(AlwaysTrue())

    def run(self, argv=[]):
        self.args = ''
        for arg in argv:
            if ' ' in arg:
                # append "" if the argument has more then 1 word
                self.args += '"{}" '.format(arg)
            else:
                self.args += arg + ' '
        return super().run()

    def build(self):
        try:
            cmd = 'docker-compose exec {0} {1} {2}'.format(
                self.container_name,
                self.command,
                self.args)
            self.popen(cmd)
        except CommandError as error:
            if self.show_command_errors:
                raise error
