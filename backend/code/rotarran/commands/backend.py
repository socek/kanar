from baelfire.dependencies import FileChanged
from baelfire.task import TemplateTask


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
