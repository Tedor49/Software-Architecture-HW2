from flask import Flask, jsonify, request
from datetime import datetime
import threading

app = Flask(__name__)
lock = threading.Lock()
messages = []


@app.route('/messages', methods=['POST'])
def post_message():
    data = request.json
    message_text = data.get('message')
    if message_text:
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        with lock:
            messages.append({'message': message_text, 'timestamp': timestamp})
        return jsonify({'status': 'success', 'timestamp': timestamp}), 201
    return jsonify({'status': 'error', 'message': 'Message is required.'}), 400


@app.route('/messages', methods=['GET'])
def get_messages():
    with lock:
        return jsonify(messages), 200


@app.route('/messages/count', methods=['GET'])
def count_messages():
    with lock:
        return jsonify({'count': len(messages)}), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)