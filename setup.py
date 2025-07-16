from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="smartpreter",
    version="2.0.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="AI-powered code review application with local processing",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/smartpreter",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Software Development :: Code Generators",
        "Topic :: Software Development :: Quality Assurance",
        "Topic :: Text Processing :: Linguistic",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "smartpreter=main:main",
        ],
    },
    keywords="code review, AI, static analysis, Python, GUI, PyQt5, Ollama",
    project_urls={
        "Bug Reports": "https://github.com/yourusername/smartpreter/issues",
        "Source": "https://github.com/yourusername/smartpreter",
        "Documentation": "https://github.com/yourusername/smartpreter/blob/main/DOCUMENTATION.md",
    },
)
