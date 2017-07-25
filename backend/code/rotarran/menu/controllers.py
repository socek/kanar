from rotarran.application.base.controller import JsonController
from rotarran.menu.menu import RotarranMenu


class MenuController(JsonController):

    def make(self):
        self.context['menu'] = RotarranMenu(self.request).serialize()
