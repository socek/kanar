from time import sleep

from baelfire.dependencies import Dependency
from baelfire.task.process import SubprocessTask
from sqlalchemy.exc import OperationalError

from rotarran.application.db import DatabaseConfig
from rotarran.commands.backend import IniTemplate


def is_psql_running(settings):
    config = DatabaseConfig(None, settings)
    engine = config.get_engine()
    session = config.get_maker(engine)()

    try:
        session.execute('select 1')
        return True
    except OperationalError:
        return False


class PsqlNotRunning(Dependency):

    def should_build(self):
        return not is_psql_running(self.settings)


class WaitForPsql(SubprocessTask):
    TIMEOUT = 100
    TICK = 0.1

    def create_dependecies(self):
        self.run_before(IniTemplate())
        self.build_if(PsqlNotRunning())

    def build(self):
        print('Waiting for postgresql to start...')
        counter = 0
        while not is_psql_running(self.settings):
            counter += 1
            if counter > self.TIMEOUT:
                raise RuntimeError('Waiting for postgresql timeout...')
            sleep(self.TICK)
