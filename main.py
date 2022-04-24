from flask import Flask, jsonify
from utils import search_by_title, search_by_release_year, search_by_rating, search_by_genre

app = Flask(__name__)
app.config["JSON_SORT_KEYS"] = False
app.config["JSON_AS_ASCII"] = False


@app.route("/movie/<film>")
def search_film(film):
    result = search_by_title(film)
    return jsonify(result)


@app.route("/movie/<int:year1>/to/<int:year2>")
def films_by_yaers(year1, year2):
    result = search_by_release_year(year1,year2)
    return jsonify(result)


@app.route("/rating/<rating>")
def films_by_rating(rating):
    result = search_by_rating(rating)
    return jsonify(result)


@app.route("/genre/<genre>")
def films_by_genre(genre):
    result = search_by_genre(genre)
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)