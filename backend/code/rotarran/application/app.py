from pyramid.authentication import AuthTktAuthenticationPolicy
from pyramid.authorization import ACLAuthorizationPolicy

from rotarran.application.base.app import Application
from rotarran.application.db import DatabaseConfig
from rotarran.application.routing import RotarranRouting
from rotarran.application.security import RotarranFactory


class RotarranApplication(Application):

    class Config(Application.Config):
        routing_cls = RotarranRouting
        settings_module = 'rotarran.application'

    def _create_config(self):
        super()._create_config()

        self._setup_security()

        DatabaseConfig(self.config, self.settings).build()

    def _setup_security(self):
        authn_policy = AuthTktAuthenticationPolicy(self.settings['secret'])
        authz_policy = ACLAuthorizationPolicy()
        self.config.set_authentication_policy(authn_policy)
        self.config.set_authorization_policy(authz_policy)
        self.config.set_root_factory(RotarranFactory)
