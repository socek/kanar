from pyramid.security import forget
from pyramid.security import remember

from kanar.application.base.controller import JsonController


class LoginController(JsonController):

    def make(self):
        headers = remember(self.request, 'editor')
        self.request.response.headerlist.extend(headers)
        self.context['is_authenticated'] = True


class LogoutController(JsonController):

    def make(self):
        headers = forget(self.request)
        self.request.response.headerlist.extend(headers)
        self.context['is_authenticated'] = False


class AuthDataController(JsonController):

    def make(self):
        self.context['is_authenticated'] = self.request.authenticated_userid is not None
