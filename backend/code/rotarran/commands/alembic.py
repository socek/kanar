from baelfire.dependencies import AlwaysTrue
from baelfire.task.process import CommandError

from rotarran.commands.dependecies import MigrationChanged
from rotarran.commands.command import BaseCommand
from rotarran.commands.psql import WaitForPsql


class Alembic(BaseCommand):

    def alembic(self, command, *args, **kwargs):
        fullcommand = '{alembic} -c {ini} '.format(
            alembic=self.paths.get('exe:alembic'),
            ini=self.paths.get('backend:ini'))
        fullcommand += command
        try:
            self.popen(
                fullcommand,
                cwd=self.paths.get('code'),
                *args,
                **kwargs)
        except CommandError:
            pass


class AlembicCommand(Alembic):

    def create_dependecies(self):
        super().create_dependecies()
        self.run_before(WaitForPsql())
        self.build_if(AlwaysTrue())

    def build(self):
        self.alembic(self.args)


class AlembicUpgrade(Alembic):

    def create_dependecies(self):
        super().create_dependecies()
        self.run_before(WaitForPsql())
        self.build_if(MigrationChanged('versions', 'sqlite_db'))

    def build(self):
        self.alembic('upgrade head')
        self.touch('sqlite_db')
