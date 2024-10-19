from flask import Flask
import os
from datetime import datetime

app = Flask(__name__)

@app.route('/htop')
def htop():
    # Get full name and username
    full_name = "DIMPLE R" 
    username = os.environ.get('USER') or os.environ.get('LOGNAME') or 'Unknown User'
    
    # Get current server time in IST
    server_time = datetime.now().astimezone().strftime('%Y-%m-%d %H:%M:%S')

    # Gather process information from /proc
    process_info = []
    for pid in os.listdir('/proc'):
        if pid.isdigit():  # Check if the directory name is a PID
            try:
                with open(f'/proc/{pid}/stat', 'r') as f:
                    stat = f.read().split()
                    process_info.append(f'PID: {pid}, Name: {stat[1]}, State: {stat[2]}')
            except Exception as e:
                continue  # Skip any PIDs that cannot be accessed

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
        <p><strong>Full Name:</strong> {full_name}</p>
        <p><strong>Username:</strong> {username}</p>
        <p><strong>Server Time (IST):</strong> {server_time}</p>
        <h2>Processes:</h2>
        <pre>{'\n'.join(process_info)}</pre>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
