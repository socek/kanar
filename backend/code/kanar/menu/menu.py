from kanar.menu.models import Menu
from kanar.menu.models import MenuElement


class KanarMenu(Menu):

    def make_menu(self):
        with self.add('Dashboard') as main:
            main.add(MenuElement('dashboard_home', 'Home', '#/'))
