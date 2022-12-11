import allure


class LeftMenuLocators():
    REGIONS = {
        'Россия': '.list-parent a[href="/route/russia"]',
        'Алтай': '.list-parent a[href="/route/altai"]'
    }
    SEAZON_BUTTONS = {
        'Лето': '.toggle-navigation-multiple *[data-value="2"]'
    }
    BUTTON_TO_SHOW = '#search-popper .btn-orange'


class LeftMenu():
    def item_click(self, browser, value):
        left_menu_locators = LeftMenuLocators()
        locator_item = left_menu_locators.REGIONS[value]

        with allure.step(f'В меню слева выбираем раздел "{value}"'):
            browser.all(locator_item).first.click()

    def seazon_select(self, browser, value):
        left_menu_locators = LeftMenuLocators()
        locator_seazon_button = left_menu_locators.SEAZON_BUTTONS[value]
        locator_button_to_show = left_menu_locators.BUTTON_TO_SHOW

        with allure.step(f'На панели слева нажимаем кнопку "{value}"'):
            browser.element(locator_seazon_button).click()
        with allure.step('Нажимаем на кнопку "Показать"'):
            browser.with_(timeout=6).element(locator_button_to_show).click()









