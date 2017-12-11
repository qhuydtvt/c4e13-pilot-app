from flask import Flask, render_template, request
import mlab
from mongoengine import *

app = Flask(__name__)

#1. Connect to database
mlab.connect()

#2. Design collection
class Item(Document):
    title = StringField()
    image = StringField()
    description = StringField()
    price = IntField()


@app.route('/')
def index():
    items = Item.objects() # Get ALL items
    return render_template('index.html', items=items)


@app.route('/add_item', methods=['GET', 'POST'])
def add_item():
    if request.method == "GET": # Get form
        return render_template('add_item.html')
    elif request.method == "POST": # Receive form
        # 1 Extract data in form
        form = request.form
        title = form['title']
        image = form['image']
        description = form['description']
        price = form['price']

        # 2 Add into database
        new_item = Item(title=title, image=image, description=description, price=price)
        new_item.save() # Save into database

        return "OKe anh"


if __name__ == '__main__':
  app.run(debug=True)
