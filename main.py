from flask import Flask, jsonify
from utils import search_by_title

app = Flask(__name__)
app.config["JSON_SORT_KEYS"] = False

@app.route("/<film>")
def page_index(film):
    res = search_by_title(film)
    return jsonify(res)


if __name__ == "__main__":
    app.run(debug=True)