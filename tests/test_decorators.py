from spracvit.decorators import repeat, measure
import re


def test_decorator_repeat():
    N_REPEATS = 42
    calls = 0

    @repeat(N_REPEATS)
    def repeat_me():
        nonlocal calls
        calls += 1

    result = repeat_me()
    assert calls == N_REPEATS
    assert len(result) == N_REPEATS


def test_decorator_measure(caplog):

    @measure
    def measure_me(var):
        return var

    assert measure_me("hello") == "hello"
    expected = r".*INFO.*measure_me.*s"
    assert re.findall(expected, caplog.text)


