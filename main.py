import json
import os

from flask import Flask, render_template, jsonify, request, make_response, url_for

app = Flask(__name__)

def getData():
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    json_url = os.path.join(SITE_ROOT, 'static', 'data.json')
    res = json.load(open(json_url, encoding='utf-8'))
    return res

res = getData()

@app.route('/subject', methods=['GET'])
def getting():

    return jsonify(res)


@app.route('/subject', methods=['POST'])
def posting():

    res["data"].append({
        "id": 11,
        "name": 'Японська мова'
    })

    return jsonify(res)


@app.route('/subject/<int:id>', methods=['PUT'])
def putting(id):

    res["data"][id - 1].update({
        "id": 34,
        "name": "nothing"
    })

    return jsonify(res)


@app.route('/subject/<int:id>', methods=['DELETE'])
def deleting(id):

    del res["data"][id - 1]

    return jsonify(res)


if __name__ == '__main__':
    app.run(debug=True)
