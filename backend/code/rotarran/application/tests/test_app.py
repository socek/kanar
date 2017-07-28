from mock import MagicMock
from mock import patch
from mock import sentinel
from morfdict import StringDict
from pytest import fixture
from pytest import yield_fixture

from rotarran.application.app import RotarranApplication
from rotarran.application.security import RotarranFactory


class TestRotarranApplication(object):

    @fixture
    def application(self):
        obj = RotarranApplication()
        obj.config = MagicMock()
        obj.settings = StringDict({'secret': sentinel.secret})
        return obj

    @yield_fixture
    def msecurity_setup(self, application):
        with patch.object(application, '_setup_security') as mock:
            yield mock

    @yield_fixture
    def mdatabase_config(self):
        with patch('rotarran.application.app.DatabaseConfig') as mock:
            yield mock

    @yield_fixture
    def mcreate_config(self):
        patcher = patch('rotarran.application.app.Application._create_config')
        with patcher as mock:
            yield mock

    @yield_fixture
    def mauth_tkt_authentication_policy(self):
        patcher = patch('rotarran.application.app.AuthTktAuthenticationPolicy')
        with patcher as mock:
            yield mock

    @yield_fixture
    def macl_authorization_policy(self):
        patcher = patch('rotarran.application.app.ACLAuthorizationPolicy')
        with patcher as mock:
            yield mock

    def test_create_config(
        self,
        application,
        msecurity_setup,
        mdatabase_config,
    ):
        """
        ._create_config should setup security and database
        """
        application._create_config()

        msecurity_setup.assert_called_once_with()
        mdatabase_config.assert_called_once_with(application.config,
                                                 application.settings)
        mdatabase_config.return_value.build.assert_called_once_with()

    def test_setup_security(
        self,
        application,
        mauth_tkt_authentication_policy,
        macl_authorization_policy,
    ):
        """
        ._setup_security should create AuthTktAuthenticationPolicy and
        ACLAuthorizationPolicy.
        """
        application._setup_security()

        mauth_tkt_authentication_policy.assert_called_once_with(sentinel.secret)
        macl_authorization_policy.assert_called_once_with()

        application.config.set_authentication_policy.assert_called_once_with(
            mauth_tkt_authentication_policy.return_value)
        application.config.set_authorization_policy.assert_called_once_with(
            macl_authorization_policy.return_value)
        application.config.set_root_factory.assert_called_once_with(
            RotarranFactory)
