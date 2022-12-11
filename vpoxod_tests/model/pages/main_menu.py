import allure


class MainMenuLocators():
    FIRST_LEVEL_LOCATORS = {
        'Регионы': '.item_1 a[href="/route"]',
        'Типы': '.item_2 a[href="/types"]',
        'Путешествия': '.item_10 > a[href*="name"]',
        'Полезно знать': '.item_6 a[href="/faq"]'
    }
    SECOND_LEVEL_LOCATORS = {
        'Вело': '.main_navigation a[href="/types/6-Velo"]',
        'Календарь дат': '.main_navigation_inner a[href*="date"]',
        'Списки снаряжения': '.item_6 a[href="/equip#content-top"]'
    }


class MainMenu():
    def first_level_click(self, browser, value):
        main_menu_locators = MainMenuLocators()
        locator_first_level_element = main_menu_locators.FIRST_LEVEL_LOCATORS[value]

        with allure.step(f'В хедере нажимаем на кнопку "{value}" '):
            browser.all(locator_first_level_element).first.click()

    def first_level_hover(self, browser, value):
        main_menu_locators = MainMenuLocators()
        locator_first_level_element = main_menu_locators.FIRST_LEVEL_LOCATORS[value]

        with allure.step(f'В хедере наводим курсор на кнопку "{value}"'):
            browser.all(locator_first_level_element).first.hover()

    def second_level_click(self, browser, value):
        main_menu_locators = MainMenuLocators()
        locator_second_level_element = main_menu_locators.SECOND_LEVEL_LOCATORS[value]

        with allure.step(f'В открывшемся меню выбираем раздел "{value}"'):
            browser.with_(timeout=8).element(locator_second_level_element).click()






