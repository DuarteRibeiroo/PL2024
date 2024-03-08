import ply.lex as lex
import sys

tokens = (
    'COMMAND',
    'ALIAS',
    'FROM',
    'WHERE',
    'SIGNALS',
    'NUM',
    'LOGIC',
    'IN',
    'DELIMITER',
    'FUNCTION',
    'LEFT_P',
    'RIGHT_P',
    'FIELDS',
    'COMMAND_END',
    'IGNORE',
)

t_COMMAND = r'(\b|\))(SELECT|CREATE TABLE|CREATE INDEX|DROP TABLE|DROP INDEX|DELETE|ALTER TABLE)(\b|\()'
t_ALIAS = r'(\b|\))AS(\b|\()'
t_FROM = r'(\b|\))FROM(\b|\()'
t_WHERE = r'(\b|\))WHERE(\b|\()'
t_SIGNALS = r'>=|<=|\+|-|>|<|='
# A regular expression rule with some action code
def t_NUM(t):
    r'\d+'
    t.value = int(t.value)
    return t

t_LOGIC = r'(\b|\))AND|OR(\b|\()'
t_IN = r'(\b|\))IN(\b|\()'
t_DELIMITER = r','
t_FUNCTION = r'(\b|\))(AVG|MIN|COUNT|MAX)(\b|\()'
t_LEFT_P = r'\('
t_RIGHT_P = r'\)'
t_FIELDS= r'\w+'
t_COMMAND_END = r';'

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()

def main():
    text = sys.stdin.read()
    lexer.input(text)
    # Tokenize
    while True:
        tok = lexer.token()
        if not tok:
            break      # No more input
        print(tok)
    

if __name__ == '__main__':
    main()