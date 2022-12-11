# Проект автоматизации тестирования UI для сайта "Клуб приключений"
<img width="1399" alt="image" src="https://user-images.githubusercontent.com/109241600/206396626-cd4bb46b-637e-423f-8859-4eb1062a508f.png">

<a href="https://www.vpoxod.ru" target="_blank">«Клуб Приключений»</a> — это сайт, на котором можно выбрать для себя интересный активный тур (поход) по России и другим странам.

## Содержание
+ [Технологии и инструменты](#Технологии)
+ [Тест-кейсы](#Тесты)
+ [Запуск автотестов из Jenkins](#Jenkins) 
+ [Оповещение о результатах через Telegram-бот](#Telegram) 
+ [Отчеты о прохождении тестов Allure report](#Allure) 
+ [Интеграция с Allure TestOPS](#TestOPS) 
+ [Интеграция с Jira](#Jira) 

## <a name="Технологии">Технологии и инструменты, использованные в проекте</a>
<p align="center">
<img width="6%" title="PyCharm" src="images/logo/pycharm.svg">
<img width="6%" title="Python" src="images/logo/python.svg">
<img width="6%" title="Pytest" src="images/logo/pytest.svg">
<img width="6%" title="Selenium" src="images/logo/selenium.png">
<img width="6%" title="Selene" src="images/logo/selene.png">
<img width="6%" title="Selenoid" src="images/logo/Selenoid.svg">
<img width="6%" title="GitHub" src="images/logo/GitHub.svg">
<img width="6%" title="Jenkins" src="images/logo/Jenkins.svg">  
<img width="6%" title="AllureReport" src="images/logo/Allure_Report.svg">  
<img width="6%" title="AllureTestOPS" src="images/logo/Allure_TO.svg"> 
<img width="6%" title="Telegram" src="images/logo/Telegram.svg">  
<img width="6%" title="Jira" src="images/logo/jira.svg"> 
</p>

## <a name="Тесты">Тест-кейсы</a>
###### Навигация по сайту:
  - Найти все походы на Алтай
  - Найти все велосипедные походы
  - Найти все летние походы
  - Найти описание снаряжения (обувь)
###### Действия на странице похода:
  - Посмотреть информацию о маршруте
  - Посмотреть информацию о сроках и стоимости
  - Посмотреть отзывы о походе
  
## <a name="Jenkins">Запуск автотестов из Jenkins</a>
Для удаленного запуска автотестов в <a href="https://jenkins.autotests.cloud/job/002-annazukowska-python-vpoxod_ui/" target="_blank">Jenkins</a> создана задача (job), настроена и связана с репозиторием в GitHub.

<img width="1234" alt="image" src="https://user-images.githubusercontent.com/109241600/206928850-b4616595-65a5-4bdd-bdf3-f4ae78c4f5f2.png">

## <a name="Telegram">Уведомление о результатах тестирования через Telegram-бот</a>
После завершения тестов приходит такое оповещение в Telegram с помощью заранее созданного Telegram-бота, привязанного к задаче в Jenkins.

<img width="359" alt="image" src="https://user-images.githubusercontent.com/109241600/206928869-86898176-d7ac-4c52-a01d-d27c73a69645.png">

## <a name="Allure">Отчеты о прохождении тестов Allure report</a>
После завершения тестов также формируются отчеты <a href="https://jenkins.autotests.cloud/job/002-annazukowska-python-vpoxod_ui/6/allure/#behaviors/10c615c00b45c542038c6c30e1341f76" target="_blank">Allure report</a>, которые можно посмотреть со страницы задачи в Jenkins.

<img width="1430" alt="image" src="https://user-images.githubusercontent.com/109241600/206929379-0138c81e-a73d-4e0a-bc9b-17cfc02a0a54.png">
<img width="1432" alt="image" src="https://user-images.githubusercontent.com/109241600/206929433-59c19efa-d3c7-4fb7-914b-264740776a40.png">

К отчетам прикреплены логи, скриншот и видеозапись прохождения тестов
<img width="780" alt="image" src="https://user-images.githubusercontent.com/109241600/206929302-1d0dd425-43ae-4462-b0c5-ad93eadc9145.png">

## <a name="TestOPS">Интеграция с Allure TestOPS</a>
Настроена интеграция Jenkins с Allure TestOPS.
При первом после интеграции прохождении тестов в Jenkins, в Allure TestOPS были автоматически созданы такие тест-кейсы:


