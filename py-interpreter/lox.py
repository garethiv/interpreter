from pathlib import Path
from scanner import Scanner

class Lox:
    had_error = False

    @staticmethod
    def run_file(file):
        path = Path(file).absolute()
        source = path.read_text(encoding='utf-8', errors='strict')
        Lox.run(source)

        if Lox.had_error:
            exit(65)

    @staticmethod
    def run_prompt():
        while True:
            try:
                print('>>>')

                expr = input()
                print(expr) 
                
                if expr.split(' ')[0] == 'exit':
                    exit()
                else:
                    Lox.run(expr)
                    Lox.had_error = False

            except EOFError:
                exit(0)

    @staticmethod
    def run(source):
        scanner = Scanner(source)
        tokens = scanner.scan_tokens()

        for token in tokens:
            print(token)

    @staticmethod
    def error(line, message):
        report(line, '', message)

    @staticmethod
    def report(line, where, message):
        print('[line {}] Error{}: {}'.format( line, where, error )) # todo change to showing error
        Lox.had_error = True
    