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
