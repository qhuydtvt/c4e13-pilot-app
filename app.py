from flask import Flask, render_template
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


if __name__ == '__main__':
  app.run(debug=True)
