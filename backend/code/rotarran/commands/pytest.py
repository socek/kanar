from baelfire.dependencies import AlwaysTrue
from baelfire.task.process import CommandError

from rotarran.commands.alembic import AlembicUpgrade
from rotarran.commands.command import BaseCommand


class PyTest(BaseCommand):

    def create_dependecies(self):
        super().create_dependecies()

        self.run_before(AlembicUpgrade())
        self.build_if(AlwaysTrue())

    def build(self):
        fullcommand = '{pytest} {args}'.format(
            pytest=self.paths.get('exe:pytest'),
            args=self.args)
        try:
            self.popen(
                fullcommand,
                cwd=self.paths.get('code'))
        except CommandError:
            pass
