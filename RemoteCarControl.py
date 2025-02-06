from flask import Flask, request, jsonify
import serial

# Setting up the connection with Arduino
arduino = serial.Serial('/dev/ttyUSB0', 9600) # Define the port

app = Flask(__name__)

# PAGE CONTENT
@app.route('/')
def index():
    return '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Remote Car Control</title>
    <style>
    body {
        font-family: Arial, sans-serif;
        margin: 0;
        padding: 0;
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100vh;
        background-color: #f4f4f4;
    }
    .container {
        text-align: center;
        background: white;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        width: 300px;
    }
    h1 {
        color: #333;
        margin-bottom: 20px;
    }
    .control-panel {
        display: grid;
        grid-template-rows: repeat(3, 1fr);
        grid-template-columns: repeat(3, 1fr);
        gap: 10px;
        justify-items: center;
        align-items: center;
    }
    .arrow {
        width: 80px;
        height: 80px;
        display: flex;
        justify-content: center;
        align-items: center;
        border: 2px solid #007bff;
        background-color: #e7f1ff;
        color: #007bff;
        font-size: 24px;
        font-weight: bold;
        border-radius: 10px;
        cursor: pointer;
        transition: all 0.3s ease;
    }
    .arrow:hover {
        background-color: #007bff;
        color: white;
    }
    .stop {
        background-color: #dc3545;
        border-color: #dc3545;
        color: white;
    }
    .stop:hover {
        background-color: #a71d2a;
    }
    #status {
        margin-top: 20px;
        font-size: 16px;
        color: #333;
    }
    </style>
        <!--BUTTONS FOR COMMANDS-->
    </head>
    <body>
    <div class="container">
        <h1>Car Control</h1>
        <div class="control-panel">
        <div></div>
        <div class="arrow" onclick="sendCommand('f')">↑</div>
        <div></div>
        <div class="arrow" onclick="sendCommand('r')">←</div>
        <div class="arrow stop" onclick="sendCommand('s')">■</div>
        <div class="arrow" onclick="sendCommand('l')">→</div>
        <div></div>
        <div class="arrow" onclick="sendCommand('b')">↓</div>
        <div></div>
        </div>
        <div id="status">Status: Waiting for command...</div>
    </div>
        <!--FUNCTION TO SEND MOVEMENT COMMANDS TO THE SERVER BASED ON THE SPECIFIED DIRECTION-->
    <script>
    function sendCommand(direction) {
        fetch('/move', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ direction: direction })
        })
        .then(response => response.json())
        .then(data => {
            document.getElementById('status').textContent =
            'Status: ' + data.message;
        })
        .catch(error => {
            document.getElementById('status').textContent =
            'Error sending command.';
            console.error('Error:', error);
        });
    }
    </script>
    </body>
    </html>
    '''

# Path to process commands
@app.route('/move', methods=['POST']) #METHOD FOR SEND THE MOVMENT
def move():
    data = request.get_json()
    direction = data.get('direction', '')
    if direction in ['f', 'b', 'l', 'r', 's']: #SPECIFIED LETTERS OF MOVEMENTS
        arduino.write(direction.encode()) # Send the command to the Arduino --HERE
        return jsonify({'message': f'Movement sent: {direction}'}) # MAYBE WORKING
    else:
        return jsonify({'message': 'Unrecognized command'}), 400 #NOT WORKING 
# Starts the app.
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4353)  # App will start on your IP (EXAMPLE) 192.168.1.100 and port 4353

