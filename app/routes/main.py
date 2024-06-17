from flask import jsonify

import app

@app.route('/ping', methods=['GET'])
def ping():
    return jsonify('pong')