from sys import argv
from .lox import Lox

def main(args):
    print('running main')
    if len(args) > 1:
        print('Usage: pyLox [file]')
        exit(64)
    elif len(args) == 1:
        Lox.run_file(args[0])
    else:
        Lox.run_prompt()

if __name__ == "__main__":
    print('yes!')
    main(argv[1:])