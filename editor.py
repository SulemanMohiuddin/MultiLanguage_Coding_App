from PyQt6.QtWidgets import QTextEdit

class CodeEditor(QTextEdit):
    def __init__(self):
        super().__init__()
        self.setPlaceholderText("Write your code here...")
        self.setFontPointSize(12)
        self.setAcceptRichText(False)
