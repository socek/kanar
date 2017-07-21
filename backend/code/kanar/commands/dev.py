from baelfire.dependencies import AlwaysTrue
from baelfire.task.process import SubprocessTask

from kanar.commands.alembic import AlembicUpgrade


class RunDevServer(SubprocessTask):

    def create_dependecies(self):
        self.run_before(AlembicUpgrade())

        self.build_if(AlwaysTrue())

    def build(self):
        self.popen(
            '{cmd} backend.ini --reload'.format(
                cmd=self.paths.get('exe:pserve')),
            cwd=self.paths.get('code'))
