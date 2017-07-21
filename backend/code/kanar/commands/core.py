from baelfire.core import Core

from kanar.application.app import KanarApplication


class BackendCore(Core):

    def phase_settings(self):
        super().phase_settings()
        self.app = KanarApplication()
        self.app.run_command()

        self.settings.update(self.app.settings)
        self.paths.paths.update(self.app.paths.paths)
