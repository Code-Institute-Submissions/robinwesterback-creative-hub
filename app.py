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


def validate_form(form, collection):
    """ Returns an error list if the user, login, brief or
    creative ad forms fails on validation
    """

    # variable initialization
    max_first_name = 30
    max_last_name = 30
    max_email = 40
    max_phone = 30
    max_city = 30
    max_country = 30
    min_password = 8
    max_password = 30
    error_list = []

    # validates users form
    if collection == 'users':
        if not form['first_name'] or len(form['first_name']) > max_first_name:
            error_list.append(
                'First name must not be empty or more than {} characters!'
                .format(max_first_name)
            )

        if not form['last_name'] or len(form['last_name']) > max_last_name:
            error_list.append(
                'Last name must not be empty or more than {} characters!'
                .format(max_last_name)
            )

        if not form['email'] or len(form['email']) > max_email:
            error_list.append(
                'E-mail must not be empty or more than {} characters!'
                .format(max_email)
            )

        if len(form['phone']) > max_phone:
            error_list.append(
                'Phone cannot contain more than {} characters!'
                .format(max_phone)
            )

        if not form['city'] or len(form['city']) > max_city:
            error_list.append(
                'City must not be empty or more than {} characters!'
                .format(max_city)
            )

        if not form['country'] or len(form['country']) > max_country:
            error_list.append(
                'Country must not be empty or more than {} characters!'
                .format(max_country)
            )

        if not form['password']:
            error_list.append(
                'Password must not be empty!'
            )

        if len(form['password']) > max_password:
            error_list.append(
                'Password must not be more than {} characters!'
                .format(max_password)
            )

        if len(form['password']) < min_password:
            error_list.append(
                'Password must not be less than {} characters!'
                .format(min_password)
            )

    # validates login form
    elif collection == 'login':
        if not form['email'] or len(form['email']) > max_email:
            error_list.append(
                'E-mail must not be empty or more than {} characters!'
                .format(max_email)
            )

        if not form['password']:
            error_list.append(
                'Password must not be empty!'
            )

        if len(form['password']) > max_password:
            error_list.append(
                'Password must not be more than {} characters!'
                .format(max_password)
            )

        if len(form['password']) < min_password:
            error_list.append(
                'Password must not be less than {} characters!'
                .format(min_password)
            )

    # returns errors on an empty list
    return error_list


# Index
@app.route('/')
def home():
    return render_template('index.html', page_title='Home')


# Register
@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        users = mongo.db.users
        existing_user = users.find_one({'email': request.form['email']})
        form = request.form
        error_list = validate_form(form, 'users')

        if error_list == []:

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

            error_list.append(
                'The email you want to register is already registered.'
            )

            return render_template('register.html', errors=error_list)

        return render_template('register.html', errors=error_list)

    return render_template('register.html')


# User Interface
@app.route('/user_interface')
def user_interface():
    if 'email' in session:
        user = mongo.db.users.find_one({'email': session['email']})
        briefs = mongo.db.briefs.find({'email': session['email']})
        creatives = mongo.db.creatives.find({'email': session['email']})
        return render_template('userInterface.html', user=user, briefs=briefs, creatives=creatives, page_title='User Interface')

    return render_template('login.html', page_title='Login')


# Login
@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = mongo.db.users
        login_user = user.find_one({'email': request.form['email']})
        form = request.form
        error_list = validate_form(form, 'login')

        if error_list == []:

            if login_user:
                if bcrypt.hashpw(request.form['password'].encode('utf-8'), login_user['password']) == login_user['password']:
                    session['email'] = request.form['email']
                    return redirect(url_for('user_interface'))

            error_list.append(
                'Invalid email/password combination.'
            )

            return render_template('login.html', errors=error_list)

        error_list.append(
            'Invalid email/password combination.'
        )

        return render_template('login.html', errors=error_list)

    return render_template('login.html')


# Logout
@app.route('/logout')
def logout():
    session.clear()

    return render_template('index.html', page_title='Home')


# Update user
@app.route('/update_user', methods=["POST"])
def update_user():
    users = mongo.db.users
    users.update_one({'email': session['email']},
                     {'$set':
                      {
                          'first_name': request.form.get('first_name'),
                          'last_name': request.form.get('last_name'),
                          'phone': request.form.get('phone'),
                          'city': request.form.get('city'),
                          'country': request.form.get('country')
                      }
                      })
    return redirect(url_for('user_interface'))


