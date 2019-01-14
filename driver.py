# MAIN FILE
from menu_driver import Menu_Driver


class Driver:
    menu_driver = Menu_Driver()

    def run(self):
        self.menu_driver.run_menu_driver()


driver = Driver()
driver.run()
