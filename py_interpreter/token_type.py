from enum import Enum

class TokenType(Enum):
    # Single-character tokens
    LEFT_PAREN = '('
    RIGHT_PAREN = ')'
    LEFT_BRACE = '['
    RIGHT_BRACE = ']'
    LEFT_CURLY_BRACE = '{'
    RIGHT_CURLY_BRACE = '}'
    COMMA = ','
    DOT = '.'
    MINUS = '-'
    PLUS = '+'
    COLON = ':'
    SEMICOLON = ';'
    SLASH = '/'
    STAR = '*'
    UNDERSCORE = '_'
    QUOTATION_MARK = '?'
    PERCENT = '%'
    AT_SIGN = '@'
    AMPERSAND = '&'
    DOLLAR_SIGN = '$'
    CARET = '^'
    TILDE = '~'
    PIPE = '|'
    

    # One or two+ character tokens
    BANG = '!'
    BANG_EQUAL = '!='
    EQUAL = '='
    EQUAL_EQUAL = '=='
    GREATER = '>'
    GREATER_EQUAL = '>='
    LESS = '<'
    LESS_EQUAL = '<='
    ARROW = '=>'
    SHEBANG = '#!'
    HASH = '#'
    ELLIPSIS = '...'
    TRIPLE_QUOTE = '"""'

    # Keywords
    GET = 'get'
    SET = 'set'
    DELETE = 'delete'
    AND = 'and'
    OR = 'or'
    NOT = 'not'
    IF = 'if'
    ELSE = 'else'
    SWITCH = 'switch'
    CASE = 'case'
    WHEN = 'when'
    WHILE = 'while'
    UNLESS = 'unless'
    BREAK = 'break'
    FOR = 'for'
    IN = 'in'
    DO = 'do'
    NULL = 'null'
    TRUE = 'true'
    FALSE = 'false'
    TRY = 'try'
    CATCH = 'catch'
    FINALLY = 'finally'
    NEW = 'new'
    CLASS = 'class'
    EXTENDS = 'extends'
    SUPER = 'super'
    SELF = 'self'
    THIS = 'this'
    INTERFACE = 'interface'
    IMPLEMENTS = 'implements'
    FUNCTION = 'function'
    RETURN = 'return'
    GENERATOR = 'generator'
    YIELD = 'yield'
    ASYNC = 'async'
    AWAIT = 'await'
    STATIC = 'static'
    LAMBDA = 'lambda'
    CONST = 'const'
    LET = 'let'
    VAR = 'var'
    PRIVATE = 'private'
    END = 'end'
    PRINT = 'print'

    # String starters
    SINGLE_QUOTE = "'"
    DOUBLE_QUOTE = '"'

    # New line
    NEW_LINE = '\n'

    # Space
    TAB = '\t'
    SPACE = ' '

    # String terminator
    NULL_CHARACTER = '\0'

    # End-user identifiers
    IDENTIFIER = 'identifier'
    INTEGER = 'int'
    FLOAT = 'float'
    STRING = 'str'

    # end-of-file
    EOF = ''
