import allure
from selene import query
from selene.support.conditions import have, be


def test_open_tours_altai(setup_browser):
    browser = setup_browser
    with allure.step('Переходим на главную страницу'):
        browser.open('https://www.vpoxod.ru')

    with allure.step('В хедере нажимаем на кнопку "Регионы"'):
        browser.all(".item_1 a[href='/route']").first.click()

    with allure.step('В меню слева выбираем раздел "Россия"'):
        browser.all(".list-parent a[href='/route/russia']").first.click()

    with allure.step('В меню слева выбираем раздел "Алтай"'):
        browser.element(".list-parent a[href='/route/altai']").click()

    with allure.step('Проверяем результат'):
        with allure.step('Проверяем url'):
            browser.with_(timeout=6).should(have.url('https://www.vpoxod.ru/route/altai'))
        with allure.step('Проверяем заголовок страницы'):
            browser.with_(timeout=6).element('.main_top > *:first-child').should(have.text('ТУРЫ НА АЛТАЙ'))
        with allure.step('Проверяем, что отображаются блоки с информацией о турах'):
            browser.with_(timeout=6).all('.main_page_hikes_list article').should(have.size_greater_than(0))
        with allure.step('Проверяем, что отображаемые туры относятся к Алтаю'):
            list_regions = browser.with_(timeout=6).all('.scroll-on-hover')
            for region in list_regions:
                region.should(have.text('Алтай'))


def test_open_tours_bicycle(setup_browser):
    browser = setup_browser
    with allure.step('Переходим на главную страницу'):
        browser.open('https://www.vpoxod.ru')
    with allure.step('В хедере наводим курсор на кнопку "Типы"'):
        browser.all(".item_2 a[href='/types']").first.hover()
    with allure.step('В открывшемся меню выбираем раздел "Вело"'):
        browser.element(".main_navigation a[href='/types/6-Velo']").click()

    with allure.step('Проверяем результат'):
        with allure.step('Проверяем url'):
            browser.should(have.url('https://www.vpoxod.ru/types/6-Velo'))
        with allure.step('Проверяем заголовок страницы'):
            browser.element('.main_top > *:first-child').should(have.text('ВЕЛОПОХОДЫ: ВСЕ МАРШРУТЫ'))
        with allure.step('Проверяем, что отображаются блоки с информацией о турах'):
            browser.all('.main_page_hikes_list article').should(have.size_greater_than(0))
        with allure.step('Проверяем, что отображаемые туры относятся к Вело'):
            groups_logo_kinds = browser.all('.route_search_tab_icons')
            for group in groups_logo_kinds:
                group.element("*[data-original-title*='/types/6-Velo']").should(be.visible)


def test_open_tours_summer(setup_browser):
    browser = setup_browser
    with allure.step('Переходим на главную страницу'):
        browser.open('https://www.vpoxod.ru')
    with allure.step('В хедере наводим курсор на кнопку "Путешествия"'):
        browser.all(".item_10 > a[href*='name']").first.hover()
    with allure.step('В открывшемся меню выбираем раздел "Календарь дат"'):
        browser.element(".main_navigation_inner a[href*='date']").click()
    with allure.step('На панели слева нажимаем кнопку "Лето"'):
        browser.with_(timeout=6).element(".toggle-navigation-multiple *[data-value='2']").click()
    with allure.step('Нажимаем на кнопку "Показать"'):
        browser.with_(timeout=6).element('#search-popper .btn-orange').click()

    with allure.step('Проверяем результат'):
        with allure.step('Проверяем, что кнопка "Лето" выделена как нажатая'):
            class_winter = browser.element(".toggle-navigation-multiple *[data-value='2']").get(query.attribute('class'))
            assert 'active' in class_winter
        with allure.step('Проверяем, что отображаются блоки с информацией о турах'):
            browser.all('.item_header').should(have.size_greater_than(0))
            browser.all('.first.item_1').should(have.size_greater_than(1))
        with allure.step('Проверяем, что отображаемые туры начинаются летом'):
            start_date_tours = browser.all(".table_term *[itemprop='startDate']")
            for date in start_date_tours:
                date_str = date.get(query.attribute('content'))
                month = date_str[5:7:]
                assert month in ['06', '07', '08']


def test_open_equipment_footwear(setup_browser):
    browser = setup_browser
    with allure.step('Переходим на главную страницу'):
        browser.open('https://www.vpoxod.ru')
    with allure.step('В хедере наводим курсор на кнопку "Полезно знать"'):
        browser.all(".item_6 a[href='/faq']").first.hover()
    with allure.step('В открывшемся меню выбираем раздел "Списки снаряжения"'):
        browser.element(".item_6 a[href='/equip#content-top']").click()
    with allure.step('На открывшейся странице отмечаем чек-бокс "Обувь"'):
        browser.with_(timeout=6).element(".checkbox[data-category='4']").click()

    with allure.step('Проверяем результат'):
        with allure.step('Проверяем, что чек-бокс "Обувь" выделен как отмеченный'):
            class_footwear = browser.with_(timeout=6).element(".checkbox[data-category='4']").get(query.attribute('class'))
            assert 'checked' in class_footwear
        with allure.step('Проверяем заголовок раздела снаряжения'):
            browser.element(".js-equip-category[data-key='4'] > *:first-child").should(have.text('Обувь'))
        with allure.step('Проверяем, что отображаются блоки с информацией об обуви'):
            browser.all(".js-equip-category[data-key='4'] .info").should(have.size_greater_than(0))





