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


<a name="Технологии">

## Технологии и инструменты, использованные в проекте
<p align="center">
<img width="6%" title="PyCharm" src="vpoxod_tests/utils/images/pycharm.svg">
<img width="6%" title="Python" src="vpoxod_tests/utils/images/python.svg">
<img width="6%" title="Pytest" src="vpoxod_tests/utils/images/pytest.svg">
<img width="6%" title="Selenium" src="vpoxod_tests/utils/images/selenium.png">
<img width="6%" title="Selene" src="vpoxod_tests/utils/images/selene.png">
<img width="6%" title="Selenoid" src="vpoxod_tests/utils/images/Selenoid.svg">
<img width="6%" title="GitHub" src="vpoxod_tests/utils/images/GitHub.svg">
<img width="6%" title="Jenkins" src="vpoxod_tests/utils/images/Jenkins.svg">  
<img width="6%" title="AllureReport" src="vpoxod_tests/utils/images/Allure_Report.svg">  
<img width="6%" title="AllureTestOPS" src="vpoxod_tests/utils/images/Allure_TO.svg"> 
<img width="6%" title="Telegram" src="vpoxod_tests/utils/images/Telegram.svg">  
<img width="6%" title="Jira" src="vpoxod_tests/utils/images/jira.svg"> 
</p>



<a name="Тесты">

## Тест-кейсы
###### Навигация по сайту:
  - Найти все походы на Алтай
  - Найти все велосипедные походы
  - Найти все летние походы
  - Найти описание снаряжения (обувь)
###### Действия на странице похода:
  - Посмотреть информацию о маршруте
  - Посмотреть информацию о сроках и стоимости
  - Посмотреть отзывы о походе
  


<a name="Jenkins">

## Запуск автотестов из Jenkins
Для удаленного запуска автотестов в <a href="https://jenkins.autotests.cloud/job/002-annazukowska-python-vpoxod_ui/" target="_blank">Jenkins</a> создана задача (job), настроена и связана с репозиторием в GitHub.
При подготовке сборки можно выбрать версию браузера Chrome, разрешение экрана, а также какие именно тесты будут запущены: 
- все тесты
- только тесты из раздела 'Навигация по сайту'
- только тесты из раздела 'Действия на странице похода'

![Запись экрана 2022-12-18 в 02 44 43](https://user-images.githubusercontent.com/109241600/208267187-50ebdc5a-36eb-426e-8ee0-f5c81bc2871f.gif)



<a name="Telegram">

## Уведомление о результатах тестирования через Telegram-бот
После завершения тестов приходит такое оповещение в Telegram с помощью заранее созданного Telegram-бота, привязанного к задаче в Jenkins.

<img width="343" alt="image" src="https://user-images.githubusercontent.com/109241600/206930833-321274f8-94e6-4ebf-9782-02310782525d.png">



<a name="Allure">

## Отчеты о прохождении тестов Allure report
После завершения тестов также формируются отчеты <a href="https://jenkins.autotests.cloud/job/002-annazukowska-python-vpoxod_ui/6/allure/#behaviors/10c615c00b45c542038c6c30e1341f76" target="_blank">Allure report</a>, которые можно посмотреть со страницы задачи в Jenkins.

<img width="1430" alt="image" src="https://user-images.githubusercontent.com/109241600/206929379-0138c81e-a73d-4e0a-bc9b-17cfc02a0a54.png">
<img width="1432" alt="image" src="https://user-images.githubusercontent.com/109241600/206929433-59c19efa-d3c7-4fb7-914b-264740776a40.png">

К отчетам прикреплены логи, скриншот и видеозапись прохождения тестов
<img width="780" alt="image" src="https://user-images.githubusercontent.com/109241600/206929302-1d0dd425-43ae-4462-b0c5-ad93eadc9145.png">



<a name="TestOPS">

## Интеграция с Allure TestOPS
Настроена интеграция Jenkins с Allure TestOPS.
При первом после интеграции прохождении тестов в Jenkins, в Allure TestOPS были автоматически созданы такие тест-кейсы:

<img width="1434" alt="image" src="https://user-images.githubusercontent.com/109241600/206929969-59fa14d9-14ed-480c-842b-57c7a0e1e63d.png">

Можно посмотреть историю выполненных прогонов:
<img width="1436" alt="image" src="https://user-images.githubusercontent.com/109241600/206930141-02c17beb-a7f1-4ef5-8c23-2ed48873b7a9.png">
<img width="1434" alt="image" src="https://user-images.githubusercontent.com/109241600/206930178-fb4c6d4c-284e-4490-90af-28b791cdf2af.png">



<a name="Jira">

## Интеграция с Jira
Настроена интеграция Allure TestOPS с Jira. К задаче в Jira привязаны тест-кейсы и прогон с результатами тестирования из Allure TestOPS.

<img width="1431" alt="image" src="https://user-images.githubusercontent.com/109241600/206930484-8d2ffc39-f863-492e-966f-b6ee5f0f23a2.png">
<img width="1432" alt="image" src="https://user-images.githubusercontent.com/109241600/206930506-968cb7ea-9095-41cd-b1c9-a757f1c7eaa2.png">

