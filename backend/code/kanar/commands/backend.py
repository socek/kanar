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
