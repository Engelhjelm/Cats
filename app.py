from flask import Flask, request, jsonify
from flask_cors import CORS
from src.db_handler import create_content, get_content


app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/cats/list', methods=['GET'])
def cats_get_content():
    return jsonify(get_content())

@app.route('/cats/create',  methods = ['POST'])
def cats_create_content():
    content = request.get_json()
    return jsonify(create_content(content))

if __name__ == "__main__":
    #app.debug = True
    #app.run(debug=True)
    app.run()
