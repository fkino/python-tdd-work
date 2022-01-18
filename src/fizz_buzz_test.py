def add(a, b):
    return a + b

def test_first():
    assert add(1, 2) == 3

def fizzbuzz(a):
    if a % 3 == 0:
        return "Fizz"
    return a

def test_変換せずに数値をそのまま返す():
    assert fizzbuzz(1) == 1

def test_3の倍数の時はFizzを返す():
    assert fizzbuzz(3) == "Fizz"

def test_3の倍数の時はFizzを返す_6の場合():
    assert fizzbuzz(6) == "Fizz"