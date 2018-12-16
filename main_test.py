from nanolisp import *
import pytest

def test_get_welcome_text():
    assert "NanoLisp" in get_welcome_text()

def test_evaluate_with_state():
    state = {}
    evaluate("(defvar x 10)", state)
    assert state['x'] == 10

def test_eval_types():
    state = {}
    assert evaluate(3, state) == 3
    assert evaluate(3.0, state) == 3.0
    assert not evaluate("str", state)