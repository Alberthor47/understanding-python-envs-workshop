#!/usr/bin/env python3
"""
Sample Flask Application for Container Demo

This is a simple web application that demonstrates:
- Environment variable usage
- Health checks
- Logging
- Basic API endpoints

Perfect for containerization examples!
"""

import os
import logging
from datetime import datetime
from flask import Flask, jsonify, request

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)

# Configuration from environment variables
app.config['ENV'] = os.getenv('FLASK_ENV', 'production')
app.config['DEBUG'] = os.getenv('FLASK_DEBUG', 'False').lower() == 'true'
app.config['HOST'] = os.getenv('HOST', '0.0.0.0')
app.config['PORT'] = int(os.getenv('PORT', 8000))

@app.route('/')
def home():
    """Home endpoint with environment info"""
    return jsonify({
        'message': 'Welcome to the Python Environment Container Demo!',
        'environment': app.config['ENV'],
        'python_version': os.sys.version,
        'timestamp': datetime.now().isoformat(),
        'container_info': {
            'hostname': os.getenv('HOSTNAME', 'unknown'),
            'user': os.getenv('USER', 'unknown')
        }
    })

@app.route('/health')
def health_check():
    """Health check endpoint for container orchestration"""
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.now().isoformat(),
    }), 200

@app.route('/env')
def environment_info():
    """Show relevant environment variables"""
    env_vars = {
        'FLASK_ENV': os.getenv('FLASK_ENV'),
        'FLASK_DEBUG': os.getenv('FLASK_DEBUG'),
        'HOST': os.getenv('HOST'),
        'PORT': os.getenv('PORT'),
        'PATH': os.getenv('PATH')[:100] + '...' if os.getenv('PATH') else None
    }
    
    return jsonify({
        'environment_variables': env_vars,
        'sys_path': os.sys.path[:5]  # First 5 entries only
    })

@app.route('/api/echo', methods=['POST'])
def echo():
    """Echo endpoint for testing"""
    data = request.get_json() or {}
    return jsonify({
        'received': data,
        'method': request.method,
        'timestamp': datetime.now().isoformat()
    })

@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Endpoint not found'}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({'error': 'Internal server error'}), 500

if __name__ == '__main__':
    logger.info(f"Starting application on {app.config['HOST']}:{app.config['PORT']}")
    logger.info(f"Environment: {app.config['ENV']}")
    logger.info(f"Debug mode: {app.config['DEBUG']}")
    
    app.run(
        host=app.config['HOST'],
        port=app.config['PORT'],
        debug=app.config['DEBUG']
    )
