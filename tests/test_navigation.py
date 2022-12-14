import allure
from allure_commons.types import Severity
from vpoxod_tests.model import app


@allure.tag('critical')
@allure.severity(Severity.CRITICAL)
@allure.feature('UI-тесты vpoxod.ru')
@allure.story('Навигация по сайту')
@allure.title('Найти все походы на Алтай')
def test_open_tours_altai(setup_browser):
    browser = setup_browser
    app.main_page.open(browser)

    app.main_menu.first_level_click(browser, 'Регионы')
    app.left_menu.item_click(browser, 'Россия')
    app.left_menu.item_click(browser, 'Алтай')

    app.list_tours_page.assert_tours_region(browser, 'Алтай')


@allure.tag('critical')
@allure.severity(Severity.CRITICAL)
@allure.feature('UI-тесты vpoxod.ru')
@allure.story('Навигация по сайту')
@allure.title('Найти все велосипедные походы')
def test_open_tours_bicycle(setup_browser):
    browser = setup_browser
    app.main_page.open(browser)

    app.main_menu.first_level_hover(browser, 'Типы')
    app.main_menu.second_level_click(browser, 'Вело')

    app.list_tours_page.assert_tours_types(browser, 'Вело')


@allure.tag('critical')
@allure.severity(Severity.CRITICAL)
@allure.feature('UI-тесты vpoxod.ru')
@allure.story('Навигация по сайту')
@allure.title('Найти все летние походы')
def test_open_tours_summer(setup_browser):
    browser = setup_browser
    app.main_page.open(browser)

    app.main_menu.first_level_hover(browser, 'Путешествия')
    app.main_menu.second_level_click(browser, 'Календарь дат')
    app.left_menu.seazon_select(browser, 'Лето')

    app.list_tours_page.assert_tours_seazon(browser, 'Лето')


@allure.tag('critical')
@allure.severity(Severity.CRITICAL)
@allure.feature('UI-тесты vpoxod.ru')
@allure.story('Навигация по сайту')
@allure.title('Найти описание снаряжения (обувь)')
def test_open_equipment_footwear(setup_browser):
    browser = setup_browser
    app.main_page.open(browser)

    app.main_menu.first_level_hover(browser, 'Полезно знать')
    app.main_menu.second_level_click(browser, 'Списки снаряжения')
    app.equipment_page.select_checkbox(browser, 'Обувь')

    app.equipment_page.assert_list_equipment(browser, 'Обувь')







