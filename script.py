#!/usr/bin/env python3
"""
Activity: Debug This!

This script demonstrates a common Python environment issue.
Try running this script and debug the ModuleNotFoundError.

Steps to debug:
1. Check which Python you're using: which python
2. Check which pip is active: pip --version
3. List installed packages: pip list
4. Install the missing package in the correct environment
5. Document your solution

Expected error: ModuleNotFoundError: No module named 'flask'
"""

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, Python Environment Workshop!"

@app.route('/health')
def health():
    return {"status": "healthy", "message": "Flask is working!"}

if __name__ == '__main__':
    print("Starting Flask application...")
    print("If you see this message, Flask was imported successfully!")
    app.run(debug=True, port=5000)
