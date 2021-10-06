1) запуск тестов c allure-отчетом:
выполнить команду в терминале
python -m pytest --alluredir=/bin/tests/reports

2) формирование allure-отчета в читаемом виде:
выполнить команду в терминале
allure serve \bin\tests\reports

3) запуск сервера selenium grid
выполнить команду в терминале:
java -jar selenium-server-standalone-3.141.59.jar

