from flask import Flask, render_template, request
import requests


app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        search_input = request.form.get("searchInput")
        books = requests.get("http://my-api-server.gvgndnaudhgyd7gm.eastus.azurecontainer.io/").json()

        matches = []
        for book in books:
            for value in book.values():
                if search_input.lower() in str(value).lower():
                    matches.append(book)
                    break
            
        return render_template("browse.html", results = matches)

    return render_template("browse.html",  results=None)
