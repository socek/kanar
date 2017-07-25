from baelfire.dependencies import AlwaysTrue
from baelfire.task.process import SubprocessTask

from rotarran.commands.alembic import AlembicUpgrade


class Shell(SubprocessTask):

    def create_dependecies(self):
        self.run_before(AlembicUpgrade())
        self.build_if(AlwaysTrue())

    def shell(self, command='', *args, **kwargs):
        fullcommand = '{pshell} {ini} '.format(
            pshell=self.paths.get('exe:pshell'),
            ini=self.paths.get('backend:ini'))
        fullcommand += command
        self.popen(
            fullcommand,
            cwd=self.paths.get('code'),
            *args,
            **kwargs)

    def build(self):
        self.shell()
