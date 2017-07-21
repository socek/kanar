from pyramid.authentication import AuthTktAuthenticationPolicy
from pyramid.authorization import ACLAuthorizationPolicy

from kanar.application.base.app import Application
from kanar.application.db import DatabaseConfig
from kanar.application.routing import KanarRouting
from kanar.application.security import KanarFactory


class KanarApplication(Application):

    class Config(Application.Config):
        routing_cls = KanarRouting
        settings_module = 'kanar.application'

    def _create_config(self):
        super()._create_config()

        # Security policies
        authn_policy = AuthTktAuthenticationPolicy(self.settings['secret'])
        authz_policy = ACLAuthorizationPolicy()
        self.config.set_authentication_policy(authn_policy)
        self.config.set_authorization_policy(authz_policy)
        self.config.set_root_factory(KanarFactory)

        self.config.include('pyramid_debugtoolbar')

        DatabaseConfig(self.config, self.settings).build()
