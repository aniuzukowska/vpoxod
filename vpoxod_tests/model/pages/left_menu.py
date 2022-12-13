import allure


class LeftMenu():
    regions = {
        'Россия': '.list-parent a[href="/route/russia"]',
        'Алтай': '.list-parent a[href="/route/altai"]'
    }
    button_seazon = {
        'Лето': '.toggle-navigation-multiple *[data-value="2"]'
    }
    button_to_show = '#search-popper .btn-orange'

    def item_click(self, browser, value):
        with allure.step(f'В меню слева выбираем раздел "{value}"'):
            browser.all(self.regions[value]).first.click()

    def seazon_select(self, browser, value):
        with allure.step(f'На панели слева нажимаем кнопку "{value}"'):
            browser.element(self.button_seazon[value]).click()
        with allure.step('Нажимаем на кнопку "Показать"'):
            browser.with_(timeout=6).element(self.button_to_show).click()









