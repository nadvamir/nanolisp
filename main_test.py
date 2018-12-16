from nanolisp import *

def test_get_welcome_text():
    assert "NanoLisp" in get_welcome_text()

def test_evaluate_with_state():
    state = {}
    evaluate("(defvar x 10)", state)
    assert state['x'] == 10
