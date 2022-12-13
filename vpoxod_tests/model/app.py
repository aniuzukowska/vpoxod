import os

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


def open_main_page(browser):
    with allure.step(f'Открываем главную страницу'):
        browser.open('')


def open_tour_page(browser):
    with allure.step(f'Открываем страницу тура'):
        tour_url = os.getenv('TOUR_URL')
        browser.open(f'{tour_url}#content-top')


