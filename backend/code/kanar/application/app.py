from kanar.application.base.app import Application


class KanarApplication(Application):

    class Config(Application.Config):
        settings_module = 'kanar.application'


