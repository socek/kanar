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

    def generate_context(self):
        context = super().generate_context()
        context['sqlalchemy_url'] = '{type}://{login}:{password}@{host}:{port}/{name}'.format(
            type=self.settings['db:type'],
            login=self.settings['db:login'],
            password=self.settings['db:password'],
            host=self.settings['db:host'],
            port=self.settings['db:port'],
            name=self.settings['db:name'])
        return context


class RunDevServer(SubprocessTask):

    def create_dependecies(self):
        self.run_before(IniTemplate())

        self.build_if(AlwaysTrue())

    def build(self):
        self.popen(
            '{cmd} backend.ini --reload'.format(
                cmd=self.paths.get('exe:pserve')),
            cwd=self.paths.get('code'))
