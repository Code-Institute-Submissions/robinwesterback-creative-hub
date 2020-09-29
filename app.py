import os
import bcrypt
from flask import Flask, render_template, redirect, request, url_for, session
from flask_pymongo import PyMongo
from bson.objectid import ObjectId


# DB URI import for local workspace
from os import path
if path.exists('env.py'):
    import env

app = Flask(__name__)

app.config['MONGO_DBNAME'] = os.environ.get('MONGO_DBNAME')
app.config['MONGO_URI'] = os.environ.get('MONGO_URI')

mongo = PyMongo(app)


# Index
@app.route('/')
def home():
    return render_template('index.html', page_title='Home')


# User Interface
@app.route('/user_interface')
def user_interface():
    if 'email' in session:
        return render_template('userInterface.html', page_title='User Interface')

    return render_template('login.html', page_title='Login')


# Login
@app.route('/login', methods=['POST'])
def login():
    users = mongo.db.users
    login_user = users.find_one({'email': request.form['email']})

    if login_user:
        if bcrypt.hashpw(request.form['password'].encode('utf-8'), login_user['password']) == login_user['password']:
            session['email'] = request.form['email']
            return redirect(url_for('user_interface'))

    return 'Invalid email/password combination'


# Register
@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        users = mongo.db.users
        existing_user = users.find_one({'email': request.form['email']})

        if existing_user is None:
            hashpass = bcrypt.hashpw(
                request.form['password'].encode('utf-8'), bcrypt.gensalt())
            users.insert({'email': request.form['email'],
                          'first_name': request.form.get('first_name'),
                          'last_name': request.form.get('last_name'),
                          'email': request.form.get('email'),
                          'phone': request.form.get('phone'),
                          'city': request.form.get('city'),
                          'country': request.form.get('country'),
                          'password': hashpass})
            session['email'] = request.form['email']
            return redirect(url_for('user_interface'))

        return 'That email already exists!'

    return render_template('register.html')


# Register Creative
@app.route('/register_creative', methods=['POST', 'GET'])
def register_creative():
    if request.method == 'POST':
        users = mongo.db.users
        creatives = mongo.db.creatives
        existing_user = users.find_one({'email': request.form['email']})

        if existing_user is None:
            hashpass = bcrypt.hashpw(
                request.form['password'].encode('utf-8'), bcrypt.gensalt())
            users.insert({'email': request.form['email'],
                          'first_name': request.form.get('first_name'),
                          'last_name': request.form.get('last_name'),
                          'email': request.form.get('email'),
                          'phone': request.form.get('phone'),
                          'city': request.form.get('city'),
                          'country': request.form.get('country'),
                          'password': hashpass})
            creatives.insert({'skills': request.form['skills'],
                              'hourly_rate': request.form['hourly_rate'],
                              'description': request.form['description']})
            session['email'] = request.form['email']
            return redirect(url_for('user_interface'))

        return 'That email already exists!'

    return render_template('register_creative.html')


# Register Client
@app.route('/register_client', methods=['POST', 'GET'])
def register_client():
    if request.method == 'POST':
        users = mongo.db.users
        clients = mongo.db.clients
        existing_user = users.find_one({'email': request.form['email']})

        if existing_user is None:
            hashpass = bcrypt.hashpw(
                request.form['password'].encode('utf-8'), bcrypt.gensalt())
            users.insert({'email': request.form['email'],
                          'first_name': request.form.get('first_name'),
                          'last_name': request.form.get('last_name'),
                          'email': request.form.get('email'),
                          'password': hashpass})
            clients.insert({'company_name': request.form['company_name'],
                            'phone': request.form.get('phone'),
                            'address': request.form['address'],
                            'city': request.form.get('city'),
                            'country': request.form.get('country'),
                            'vat_id': request.form['vat_id']})
            session['email'] = request.form['email']
            return redirect(url_for('user_interface'))

        return 'That email already exists!'

    return render_template('register_client.html')


# Get Creatives
@app.route('/get_creatives')
def get_creatives():
    return render_template("creatives.html",
                           creatives=mongo.db.creatives.find())


# Create creative
@app.route('/create_creative')
def create_creative():
    return render_template('createCreative.html')


# Insert creative
@app.route('/insert_creative', methods=['POST'])
def insert_creative():
    creatives = mongo.db.creatives
    creatives.insert_one(request.form.to_dict())
    return redirect(url_for('get_creatives'))


# Edit creative
@app.route('/edit_user/<creative_id>')
def edit_creative(creative_id):
    the_creative = mongo.db.creatives.find_one({"_id": ObjectId(creative_id)})
    return render_template('editCreative.html', creative=the_creative)


# Update creative
@app.route('/update_creative/<creative_id>', methods=["POST"])
def update_creative(creative_id):
    creatives = mongo.db.creatives
    creatives.update({'_id': ObjectId(creative_id)},
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


# Delete creative
@app.route('/delete_creative/<creative_id>')
def delete_creative(creative_id):
    mongo.db.creatives.remove({'_id': ObjectId(creative_id)})
    return redirect(url_for('get_creatives'))


if __name__ == '__main__':
    app.secret_key = 'mysecret'
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
