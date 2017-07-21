from baelfire.dependencies import AlwaysTrue
from baelfire.dependencies import FileChanged
from baelfire.task import TemplateTask
from baelfire.task.process import SubprocessTask


class IniTemplate(TemplateTask):

    source_name = 'template:backendini'
    output_name = 'backend:ini'

    def create_dependecies(self):
        super().create_dependecies()

        self.build_if(FileChanged('settings:command'))
        self.build_if(FileChanged('settings:default'))
        self.build_if(FileChanged('settings:local'))
        self.build_if(FileChanged('settings:paths'))
        self.build_if(FileChanged('settings:tests'))


class RunDevServer(SubprocessTask):

    def create_dependecies(self):
        self.run_before(IniTemplate())

        self.build_if(AlwaysTrue())

    def build(self):
        self.popen(
            '{cmd} backend.ini --reload'.format(
                cmd=self.paths.get('exe:pserve')),
            cwd=self.paths.get('code'))
