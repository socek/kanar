from pyramid.security import forget
from pyramid.security import remember

from kanar.application.base.controller import JsonController


class LoginController(JsonController):

    def make(self):
        headers = remember(self.request, 'editor')
        self.request.response.headerlist.extend(headers)
        self.context['logged'] = True


class LogoutController(JsonController):

    def make(self):
        headers = forget(self.request)
        self.request.response.headerlist.extend(headers)


class AuthDataController(JsonController):
    permission = 'create'

    def make(self):
        self.context['ctrl'] = 'auth'
        self.context['userid'] = self.request.authenticated_userid
