#!/usr/bin/env python3
"""
SmartPreter Build Script
Creates standalone executable using PyInstaller
"""

import os
import sys
import shutil
import subprocess
from pathlib import Path

def clean_build():
    """Clean previous build artifacts"""
    dirs_to_clean = ['build', 'dist', '__pycache__']
    
    for dir_name in dirs_to_clean:
        if os.path.exists(dir_name):
            print(f"🧹 Cleaning {dir_name}/")
            shutil.rmtree(dir_name)
    
    # Clean .pyc files
    for root, dirs, files in os.walk('.'):
        for file in files:
            if file.endswith('.pyc'):
                os.remove(os.path.join(root, file))

def create_icon():
    """Create a placeholder icon if it doesn't exist"""
    icon_path = Path('assets/icon.ico')
    icon_path.parent.mkdir(exist_ok=True)
    
    if not icon_path.exists():
        print("📦 Creating placeholder icon...")
        # Create a simple text file as placeholder
        with open(icon_path, 'w') as f:
            f.write("# Placeholder icon - replace with actual .ico file")

def build_executable():
    """Build standalone executable"""
    print("🔨 Building SmartPreter executable...")
    
    # Ensure assets directory exists
    create_icon()
    
    # PyInstaller command
    cmd = [
        'pyinstaller',
        '--onefile',                    # Single executable
        '--windowed',                   # No console window
        '--name=SmartPreter',           # Executable name
        '--add-data=syntax_highlighter.py:.',
        '--add-data=ollama_runner.py:.',
        '--hidden-import=PyQt5.QtCore',
        '--hidden-import=PyQt5.QtGui',
        '--hidden-import=PyQt5.QtWidgets',
        '--hidden-import=ollama',
        '--clean',                      # Clean cache
        '--noconfirm',                  # Overwrite without asking
        'main.py'
    ]
    
    # Add icon if it exists and is a real ico file
    if os.path.exists('assets/icon.ico') and os.path.getsize('assets/icon.ico') > 100:
        cmd.insert(-1, '--icon=assets/icon.ico')
    
    try:
        subprocess.run(cmd, check=True)
        print("✅ Executable built successfully!")
        print(f"📁 Output: {os.path.abspath('dist/SmartPreter')}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Build failed: {e}")
        return False
    except FileNotFoundError:
        print("❌ PyInstaller not found. Install with: pip install pyinstaller")
        return False

def create_distribution():
    """Create distribution packages"""
    print("📦 Creating distribution packages...")
    
    # Create directories
    os.makedirs('dist', exist_ok=True)
    
    # Files to include in distribution
    files_to_include = [
        'main.py',
        'syntax_highlighter.py',
        'ollama_runner.py',
        'requirements.txt',
        'README.md',
        'LICENSE'
    ]
    
    # Create source distribution
    print("📦 Creating source distribution...")
    import tarfile
    with tarfile.open('dist/smartpreter-source.tar.gz', 'w:gz') as tar:
        for file in files_to_include:
            if os.path.exists(file):
                tar.add(file)
        
        # Add docs if exists
        if os.path.exists('docs'):
            tar.add('docs')
    
    # Create ZIP for Windows
    print("📦 Creating Windows ZIP...")
    import zipfile
    with zipfile.ZipFile('dist/smartpreter-windows.zip', 'w') as zip_file:
        for file in files_to_include:
            if os.path.exists(file):
                zip_file.write(file)
        
        # Add docs if exists
        if os.path.exists('docs'):
            for root, dirs, files in os.walk('docs'):
                for file in files:
                    file_path = os.path.join(root, file)
                    zip_file.write(file_path)

def main():
    """Main build process"""
    print("🚀 Starting SmartPreter build process...")
    
    # Clean previous builds
    clean_build()
    
    # Build executable
    if build_executable():
        print("✅ Build completed successfully!")
        
        # Create distribution packages
        create_distribution()
        
        print("\n📦 Build artifacts created:")
        if os.path.exists('dist'):
            for item in os.listdir('dist'):
                print(f"  - {item}")
        
        print("\n🎉 SmartPreter build complete!")
        print("📁 Check the dist/ folder for your executable and distribution packages.")
        
    else:
        print("❌ Build failed!")
        sys.exit(1)

if __name__ == "__main__":
    main()
