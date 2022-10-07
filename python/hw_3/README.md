## Домашнее задание №3

Организация папки:

- issues.md - задание

- morse.py
- test_morse.py

- one_hot_encoder.py
- test_unittest_one_hot_encoder.py
- test_pytest_one_hot_encoder.py

- what_is_year_now.py
- test_what_is_year_now.py

- result_{i} - результат выполнения для каждого issue-{0i}

- fast_check.ipynb - ноутбук для прогона codestyle и файлов с тестом (вне дз, для личного пользования, но может быть удобен для проверки)


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

Для проведения pytest:

1. `cd path_to_folder_with_pyfile`
2. `pytest test_what_is_year_now.py > result_5.txt`
