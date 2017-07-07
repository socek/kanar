from kanar.application.base.app import Application
from kanar.application.routing import KanarRouting


class KanarApplication(Application):

    class Config(Application.Config):
        routing_cls = KanarRouting
        settings_module = 'kanar.application'


