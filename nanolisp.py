#!/usr/bin/python3

def get_welcome_text():
    return "NanoLisp v0.1 REPL"

def evaluate(command):
    return False

def repl():
    command = input("> ")
    return evaluate(command)

if __name__ == "__main__":
    print(get_welcome_text())
    while repl():
        pass
