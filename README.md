UI тесты были написаны на Python, с использованием паттерна PageObject, прикручена отчетность в Allure.

Добавлены Allure Steps к тестам, Features/Titles/Severity
Добавлены Фикстуры для запуска тестов локально и удаленно
При падении тестов, производится снятие скриншота в Allure отчете
Добавлен скрипт clean.sh по отчиске /allure-results

Для того, чтобы запустить тесты локально, необходимо: 

1) Скачать к себе локально проект с гитлаба: 

git clone https://github.com/kraime/Tribuna-UI.git

2) Создать новое виртуальное окружение 

python3 -m venv <название окружения>

3) Установить все зависимости:

pip install -r requirements.txt

4) Запустить тесты

5) Сгенерировать Allure отчет и сразу же открыть его: 

allure generate --clean && allure open

