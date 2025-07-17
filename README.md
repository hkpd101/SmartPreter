# SmartPreter - AI-Powered Code Reviewer

<div align="center">
  <img src="https://img.shields.io/badge/Python-3.8+-blue.svg" alt="Python Version">
  <img src="https://img.shields.io/badge/PyQt5-5.15+-green.svg" alt="PyQt5">
  <img src="https://img.shields.io/badge/Ollama-Latest-orange.svg" alt="Ollama">
  <img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License">
</div>

## 🚀 Overview

SmartPreter is a powerful AI-powered code review tool that provides comprehensive analysis of Python code using local language models through Ollama. It offers multiple review types including bug detection, performance optimization, security analysis, and style checking - all processed locally for maximum privacy and security.

## ✨ Features

### 🔍 **Multi-Type Code Analysis**
- **Code Explanation** - Detailed step-by-step code breakdown
- **Bug Detection** - Identify potential issues and runtime errors
- **Performance Optimization** - Suggest improvements and optimizations
- **Security Review** - Detect vulnerabilities and security risks
- **Style Analysis** - PEP 8 compliance and readability improvements

### 🎨 **Professional UI**
- **Syntax Highlighting** - Beautiful Python code coloring
- **Dark Theme** - Easy on the eyes interface
- **Resizable Panels** - Customizable layout with splitter
- **File Operations** - Load, save, and export functionality
- **Progress Indication** - Visual feedback during analysis

### 🔧 **Advanced Features**
- **100% Local Processing** - No data sent to external servers
- **Async Processing** - Non-blocking UI during analysis
- **Export Results** - Save reviews as text or markdown
- **Clipboard Integration** - Easy result copying
- **Professional Styling** - Modern dark theme with hover effects

## 📦 Installation

### Prerequisites
- Python 3.8 or higher
- Ollama installed and running
- PyQt5

### Quick Start

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/SmartPreter.git
cd SmartPreter
```

2. **Create virtual environment**
```bash
python -m venv smartpreter_env
source smartpreter_env/bin/activate  # On Windows: smartpreter_env\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Install and start Ollama**
```bash
# Install Ollama (Linux/Mac)
curl -fsSL https://ollama.ai/install.sh | sh

# Start Ollama service
ollama serve

# Pull a model (in another terminal)
ollama pull llama2
```

5. **Run SmartPreter**
```bash
python main.py
```

### 📱 Standalone Installation

#### Build Executable
```bash
# Install build dependencies
pip install pyinstaller

# Build standalone executable
python build_installer.py

# Or build everything
chmod +x build_all.sh
./build_all.sh
```

#### Install as Python Package
```bash
pip install -e .
smartpreter
```

## 🛠️ Usage

### Basic Usage
1. **Load Code**: Paste Python code or load from file using 📁 Load File
2. **Choose Review Type**: Select from explanation, bugs, optimization, security, or style
3. **Analyze**: Click the desired review button
4. **Export**: Save results using 📋 Save Results or copy to clipboard

### Review Types

#### 🔍 **Explain Code**
- Provides detailed explanation of code functionality
- Step-by-step breakdown of logic
- Identifies patterns and techniques used

#### 🐛 **Find Bugs**
- Detects logical errors and edge cases
- Identifies potential runtime exceptions
- Suggests fixes for found issues

#### ⚡ **Optimize**
- Finds performance bottlenecks
- Suggests algorithm improvements
- Recommends better data structures

#### 🔒 **Security Check**
- Scans for security vulnerabilities
- Identifies input validation issues
- Suggests secure coding practices

#### 📐 **Style Review**
- Checks PEP 8 compliance
- Analyzes code readability
- Suggests naming improvements

## 🧪 Test Cases

Copy these example code snippets into SmartPreter to test different review types:

### Test Case 1: Basic Function (Good for "Explain Code")
```python
def fibonacci(n):
    """Calculate fibonacci number recursively"""
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
```

### Test Case 2: Code with Bugs (Good for "Find Bugs")
```python
def divide_numbers(a, b):
    result = a / b  # Bug: No zero division check
    return result

def process_list(items):
    for i in range(len(items) + 1):  # Bug: Index out of range
        print(items[i])
```

### Test Case 3: Inefficient Code (Good for "Optimize")
```python
def find_duplicates(numbers):
    duplicates = []
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if i != j and numbers[i] == numbers[j]:
                if numbers[i] not in duplicates:
                    duplicates.append(numbers[i])
    return duplicates
```

### Test Case 4: Security Issues (Good for "Security Check")
```python
import subprocess
import os

def run_command(user_input):
    # Security issue: Command injection vulnerability
    os.system(user_input)
    
def sql_query(username):
    # Security issue: SQL injection vulnerability
    query = f"SELECT * FROM users WHERE username = '{username}'"
    return query
```

### Test Case 5: Style Issues (Good for "Style Review")
```python
def badFunction(x,y):
    if x>y:
        return x
    else:
        return y

class myClass:
    def __init__(self,name):
        self.name=name
        
    def getName(self):
        return self.name
```

### Test Case 6: Complex Algorithm (Good for "Explain Code")
```python
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)
```

## 🔧 Configuration

### Ollama Models
You can use different models by modifying `ollama_runner.py`:

```python
# Default model
MODEL_NAME = "llama2"

# Other supported models
# MODEL_NAME = "codellama"
# MODEL_NAME = "mistral"
# MODEL_NAME = "phi"
```

