from mock import MagicMock
from mock import patch
from pytest import fixture
from pytest import yield_fixture

from rotarran.application.db import DatabaseConfig
from rotarran.application.db import DatabaseGenerator


class TestDatabaseConfig(object):

    @fixture
    def settings(self):
        return {}

    @fixture
    def mconfig(self):
        return MagicMock()

    @fixture
    def database(self, mconfig, settings):
        return DatabaseConfig(mconfig, settings)

    @yield_fixture
    def mget_engine(self, database):
        with patch.object(database, 'get_engine') as mock:
            yield mock

    @yield_fixture
    def msessionmaker(self):
        with patch('rotarran.application.db.sessionmaker') as mock:
            yield mock

    @yield_fixture
    def mget_url(self, database):
        with patch.object(database, 'get_url') as mock:
            yield mock

    @yield_fixture
    def mcreate_engine(self):
        with patch('rotarran.application.db.create_engine') as mock:
            yield mock

    @yield_fixture
    def mdatabase_generator(self):
        with patch('rotarran.application.db.DatabaseGenerator') as mock:
            yield mock

    def test_build(self, database, mget_engine, msessionmaker, mconfig, mdatabase_generator):
        """
        .build should append sessionmaker to a registry and add database generator to the request object
        """
        database.build()

        mget_engine.assert_called_once_with()
        msessionmaker.assert_called_once_with(bind=mget_engine.return_value)
        assert mconfig.registry.dbmaker == msessionmaker.return_value
        mconfig.add_request_method.assert_called_once_with(
            mdatabase_generator.return_value,
            name='database',
            reify=True)

    def test_get_engine(self, database, mget_url, mcreate_engine, settings):
        """
        .get_engine should create sqlalchemy engine from application's settings
        """
        settings['db:options'] = {'one': 1, 'two': '2', 'three': 'three'}
        assert database.get_engine() == mcreate_engine.return_value

        mget_url.assert_called_once_with()
        mcreate_engine.assert_called_once_with(
            mget_url.return_value,
            one=1,
            two='2',
            three='three')

    def test_get_url(self, database, settings):
        """
        .get_url should create sqlalchemy's database url from application's settings
        """
        settings['db:type'] = 'postgresql'
        settings['db:login'] = 'mylogin'
        settings['db:password'] = 'mypassword'
        settings['db:host'] = 'google.pl'
        settings['db:port'] = '123'
        settings['db:name'] = 'superdb'

        assert database.get_url() == 'postgresql://mylogin:mypassword@google.pl:123/superdb'


class TestDatabaseGenerator(object):

    @fixture
    def generator(self):
        return DatabaseGenerator()

    @fixture
    def mrequest(self):
        return MagicMock()

    @fixture
    def msession(self, generator):
        generator.session = MagicMock()
        return generator.session

    def test_call(self, generator, mrequest):
        """
        .__call__ should create new session and add cleanup step for it.
        """
        assert generator(mrequest) == mrequest.registry.dbmaker.return_value

        mrequest.registry.dbmaker.assert_called_once_with()
        mrequest.add_finished_callback(generator.cleanup)

    def test_cleanup_on_exception(self, generator, msession, mrequest):
        """
        .cleanup should rollback database changes on exception
        """
        mrequest.exception = True

        generator.cleanup(mrequest)
        msession.rollback.assert_called_once_with()
        msession.close.assert_called_once_with()

    def test_cleanup_on_success(self, generator, msession, mrequest):
        """
        .cleanup should commit changes on response success
        """
        mrequest.exception = None

        generator.cleanup(mrequest)
        msession.commit.assert_called_once_with()
        msession.close.assert_called_once_with()
