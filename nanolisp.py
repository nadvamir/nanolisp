#!/usr/bin/python3

import re

def attempt_baseType(x):
    try:
        x = int(x)
        return True, x
    except:
        pass
    try:
        x = float(x)
        return True, x
    except:
        pass
    return False, x 

def get_list_elements(list_expression):
    list_expression = list_expression[1:-1]
    if len(list_expression) == 0:
        return []
    return re.findall('(\w|\(.*\))', list_expression, re.DOTALL)

def evaluate(x, env):
    if x in env:
        return env[x]
    isBaseType, x = attempt_baseType(x)
    if isBaseType:
        return x
    x = get_list_elements(x)
    if len(x) == 0:
        return '()'
    if x[0] == 'defvar':
        store_state(x[1], x[2], env)
    if x[0] == 'print':
        return evaluate(x[1], env)
    return "Error parsing input"

def store_state(name, expression, env):
    env[name] = evaluate(expression, env)

def get_welcome_text():
    return "NanoLisp v0.1 REPL"

def repl(state):
    command = input("> ")
    if command == "exit":
        return False
    print(evaluate(command, state))
    return True

if __name__ == "__main__":
    print(get_welcome_text())
    state = {}
    while repl(state):
        pass
