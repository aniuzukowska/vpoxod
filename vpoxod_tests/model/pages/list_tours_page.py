import allure
from selene import query
from selene.support.conditions import have, be
from .left_menu import LeftMenuLocators
from ...data.data_tests import Data


class ListToursPageLocators():
    TYPES_TOURS = {
        'Вело': {
            'logo': '*[data-original-title*="/types/6-Velo"]'
        }
    }
    TOUR_START_DATE = '.table_term *[itemprop="startDate"]'
    TITLE = '.main_top > *:first-child'
    GROUP_LOGO_TYPES = '.route_search_tab_icons'
    MARKER_REGION = '.scroll-on-hover'
    TOUR_CONTENT = '.main_page_hikes_list article'
    TOUR_CONTENT_FOR_SEAZON = {
        'part 1': '.item_header',
        'part 2': '.first.item_1'
    }


class ListToursPage():
    def assert_tours_region(self, browser, value):
        list_tours_page_locators = ListToursPageLocators()
        locator_title = list_tours_page_locators.TITLE
        locator_marker_region = list_tours_page_locators.MARKER_REGION
        locator_tour_content = list_tours_page_locators.TOUR_CONTENT

        data = Data()
        url = data.REGIONS[value]['url']
        title = data.REGIONS[value]['title']

        with allure.step('Проверяем результат'):
            with allure.step('Проверяем url'):
                browser.with_(timeout=6).should(have.url(url))

            with allure.step('Проверяем заголовок страницы'):
                browser.with_(timeout=6).element(locator_title).should(have.text(title))

            with allure.step('Проверяем, что отображаются блоки с информацией о походах'):
                browser.with_(timeout=6).all(locator_tour_content).should(have.size_greater_than(0))

            with allure.step(f'Проверяем, что отображаемые походы относятся к региону {value}'):
                list_regions = browser.with_(timeout=6).all(locator_marker_region)
                for region in list_regions:
                    region.should(have.text(value))

    def assert_tours_types(self, browser, value):
        list_tours_page_locators = ListToursPageLocators()
        locator_logo = list_tours_page_locators.TYPES_TOURS[value]['logo']
        locator_title = list_tours_page_locators.TITLE
        locator_groups_logo_types = list_tours_page_locators.GROUP_LOGO_TYPES
        locator_tour_content = list_tours_page_locators.TOUR_CONTENT

        data = Data()
        url = data.TYPES_TOURS[value]['url']
        title = data.TYPES_TOURS[value]['title']

        with allure.step('Проверяем результат'):
            with allure.step('Проверяем url'):
                browser.with_(timeout=6).should(have.url(url))
            with allure.step('Проверяем заголовок страницы'):
                browser.element(locator_title).should(have.text(title))
            with allure.step('Проверяем, что отображаются блоки с информацией о походах'):
                browser.all(locator_tour_content).should(have.size_greater_than(0))
            with allure.step(f'Проверяем, что отображаемые походы относятся к {value}'):
                groups_logo_types = browser.all(locator_groups_logo_types)
                for group in groups_logo_types:
                    group.element(locator_logo).should(be.visible)

    def assert_tours_seazon(self, browser, value):
        left_menu_locators = LeftMenuLocators()
        locator_seazon_button = left_menu_locators.SEAZON_BUTTONS[value]

        list_tours_page_locators = ListToursPageLocators()
        locator_tour_start_date = list_tours_page_locators.TOUR_START_DATE
        locator_content_part_1 = list_tours_page_locators.TOUR_CONTENT_FOR_SEAZON['part 1']
        locator_content_part_2 = list_tours_page_locators.TOUR_CONTENT_FOR_SEAZON['part 2']

        data = Data()
        seazon_months = data.SEAZON_MONTHS[value]

        with allure.step('Проверяем результат'):
            with allure.step(f'Проверяем, что кнопка "{value}" выделена как нажатая'):
                class_seazon = browser.element(locator_seazon_button).get(query.attribute('class'))
                assert 'active' in class_seazon

            with allure.step('Проверяем, что отображаются блоки с информацией о походах'):
                browser.all(locator_content_part_1).with_(timeout=6).should(have.size_greater_than(0))
                browser.all(locator_content_part_2).with_(timeout=6).should(have.size_greater_than(1))

            with allure.step(f'Проверяем, что отображаемые походы начинаются в сезоне {value}'):
                tour_start_date_list = browser.all(locator_tour_start_date)
                for date in tour_start_date_list:
                    date_str = date.get(query.attribute('content'))
                    month = date_str[5:7:]
                    assert month in seazon_months






