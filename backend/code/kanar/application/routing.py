from kanar.application.base.routing import Routing


class KanarRouting(Routing):

    def make(self):
        super().make()
        self.read_from_file(self.paths.get('app:home:routing'))

