from tkinter import *
#from .config import connector
#from .highlight import highlighter
#from .filehandler import filehandler

def count_monkeypatch(self, index1, index2, *args):
    args = [self._w, "count"] + ["-" + arg for arg in args] + [index1, index2]
    result = self.tk.call(*args)
    return result

Text.count = count_monkeypatch


class textEditor(Text):
    def __init__(self, root, *args, **kwargs):
        Text.__init__(self, *args, **kwargs)
        self.root = root
        self._tag_configs()
        self._pack()
        #self.connect_external_modules()
        #self.highlight = highlighter(self)
        #self.bind("<KeyRelease>", self.highlight.highlightLine)

    def _pack(self):
        self.configure(tabs='34', highlightbackground='#212835', bg='#212835',
                        borderwidth=0, highlightthickness=0, insertbackground='white', fg='white', wrap='none',)
        self.pack(fill='both', expand=True)


    def _tag_configs(self):
        self.tag_configure("Token.Keyword", foreground='#c678dd')
        self.tag_configure("Token.Keyword.Constant", foreground='#c678dd')
        self.tag_configure("Token.Keyword.Declaration", foreground='#c678dd')
        self.tag_configure("Token.Keyword.Namespace", foreground='#c678dd')
        self.tag_configure("Token.Keyword.Pseudo", foreground='#c678dd')
        self.tag_configure("Token.Keyword.Reserved", foreground='#c678dd')
        self.tag_configure("Token.Keyword.Type", foreground='#c678dd')

        self.tag_configure("Token.Name.Class", foreground='#e5c07b')
        self.tag_configure("Token.Name.Exception", foreground="#003D99")
        self.tag_configure("Token.Name.Function", foreground='#61afef')
        self.tag_configure("Token.Name.Function.Magic", foreground='#61afef')
        self.tag_configure("Token.Name.Builtin", foreground='#56b6c2')
        self.tag_configure("Token.Operator.Word", foreground='#c678dd')
        self.tag_configure("Token.Comment.Single", foreground='#5c6370')
        self.tag_configure("Token.Literal.String.Single", foreground="#248F24")
        self.tag_configure("Token.Literal.String.Doc", foreground="#248F24")
        self.tag_configure("Token.Literal.String.Double", foreground="#248F24")
        self.tag_configure("function", foreground="#CC7A00")
