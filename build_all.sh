#!/bin/bash

# SmartPreter Complete Build Script
# Creates all distribution packages and installers

echo "🚀 SmartPreter Complete Build Process"
echo "====================================="

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Function to print colored output
print_status() {
    echo -e "${GREEN}[INFO]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    print_error "Python 3 is not installed or not in PATH"
    exit 1
fi

# Check if pip is installed
if ! command -v pip &> /dev/null; then
    print_error "pip is not installed"
    exit 1
fi

# Create virtual environment for building
print_status "Creating build environment..."
python3 -m venv build_env
source build_env/bin/activate

# Install build dependencies
print_status "Installing build dependencies..."
pip install --upgrade pip
pip install pyinstaller setuptools wheel twine

# Install project dependencies
print_status "Installing project dependencies..."
pip install -r requirements.txt

# Create directories
print_status "Creating output directories..."
mkdir -p dist
mkdir -p installers
mkdir -p assets

# Create placeholder icon if it doesn't exist
if [ ! -f "assets/icon.ico" ]; then
    print_warning "No icon found, creating placeholder..."
    touch assets/icon.ico
fi

# Build executable
print_status "Building standalone executable..."
python build_installer.py

# Build Python package
print_status "Building Python package..."
python setup.py sdist bdist_wheel

# Create Docker image (optional)
if command -v docker &> /dev/null; then
    print_status "Building Docker image..."
    docker build -t smartpreter:latest .
    docker save smartpreter:latest -o dist/smartpreter-docker.tar
else
    print_warning "Docker not found, skipping Docker build"
fi

# Create installation script
print_status "Creating installation script..."
cat > installers/install.sh << 'EOF'
#!/bin/bash

# SmartPreter Installation Script

echo "🚀 Installing SmartPreter..."

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is required but not installed"
    exit 1
fi

# Check if Ollama is installed
if ! command -v ollama &> /dev/null; then
    echo "⚠️  Ollama is not installed. Please install it from https://ollama.ai"
    read -p "Continue anyway? (y/n): " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        exit 1
    fi
fi

# Create directory
INSTALL_DIR="$HOME/.local/share/smartpreter"
mkdir -p "$INSTALL_DIR"

# Extract files
echo "📦 Extracting SmartPreter..."
tar -xzf smartpreter-source.tar.gz -C "$INSTALL_DIR"

# Create virtual environment
echo "🔧 Setting up Python environment..."
cd "$INSTALL_DIR"
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Create launcher script
cat > "$HOME/.local/bin/smartpreter" << 'LAUNCHER'
#!/bin/bash
cd "$HOME/.local/share/smartpreter"
source venv/bin/activate
python main.py
LAUNCHER

chmod +x "$HOME/.local/bin/smartpreter"

# Create desktop entry
mkdir -p "$HOME/.local/share/applications"
cat > "$HOME/.local/share/applications/smartpreter.desktop" << 'DESKTOP'
[Desktop Entry]
Version=1.0
Type=Application
Name=SmartPreter
Comment=AI-powered code review application
Exec=$HOME/.local/bin/smartpreter
Icon=applications-development
Terminal=false
Categories=Development;IDE;
DESKTOP

echo "✅ SmartPreter installed successfully!"
echo "🚀 You can now run 'smartpreter' from the command line"
echo "   or find it in your applications menu"
EOF

chmod +x installers/install.sh

# Create Windows batch installer
cat > installers/install.bat << 'EOF'
@echo off
echo Installing SmartPreter...

REM Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Python is required but not installed
    pause
    exit /b 1
)

REM Create directory
set INSTALL_DIR=%APPDATA%\SmartPreter
mkdir "%INSTALL_DIR%" 2>nul

REM Extract files (assuming user has extracted manually)
echo Copying files...
copy /Y *.py "%INSTALL_DIR%\"
copy /Y requirements.txt "%INSTALL_DIR%\"
copy /Y README.md "%INSTALL_DIR%\"

REM Create virtual environment
echo Setting up Python environment...
cd /d "%INSTALL_DIR%"
python -m venv venv
call venv\Scripts\activate.bat

REM Install dependencies
pip install -r requirements.txt

REM Create launcher
echo @echo off > "%INSTALL_DIR%\smartpreter.bat"
echo cd /d "%INSTALL_DIR%" >> "%INSTALL_DIR%\smartpreter.bat"
echo call venv\Scripts\activate.bat >> "%INSTALL_DIR%\smartpreter.bat"
echo python main.py >> "%INSTALL_DIR%\smartpreter.bat"

echo SmartPreter installed successfully!
echo You can run it from: %INSTALL_DIR%\smartpreter.bat
pause
EOF

# Create summary
print_status "Build completed! Created files:"
echo "================================"
ls -la dist/
echo ""
ls -la installers/
echo ""

print_status "Distribution packages created:"
echo "- dist/SmartPreter (executable)"
echo "- dist/smartpreter-*.whl (Python package)"
echo "- dist/smartpreter-*.tar.gz (source distribution)"
echo "- installers/install.sh (Linux/Mac installer)"
echo "- installers/install.bat (Windows installer)"

if [ -f "dist/smartpreter-docker.tar" ]; then
    echo "- dist/smartpreter-docker.tar (Docker image)"
fi

print_status "To distribute your application:"
echo "1. Share the executable: dist/SmartPreter"
echo "2. Or share the installer: installers/install.sh"
echo "3. Or upload to PyPI: twine upload dist/*"

# Cleanup
deactivate
rm -rf build_env

print_status "Build process complete! 🎉"
