from os.path import dirname

from baelfire.core import Core

import kbh


class KbhCore(Core):

    def phase_settings(self):
        super().phase_settings()

        self.paths.set('project', self.get_project_dir(), is_root=True)  # TODO: change to generate path
        self.paths.set('data', 'data', parent='project')
        self.paths.set('flags_backend', 'flags', parent='data')
        self.paths.set('backend_dockerfile_flag', 'backend_dockerfile_flag', parent='flags_backend')

        self.paths.set('backend', 'backend', parent='project')
        self.paths.set('backend_dockerfile', 'Dockerfile', parent='backend')
        self.paths.set('backend_code', 'code', parent='backend')
        self.paths.set('backend_setuppy', 'setup.py', parent='backend_code')

    def get_project_dir(self):
        project_dir = kbh.__file__
        for index in range(3):
            project_dir = dirname(project_dir)
        return project_dir
