from example_taskipy.app.calculator.add import compute_add


def test_add():
    result = compute_add(1, 1)
    assert result == 2
