from flask import Flask, jsonify
import subprocess

app = Flask(__name__)
@app.route('/', methods=['GET'])
def index():
    return jsonify({'message': 'Hello World'})

@app.route('/start_etl', methods=['POST'])
def start_etl():
    app.logger.info("start_etl hitted!")
    try:
        # Run the ETL script
        result = subprocess.run(['python3', '/app/main.py'], capture_output=True, text=True)
        if result.returncode == 0:
            return jsonify({'status': 'success', 'output': result.stdout}), 200
        else:
            return jsonify({'status': 'error', 'output': result.stderr}), 500
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
 