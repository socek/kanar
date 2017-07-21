from sys import argv

from baelfire.dependencies import AlwaysTrue
from baelfire.task.process import CommandError
from baelfire.task.process import SubprocessTask

from kanar.commands.backend import IniTemplate
from kanar.commands.core import BackendCore
from kanar.commands.dependecies import MigrationChanged


class Alembic(SubprocessTask):

    def create_dependecies(self):
        self.run_before(IniTemplate())

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

        self.build_if(AlwaysTrue())

    def build(self):
        args = ''
        for arg in argv[1:]:
            if ' ' in arg:
                args += '"{}" '.format(arg)
            else:
                args += arg + ' '
        self.alembic(args)


class AlembicUpgrade(Alembic):

    def create_dependecies(self):
        super().create_dependecies()
        self.build_if(MigrationChanged('versions', 'sqlite_db'))

    def build(self):
        self.alembic('upgrade head')


def run_alembic():
    AlembicCommand(BackendCore()).run()
