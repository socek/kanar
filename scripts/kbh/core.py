from os.path import dirname

from baelfire.core import Core

import kbh


class KbhCore(Core):

    def phase_settings(self):
        super().phase_settings()

        with self.paths.set('project', self.get_project_dir(), is_root=True) as project:
            with project.set('data', 'data') as data:
                with data.set('flags:backend', 'flags') as flags:
                    flags.set('backend:dockerfile_flag', 'backend_dockerfile_flag')

            with project.set('backend', 'backend') as backend:
                backend.set('backend:dockerfile', 'Dockerfile')

                with backend.set('backend:code', 'code') as code:
                    code.set('backend:setuppy', 'setup.py')
                    code.set('backend:ini', 'backend.ini')

            with project.set('scripts', 'scripts') as scripts:
                with scripts.set('kbh', 'kbh') as kbhdir:
                    with kbhdir.set('kbh:templates', 'templates') as templates:
                        templates.set('template:backendini', 'backend.ini.jinja2')

        self.settings['loggers'] = {
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

    def get_project_dir(self):
        project_dir = kbh.__file__
        for index in range(3):
            project_dir = dirname(project_dir)
        return project_dir
