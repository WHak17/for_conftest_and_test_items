# for_conftest_and_test_items
запуск автотестов для разных языков интерфейса


#Тестирование интернет-магазина с разными языками

Этот проект предназначен для тестирования интернет-магазина с возможностью выбора различных языков через аргумент командной строки.

## Как запустить тесты?

Запустите следующие команды:

```bash
pip install pytest selenium
python -m pytest --language=es test_items.py
