import allure
from selene import query
from selene.support.conditions import have


class EquipmentPageLocators():
    TYPES_EQUIPMENT = {
        'Обувь': {
            'checkbox': '.checkbox[data-category="4"]',
            'title': '.js-equip-category[data-key="4"] > *:first-child',
            'content': '.js-equip-category[data-key="4"] .info'
        }
    }


class EquipmentPage():
    def select_checkbox(self, browser, value):
        equipment_page_locators = EquipmentPageLocators()
        locator_checkbox = equipment_page_locators.TYPES_EQUIPMENT[value]['checkbox']

        with allure.step(f'На открывшейся странице отмечаем чек-бокс "{value}"'):
            browser.with_(timeout=6).element(locator_checkbox).click()

    def assert_list_equipment(self, browser, value):
        equipment_page_locators = EquipmentPageLocators()
        locator_checkbox = equipment_page_locators.TYPES_EQUIPMENT[value]['checkbox']
        locator_title = equipment_page_locators.TYPES_EQUIPMENT[value]['title']
        locator_content = equipment_page_locators.TYPES_EQUIPMENT[value]['content']

        with allure.step('Проверяем результат'):
            with allure.step(f'Проверяем, что чек-бокс "{value}" выделен как отмеченный'):
                class_checkbox = browser.with_(timeout=6).element(locator_checkbox).get(query.attribute('class'))
                assert 'checked' in class_checkbox

            with allure.step('Проверяем заголовок раздела снаряжения'):
                browser.element(locator_title).should(have.text(f'{value}'))

            with allure.step(f'Проверяем, что отображаются блоки с информацией об экипировке {value}'):
                browser.all(locator_content).should(have.size_greater_than(0))

