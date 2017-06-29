from baelfire.dependencies import AlwaysTrue
from baelfire.task.process import SubprocessTask


class BackendContainer(SubprocessTask):

    def create_dependecies(self):
        self.build_if(AlwaysTrue())

    def build(self):
        self.popen(['docker-compose up -d'])
