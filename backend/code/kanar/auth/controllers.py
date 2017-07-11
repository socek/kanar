from kanar.application.base.controller import JsonController


class LoginController(JsonController):

    def make(self):
        self.context['ctrl'] = 'login'


class LogoutController(JsonController):

    def make(self):
        self.context['ctrl'] = 'logout'


class AuthDataController(JsonController):

    def make(self):
        self.context['ctrl'] = 'auth'
