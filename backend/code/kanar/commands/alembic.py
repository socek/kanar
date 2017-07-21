from logging import getLogger

from alembic import command
from alembic.config import Config
from baelfire.dependencies import AlwaysTrue
from baelfire.task import Task

from kbh.backend import IniTemplate
from kbh.containers import RunBackendContainer
from kbh.dependecies import MigrationChanged

log = getLogger(__name__)


class AlembicUpgrade(Task):

    def create_dependecies(self):
        self.run_before(IniTemplate())
        self.run_before(RunBackendContainer())
        self.build_if(MigrationChanged('versions', 'sqlite_db'))

    def build(self):
        log.info("Running migrations...")
        alembic_cfg = Config(self.paths.get('frontendini'))
        command.upgrade(alembic_cfg, "head")
        self.touch('sqlite_db')


class AlembicRevision(Task):

    def create_dependecies(self):
        self.run_before(IniTemplate())
        self.run_before(RunBackendContainer())
        self.build_if(AlwaysTrue())

    def build(self):
        alembic_cfg = Config(self.paths.get('frontendini'))
        message = input('Revision message:')
        command.revision(alembic_cfg, message)
