import urllib.request
import json
import pytest
from unittest.mock import patch


API_URL = 'http://worldclockapi.com/api/json/utc/now'

YMD_SEP = '-'
YMD_SEP_INDEX = 4
YMD_YEAR_SLICE = slice(None, YMD_SEP_INDEX)

DMY_SEP = '.'
DMY_SEP_INDEX = 5
DMY_YEAR_SLICE = slice(DMY_SEP_INDEX + 1, DMY_SEP_INDEX + 5)


def what_is_year_now() -> int:
    """
    Получает текущее время из API-worldclock и извлекает из поля 'currentDateTime' год

    Предположим, что currentDateTime может быть в двух форматах:
      * YYYY-MM-DD - 2019-03-01
      * DD.MM.YYYY - 01.03.2019
    """
    with urllib.request.urlopen(API_URL) as resp:
        resp_json = json.load(resp)

    datetime_str = resp_json['currentDateTime']

    if datetime_str[YMD_SEP_INDEX] == YMD_SEP:
        year_str = datetime_str[YMD_YEAR_SLICE]
    elif datetime_str[DMY_SEP_INDEX] == DMY_SEP:
        year_str = datetime_str[DMY_YEAR_SLICE]
    else:
        raise ValueError('Invalid format')

    return int(year_str)


def test_work_case():
    assert 2022 == what_is_year_now()


def test_dash_case():
    with patch("json.load") as mocked_json_load:
        mocked_json_load.return_value = {'currentDateTime': '2019-10-07T21:32Z'}

        assert 2019 == what_is_year_now()


def test_dot_case():
    with patch("json.load") as mocked_json_load:
        mocked_json_load.return_value = {'currentDateTime': '07.10.2020T21:21Z'}

        assert 2020 == what_is_year_now()


def test_invalid_case():
    with patch("json.load") as mocked_json_load, pytest.raises(ValueError) as exc_info:
        mocked_json_load.return_value = {'currentDateTime': '450450450'}

        what_is_year_now()
        assert str(exc_info.value) == 'Invalid format'


if __name__ == '__main__':
    year = what_is_year_now()
    exp_year = 2022

    print(year)
    assert year == exp_year