### UI Customization
Modify the dark theme in `main.py`:

```python
def apply_dark_theme(self):
    # Customize colors and styles here
    dark_style = """
    QWidget {
        background-color: #2b2b2b;
        color: #ffffff;
    }
    """
```

## 📁 Project Structure

```
SmartPreter/
├── main.py                 # Main application
├── syntax_highlighter.py   # Python syntax highlighting
├── ollama_runner.py        # Ollama integration
├── build_installer.py      # Executable builder
├── build_all.sh           # Complete build script
├── requirements.txt        # Dependencies
├── setup.py               # Package setup
├── README.md              # This file
└── assets/                # Images and resources
```

## 🏗️ Development

### Build System
```bash
# Build executable
python build_installer.py

# Build Python package
python setup.py sdist bdist_wheel

# Complete build (all platforms)
chmod +x build_all.sh
./build_all.sh
```

### Testing
```bash
# Quick test
python main.py

# Test installation
python -c "import main; print('✅ Installation successful')"

# Test with sample code
# Copy test cases from above into the application
```

## 📊 Performance

- **Startup time**: ~2-3 seconds
- **Analysis time**: 5-30 seconds (depends on code complexity and model)
- **Memory usage**: ~100-500MB (depends on model size)
- **Local processing**: 100% offline, no external API calls

## 🔒 Privacy & Security

- **100% Local**: All analysis happens on your machine
- **No data transmission**: Code never leaves your computer
- **Open source**: Full transparency in code processing
- **GDPR/CCPA compliant**: No external data sharing

## 🎯 Use Cases

### **Professional Development**
- **Code Reviews**: Automated first-pass review before human review
- **Pre-commit Checks**: Validate code quality before pushing
- **Security Audits**: Identify vulnerabilities in proprietary code
- **Performance Optimization**: Find bottlenecks and improvements

### **Learning & Education**
- **Student Learning**: Understand complex code patterns
- **Teaching Tool**: Demonstrate code analysis techniques
- **Self-improvement**: Learn best practices and patterns
- **Mentorship**: Explain code to junior developers

### **Enterprise Applications**
- **Compliance**: Meet coding standards and regulations
- **Security**: Identify vulnerabilities before deployment
- **Cost Reduction**: No subscription fees for code review tools
- **Privacy**: Keep proprietary code internal

## 🛠️ Troubleshooting

### Common Issues
1. **Qt warnings**: Install Qt5 development packages
   ```bash
   sudo apt-get install qtbase5-dev  # Linux
   ```

2. **Ollama connection**: Ensure Ollama is running
   ```bash
   ollama serve
   ```

3. **Module not found**: Check virtual environment
   ```bash
   which python
   pip list
   ```

4. **Permission errors**: Run with appropriate permissions
   ```bash
   chmod +x build_all.sh
   ```

### Performance Tips
- Use `codellama` model for better code analysis
- Increase system RAM for larger models
- Close other applications during analysis
- Use SSD for faster model loading

## 🤝 Contributing

We welcome contributions! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Development Setup
```bash
# Clone and setup
git clone https://github.com/yourusername/SmartPreter.git
cd SmartPreter

# Create development environment
python -m venv dev_env
source dev_env/bin/activate

# Install in development mode
pip install -e .

# Run tests
python -m pytest tests/
```

## 📋 Roadmap

### Current Version (v1.0)
- [x] Multi-type code analysis
- [x] Professional GUI interface
- [x] Local AI processing
- [x] File operations
- [x] Syntax highlighting

### Future Versions
- [ ] Multi-language support (JavaScript, Java, C++)
- [ ] Batch file processing
- [ ] Code execution environment
- [ ] Web interface
- [ ] VSCode extension
- [ ] Plugin system
- [ ] Team collaboration features
- [ ] Git integration

## 🐛 Known Issues

- **Qt warnings**: Some Qt OpenGL warnings may appear (harmless)
- **Large files**: Very large files may take longer to analyze
- **Model dependencies**: Requires Ollama to be running locally
- **Memory usage**: Large models consume significant RAM

## 💡 Tips & Tricks

### Performance Optimization
```python
# Use smaller models for faster analysis
MODEL_NAME = "phi"  # Faster, smaller model

# Or use larger models for better accuracy
MODEL_NAME = "codellama"  # Better for code analysis
```

### Keyboard Shortcuts
- `Ctrl+O`: Load file
- `Ctrl+S`: Save code
- `Ctrl+C`: Copy results
- `F5`: Clear all

### Best Practices
1. **Test incrementally**: Start with small code snippets
2. **Use appropriate review types**: Match the analysis to your needs
3. **Save results**: Export important findings for reference
4. **Combine analyses**: Use multiple review types for comprehensive analysis

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [Ollama](https://ollama.ai/) for providing local LLM infrastructure
- [PyQt5](https://www.riverbankcomputing.com/software/pyqt/) for the GUI framework
- Python community for excellent tools and libraries
- Open source contributors and testers

## 📞 Support

- **Issues**: [GitHub Issues](https://github.com/yourusername/SmartPreter/issues)
- **Discussions**: [GitHub Discussions](https://github.com/yourusername/SmartPreter/discussions)
- **Documentation**: This README file
- **Email**: your.email@example.com

---

<div align="center">
  <strong>Made with ❤️ for the developer community</strong>
  <br>
  <em>AI-powered code review that respects your privacy</em>
</div>