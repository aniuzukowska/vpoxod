from vpoxod_tests.model import app


def test_tour_open_tab_route(setup_browser):
    browser = setup_browser
    app.open_page(browser, 'https://www.vpoxod.ru/route/altai/oroktojskim-hrebtom-k-akkemskomu-ozeru-i-podnozu-beluhi#content-top')
    app.tour_page.tab_click(browser, 'Маршруты')
    app.tour_page.assert_tab_info(browser, 'Маршруты')


def test_tour_open_date_and_price(setup_browser):
    browser = setup_browser
    app.open_page(browser, 'https://www.vpoxod.ru/route/altai/oroktojskim-hrebtom-k-akkemskomu-ozeru-i-podnozu-beluhi#content-top')
    app.tour_page.button_click(browser, 'Сроки походов')
    app.tour_page.assert_date_and_price(browser)


def test_tour_open_feedback(setup_browser):
    browser = setup_browser
    app.open_page(browser, 'https://www.vpoxod.ru/route/altai/oroktojskim-hrebtom-k-akkemskomu-ozeru-i-podnozu-beluhi#content-top')
    app.tour_page.tab_click(browser, 'Отзывы')
    app.tour_page.assert_tab_info(browser, 'Отзывы')




