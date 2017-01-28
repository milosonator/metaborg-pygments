import re
from pygments.lexer import RegexLexer, words
from pygments.token import *

class GraceLexer(RegexLexer):
    name      = 'Grace'
    aliases   = ['grace', 'grc']
    filenames = ['*.grace']

    tokens = {
        'root': [
            (words(('alias','as','class', 'def', 'dialect', 'exclude',
                    'import','inherit','is','method','object',
                    'outer','prefix','required','return','self',
                    'Self','trait','type','use','var','where',
                    'true','false','case'), suffix=r'\b'), Keyword),
            (r'(\.|\.\.\.|\:=|=|;|{|}|[|]|\(|\)|\:|-\>)', Operator),
            (r'"[^"^\n]*"', Literal.String),
            (r'\d+', Literal.Number),
            (r'[\w_-]+', Name.Variable),
            (r'[\,\|\[\]\(\)\{\}\;]', Text.Punctuation),
            (r'/\*', Comment.Multiline, 'comment'),
            (r'//.*?$', Comment.Singleline),
            (r'\s+', Text.Whitespace),
            (r'.', Text),
        ],
        'comment': [
            (r'[^*/]', Comment.Multiline),
            (r'/\*', Comment.Multiline, '#push'),
            (r'\*/', Comment.Multiline, '#pop'),
            (r'[*/]', Comment.Multiline)
        ],
    }
