from token_type import TokenType
from token import Token

SINGLE_CHARS = ['(', ')', '{', '}', ',', '.', '-', '+', ';', '*']
NULL_CHARS = [' ', '\r', '\t']
RESERVED_WORDS = ['true', 'false', 'null', 'and', 'or', 'if', 'else', 'function', 'return',
                  'for', 'class', 'super', 'this', 'const', 'let', 'while', 'var', 'print']
KEYWORDS = {key : TokenType(key) for key in RESERVED_WORDS}

class Scanner:
    def __init__(self, source):
        self.source = source
        self.tokens = []
        self.start = 0
        self.current = 0
        self.line = 1

    def scan_tokens(self):
        while not self.is_at_end():
            self.start = self.current
            self.scan_token()
        
        self.tokens.append(Token(TokenType.EOF, '', None, self.line))
        return self.tokens

    def scan_token(self):
        c = self.advance()
        if c in SINGLE_CHARS:
            self.add_token(TokenType(c))
        elif c == '!':
            self.add_token(TokenType.BANG_EQUAL if self.match('=') else TokenType.BANG)
        elif c == '=':
            self.add_token(TokenType.EQUAL_EQUAL if self.match('=') else TokenType.EQUAL)
        elif c == '<':
            self.add_token(TokenType.LESS_EQUAL if self.match('=') else TokenType.LESS)
        elif c == '>':
            self.add_token(TokenType.GREATER_EQUAL if self.match('=') else TokenType.GREATER)
        elif c == '/':
            if self.match('/'):
                while self.peek() != '\n' and not self.is_at_end():
                    self.advance()
            else:
                self.add_token(TokenType.SLASH)
        elif c in NULL_CHARS:
            pass
        elif c == '\n':
            self.line += 1
        elif c == '"':
            self.string()
        elif c.isdigit():
            self.number()
        elif c.isalpha():
            self.identifier()
        else:
            raise SyntaxError('Unexecpted character {} at {}'.format(c, self.line))

    def identifier(self):
        while self.peek().isalnum():
            self.advance()
    
        val = self.source[self.start:self.current]
        typ = KEYWORDS.get(val, TokenType.IDENTIFIER)
        self.add_token(typ)

    def number(self):
        def _consume_digits():
            while self.peek().isdigit():
                self.advance()

        typ = TokenType.INTEGER
        _consume_digits()
        
        if self.peek() == '.' and self.peek_next().isdigit():
            typ = TokenType.FLOAT
            self.advance()
            _consume_digits()
        
        val = self.source[self.start:self.current]
        val = float(val) if '.' in val else int(val)
        self.add_token(typ, val)

    def string(self):
        while self.peek() != '"' and not self.is_at_end():
            if self.peek() == '\n':
                self.line += 1
            self.advance()
        if self.is_at_end():
            raise RuntimeError('{} unterminated string'.format( self.line ))
        self.advance()
        val = self.source[self.start+1:self.current-1]
        self.add_token(TokenType.STRING, val)

    def match(self, expected):
        if is_at_end():
            return False
        if self.source[self.current] != expected:
            return False

        self.current += 1
        return True

    def peek(self):
        if self.is_at_end():
            return '\0'
        return self.source[self.current]

    def peek_next(self):
        if self.current + 1 >= len(self.source):
            return '\0'
        return self.source[self.current+1]

    def is_at_end(self):
        return self.current >= len(self.source)

    def advance(self):
        self.current += 1
        return self.source[self.current-1]

    def add_token(self, typ, literal = None):
        token = Token(typ, self.source[self.start : self.current], literal, self.line)
        self.tokens.append(token)
