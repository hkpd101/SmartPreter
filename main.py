import sys
import os
import threading
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QTextEdit, 
    QLabel, QProgressBar, QSplitter, QFrame
)
from PyQt5.QtCore import QThread, pyqtSignal, Qt, QTimer
from PyQt5.QtGui import QFont
from ollama_runner import run_ollama_inference

# Suppress Qt OpenGL warnings
os.environ['QT_LOGGING_RULES'] = 'qt.glx.debug=false'

class InferenceThread(QThread):
    finished = pyqtSignal(str)
    error = pyqtSignal(str)
    
    def __init__(self, prompt):
        super().__init__()
        self.prompt = prompt
    
    def run(self):
        try:
            result = run_ollama_inference(self.prompt)
            self.finished.emit(result)
        except Exception as e:
            self.error.emit(str(e))

class Smartpreter(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("SmartPreter – AI Code Reviewer")
        self.resize(1200, 800)
        
        # Apply dark theme
        self.apply_dark_theme()
        
        # Create main layout
        main_layout = QVBoxLayout()
        
        # Create splitter for resizable panels
        splitter = QSplitter(Qt.Horizontal)
        
        # Left panel - Input
        left_panel = QWidget()
        left_layout = QVBoxLayout()
        
        self.input_label = QLabel("📝 Code to Review:")
        self.input_label.setFont(QFont("Arial", 10, QFont.Bold))
        
        self.input_box = QTextEdit()
        self.input_box.setPlaceholderText("Paste your Python code here for review...")
        self.input_box.setFont(QFont("Consolas", 10))
        
        # Button panel
        button_layout = QHBoxLayout()
        
        # Review action buttons
        self.explain_button = QPushButton("🔍 Explain Code")
        self.explain_button.clicked.connect(lambda: self.review_code("explain"))
        
        self.bugs_button = QPushButton("🐛 Find Bugs")
        self.bugs_button.clicked.connect(lambda: self.review_code("bugs"))
        
        self.optimize_button = QPushButton("⚡ Optimize")
        self.optimize_button.clicked.connect(lambda: self.review_code("optimize"))
        
        self.security_button = QPushButton("🔒 Security Check")
        self.security_button.clicked.connect(lambda: self.review_code("security"))
        
        self.style_button = QPushButton("📐 Style Review")
        self.style_button.clicked.connect(lambda: self.review_code("style"))
        
        # Style buttons
        for btn in [self.explain_button, self.bugs_button, self.optimize_button, 
                   self.security_button, self.style_button]:
            btn.setMinimumHeight(35)
            btn.setFont(QFont("Arial", 9))
        
        button_layout.addWidget(self.explain_button)
        button_layout.addWidget(self.bugs_button)
        button_layout.addWidget(self.optimize_button)
        button_layout.addWidget(self.security_button)
        button_layout.addWidget(self.style_button)
        
        # Progress bar
        self.progress_bar = QProgressBar()
        self.progress_bar.setVisible(False)
        self.progress_bar.setRange(0, 0)
        
        left_layout.addWidget(self.input_label)
        left_layout.addWidget(self.input_box)
        left_layout.addLayout(button_layout)
        left_layout.addWidget(self.progress_bar)
        
        left_panel.setLayout(left_layout)
        
        # Right panel - Output
        right_panel = QWidget()
        right_layout = QVBoxLayout()
        
        self.output_label = QLabel("📊 Review Results:")
        self.output_label.setFont(QFont("Arial", 10, QFont.Bold))
        
        self.output_box = QTextEdit()
        self.output_box.setReadOnly(True)
        self.output_box.setPlaceholderText("Code review results will appear here...")
        self.output_box.setFont(QFont("Consolas", 10))
        
        # Add copy button
        copy_button = QPushButton("📋 Copy Results")
        copy_button.clicked.connect(self.copy_results)
        copy_button.setMaximumWidth(120)
        
        right_layout.addWidget(self.output_label)
        right_layout.addWidget(self.output_box)
        right_layout.addWidget(copy_button, alignment=Qt.AlignRight)
        
        right_panel.setLayout(right_layout)
        
        # Add panels to splitter
        splitter.addWidget(left_panel)
        splitter.addWidget(right_panel)
        splitter.setSizes([500, 700])  # Set initial sizes
        
        main_layout.addWidget(splitter)
        self.setLayout(main_layout)
        
        # Store current review type
        self.current_review_type = "explain"
    
    def apply_dark_theme(self):
        """Apply dark theme to the application"""
        dark_style = """
        QWidget {
            background-color: #2b2b2b;
            color: #ffffff;
        }
        
        QTextEdit {
            background-color: #1e1e1e;
            border: 1px solid #3c3c3c;
            border-radius: 4px;
            padding: 8px;
            color: #ffffff;
        }
        
        QPushButton {
            background-color: #404040;
            border: 1px solid #555555;
            border-radius: 4px;
            padding: 6px 12px;
            color: #ffffff;
        }
        
        QPushButton:hover {
            background-color: #4a4a4a;
        }
        
        QPushButton:pressed {
            background-color: #363636;
        }
        
        QPushButton:disabled {
            background-color: #2a2a2a;
            color: #666666;
        }
        
        QLabel {
            color: #ffffff;
        }
        
        QProgressBar {
            border: 1px solid #3c3c3c;
            border-radius: 4px;
            background-color: #1e1e1e;
        }
        
        QProgressBar::chunk {
            background-color: #0078d4;
            border-radius: 3px;
        }
        
        QSplitter::handle {
            background-color: #404040;
        }
        """
        self.setStyleSheet(dark_style)
    
    def review_code(self, review_type):
        """Handle different types of code reviews"""
        code = self.input_box.toPlainText().strip()
        if not code:
            self.output_box.setPlainText("Please enter some code to review.")
            return
        
        self.current_review_type = review_type
        
        # Show progress
        self.progress_bar.setVisible(True)
        self.output_box.setPlainText("🔄 Analyzing code... This may take a moment.")
        self.disable_buttons(True)
        
        # Generate appropriate prompt based on review type
        prompt = self.generate_prompt(code, review_type)
        
        # Run inference in background thread
        self.inference_thread = InferenceThread(prompt)
        self.inference_thread.finished.connect(self.on_inference_finished)
        self.inference_thread.error.connect(self.on_inference_error)
        self.inference_thread.start()
    
    def generate_prompt(self, code, review_type):
        """Generate specific prompts for different review types"""
        prompts = {
            "explain": f"""You are a senior software developer doing code review.
Explain the following Python code in detail:

```python
{code}
```

Provide:
1. Overview of what the code does
2. Step-by-step explanation of each part
3. Any notable patterns or techniques used
4. Potential edge cases to consider
""",
            
            "bugs": f"""You are a senior software developer doing code review.
Analyze the following Python code for potential bugs, errors, and issues:

```python
{code}
```

Focus on:
1. Logical errors and edge cases
2. Runtime exceptions that could occur
3. Potential null/None reference issues
4. Type-related problems
5. Resource management issues
6. Infinite loops or performance problems

For each issue found, provide:
- The specific line or section
- What the problem is
- Why it's problematic
- How to fix it
""",
            
            "optimize": f"""You are a senior software developer doing code review.
Analyze the following Python code for performance optimization opportunities:

```python
{code}
```

Provide:
1. Performance bottlenecks and inefficiencies
2. Memory usage improvements
3. Algorithm optimization suggestions
4. Better data structure choices
5. Pythonic improvements
6. Specific code refactoring recommendations

For each optimization, explain:
- Current issue
- Proposed solution
- Expected performance improvement
""",
            
            "security": f"""You are a senior software developer doing security code review.
Analyze the following Python code for security vulnerabilities:

```python
{code}
```

Check for:
1. Input validation issues
2. SQL injection vulnerabilities
3. Cross-site scripting (XSS) risks
4. File system security issues
5. Authentication/authorization problems
6. Data exposure risks
7. Cryptographic weaknesses

For each security issue:
- Describe the vulnerability
- Explain the risk level
- Provide secure coding recommendations
""",
            
            "style": f"""You are a senior software developer doing code review.
Analyze the following Python code for style, readability, and best practices:

```python
{code}
```

Review:
1. PEP 8 compliance
2. Code readability and clarity
3. Variable and function naming conventions
4. Documentation and comments
5. Code structure and organization
6. Pythonic idioms and patterns
7. Maintainability concerns

Provide specific suggestions for improvement with examples.
"""
        }
        
        return prompts.get(review_type, prompts["explain"])
    
    def disable_buttons(self, disabled):
        """Enable/disable all review buttons"""
        buttons = [self.explain_button, self.bugs_button, self.optimize_button, 
                  self.security_button, self.style_button]
        for button in buttons:
            button.setEnabled(not disabled)
    
    def copy_results(self):
        """Copy review results to clipboard"""
        text = self.output_box.toPlainText()
        if text:
            clipboard = QApplication.clipboard()
            clipboard.setText(text)
            self.output_label.setText("📊 Review Results: (Copied to clipboard!)")
            # Reset label after 2 seconds
            QTimer.singleShot(2000, lambda: self.output_label.setText("📊 Review Results:"))
    
    def on_inference_finished(self, result):
        self.progress_bar.setVisible(False)
        self.output_box.setPlainText(result)
        self.disable_buttons(False)
        
        # Update label based on review type
        labels = {
            "explain": "📊 Code Explanation:",
            "bugs": "🐛 Bug Analysis:",
            "optimize": "⚡ Optimization Report:",
            "security": "🔒 Security Review:",
            "style": "📐 Style Review:"
        }
        self.output_label.setText(labels.get(self.current_review_type, "📊 Review Results:"))
    
    def on_inference_error(self, error):
        self.progress_bar.setVisible(False)
        self.output_box.setPlainText(f"❌ Error: {error}")
        self.disable_buttons(False)

if __name__ == "__main__":
    print("Starting SmartPreter Code Reviewer...")
    
    # Set Qt platform options to reduce warnings
    os.environ['QT_XCB_GL_INTEGRATION'] = 'none'
    os.environ['QT_QUICK_BACKEND'] = 'software'
    
    app = QApplication(sys.argv)
    
    # Disable OpenGL if causing issues
    try:
        app.setAttribute(app.AA_UseSoftwareOpenGL, True)
    except AttributeError:
        # Fallback for older Qt versions
        pass
    
    window = Smartpreter()
    window.show()
    print("Code Reviewer launched.")
    sys.exit(app.exec_())