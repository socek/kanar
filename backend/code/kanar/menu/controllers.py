from kanar.application.base.controller import JsonController
from kanar.menu.menu import KanarMenu


class MenuController(JsonController):

    def make(self):
        self.context['menu'] = KanarMenu(self.request).serialize()
