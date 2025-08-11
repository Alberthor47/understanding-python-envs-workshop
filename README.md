# Understanding Python Environments Workshop

![Python](https://img.shields.io/badge/python-v3.8+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Workshop](https://img.shields.io/badge/workshop-GHW%20Beginners-orange.svg)

**A comprehensive workshop for understanding Python environments, virtual environments, and containerization.**

Presented at **Global Hack Week 🌐 Beginners** by Alberto Camarena

---

## 📋 Table of Contents

- [Overview](#overview)
- [Workshop Structure](#workshop-structure)
- [Prerequisites](#prerequisites)
- [Quick Start](#quick-start)
- [Project Structure](#project-structure)
- [Learning Objectives](#learning-objectives)
- [Hands-On Activities](#hands-on-activities)
- [Troubleshooting](#troubleshooting)
- [Resources](#resources)
- [Contributing](#contributing)
- [License](#license)

---

## 🎯 Overview

This workshop teaches you everything you need to know about Python environments - from the basics of what Python needs to run, to advanced containerization techniques. Perfect for beginners who want to understand how to manage Python projects professionally.

### Why This Workshop Matters

- **Reproducibility**: Ensure your code works the same everywhere
- **Isolation**: Prevent dependency conflicts between projects
- **Collaboration**: Share exact development setups with your team
- **Deployment**: Package applications for production environments

---

## 🏗 Workshop Structure

### Part 1: Foundations
- What's needed to run Python
- Interpreter vs Environment vs Project
- Virtual environments with `venv`, `virtualenv`, `conda`, and `poetry`
- Common pitfalls and troubleshooting

### Part 2: Advanced Topics
- Environment switching and management
- Best practices for dependency management
- Containerization with Docker
- When to use containers vs virtual environments

---

## 📚 Prerequisites

### Required
- Python 3.8+ installed on your system
- Basic command line familiarity
- Text editor or IDE (VS Code recommended)

### Optional (for Part 2)
- Docker Desktop installed
- Basic Git knowledge

### Installation Check
```bash
# Check Python version
python --version  # or python3 --version

# Check pip
pip --version

# Check Docker (optional)
docker --version
```

---

## 🚀 Quick Start

### 1. Clone the Repository
```bash
git clone https://github.com/Alberthor47/understanding-python-envs-workshop.git
cd understanding-python-envs-workshop
```

### 2. Try the Debug Activity
```bash
# This will fail - that's expected!
python script.py

# Fix it by creating a virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
python script.py
```

### 3. Explore Containerization
```bash
cd container
./run.sh  # Interactive script for Docker demo
```

### 4. View the Slides
Open `slides/slides.html` or `slides/slides.pdf` in your browser or PDF viewer.

---

## 📁 Project Structure

```
understanding-python-envs-workshop/
├── README.md                 # This file
├── .gitignore               # Git ignore rules
├── requirements.txt         # Project dependencies
├── script.py               # Debug activity file
├── system.py               # System information utility
├── slides/                 # Workshop presentation
│   ├── slides.md           # Part 1 slides (Marp format)
│   ├── slides2.md          # Part 2 slides
│   ├── slides.html         # Rendered HTML
│   ├── slides.pdf          # PDF version
│   └── README.md           # Slides documentation
└── container/              # Docker examples
    ├── README.md           # Container overview
    ├── README-container.md # Detailed container guide
    ├── app.py             # Flask demo application
    ├── requirements.txt   # Container dependencies
    ├── Dockerfile         # Container definition
    ├── docker-compose.yml # Multi-service setup
    ├── .dockerignore      # Docker ignore rules
    ├── .env.example       # Environment variables template
    └── run.sh             # Build and run script
```

---

## 🎓 Learning Objectives

By the end of this workshop, you'll be able to:

### Part 1: Foundations
- [x] Explain what components are needed to run Python code
- [x] Distinguish between Python interpreter, environment, and project
- [x] Create and manage isolated Python environments
- [x] Use `venv`, `virtualenv`, `conda`, and `poetry` effectively
- [x] Troubleshoot common environment issues
- [x] Debug dependency problems

### Part 2: Advanced Usage
- [x] Switch between multiple environments efficiently
- [x] Apply best practices for dependency management
- [x] Choose between virtual environments and containers
- [x] Containerize Python applications with Docker
- [x] Set up multi-service applications with docker-compose
- [x] Configure development vs production environments

---

## 🛠 Hands-On Activities

### Activity 1: Debug This! 🐛
**Location**: `script.py`

Practice troubleshooting a common `ModuleNotFoundError`:
1. Run the script and observe the error
2. Identify the missing dependency
3. Create a virtual environment
4. Install dependencies
5. Verify the fix

### Activity 2: Environment Comparison 📊
**Location**: Root directory

Compare different environment tools:
```bash
# Try with venv
python -m venv test-venv
source test-venv/bin/activate
pip install requests
deactivate

# Try with conda (if available)
conda create -n test-conda python=3.11
conda activate test-conda
conda install requests
conda deactivate
```

### Activity 3: Container Workshop 🐳
**Location**: `container/`

Learn Docker basics:
1. Build a Python application container
2. Run the application
3. Test with different configurations
4. Use docker-compose for multi-service setup

---

## 🔧 Environment Tools Comparison

| Tool | Manages Python Version? | Manages Packages? | Handles Non-Python Deps? | Best For |
|------|------------------------|-------------------|-------------------------|----------|
| **venv** | ❌ | ✅ | ❌ | Simple projects, built into Python |
| **virtualenv** | ❌ | ✅ | ❌ | Legacy projects, more features than venv |
| **conda** | ✅ | ✅ | ✅ | Data science, complex dependencies |
| **poetry** | ❌ | ✅ | ❌ | Modern projects, dependency resolution |
| **pyenv** | ✅ | ❌ | ❌ | Managing multiple Python versions |
| **Docker** | ✅ | ✅ | ✅ | Deployment, full isolation |

---

## 🩺 Troubleshooting

### Common Issues

#### "Command not found: python"
```bash
# Try python3 instead
python3 --version

# Or add alias to your shell profile
echo "alias python=python3" >> ~/.bashrc  # or ~/.zshrc
```

#### "ModuleNotFoundError"
```bash
# Check which Python you're using
which python
which pip

# Check if you're in the right environment
pip list

# Install the missing package
pip install package-name
```

#### "Permission denied"
```bash
# Don't use sudo with pip in virtual environments
# Create a virtual environment instead
python -m venv .venv
source .venv/bin/activate
pip install package-name
```

#### Docker Issues
```bash
# Check if Docker is running
docker version

# Check available space
docker system df

# Clean up if needed
docker system prune
```

---

## 📖 Additional Resources

### Official Documentation
- [Python Virtual Environments Guide](https://docs.python.org/3/tutorial/venv.html)
- [pip User Guide](https://pip.pypa.io/en/stable/user_guide/)
- [Conda Documentation](https://docs.conda.io/en/latest/)
- [Poetry Documentation](https://python-poetry.org/docs/)
- [Docker Python Guide](https://docs.docker.com/language/python/)

### Recommended Reading
- [Python Packaging Authority](https://www.pypa.io/)
- [Real Python: Virtual Environments](https://realpython.com/python-virtual-environments-a-primer/)
- [Effective Python Environments](https://www.effectivepython.com/)

### Tools to Explore
- [pyenv](https://github.com/pyenv/pyenv) - Python version management
- [pipenv](https://pipenv.pypa.io/) - Higher-level pip + virtualenv
- [PDM](https://pdm.fming.dev/) - Modern dependency management
- [Hatch](https://hatch.pypa.io/) - Modern project management

---

### Workshop Schedule
This workshop was presented at **Global Hack Week Beginners**:
- **Part 1**: August 8, 2025
- **Part 2**: August 11, 2025

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

**Happy Hacking! 🐍✨**

> Remember: The best environment is the one that works reliably for your project and team!
