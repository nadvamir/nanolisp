#!/usr/bin/python3

def get_welcome_text():
    return "NanoLisp v0.1 REPL"

def evaluate(command, state):
    state['x'] = 10
    return False

def repl(state):
    command = input("> ")
    return evaluate(command, state)

if __name__ == "__main__":
    print(get_welcome_text())
    state = {}
    while repl(state):
        pass
