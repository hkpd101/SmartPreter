from PyQt5.QtGui import QSyntaxHighlighter, QTextCharFormat, QColor, QFont
from PyQt5.QtCore import QRegExp

class PythonSyntaxHighlighter(QSyntaxHighlighter):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        # Define highlighting rules
        self.highlighting_rules = []
        
        # Keywords
        keyword_format = QTextCharFormat()
        keyword_format.setForeground(QColor(86, 156, 214))  # Blue
        keyword_format.setFontWeight(QFont.Bold)
        
        keywords = [
            'and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 
            'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 
            'import', 'in', 'is', 'lambda', 'not', 'or', 'pass', 'raise', 
            'return', 'try', 'while', 'with', 'yield', 'True', 'False', 'None'
        ]
        
        for keyword in keywords:
            pattern = QRegExp(f'\\b{keyword}\\b')
            self.highlighting_rules.append((pattern, keyword_format))
        
        # Strings
        string_format = QTextCharFormat()
        string_format.setForeground(QColor(206, 145, 120))  # Orange
        self.highlighting_rules.append((QRegExp('"[^"\\\\]*(\\\\.[^"\\\\]*)*"'), string_format))
        self.highlighting_rules.append((QRegExp("'[^'\\\\]*(\\\\.[^'\\\\]*)*'"), string_format))
        
        # Comments
        comment_format = QTextCharFormat()
        comment_format.setForeground(QColor(106, 153, 85))  # Green
        comment_format.setFontItalic(True)
        self.highlighting_rules.append((QRegExp('#[^\r\n]*'), comment_format))
        
        # Numbers
        number_format = QTextCharFormat()
        number_format.setForeground(QColor(181, 206, 168))  # Light green
        self.highlighting_rules.append((QRegExp('\\b\\d+\\b'), number_format))
        self.highlighting_rules.append((QRegExp('\\b\\d+\\.\\d+\\b'), number_format))
        
        # Functions
        function_format = QTextCharFormat()
        function_format.setForeground(QColor(220, 220, 170))  # Yellow
        self.highlighting_rules.append((QRegExp('\\b[A-Za-z_][A-Za-z0-9_]*(?=\\()'), function_format))
        
        # Decorators
        decorator_format = QTextCharFormat()
        decorator_format.setForeground(QColor(255, 255, 0))  # Bright yellow
        self.highlighting_rules.append((QRegExp('@[A-Za-z_][A-Za-z0-9_]*'), decorator_format))
    
    def highlightBlock(self, text):
        for pattern, format in self.highlighting_rules:
            expression = QRegExp(pattern)
            index = expression.indexIn(text)
            while index >= 0:
                length = expression.matchedLength()
                self.setFormat(index, length, format)
                index = expression.indexIn(text, index + length)