from pyramid.security import forget
from pyramid.security import remember

from kanar.application.base.controller import JsonController
from kanar.auth.forms import LoginSchema
from kanar.application.base.controller import FormController


class LoginController(FormController):

    def post(self):
        fields = self.prepere_context()
        schema = LoginSchema()

        if self.schema_validated(schema, fields):
            if self.authenticated(fields):
                self.on_success(fields)
            else:
                self.on_fail()

    def authenticated(self, fields):
        return fields['username']['value'] == 'socek'

    def on_success(self, fields):
        self.context['form_error'] = ''
        self.context['validate'] = True
        headers = remember(self.request, fields['username'])
        self.request.response.headerlist.extend(headers)

    def on_fail(self):
        self.context['validate'] = False
        self.context['form_error'] = "Username and/or password do not match."


class LogoutController(JsonController):

    def make(self):
        headers = forget(self.request)
        self.request.response.headerlist.extend(headers)
        self.context['is_authenticated'] = False


class AuthDataController(JsonController):

    def make(self):
        self.context['is_authenticated'] = self.request.authenticated_userid is not None
