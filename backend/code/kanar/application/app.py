from kanar.application.base.app import Application
from kanar.application.routing import KanarRouting


class KanarApplication(Application):

    class Config(Application.Config):
        routing_cls = KanarRouting
        settings_module = 'kanar.application'

    def _create_config(self):
        super()._create_config()

        self.config.include('pyramid_debugtoolbar')
