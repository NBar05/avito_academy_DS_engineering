from one_hot_encoder import fit_transform
import pytest


def test_1_len():
    assert len(fit_transform(['', 2, '1', 1, ('12', '341')])) == 5


def test_2_one_cat():
    assert [el[1][0] == 1 for el in fit_transform(['', '', '', ''])] == [True, True, True, True]


def test_3_equal():
    cities = ['Moscow', 'New York', 'Moscow', 'London']
    expected = [
        ('Moscow', [0, 0, 1]),
        ('New York', [0, 1, 0]),
        ('Moscow', [0, 0, 1]),
        ('London', [1, 0, 0]),
    ]

    assert fit_transform(cities) == expected


def test_4_raise():
    with pytest.raises(TypeError) as exc_info:
        _ = fit_transform()

    assert str(exc_info.value) == 'expected at least 1 arguments, got 0'
