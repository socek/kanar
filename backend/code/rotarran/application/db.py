from sqlalchemy.engine import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Model = declarative_base()


class DatabaseConfig(object):

    def __init__(self, config, settings):
        self.config = config
        self.settings = settings

    def build(self):
        url = self.get_url()
        engine = create_engine(url, **self.settings['db:options'])
        self.config.registry.dbmaker = sessionmaker(bind=engine)
        self.config.add_request_method(self.database, reify=True)

    def database(self, request):
        maker = request.registry.dbmaker
        session = maker()

        def cleanup(request):
            if request.exception is not None:
                session.rollback()
            else:
                session.commit()
            session.close()
        request.add_finished_callback(cleanup)

        return session

    def get_url(self):
        return '{type}://{login}:{password}@{host}:{port}/{name}'.format(
            type=self.settings['db:type'],
            login=self.settings['db:login'],
            password=self.settings['db:password'],
            host=self.settings['db:host'],
            port=self.settings['db:port'],
            name=self.settings['db:name'])
