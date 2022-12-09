import allure
from selene import query
from selene.support.conditions import have, be


class ListToursPage():
    def assert_tours_region(self, browser, value):
        region_url = None
        title = None
        if value == 'Алтай':
            region_url = 'https://www.vpoxod.ru/route/altai'
            title = 'ТУРЫ НА АЛТАЙ'

        with allure.step('Проверяем результат'):
            with allure.step('Проверяем url'):
                browser.with_(timeout=6).should(have.url(region_url))

            with allure.step('Проверяем заголовок страницы'):
                browser.with_(timeout=6).element('.main_top > *:first-child').should(have.text(title))

            with allure.step('Проверяем, что отображаются блоки с информацией о походах'):
                browser.with_(timeout=6).all('.main_page_hikes_list article').should(have.size_greater_than(0))

            with allure.step(f'Проверяем, что отображаемые походы относятся к региону {value}'):
                list_regions = browser.with_(timeout=6).all('.scroll-on-hover')
                for region in list_regions:
                    region.should(have.text(value))


    def assert_tours_types(self, browser, value):
        type_url = None
        title = None
        logo_css = None

        if value == 'Вело':
            type_url = 'https://www.vpoxod.ru/types/6-Velo'
            title = 'ВЕЛОПОХОДЫ: ВСЕ МАРШРУТЫ'
            logo_css = "*[data-original-title*='/types/6-Velo']"

        with allure.step('Проверяем результат'):
            with allure.step('Проверяем url'):
                browser.with_(timeout=6).should(have.url(type_url))
            with allure.step('Проверяем заголовок страницы'):
                browser.element('.main_top > *:first-child').should(have.text(title))
            with allure.step('Проверяем, что отображаются блоки с информацией о походах'):
                browser.all('.main_page_hikes_list article').should(have.size_greater_than(0))
            with allure.step(f'Проверяем, что отображаемые походы относятся к {value}'):
                groups_logo_kinds = browser.all('.route_search_tab_icons')
                for group in groups_logo_kinds:
                    group.element(logo_css).should(be.visible)

    def assert_tours_seazon(self, browser, value):
        seazon_months = None
        element = None

        if value == 'Лето':
            seazon_months = ['06', '07', '08']
            element = browser.with_(timeout=6).element(".toggle-navigation-multiple *[data-value='2']")

        with allure.step('Проверяем результат'):
            browser.all('.item_header a').first.should(be.clickable)

            with allure.step(f'Проверяем, что кнопка "{value}" выделена как нажатая'):
                class_seazon = element.get(query.attribute('class'))
                assert 'active' in class_seazon

            with allure.step('Проверяем, что отображаются блоки с информацией о походах'):
                browser.all('.item_header').with_(timeout=6).should(have.size_greater_than(0))
                browser.all('.first.item_1').with_(timeout=6).should(have.size_greater_than(1))

            with allure.step(f'Проверяем, что отображаемые походы начинаются в сезоне {value}'):
                start_date_tours = browser.all(".table_term *[itemprop='startDate']")
                for date in start_date_tours:
                    date_str = date.get(query.attribute('content'))
                    month = date_str[5:7:]
                    assert month in seazon_months






