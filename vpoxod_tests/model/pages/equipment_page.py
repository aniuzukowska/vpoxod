import allure
from selene import query
from selene.support.conditions import have


class EquipmentPage():
    types_equipment = {
        'Обувь': {
            'checkbox': '.checkbox[data-category="4"]',
            'title': '.js-equip-category[data-key="4"] > *:first-child',
            'content': '.js-equip-category[data-key="4"] .info'
        }
    }

    def select_checkbox(self, browser, value):
        with allure.step(f'На открывшейся странице отмечаем чек-бокс "{value}"'):
            browser.with_(timeout=6).element(self.types_equipment[value]['checkbox']).click()

    def assert_list_equipment(self, browser, value):
        with allure.step('Проверяем результат'):
            with allure.step(f'Проверяем, что чек-бокс "{value}" выделен как отмеченный'):
                class_checkbox = browser.with_(timeout=6).\
                    element(self.types_equipment[value]['checkbox']).get(query.attribute('class'))
                assert 'checked' in class_checkbox

            with allure.step('Проверяем заголовок раздела снаряжения'):
                browser.element(self.types_equipment[value]['title']).should(have.text(f'{value}'))

            with allure.step(f'Проверяем, что отображаются блоки с информацией об экипировке {value}'):
                browser.all(self.types_equipment[value]['content']).should(have.size_greater_than(0))

