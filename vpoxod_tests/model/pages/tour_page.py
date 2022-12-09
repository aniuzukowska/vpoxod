import allure
from selene import query, command
from selene.support.conditions import have, be


class TourPage():
    def tab_click(self, browser, value):
        element = None
        if value == 'Маршруты':
            element = browser.with_(timeout=6).element(".tabs_title a[href='/route/altai/oroktojskim-hrebtom-k-akkemskomu-ozeru-i-podnozu-beluhi/about#tabs']")
        elif value == 'Отзывы':
            element = browser.with_(timeout=6).element(".tabs_title a[href='/route/altai/oroktojskim-hrebtom-k-akkemskomu-ozeru-i-podnozu-beluhi/responses#tabs']")

        with allure.step(f'Переходим на вкладку "{value}"'):
            element.perform(command.js.scroll_into_view)
            element.click()

    def assert_tab_info(self, browser, value):
        element = None
        data = None
        if value == 'Маршруты':
            element = browser.with_(timeout=6).element(
                ".tabs_title a[href='/route/altai/oroktojskim-hrebtom-k-akkemskomu-ozeru-i-podnozu-beluhi/about#tabs']")
            data = browser.all('.route_description_days *')
        elif value == 'Отзывы':
            element = browser.with_(timeout=6).element(
                ".tabs_title a[href='/route/altai/oroktojskim-hrebtom-k-akkemskomu-ozeru-i-podnozu-beluhi/responses#tabs']")
            data = browser.all('.comments_list article')

        with allure.step('Проверяем результат'):
            with allure.step(f'Проверяем, что открыта вкладка "{value}"'):
                class_tab = element.get(query.attribute('class'))
                assert 'active' in class_tab
            with allure.step(f'Проверяем, что отображается содержимое вкладки {value}'):
                data.should(have.size_greater_than(0))

    def button_click(self, browser, value):
        element = None
        if value == 'Сроки походов':
            element = browser.element('.route_button')

        with allure.step(f'Нажимаем кнопку "{value}"'):
            element.click()

    def assert_date_and_price(self, browser):
        with allure.step('Проверяем результат'):
            with allure.step('Проверяем заголовок'):
                browser.element('.route_table .route_title').should(have.text('БЛИЖАЙШИЕ ПОХОДЫ'))
                browser.element('.route_table .route_title').should(be.visible)
            with allure.step('Проверяем, что отображаются данные со сроками и стоимостью походов'):
                browser.all('.first.item_1').should(have.size_greater_than(1))
                browser.all('.tippy.table_price_left').should(have.size_greater_than(0))

