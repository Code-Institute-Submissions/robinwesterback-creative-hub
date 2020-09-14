import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'creativeHub'
app.config["MONGO_URI"] = 'mongodb+srv://robin:Kungen1989@myfirstcluster.lxmdn.mongodb.net/creativeHub?retryWrites=true&w=majority'

mongo = PyMongo(app)


@app.route('/')
@app.route('/get_work')
def get_work():
    return render_template("work.html", work=mongo.db.work.find())


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
