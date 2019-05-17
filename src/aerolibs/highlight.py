from tkinter import *
from pygments import lex
#from .text import textEditor
from pygments.lexers import PythonLexer, get_lexer_for_filename


class highlighter:
    def __init__(self, root, textpad):
        self.root = root
        self.textpad = textpad
        self.lexer = None
        self.textpad.bind('<KeyRelease>', self.highlightLine)


    def highlightLine(self, *args, **kwargs):
        display = self.textpad.count("1.0", "end", "lines")
        cursor = self.textpad.index(INSERT)
        cursorSplit = cursor.split('.')
        line = cursorSplit[0]
        column = cursorSplit[1]
        lineContext = self.textpad.get(float(str(line) + '.0'), float(cursor))
        self.textpad.mark_set("range_start", str(line) + '.0')

        for token, context in lex(lineContext, PythonLexer()):
            self.textpad.mark_set("range_end", "range_start + %dc" % len(context))
            self.textpad.tag_add(str(token), "range_start", "range_end")
            self.textpad.mark_set("range_start", "range_end")


    def highlightFile(self, *args, **kwargs):
        to_highliget = self.textpad.get('1.0', 'end-1c')
        self.textpad.mark_set("range_start", '1.0')
        lexerToUse = get_lexer_for_filename(str(self.root.filehandler.file))
        self.lexer = lexerToUse

        for token, context in lex(to_highliget, lexerToUse):
            self.textpad.mark_set("range_end", "range_start + %dc" % len(context))
            self.textpad.tag_add(str(token), "range_start", "range_end")
            self.textpad.mark_set("range_start", "range_end")
