from deform import Form
from deform import ValidationFailure
from pyramid.security import forget
from pyramid.security import remember

from kanar.application.base.controller import JsonController
from kanar.auth.forms import LoginForm


class FormController(JsonController):
    form_cls = None

    def make(self):
        self.context['form_error'] = ''
        data = self.context['fields'] = self.request.json_body
        form = Form(self.form_cls(), use_ajax=True)

        try:
            self.validate_form(form, data)
            for key, value in data.items():
                data[key]['error'] = ''
        except ValidationFailure as error:
            self.context['validate'] = False
            errors = error.error.asdict()
            for key, value in data.items():
                data[key]['error'] = errors.get(key, '')
            self.fail(data)
            return

        self.success(data)

    def validate_form(self, form, data):
        data = [(key, item['value']) for key, item in data.items()]
        return form.validate(data)

    def success(self, data):
        pass

    def fail(self, data):
        pass


class LoginController(FormController):
    form_cls = LoginForm

    def success(self, data):
        if data['username']['value'] != 'socek':
            self.context['validate'] = False
            self.context['form_error'] = "Username and/or password do not match."
        else:
            self.context['form_error'] = ''
            self.context['validate'] = True
            headers = remember(self.request, data['username'])
            self.request.response.headerlist.extend(headers)


class LogoutController(JsonController):

    def make(self):
        headers = forget(self.request)
        self.request.response.headerlist.extend(headers)
        self.context['is_authenticated'] = False


class AuthDataController(JsonController):

    def make(self):
        self.context['is_authenticated'] = self.request.authenticated_userid is not None
