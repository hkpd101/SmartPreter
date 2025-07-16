# SmartPreter - AI Code Reviewer Documentation

## 📋 Table of Contents
1. [Project Overview](#project-overview)
2. [Current Features](#current-features)
3. [Technical Architecture](#technical-architecture)
4. [Development Progress](#development-progress)
5. [Installation & Setup](#installation--setup)
6. [Usage Guide](#usage-guide)
7. [Deployment Options](#deployment-options)
8. [Future Enhancements](#future-enhancements)
9. [Contributing](#contributing)
10. [Troubleshooting](#troubleshooting)

---

## 🚀 Project Overview

**SmartPreter** is a desktop AI-powered code review application built with PyQt5 and Ollama. It provides comprehensive code analysis including explanations, bug detection, optimization suggestions, security reviews, and style checks.

### Key Highlights
- **Local AI Processing**: Uses Ollama for offline code analysis
- **Multi-Modal Reviews**: 5 different types of code analysis
- **Modern UI**: Dark theme with syntax highlighting
- **File Management**: Load, save, and export functionality
- **Professional Output**: Structured review results with export options

---

## ✨ Current Features

### 🔍 Code Analysis Types
1. **Explain Code** - Detailed code explanation and walkthrough
2. **Find Bugs** - Identifies potential errors, edge cases, and runtime issues
3. **Optimize Code** - Performance improvements and efficiency suggestions
4. **Security Check** - Vulnerability analysis and security recommendations
5. **Style Review** - PEP 8 compliance and code readability improvements

### 🎨 User Interface
- **Dark Theme**: Professional dark mode interface
- **Syntax Highlighting**: Python code highlighting with proper colors
- **Resizable Panels**: Adjustable input/output split view
- **Progress Indicators**: Real-time feedback during analysis
- **Copy to Clipboard**: Easy result sharing

### 📁 File Operations
- **Load Files**: Open Python files directly into the editor
- **Save Code**: Save current code with file path tracking
- **Export Results**: Save review results as text or markdown
- **Clear All**: Reset functionality with confirmation dialog

### 🔧 Technical Features
- **Asynchronous Processing**: Non-blocking UI during analysis
- **Error Handling**: Comprehensive error management
- **Memory Efficient**: Optimized for performance
- **Cross-Platform**: Works on Linux, Windows, and macOS

---

## 🏗️ Technical Architecture

### Core Components

#### 1. **Main Application** (`main.py`)
- **InferenceThread**: Handles AI processing in background
- **Smartpreter**: Main GUI application class
- **Dark Theme**: Custom styling for professional appearance
- **Event Handlers**: Button clicks, file operations, and user interactions

#### 2. **Syntax Highlighter** (`syntax_highlighter.py`)
- **PythonSyntaxHighlighter**: Custom syntax highlighting for Python code
- **Regex Patterns**: Keywords, strings, comments, numbers, functions
- **Color Schemes**: Dark theme compatible color palette

#### 3. **AI Backend** (`ollama_runner.py`)
- **LocalOllamaRunner**: Manages Ollama server and model interactions
- **Model Management**: Automatic model downloading and availability checks
- **Inference Pipeline**: Handles prompt generation and response processing

### Dependencies
```python
# Core GUI Framework
PyQt5>=5.15.0

# AI Processing
ollama>=0.1.0

# System Requirements
Python>=3.8
```

---

## 📈 Development Progress

### ✅ Completed Features

#### Phase 1: Core Functionality
- [x] Basic PyQt5 GUI setup
- [x] Ollama integration for AI processing
- [x] Single code explanation functionality
- [x] Basic error handling

#### Phase 2: Enhanced UI
- [x] Dark theme implementation
- [x] Resizable panel layout
- [x] Progress indicators
- [x] Professional styling

#### Phase 3: Multi-Modal Analysis
- [x] 5 different review types
- [x] Specialized prompts for each analysis type
- [x] Dynamic UI updates based on review type
- [x] Comprehensive error handling

#### Phase 4: Advanced Features
- [x] Python syntax highlighting
- [x] File load/save operations
- [x] Export functionality (text/markdown)
- [x] Copy to clipboard
- [x] Clear all with confirmation

### 🔄 Current Status
- **Version**: 2.0.0
- **Stability**: Production Ready
- **Performance**: Optimized for local AI processing
- **UI/UX**: Professional grade interface

---

## 🛠️ Installation & Setup

### Prerequisites
1. **Python 3.8+** installed
2. **Ollama** installed and running
3. **Virtual environment** (recommended)

### Step-by-Step Installation

#### 1. Clone/Download Project
```bash
git clone <repository-url>
cd SmartPreter
```

#### 2. Create Virtual Environment
```bash
python -m venv smartpreterenv
source smartpreterenv/bin/activate  # Linux/Mac
# or
smartpreterenv\Scripts\activate     # Windows
```

#### 3. Install Dependencies
```bash
pip install PyQt5 ollama
```

#### 4. Setup Ollama Model
```bash
# Install Ollama (if not already installed)
curl -fsSL https://ollama.ai/install.sh | sh

# Download the model
ollama pull deepseek-coder:6.7b-instruct
```

#### 5. Run Application
```bash
python main.py
```

### File Structure
```
SmartPreter/
├── main.py                 # Main application
├── syntax_highlighter.py   # Syntax highlighting
├── ollama_runner.py        # AI backend
├── DOCUMENTATION.md        # This file
├── README.md              # Project readme
└── requirements.txt       # Dependencies
```

---

## 📖 Usage Guide

### Basic Usage
1. **Launch Application**: Run `python main.py`
2. **Load Code**: Either paste code or load from file
3. **Choose Analysis**: Click desired review type button
4. **Review Results**: View analysis in right panel
5. **Export**: Save results or copy to clipboard

### Advanced Features

#### File Operations
- **Load File**: `📁 Load File` - Open Python files
- **Save Code**: `💾 Save Code` - Save current code
- **Save Results**: `📋 Save Results` - Export review results
- **Clear All**: `🗑️ Clear` - Reset everything

#### Review Types
- **🔍 Explain Code**: Comprehensive code explanation
- **🐛 Find Bugs**: Bug detection and error analysis
- **⚡ Optimize**: Performance optimization suggestions
- **🔒 Security Check**: Security vulnerability analysis
- **📐 Style Review**: Code style and PEP 8 compliance

#### Keyboard Shortcuts
- **Ctrl+O**: Load file
- **Ctrl+S**: Save code
- **Ctrl+C**: Copy results (when results are selected)
- **Ctrl+A**: Select all (in active text area)

---

## 🚀 Deployment Options

### 1. **PyInstaller - Standalone Executable**
```bash
# Install PyInstaller
pip install pyinstaller

# Create executable
pyinstaller --onefile --windowed main.py

# Find executable in dist/ folder
```

### 2. **Docker Container**
```dockerfile
FROM python:3.9-slim

WORKDIR /app
COPY . .

RUN pip install -r requirements.txt
CMD ["python", "main.py"]
```

### 3. **Python Package**
```bash
# Create setup.py and build package
python setup.py sdist bdist_wheel
pip install dist/smartpreter-2.0.0.tar.gz
```

### 4. **Snap Package** (Linux)
```yaml
# snapcraft.yaml
name: smartpreter
version: '2.0.0'
summary: AI Code Reviewer
description: Professional code review with AI
```

---

## 🔮 Future Enhancements

### Planned Features

#### Phase 5: Code Execution
- [ ] Safe code execution environment
- [ ] Output capture and display
- [ ] Interactive debugging mode
- [ ] Unit test generation

#### Phase 6: Multi-Language Support
- [ ] JavaScript support
- [ ] Java support
- [ ] C++ support
- [ ] Language auto-detection

#### Phase 7: Advanced UI
- [ ] Multi-tab interface
- [ ] Code comparison view
- [ ] Settings panel
- [ ] Theme customization

#### Phase 8: Integration Features
- [ ] Git integration
- [ ] VS Code extension
- [ ] Web interface
- [ ] API endpoints

### Enhancement Ideas
- **Real-time Analysis**: Live code review as you type
- **Collaborative Review**: Multi-user support
- **AI Model Selection**: Choose different models
- **Custom Prompts**: User-defined review templates
- **Report Generation**: PDF export with professional formatting

---

## 🤝 Contributing

### Development Setup
1. Fork the repository
2. Create feature branch: `git checkout -b feature-name`
3. Make changes and test thoroughly
4. Submit pull request with detailed description

### Code Style
- Follow PEP 8 guidelines
- Use meaningful variable names
- Add docstrings for all functions
- Include type hints where applicable

### Testing
- Test all UI components
- Verify AI integration works
- Check file operations
- Validate error handling

---

## 🔧 Troubleshooting

### Common Issues

#### 1. **PyQt5 Import Error**
```bash
# Solution: Install PyQt5 in virtual environment
pip install PyQt5
```

#### 2. **Ollama Connection Failed**
```bash
# Solution: Start Ollama server
ollama serve

# Or check if model is available
ollama list
```

#### 3. **Model Not Found**
```bash
# Solution: Download required model
ollama pull deepseek-coder:6.7b-instruct
```

#### 4. **GUI Not Appearing**
```bash
# Solution: Check display settings
export DISPLAY=:0  # Linux
# Or try software rendering
export QT_QUICK_BACKEND=software
```

#### 5. **Performance Issues**
- Ensure adequate RAM (8GB+ recommended)
- Use SSD for better model loading
- Close unnecessary applications
- Consider using smaller AI models

### Debug Mode
```bash
# Run with debug information
python main.py --debug

# Check logs
tail -f smartpreter.log
```

---

## 📊 Performance Metrics

### System Requirements
- **Minimum**: 4GB RAM, 2-core CPU
- **Recommended**: 8GB RAM, 4-core CPU
- **Storage**: 2GB for models
- **OS**: Linux, Windows 10+, macOS 10.14+

### Response Times
- **Code Explanation**: 2-10 seconds
- **Bug Detection**: 3-15 seconds
- **Optimization**: 5-20 seconds
- **Security Review**: 3-12 seconds
- **Style Review**: 1-5 seconds

*Times vary based on code complexity and system performance*

---

## 📝 Version History

### v2.0.0 (Current)
- Multi-modal code analysis
- Syntax highlighting
- File operations
- Professional UI
- Export functionality

### v1.0.0
- Basic code explanation
- Simple UI
- Ollama integration
- Dark theme

---

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

## 📞 Support

For support and questions:
- **Issues**: Create GitHub issue
- **Documentation**: This file
- **Community**: Join discussion forums

---

**Last Updated**: July 16, 2025
**Version**: 2.0.0
**Status**: Production Ready
