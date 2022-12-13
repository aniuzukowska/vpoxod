import os
import allure
from selene import query, command
from selene.support.conditions import have, be


class TourPage():
    title = '.route_table .route_title'
    button = {'Сроки походов': '.route_button'}
    tab = {
        'Маршруты': {'part 1': '.tabs_title a[href="', 'part 2': '/about#tabs"]'},
        'Отзывы': {'part 1': '.tabs_title a[href="', 'part 2': '/responses#tabs"]'}
    }
    content = {
        'Маршруты': '.route_description_days *',
        'Отзывы': '.comments_list article'
    }
    date = '.first.item_1'
    price = '.tippy.table_price_left'

    def tab_click(self, browser, value):
        tour_url = os.getenv('TOUR_URL')
        locator_tab = self.tab[value]['part 1'] + tour_url + self.tab[value]['part 2']

        with allure.step(f'Переходим на вкладку "{value}"'):
            browser.element(locator_tab).perform(command.js.scroll_into_view)
            browser.element(locator_tab).click()

    def assert_tab_info(self, browser, value):
        tour_url = os.getenv('TOUR_URL')
        locator_tab = self.tab[value]['part 1'] + tour_url + self.tab[value]['part 2']

        with allure.step('Проверяем результат'):
            with allure.step(f'Проверяем, что открыта вкладка "{value}"'):
                class_tab = browser.element(locator_tab).get(query.attribute('class'))
                assert 'active' in class_tab
            with allure.step(f'Проверяем, что отображается содержимое вкладки {value}'):
                browser.all(self.content[value]).should(have.size_greater_than(0))

    def button_click(self, browser, value):
        with allure.step(f'Нажимаем кнопку "{value}"'):
            browser.element(self.button[value]).click()

    def assert_date_and_price(self, browser):
        with allure.step('Проверяем результат'):
            with allure.step('Проверяем заголовок'):
                browser.element(self.title).should(have.text('БЛИЖАЙШИЕ ПОХОДЫ'))
                browser.element(self.title).should(be.visible)
            with allure.step('Проверяем, что отображаются данные со сроками и стоимостью походов'):
                browser.all(self.date).should(have.size_greater_than(1))
                browser.all(self.price).should(have.size_greater_than(0))

