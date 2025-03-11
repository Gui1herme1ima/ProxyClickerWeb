import os
from app import app

if __name__ == '__main__':
    if os.environ.get('ENV') == 'development':
        app.run(debug=True, host='0.0.0.0', port=5000)
    else:
        app.run(host='0.0.0.0', port=5000)