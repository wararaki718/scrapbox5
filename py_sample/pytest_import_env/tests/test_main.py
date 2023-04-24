import importlib
from typing import Callable

import pytest
from _pytest.monkeypatch import MonkeyPatch


@pytest.fixture
def sub_env(monkeypatch: MonkeyPatch) -> None:
    monkeypatch.setenv("CALC_TYPE", "sub")


@pytest.fixture
def mul_env(monkeypatch: MonkeyPatch) -> None:
    monkeypatch.setenv("CALC_TYPE", "mul")


@pytest.fixture
def add_calc() -> Callable:
    import app.main
    importlib.reload(app.main)

    from app.main import calc
    return calc


@pytest.fixture
def sub_calc(sub_env: None) -> Callable:
    import app.main
    importlib.reload(app.main)

    from app.main import calc
    return calc


@pytest.fixture
def mul_calc(mul_env: None) -> Callable:
    import app.main
    importlib.reload(app.main)
    
    from app.main import calc
    return calc


def test_add_calc(add_calc: Callable) -> None:
    a = 10
    b = 1
    result = add_calc(a, b)
    assert result == 11


def test_sub_calc(sub_calc: Callable) -> None:
    a = 10
    b = 1
    result = sub_calc(a, b)
    assert result == 9


def test_mul_calc(mul_calc: Callable) -> None:
    a = 10
    b = 1
    result = mul_calc(a, b)
    assert result == 10
