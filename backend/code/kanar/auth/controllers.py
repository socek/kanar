from deform import Form
from deform import ValidationFailure
from pyramid.security import forget
from pyramid.security import remember

from kanar.application.base.controller import JsonController
from kanar.auth.forms import LoginForm


class LoginController(JsonController):

    def _create_form(self, cls):
        return Form(cls(), use_ajax=True)

    def make(self):
        form = self._create_form(LoginForm)
        self.context['fields'] = data = self.request.json_body
        try:
            data = self._validate_form(form, data)
        except ValidationFailure as error:
            self.context['validate'] = False
            for key, value in error.error.asdict().items():
                data[key]['error'] = value
            return

        self.context['validate'] = True
        headers = remember(self.request, data['username'])
        self.request.response.headerlist.extend(headers)

    def _validate_form(self, form, data):
        data = {key: item['value'] for key, item in data.items()}
        return form.validate(data.items())


class LogoutController(JsonController):

    def make(self):
        headers = forget(self.request)
        self.request.response.headerlist.extend(headers)
        self.context['is_authenticated'] = False


class AuthDataController(JsonController):

    def make(self):
        self.context['is_authenticated'] = self.request.authenticated_userid is not None
