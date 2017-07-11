from logging import getLogger

from kanar.application.base.controller import JsonController

log = getLogger(__name__)


class HomeController(JsonController):

    def make(self):
        self.context['yey'] = 'it worked!'
        self.context['ctrl'] = 'home'
