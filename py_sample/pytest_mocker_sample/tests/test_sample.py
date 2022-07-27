from functools import partial
from unittest.mock import patch

import pytest
from pytest_mock import MockerFixture

from app.sample import Sample


def test_create_object():
    sample = Sample()
    assert sample._value == 1


def test_create_use_mocker(mocker: MockerFixture):
    mocker.patch("app.sample.set_value", lambda: 2)
    sample = Sample()
    assert sample._value == 2


def test_create_use_patch():
    with patch("app.sample.set_value", lambda: 3):
        sample = Sample()
    assert sample._value == 3


@patch("app.sample.set_value", lambda: 4)
def test_create_use_patch_deco():
    sample = Sample()
    assert sample._value == 4


def test_list():
    sample = Sample()
    assert isinstance(sample._items, list)


@patch("os.listdir", lambda x: set())
def test_list_patch():
    sample = Sample()
    assert isinstance(sample._items, set)


def test_sample_method():
    sample = Sample()
    assert sample.method() == 1000


@patch("app.sample.Sample.method", partial(lambda: 5))
def test_sample_method_patch():
    sample = Sample()
    assert sample.method() == 5



@pytest.fixture
def sample_fixture() -> Sample:
    return Sample()


def test_fixture_method(sample_fixture: Sample):
    assert sample_fixture._value == 1


## error: _value is not class field
# @patch("app.sample.Sample._value", 1000)
# def test_fixture_method_patch(sample_fixture: Sample):
#     assert sample_fixture._value == 1000


@patch("app.sample.Sample.method", partial(lambda: 10))
def test_fixture_method_patch(sample_fixture: Sample):
    assert sample_fixture.method() == 10


def test_fixture_method_class_field(sample_fixture: Sample):
    assert sample_fixture._field == 3000


@patch("app.sample.Sample._field", 10)
def test_fixture_method_class_field(sample_fixture: Sample):
    assert sample_fixture._field == 10


def test_create_use_mocker(mocker: MockerFixture, sample_fixture: Sample):
    mocker.patch("app.sample.Sample._field", 2)
    assert sample_fixture._field == 2
