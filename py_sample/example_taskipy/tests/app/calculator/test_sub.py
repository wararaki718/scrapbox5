from example_taskipy.app.calculator.sub import compute_sub


def test_sub():
    result = compute_sub(2, 1)
    assert result == 1
