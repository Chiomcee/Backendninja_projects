from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/about', methods=['GET'])
def get_data():
    data = {
        "gender": "Female",
        "github url": "github.com/Chiomcee",
        "name": "Chioma Igwe",
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run()