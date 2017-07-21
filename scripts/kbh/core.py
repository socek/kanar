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
                    flags.set('frontend:dockerfile_flag', 'frontend_dockerfile_flag')
                    flags.set('nginx:dockerfile_flag', 'nginx_dockerfile_flag')

            with project.set('backend', 'backend') as backend:
                backend.set('backend:dockerfile', 'Dockerfile')
                backend.set('backend:requirements:dev', 'requirements_dev.txt')

                with backend.set('backend:code', 'code') as code:
                    code.set('backend:setuppy', 'setup.py')
                    code.set('backend:ini', 'backend.ini')

            with project.set('frontend', 'frontend') as frontend:
                with frontend.set('frontend:code', 'code') as code:
                    frontend.set('frontend:dockerfile', 'Dockerfile')
                    code.set('frontend:packages', 'package.json')

            with project.set('nginx', 'nginx') as nginx:
                nginx.set('nginx:dockerfile', 'Dockerfile')
                nginx.set('nginx:conf', 'nginx.conf')

        self.settings['package:name'] = 'kanar'

    def get_project_dir(self):
        project_dir = kbh.__file__
        for index in range(3):
            project_dir = dirname(project_dir)
        return project_dir
