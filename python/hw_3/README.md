## Домашнее задание №3

Организация папки (файлы для проверки выделены __жирным шрифтом__):

- issues.md - задание

- morse.py - функция, декодирующая строку из азбуки Морзе в английский
- __test_morse.py - код, дополненный doctest и pytest тестами (issue-01-02)__

- one_hot_encoder.py - функция, кодирующая значение в бинарное представление
- __test_unittest_one_hot_encoder.py - код с unittest тестами (issue-03)__
- __test_pytest_one_hot_encoder.py - код с pytest тестами (issue-04)__

- what_is_year_now.py - функция, возвращающая текущий год
- __test_what_is_year_now.py - код, дополненный тестами (issue-05)__

- __result_{i} - результат выполнения для каждого issue-{0i}__

- __htmlcov - папка с coverage html отчётами__

- fast_check.ipynb - ноутбук для прогона codestyle и файлов с тестом (вне дз, для личного пользования, но может быть удобен для проверки)


### Инструкции для запуска тестов

Необходимо скачать всю папку целиком, затем в зависимости от желаемой проверки:

### issue-01

Для проверки кода на основе doctest необходимо:

1. `cd path_to_folder_with_pyfile`
2. `python3 -m doctest -o NORMALIZE_WHITESPACE -o IGNORE_EXCEPTION_DETAIL test_morse.py > result_1.txt`

### issue-02

Для проведения pytest:

1. `cd path_to_folder_with_pyfile`
2. `pytest test_morse.py > result_2.txt`

### issue-03

Для проведения unittest:

1. `cd path_to_folder_with_pyfile`
2. `python3 -m unittest test_unittest_one_hot_encoder.py 2> result_3.txt`

### issue-04

Для проведения pytest:

1. `cd path_to_folder_with_pyfile`
2. `pytest test_pytest_one_hot_encoder.py > result_4.txt`

### issue-05

Для проведения pytest + генерации coverage html файлов:

1. `cd path_to_folder_with_pyfile`
2. `pytest test_what_is_year_now.py > result_5.txt`
3. `python3 -m pytest --cov . --cov-report html`

__test_what_is_year_now_py__ - интересуемый html-отчёт
