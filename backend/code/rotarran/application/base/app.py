from pyramid.config import Configurator

from rotarran.application.base.routing import Routing
from rotarran.application.base.settings import SettingsFactory


class Application(object):

    class Config(object):
        routing_cls = Routing
        settings_module = None
        settings = SettingsFactory

    def __init__(self):
        self.plugs = {}
        self.app_plugs = []

    def __call__(self, settings=None):
        settings = settings or {}
        return self.run_uwsgi(settings)

    def run_uwsgi(self, settings=None):
        settings = settings or {}
        self._create_app(settings, 'uwsgi')
        return self._return_wsgi_app()

    def run_tests(self, settings=None):
        settings = settings or {}
        self._create_app(settings, 'tests')

    def run_shell(self, settings=None):
        settings = settings or {}
        self._create_app(settings, 'shell')

    def run_command(self, settings=None):
        settings = settings or {}
        self._create_app(settings, 'command')

    def _create_app(self, settings={}, settings_name='uwsgi'):
        self._generate_settings(settings, settings_name)
        self._create_config()
        self._generate_registry(self.config.registry)
        self._create_routing()

    def _generate_settings(
        self,
        settings,
        endpoint,
    ):
        self.settings = settings
        self.paths = {}
        factory = self.Config.settings(
            self.Config.settings_module,
            self.settings,
            self.paths)
        self.settings, self.paths = factory.get_for(endpoint)

    def _create_config(self):
        kwargs = self._get_config_kwargs()
        self.config = Configurator(**kwargs)

    def _get_config_kwargs(self):
        return {
            'settings': self.settings.to_dict(),
        }

    def _generate_registry(self, registry):
        self.registry = registry
        registry['settings'] = self.settings
        registry['paths'] = self.paths
        registry['application'] = self

    def _create_routing(self):
        self.routing = self.Config.routing_cls(self)
        self.routing.make()

    def _return_wsgi_app(self):
        return self.config.make_wsgi_app()
