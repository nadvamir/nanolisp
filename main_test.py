from nanolisp import *

def test_func():
    assert 2*2 == 4

def test_get_welcome_text():
    assert "NanoLisp" in get_welcome_text()

