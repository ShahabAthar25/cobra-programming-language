###############################
# TOKEN TYPE
###############################

TT_INT          = 'INT'
TT_FLOAT        = 'FLOAT'
TT_IDENTIFIER   = 'IDENTIFIER'
TT_KEYWORD      = 'KEYWORD'
TT_PLUS         = 'PLUS'
TT_MINUS        = 'MINUS'
TT_MUL          = 'MUL'
TT_DIV          = 'DIV'
TT_POW          = 'POW'
TT_EQ           = 'EQ'
TT_LPAREN       = 'LPAREN'
TT_RPAREN       = 'RPAREN'
TT_LSQBRACKET   = 'RSQBRACKET'
TT_RSQBRACKET   = 'RSQBRACKET'
TT_EOF          = 'EOF'

################################
# TOKENS
################################

class Token:
    def __init__(self, type_, value=None, pos_start=None, pos_end=None):
        self.type = type_
        self.value = value

        if pos_start:
            self.pos_start = pos_start.copy()
            self.pos_end = pos_start.copy()
            self.pos_end.advance()

        if pos_end:
            self.pos_end = pos_end

    def __repr__(self):
        if self.value: return f'{self.type}:{self.value}'
        return self.type