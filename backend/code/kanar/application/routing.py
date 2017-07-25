from rotarran.application.base.routing import Routing


class RotarranRouting(Routing):

    def make(self):
        super().make()
        self.read_from_file(self.paths.get('app:auth:routing'))
        self.read_from_file(self.paths.get('app:home:routing'))
        self.read_from_file(self.paths.get('app:menu:routing'))
