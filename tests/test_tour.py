import os
import allure
from allure_commons.types import Severity
from vpoxod_tests.model import app


@allure.tag('critical')
@allure.severity(Severity.CRITICAL)
@allure.feature('UI-тесты vpoxod.ru')
@allure.story('Действия на странице похода')
@allure.title('Посмотреть информацию о маршруте')
def test_tour_open_tab_route(setup_browser):
    base_url = os.getenv('BASE_URL')
    tour_url = os.getenv('TOUR_URL')
    browser = setup_browser

    app.open_page(browser, f'{base_url}{tour_url}#content-top')
    app.tour_page.tab_click(browser, 'Маршруты')

    app.tour_page.assert_tab_info(browser, 'Маршруты')


@allure.tag('critical')
@allure.severity(Severity.CRITICAL)
@allure.feature('UI-тесты vpoxod.ru')
@allure.story('Действия на странице похода')
@allure.title('Посмотреть информацию о сроках и стоимости')
def test_tour_open_date_and_price(setup_browser):
    base_url = os.getenv('BASE_URL')
    tour_url = os.getenv('TOUR_URL')
    browser = setup_browser

    app.open_page(browser, f'{base_url}{tour_url}#content-top')
    app.tour_page.button_click(browser, 'Сроки походов')

    app.tour_page.assert_date_and_price(browser)


@allure.tag('critical')
@allure.severity(Severity.CRITICAL)
@allure.feature('UI-тесты vpoxod.ru')
@allure.story('Действия на странице похода')
@allure.title('Посмотреть отзывы о походе')
def test_tour_open_feedback(setup_browser):
    base_url = os.getenv('BASE_URL')
    tour_url = os.getenv('TOUR_URL')
    browser = setup_browser

    app.open_page(browser, f'{base_url}{tour_url}#content-top')
    app.tour_page.tab_click(browser, 'Отзывы')

    app.tour_page.assert_tab_info(browser, 'Отзывы')




