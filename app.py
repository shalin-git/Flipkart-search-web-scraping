import scraper
from flask import Flask


app = Flask(__name__)

@app.route("/<search>")
def fun(search):
    return scraper.flipkart(search)

if __name__ == "__main__":
    app.run(debug=True)