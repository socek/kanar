from kanar.menu.paths import paths_setting


def make_settings(settings, paths):
    project(settings, paths)
    database(settings, paths)
    logger(settings, paths)
    debug(settings, paths)
    paths_setting(settings, paths)


def database(settings, paths):
    # ----------------------------------------
    # This is example postgresql configuration
    # ----------------------------------------
    # settings['db:type'] = 'postgresql'
    # settings['db:login'] = 'develop'
    # settings['db:password'] = 'develop'
    # settings['db:host'] = 'localhost'
    # settings['db:port'] = '5432'
    settings['db:type'] = 'sqlite'
    settings['db:name'] = '%(project)s_develop'
    with paths.context('data') as data:
        data.set('sqlite_db', 'data', 'sqlite3.db')


def project(settings, paths):
    settings['secret'] = 'asdasdasdasdweq312iuashi1u2h13o2'


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
            'args': "('%%(log_all)s', 'a')",
            'level': 'NOTSET',
            'formatter': 'generic',
        },
        'formatter_generic': {
            'format': '%%(asctime)s %%(levelname)-5.5s [%%(name)s][%%(threadName)s] %%(message)s',
        },
    }
