import allure
from selene import query
from selene.support.conditions import have, be
from .left_menu import LeftMenu
from ...data.data_tests import Data
import time


class ListToursPage():
    types_tours = {
        'Вело': {
            'logo': '*[data-original-title*="/types/6-Velo"]'
        }
    }
    tour_start_date = '.table_term *[itemprop="startDate"]'
    title = '.main_top > *:first-child'
    group_logo_types = '.route_search_tab_icons'
    marker_region = '.scroll-on-hover'
    tour_content = '.main_page_hikes_list article'
    tour_content_for_seazon = {
        'part 1': '.item_header',
        'part 2': '.first.item_1'
    }

    def assert_tours_region(self, browser, value):
        data = Data()

        with allure.step('Проверяем результат'):
            with allure.step('Проверяем url'):
                browser.with_(timeout=6).should(have.url(data.regions[value]['url']))

            with allure.step('Проверяем заголовок страницы'):
                browser.with_(timeout=6).element(self.title).should(have.text(data.regions[value]['title']))

            with allure.step('Проверяем, что отображаются блоки с информацией о походах'):
                browser.with_(timeout=6).all(self.tour_content).should(have.size_greater_than(0))

            with allure.step(f'Проверяем, что отображаемые походы относятся к региону {value}'):
                list_regions = browser.with_(timeout=6).all(self.marker_region)
                for region in list_regions:
                    region.should(have.text(value))

    def assert_tours_types(self, browser, value):
        data = Data()

        with allure.step('Проверяем результат'):
            with allure.step('Проверяем url'):
                browser.with_(timeout=6).should(have.url(data.types_tours[value]['url']))
            with allure.step('Проверяем заголовок страницы'):
                browser.element(self.title).should(have.text(data.types_tours[value]['title']))
            with allure.step('Проверяем, что отображаются блоки с информацией о походах'):
                browser.all(self.tour_content).should(have.size_greater_than(0))
            with allure.step(f'Проверяем, что отображаемые походы относятся к {value}'):
                groups_logo_types = browser.all(self.group_logo_types)
                for group in groups_logo_types:
                    group.element(self.types_tours[value]['logo']).should(be.visible)

    def assert_tours_seazon(self, browser, value):
        left_menu = LeftMenu()
        data = Data()

        with allure.step('Проверяем результат'):
            with allure.step(f'Проверяем, что кнопка "{value}" выделена как нажатая'):
                class_seazon = browser.element(left_menu.button_seazon[value]).get(query.attribute('class'))
                assert 'active' in class_seazon

            with allure.step('Проверяем, что отображаются блоки с информацией о походах'):
                browser.all(self.tour_content_for_seazon['part 1']).with_(timeout=6).should(have.size_greater_than(0))
                browser.all(self.tour_content_for_seazon['part 2']).with_(timeout=6).should(have.size_greater_than(1))

            with allure.step(f'Проверяем, что отображаемые походы начинаются в сезоне {value}'):
                time.sleep(5)
                tour_start_date_list = browser.all(self.tour_start_date)
                for date in tour_start_date_list:
                    date_str = date.get(query.attribute('content'))
                    month = date_str[5:7:]
                    assert month in data.seazon_months[value]






