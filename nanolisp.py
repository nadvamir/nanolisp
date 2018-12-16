#!/usr/bin/python3

def store_state(name, expression, env):
    env[name] = evaluate(expression)

def get_list_elements(list_expression):
    list_expression = list_expression[1:-1]
    if len(list_expression) == 0:
        return []
    return list_expression.split("\s+")

def evaluate(x, env):
    env['x'] = 10
    if isinstance(x, float):
        return x
    if isinstance(x, int):
        return x
    if x in env:
        return env[x]
    return "Error parsing input"

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
