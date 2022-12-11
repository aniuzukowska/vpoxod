import os
import allure
from selene import query, command
from selene.support.conditions import have, be


class TourPageLocators():
    TITLE = '.route_table .route_title'
    BUTTON = {'Сроки походов': '.route_button'}
    TAB = {
        'Маршруты': {'part 1': '.tabs_title a[href="', 'part 2': '/about#tabs"]'},
        'Отзывы': {'part 1': '.tabs_title a[href="', 'part 2': '/responses#tabs"]'}
    }
    CONTENT = {
        'Маршруты': '.route_description_days *',
        'Отзывы': '.comments_list article'
    }
    DATE = '.first.item_1'
    PRICE = '.tippy.table_price_left'


class TourPage():
    def tab_click(self, browser, value):
        tour_url = os.getenv('TOUR_URL')
        tour_page_locators = TourPageLocators()
        locator_tab = tour_page_locators.TAB[value]['part 1'] + tour_url \
                      + tour_page_locators.TAB[value]['part 2']

        with allure.step(f'Переходим на вкладку "{value}"'):
            browser.element(locator_tab).perform(command.js.scroll_into_view)
            browser.element(locator_tab).click()

    def assert_tab_info(self, browser, value):
        tour_url = os.getenv('TOUR_URL')
        tour_page_locators = TourPageLocators()
        locator_tab = tour_page_locators.TAB[value]['part 1'] + tour_url \
                      + tour_page_locators.TAB[value]['part 2']
        locator_content = tour_page_locators.CONTENT[value]

        with allure.step('Проверяем результат'):
            with allure.step(f'Проверяем, что открыта вкладка "{value}"'):
                class_tab = browser.element(locator_tab).get(query.attribute('class'))
                assert 'active' in class_tab
            with allure.step(f'Проверяем, что отображается содержимое вкладки {value}'):
                browser.all(locator_content).should(have.size_greater_than(0))

    def button_click(self, browser, value):
        tour_page_locators = TourPageLocators()
        locator_button = tour_page_locators.BUTTON[value]

        with allure.step(f'Нажимаем кнопку "{value}"'):
            browser.element(locator_button).click()

    def assert_date_and_price(self, browser):
        tour_page_locators = TourPageLocators()
        locator_title = tour_page_locators.TITLE
        locator_date = tour_page_locators.DATE
        locator_price = tour_page_locators.PRICE

        with allure.step('Проверяем результат'):
            with allure.step('Проверяем заголовок'):
                browser.element(locator_title).should(have.text('БЛИЖАЙШИЕ ПОХОДЫ'))
                browser.element(locator_title).should(be.visible)
            with allure.step('Проверяем, что отображаются данные со сроками и стоимостью походов'):
                browser.all(locator_date).should(have.size_greater_than(1))
                browser.all(locator_price).should(have.size_greater_than(0))

