from baelfire.task.process import SubprocessTask

from rotarran.commands.backend import IniTemplate


class BaseCommand(SubprocessTask):

    def create_dependecies(self):
        self.run_before(IniTemplate())

    def run(self, argv=[]):
        self.args = ''
        for arg in argv:
            if ' ' in arg:
                # append "" if the argument has more then 1 word
                self.args += '"{}" '.format(arg)
            else:
                self.args += arg + ' '
        return super().run()
