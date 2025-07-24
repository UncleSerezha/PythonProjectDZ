import pytest

from src.decorators import log


@log()
def my_function(x, y):
    return x / y

def test_my_function_success(capsys):
    result = my_function(4, 2)
    assert result == 2
    captured = capsys.readouterr()
    assert "my_function ok. Результат: 2" in captured.out


def test_decorator_cupsys(capsys):
    """Тестирование декоратора с выходом ошибки с фикстурой cupsys"""
    with pytest.raises(Exception):
        my_func = my_function()
        captured = my_func.readouterr()
        assert captured.out == Exception


@log()
def faulty_function(x, y):
    return x / y
def test_faulty_function_logs_error(capsys):
    faulty_function(1, 0)
    captured = capsys.readouterr()
    assert "faulty_function error: division by zero" in captured.out