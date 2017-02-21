import re
from pygments.lexer import RegexLexer, words
from pygments.token import *

class SPTLexer(RegexLexer):
    name      = 'SPT'
    aliases   = ['spt']
    filenames = ['*.spt']

    tokens = {
        'root': [
            (words(('module','start','symbol','language','to','parse',
					'analysis', 'succeeds', 'fails', 'resolve', 'on', 'run',
                    'transform','error','errors','warning','warnings','note',
					'notes', 'test'), suffix=r'\b'), Keyword),
			(r'\[\[[^"^\n]*\]\]', Literal.String),
            (r'[\.\,\|\[\]\(\)\{\}\<\>\;\:\*\[\]]', Text.Punctuation),
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
