from baelfire.core import Core

from rotarran.application.app import RotarranApplication


class BackendCore(Core):

    def phase_settings(self):
        super().phase_settings()
        self.app = RotarranApplication()
        self.app.run_command()

        self.settings.update(self.app.settings)
        self.paths.paths.update(self.app.paths.paths)
