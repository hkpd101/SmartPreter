#!/bin/bash

# SmartPreter Deployment Script for Linux/macOS

echo "🚀 SmartPreter Deployment Script"
echo "================================="

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3.8+ first."
    exit 1
fi

# Check if Ollama is installed
if ! command -v ollama &> /dev/null; then
    echo "❌ Ollama is not installed. Installing Ollama..."
    curl -fsSL https://ollama.ai/install.sh | sh
fi

# Create virtual environment
echo "📦 Creating virtual environment..."
python3 -m venv smartpreter-env
source smartpreter-env/bin/activate

# Install dependencies
echo "📦 Installing dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

# Install PyInstaller for creating executable
echo "📦 Installing PyInstaller..."
pip install pyinstaller

# Download AI model
echo "🤖 Downloading AI model..."
ollama pull deepseek-coder:6.7b-instruct

# Create executable
echo "🔨 Creating executable..."
pyinstaller --onefile --windowed --name SmartPreter main.py

# Create distribution directory
echo "📁 Creating distribution..."
mkdir -p dist/SmartPreter
cp dist/SmartPreter dist/SmartPreter/
cp README.md dist/SmartPreter/
cp DOCUMENTATION.md dist/SmartPreter/
cp -r assets dist/SmartPreter/ 2>/dev/null || true

# Create desktop entry (Linux)
if [[ "$OSTYPE" == "linux-gnu"* ]]; then
    echo "🖥️ Creating desktop entry..."
    cat > dist/SmartPreter.desktop << EOF
[Desktop Entry]
Version=1.0
Type=Application
Name=SmartPreter
Comment=AI Code Reviewer
Exec=$(pwd)/dist/SmartPreter/SmartPreter
Icon=$(pwd)/dist/SmartPreter/icon.png
Terminal=false
StartupNotify=true
Categories=Development;IDE;
EOF
fi

echo "✅ Deployment complete!"
echo "📁 Executable location: dist/SmartPreter"
echo "🚀 Run: ./dist/SmartPreter/SmartPreter"
echo ""
echo "📋 Distribution package created in dist/ folder"
echo "📖 Read DOCUMENTATION.md for detailed usage instructions"
