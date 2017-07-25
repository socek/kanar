from rotarran.menu.models import Menu
from rotarran.menu.models import MenuElement


class RotarranMenu(Menu):

    def make_menu(self):
        with self.add('Dashboard') as main:
            main.add(MenuElement('dashboard_home', 'Home', '#/'))
