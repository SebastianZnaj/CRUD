from flask import Flask, render_template, request, redirect, url_for
from models.model import ItemList
app = Flask(__name__)


@app.route("/")
def list():
    """ Shows list of todo items stored in the database.
    """
    items = ItemList.get_all()
    return render_template("index.html", items=items)


@app.route("/add", methods=['GET', 'POST'])
def add():
    if request.method == "GET":
        return render_template("add.html")
    elif request.method == "POST":
        name = request.form["name"]
        description = request.form["description"]
        price = request.form["price"]
        last_id = ItemList.last_id()
        item = ItemList(last_id + 1, name, description, price)
        item.save()
        return redirect(url_for("list"))


@app.route("/remove/<item_id>")
def remove(item_id):
    """ Removes todo item with selected id from the database """
    item_to_remove = ItemList.get_by_id(item_id)
    item_to_remove.delete()
    return redirect(url_for("list"))



if __name__ == "__main__":
    app.run(debug=True)

