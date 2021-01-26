
class Token:
    def __init__(self, ty, lexeme, literal, line):
        self.type = ty
        self.lexeme = lexeme
        self.literal = literal
        self.line = line

    def __str__(self):
        return '{} {} {}'.format(self.type, self.lexeme, self.literal)
