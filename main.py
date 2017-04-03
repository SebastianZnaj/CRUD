from flask import Flask, render_template, request, redirect, url_for
from models.model import ItemList
app = Flask(__name__)


@app.route("/")
def list():
    """ Shows list of todo items stored in the database.
    """
    items = ItemList.get_all()
    return render_template("index.html", items=items)


if __name__ == "__main__":
    app.run(debug=True)

