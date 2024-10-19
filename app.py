from flask import Flask
import os
from datetime import datetime
import pytz
import subprocess

app = Flask(__name__)

@app.route('/htop')
def htop():
    # Get Full name and username
    full_name = "Dimple R"  
    username = os.environ.get('USER') or os.environ.get('LOGNAME') or 'Unknown User'
    
    # Get current server time in IST
    ist = pytz.timezone('Asia/Kolkata')  # IST timezone
    server_time = datetime.now(ist).strftime('%Y-%m-%d %H:%M:%S')

    # Get the top output by running the top command
    try:
        # Run the top command and capture output
        top_output = subprocess.check_output(['top', '-b', '-n', '1']).decode('utf-8')
    except Exception as e:
        top_output = f"Error retrieving top output: {str(e)}"

    # Prepare HTML output
    return f"""
    <html>
    <head>
        <title>System Info</title>
        <style>
            pre {{ font-family: monospace; }}
        </style>
    </head>
    <body>
        <h1>System Information</h1>
        <p><strong>Name:</strong> {full_name}</p>
        <p><strong>Username:</strong> {username}</p>
        <p><strong>Server Time (IST):</strong> {server_time}</p>
        <h2>TOP output:</h2>
        <pre>{top_output}</pre>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
