import allure


class MainMenu():
    def first_level_click(self, browser, value):
        element = None
        if value == 'Регионы':
            element = browser.all(".item_1 a[href='/route']").first
        with allure.step(f'В хедере нажимаем на кнопку "{value}"'):
            element.click()

    def first_level_hover(self, browser, value):
        element = None
        if value == 'Типы':
            element = browser.all(".item_2 a[href='/types']").first
        elif value == 'Путешествия':
            element = browser.all(".item_10 > a[href*='name']").first
        elif value == 'Полезно знать':
            element = browser.all(".item_6 a[href='/faq']").first
        with allure.step(f'В хедере наводим курсор на кнопку "{value}"'):
            element.hover()

    def second_level_click(self, browser, value):
        element = None
        if value == 'Вело':
            element = browser.element(".main_navigation a[href='/types/6-Velo']")
        elif value == 'Календарь дат':
            element = browser.element(".main_navigation_inner a[href*='date']")
        elif value == 'Списки снаряжения':
            element = browser.element(".item_6 a[href='/equip#content-top']")
        with allure.step(f'В открывшемся меню выбираем раздел "{value}"'):
            element.click()





