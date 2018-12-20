from fibonacci import fibonacci


def test_fibonacci_min():
    assert fibonacci(1) is None


def test_fibonacci_valid():
    assert fibonacci(10) == 55
