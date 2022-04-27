import json
import os

from flask import Flask, render_template, jsonify, request, make_response, url_for

app = Flask(__name__)


@app.route('/GET/subject', methods=['GET'])
def getting():
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    json_url = os.path.join(SITE_ROOT, 'static', 'data.json')
    res = json.load(open(json_url, encoding='utf-8'))

    return jsonify(res)


@app.route('/POST/subject', methods=['POST'])
def posting():
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    json_url = os.path.join(SITE_ROOT, 'static', 'data.json')
    res = json.load(open(json_url, encoding='utf-8'))

    res["data"].append({
        "id": 11,
        "name": 'Японська мова'
    })

    return jsonify(res)


@app.route('/PUT/subject/<int:id>', methods=['PUT'])
def putting(id):
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    json_url = os.path.join(SITE_ROOT, 'static', 'data.json')
    res = json.load(open(json_url, encoding='utf-8'))

    res["data"][id - 1].update({
        "id": 34,
        "name": "nothing"
    })

    return jsonify(res)


@app.route('/DELETE/subject/<int:id>', methods=['DELETE'])
def deleting(id):
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    json_url = os.path.join(SITE_ROOT, 'static', 'data.json')
    res = json.load(open(json_url, encoding='utf-8'))

    del res["data"][id - 1]

    return jsonify(res)


if __name__ == '__main__':
    app.run(debug=True)
