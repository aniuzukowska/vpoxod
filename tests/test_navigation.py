import allure
from selene.support.conditions import have, be


def test_open_tours_to_altai(setup_browser):
    browser = setup_browser
    with allure.step('Переходим на главную страницу'):
        browser.open('https://www.vpoxod.ru')

    with allure.step('Нажимаем на кнопку "Регионы"'):
        browser.all(".item_1 a[href='/route']").first.click()

    with allure.step('Выбираем раздел "Россия"'):
        browser.all(".list-parent a[href='/route/russia']").first.click()

    with allure.step('Выбираем раздел "Алтай"'):
        browser.element(".list-parent a[href='/route/altai']").click()

    with allure.step('Проверяем результат'):
        with allure.step('Проверяем url'):
            browser.should(have.url('https://www.vpoxod.ru/route/altai'))
        with allure.step('Проверяем, что отображается информация о турах'):
            browser.all('.main_page_hikes_list article').should(have.size_greater_than(0))














