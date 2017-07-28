from sqlalchemy.engine import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Model = declarative_base()


class DatabaseConfig(object):

    def __init__(self, config, settings):
        self.config = config
        self.settings = settings

    def build(self):
        engine = self.get_engine()
        self.config.registry.dbmaker = self.get_maker(engine)
        self.config.add_request_method(DatabaseGenerator(), name='database', reify=True)

    def get_engine(self):
        url = self.get_url()
        return create_engine(url, **self.settings['db:options'])

    def get_maker(self, engine):
        return sessionmaker(bind=engine)

    def get_url(self):
        return '{type}://{login}:{password}@{host}:{port}/{name}'.format(
            type=self.settings['db:type'],
            login=self.settings['db:login'],
            password=self.settings['db:password'],
            host=self.settings['db:host'],
            port=self.settings['db:port'],
            name=self.settings['db:name'])


class DatabaseGenerator(object):

    def __call__(self, request):
        maker = request.registry.dbmaker
        self.session = maker()
        request.add_finished_callback(self.cleanup)
        return self.session

    def cleanup(self, request):
        if request.exception is not None:
            self.session.rollback()
        else:
            self.session.commit()
        self.session.close()
