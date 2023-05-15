from sample.main import add


def test_add() -> None:
    result = add(1, 1)
    assert result == 2
