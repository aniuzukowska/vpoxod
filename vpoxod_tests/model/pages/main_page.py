import allure


class MainPage():
    def open(self, browser):
        with allure.step(f'Открываем главную страницу'):
            browser.open('')

