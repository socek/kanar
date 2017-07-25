from rotarran.application.settings.paths import paths_setting


def make_settings(settings, paths):
    project(settings, paths)
    paths_setting(settings, paths)
    database(settings, paths)
    logger(settings, paths)
    debug(settings, paths)


def database(settings, paths):
    settings['db:type'] = 'postgresql'
    settings['db:login'] = 'rotarran'
    settings['db:password'] = 'rotarran'
    settings['db:host'] = 'postgres'
    settings['db:name'] = 'rotarran'
    settings['db:port'] = '5432'
    settings['db:options'] = {}

    with paths.context('data') as data:
        data.set('sqlite_db', 'data', 'sqlite3.db')


def project(settings, paths):
    settings['secret'] = 'asdasdasdasdweq312iuashi1u2h13o2'
    settings['package:name'] = 'rotarran'


def debug(settings, paths):
    settings['debug'] = True
    settings['pyramid.reload_templates'] = True
    settings['pyramid.debug_notfound'] = True
    settings['pyramid.debug_routematch'] = True


def logger(settings, paths):
    settings['loggers'] = {
        'loggers': {
            'keys': 'root, sqlalchemy, alembic',
        },
        'handlers': {
            'keys': 'console, all',
        },
        'formatters': {
            'keys': 'generic',
        },
        'logger_root': {
            'level': 'INFO',
            'handlers': 'console, all',
        },
        'logger_sqlalchemy': {
            'level': 'INFO',
            'handlers': 'all',
            'qualname': 'sqlalchemy.engine',
            'propagate': '0',
        },
        'logger_alembic': {
            'level': 'INFO',
            'handlers': 'all',
            'qualname': 'alembic',
            'propagate': '0',
        },
        'handler_console': {
            'class': 'StreamHandler',
            'args': '(sys.stderr,)',
            'level': 'NOTSET',
            'formatter': 'generic',
        },
        'handler_all': {
            'class': 'FileHandler',
            'args': "('{}', 'a')".format(paths.get('logs:all')),
            'level': 'NOTSET',
            'formatter': 'generic',
        },
        'formatter_generic': {
            'format': '%%(asctime)s %%(levelname)-5.5s [%%(name)s][%%(threadName)s] %%(message)s',
        },
    }
