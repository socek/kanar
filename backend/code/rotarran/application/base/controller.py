from colander import Invalid
from pyramid.httpexceptions import HTTPFound


class QuitController(Exception):
    """
    Immediately ends controller. Controller will return provided response.
    """

    def __init__(self, response=None):
        self.response = response


class FinalizeController(Exception):
    """
    Ends .make method. Other Controller mechanics will work normally.
    """

    def __init__(self, context=None):
        self.context = context or {}


class Controller(object):

    def __init__(self, root_factory, request):
        super().__init__()
        self.request = request
        self.application = request.registry['application']
        self.root_factory = root_factory
        self.response = None

    def __call__(self):
        return self.run()

    def run(self):
        try:
            self._create_context()
            self._before_make()
            self._make()
            self._after_make()
            return self._get_response()
        except QuitController as end:
            self._before_quit()
            return end.response or self.response

    def _make(self):
        try:
            self.make()
        except FinalizeController as finalizer:
            self.context.update(finalizer.context)

    def _create_context(self):
        self.context = {}

    def _get_response(self):
        if self.response is None:
            self._create_widgets()
            return self.context
        else:
            return self.response

    def redirect(self, to, quit=False, **kwargs):
        url = self.request.route_url(to, **kwargs)
        self.main.response = HTTPFound(
            location=url,
            headers=self.request.response.headerlist,
        )
        if quit:
            raise QuitController(self.parent.response)

    def _before_make(self):
        pass

    def _after_make(self):
        pass

    def _create_widgets(self):
        pass

    def _before_quit(self):
        pass

    def make(self):
        pass


class JsonController(Controller):
    """
    Controller which will return context as json.
    """
    renderer = 'json'

    def _create_context(self):
        self.context = {}


class RestfulController(JsonController):

    @property
    def methods(self):
        return {
            'GET': self.get,
            'POST': self.post,
            'PUT': self.put,
            'PATCH': self.patch,
            'DELETE': self.delete,
        }

    def make(self):
        method = self.methods[self.request.method]
        method()

    def get(self):
        pass

    def post(self):
        pass

    def put(self):
        pass

    def patch(self):
        pass

    def delete(self):
        pass


class FormController(RestfulController):

    def prepere_context(self):
        """
        Prepere context for returning form data.
        """
        self.context['form_error'] = ''
        self.context['fields'] = self.request.json_body
        for key, value in self.context['fields'].items():
            self.context['fields'][key]['error'] = ''
        return self.context['fields']

    def schema_validated(self, schema, fields):
        """
        Validate if data provided are in proper schema.
        """
        try:
            cstruct = self._get_values_dict(fields)
            schema.deserialize(cstruct)
            self.context['validate'] = True
            return True
        except Invalid as error:
            self.context['validate'] = False
            self.parse_errors(fields, error)
            return False

    def parse_errors(self, fields, error=None):
        """
        Parse errors provided by colander and return in our own form format.
        """
        errors = error.asdict()
        for key, value in fields.items():
            fields[key]['error'] = errors.get(key, '')

    def _get_values_dict(self, fields):
        """
        Get "key: value" from provided fields.
        """
        return dict((key, item['value']) for key, item in fields.items())
