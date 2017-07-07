from kanar.application.base.controller import JsonController


class HomeController(JsonController):

    def make(self):
        self.context['yey'] = 'it worked!'
