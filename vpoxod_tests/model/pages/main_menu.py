import allure


class MainMenu():
    first_level_menu = {
        'Регионы': '.item_1 a[href="/route"]',
        'Типы': '.item_2 a[href="/types"]',
        'Путешествия': '.item_10 > a[href*="name"]',
        'Полезно знать': '.item_6 a[href="/faq"]'
    }
    second_level_menu = {
        'Вело': '.main_navigation a[href="/types/6-Velo"]',
        'Календарь дат': '.main_navigation_inner a[href*="date"]',
        'Списки снаряжения': '.item_6 a[href="/equip#content-top"]'
    }

    def first_level_click(self, browser, value):
        with allure.step(f'В хедере нажимаем на кнопку "{value}"'):
            browser.all(self.first_level_menu[value]).first.click()

    def first_level_hover(self, browser, value):
        with allure.step(f'В хедере наводим курсор на кнопку "{value}"'):
            browser.all(self.first_level_menu[value]).first.hover()

    def second_level_click(self, browser, value):
        with allure.step(f'В открывшемся меню выбираем раздел "{value}" '):
            browser.with_(timeout=10).element(self.second_level_menu[value]).click()







