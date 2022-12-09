import allure


class LeftMenu():
    def item_click(self, browser, value):
        element = None
        if value == 'Россия':
            element = browser.all(".list-parent a[href='/route/russia']").first
        elif value == 'Алтай':
            element = browser.element(".list-parent a[href='/route/altai']")

        with allure.step(f'В меню слева выбираем раздел "{value}"'):
            element.click()

    def seazon_select(self, browser, value):
        element = None
        if value == 'Лето':
            element = browser.with_(timeout=6).element(".toggle-navigation-multiple *[data-value='2']")

        with allure.step(f'На панели слева нажимаем кнопку "{value}"'):
            element.click()
        with allure.step('Нажимаем на кнопку "Показать"'):
            browser.with_(timeout=6).element('#search-popper .btn-orange').click()









