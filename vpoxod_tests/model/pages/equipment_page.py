import allure
from selene import query
from selene.support.conditions import have


class EquipmentPage():
    def select_checkbox(self, browser, value):
        element = None
        if value == 'Обувь':
            element = browser.with_(timeout=6).element(".checkbox[data-category='4']")
        with allure.step(f'На открывшейся странице отмечаем чек-бокс "{value}"'):
            element.click()

    def assert_list_equipment(self, browser, value):
        element = None
        blocks = None
        if value == 'Обувь':
            element = browser.with_(timeout=6).element(".checkbox[data-category='4']")
            blocks = browser.all(".js-equip-category[data-key='4'] .info")

        with allure.step('Проверяем результат'):
            with allure.step(f'Проверяем, что чек-бокс "{value}" выделен как отмеченный'):
                class_equipment = element.get(query.attribute('class'))
                assert 'checked' in class_equipment

            with allure.step('Проверяем заголовок раздела снаряжения'):
                browser.element(".js-equip-category[data-key='4'] > *:first-child").should(have.text(f'{value}'))

            with allure.step(f'Проверяем, что отображаются блоки с информацией об экипировке {value}'):
                blocks.should(have.size_greater_than(0))

