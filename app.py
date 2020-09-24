import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

# DB URI import for local workspace
from os import path
if path.exists("env.py"):
    import env

app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")

mongo = PyMongo(app)


@app.route('/')
@app.route('/get_creatives')
def get_creatives():
    return render_template("creatives.html",
                           creatives=mongo.db.creatives.find())


@app.route('/create_creative')
def create_creative():
    return render_template('createCreative.html')


@app.route('/insert_creative', methods=['POST'])
def insert_creative():
    creatives = mongo.db.creatives
    creatives.insert_one(request.form.to_dict())
    return redirect(url_for('get_creatives'))

@app.route('/edit_creative/<creative_id>')
def edit_creative(creative_id):
    the_creative = mongo.db.creatives.find_one({"_id": ObjectId(creative_id)}) 
    return render_template('editCreative.html', creative=the_creative)

@app.route('/update_creative/<creative_id>', methods=["POST"])
def update_creative(creative_id):
    creatives = mongo.db.creatives
    creatives.update( {'_id': ObjectId(creative_id)},
    {
        'first_name': request.form.get('first_name'),
        'last_name': request.form.get('last_name'),
        'email': request.form.get('email'),
        'phone': request.form.get('phone'),
        'city': request.form.get('city'),
        'country': request.form.get('country'),
        'skills': request.form.get('skills'),
        'hourly_rate': request.form.get('hourly_rate'),
        'description': request.form.get('description')
    })
    return redirect(url_for('get_creatives'))

@app.route('/delete_creative/<creative_id>')
def delete_creative(creative_id):
    mongo.db.creatives.remove({'_id': ObjectId(creative_id)})
    return redirect(url_for('get_creatives'))


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