# Get Creatives
@app.route('/get_creatives')
def get_creatives():
    return render_template("creatives.html",
                           creatives=mongo.db.creatives.find())


# Contact creative
@app.route('/contact_creative/<creative_id>')
def contact_creative(creative_id):
    the_creative = mongo.db.creatives.find_one({"_id": ObjectId(creative_id)})
    return render_template('contactCreative.html', creative=the_creative)


# Create creative
@app.route('/create_creative')
def create_creative():
    user = mongo.db.users.find_one({'email': session['email']})
    skills = mongo.db.skills.find()
    return render_template('createCreative.html', user=user, skills=skills)


# Insert creative
@app.route('/insert_creative', methods=['POST'])
def insert_creative():
    creatives = mongo.db.creatives
    form_data = request.form.to_dict()
    form_data['email'] = session['email']
    creatives.insert_one(form_data)
    return redirect(url_for('user_interface'))


# Edit creative
@app.route('/edit_user/<creative_id>')
def edit_creative(creative_id):
    the_creative = mongo.db.creatives.find_one({"_id": ObjectId(creative_id)})
    skills = mongo.db.skills.find()
    return render_template('editCreative.html', creative=the_creative, skills=skills)


# Update creative
@app.route('/update_creative/<creative_id>', methods=["POST"])
def update_creative(creative_id):
    creatives = mongo.db.creatives
    creatives.update_one({'_id': ObjectId(creative_id)},
                         {'$set':
                          {
                              'first_name': request.form.get('first_name'),
                              'last_name': request.form.get('last_name'),
                              'email': session['email'],
                              'city': request.form.get('city'),
                              'country': request.form.get('country'),
                              'skills': request.form.get('skills'),
                              'hourly_rate': request.form.get('hourly_rate'),
                              'description': request.form.get('description')
                          }
                          })
    return redirect(url_for('user_interface'))


# Delete creative
@app.route('/delete_creative/<creative_id>')
def delete_creative(creative_id):
    mongo.db.creatives.remove({'_id': ObjectId(creative_id)})
    return redirect(url_for('user_interface'))


# Get briefs
@app.route('/get_briefs')
def get_briefs():
    return render_template("briefs.html",
                           briefs=mongo.db.briefs.find())


# Contact employer
@app.route('/contact_employer/<brief_id>')
def contact_employer(brief_id):
    the_brief = mongo.db.briefs.find_one({"_id": ObjectId(brief_id)})
    return render_template('contactEmployer.html', brief=the_brief)


# Create brief
@app.route('/create_brief')
def create_brief():
    user = mongo.db.users.find_one({'email': session['email']})
    skills = mongo.db.skills.find()
    return render_template('createBrief.html', user=user, skills=skills)


# Insert brief
@app.route('/insert_brief', methods=['POST'])
def insert_brief():
    briefs = mongo.db.briefs
    form_data = request.form.to_dict()
    form_data['email'] = session['email']
    briefs.insert_one(form_data)
    return redirect(url_for('user_interface',))


# Edit brief
@app.route('/edit_brief/<brief_id>')
def edit_brief(brief_id):
    the_brief = mongo.db.briefs.find_one({"_id": ObjectId(brief_id)})
    skills = mongo.db.skills.find()
    return render_template('editBrief.html', brief=the_brief, skills=skills)


# Update brief
@app.route('/update_brief/<brief_id>', methods=["POST"])
def update_brief(brief_id):
    briefs = mongo.db.briefs
    briefs.update_one({'_id': ObjectId(brief_id)},
                      {'$set':
                       {
                           'first_name': request.form.get('first_name'),
                           'last_name': request.form.get('last_name'),
                           'email': session['email'],
                           'city': request.form.get('city'),
                           'country': request.form.get('country'),
                           'company_name': request.form.get('company_name'),
                           'title': request.form.get('title'),
                           'hours': request.form.get('hours'),
                           'duration': request.form.get('duration'),
                           'required_skills': request.form.get('required_skills'),
                           'budget': request.form.get('budget'),
                           'project_start': request.form.get('project_start'),
                           'description': request.form.get('description')
                       }
                       })
    return redirect(url_for('user_interface'))


# Delete brief
@app.route('/delete_brief/<brief_id>')
def delete_brief(brief_id):
    mongo.db.briefs.remove({'_id': ObjectId(brief_id)})
    return redirect(url_for('user_interface'))


if __name__ == '__main__':
    app.secret_key = 'mysecret'
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
