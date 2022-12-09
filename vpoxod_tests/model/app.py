import allure

from .pages.main_menu import MainMenu
from .pages.left_menu import LeftMenu
from .pages.list_tours_page import ListToursPage
from .pages.equipment_page import EquipmentPage
from .pages.tour_page import TourPage


main_menu = MainMenu()
left_menu = LeftMenu()
list_tours_page = ListToursPage()
equipment_page = EquipmentPage()
tour_page = TourPage()


def open_page(browser, url):
    with allure.step(f'Открываем страницу {url}'):
        browser.open(url)


