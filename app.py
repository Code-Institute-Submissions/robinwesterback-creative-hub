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

    # Variable initialization
    max_first_name = 30
    max_last_name = 30
    max_email = 40
    max_phone = 30
    max_city = 30
    max_country = 30
    min_password = 8
    max_password = 30
    max_company_name = 30
    max_title = 30
    min_description = 30
    max_description = 150
    error_list = []

    # Validates users form
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

    # Validates login form
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

    # Validates brief form
    elif collection == 'briefs':
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

        if not form['company_name'] or len(form['company_name']) > \
                max_company_name:
            error_list.append(
                'Company name must not be empty or more than {} characters!'
                .format(max_company_name)
            )

        if not form['title'] or len(form['title']) > max_title:
            error_list.append(
                'Title must not be empty or more than {} characters!'
                .format(max_title)
            )

        if request.form.get('hours') is None:
            error_list.append(
                'Hours needed must not be empty!'
            )

        if request.form.get('duration') is None:
            error_list.append(
                'Duration must not be empty!'
            )

        if request.form.get('required_skills') is None:
            error_list.append(
                'Required skills must not be empty!'
            )

        if request.form.get('budget') is None:
            error_list.append(
                'Budget must not be empty!'
            )

        if not form['project_start']:
            error_list.append(
                'Project start must not be empty!'
            )

        if not form['description']:
            error_list.append(
                'Description must not be empty!'
            )

        if len(form['description']) > max_description:
            error_list.append(
                'Description must not be more than {} characters!'
                .format(max_description)
            )

        if len(form['description']) < min_description:
            error_list.append(
                'Description must not be less than {} characters!'
                .format(min_description)
            )

    # Validates creatives form
    elif collection == 'creatives':
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

        if request.form.get('skills') is None:
            error_list.append(
                'Skill must not be empty!'
            )

        if request.form.get('hourly_rate') is None:
            error_list.append(
                'Hourly rate must not be empty!'
            )

        if not form['description']:
            error_list.append(
                'Description must not be empty!'
            )

        if len(form['description']) > max_description:
            error_list.append(
                'Description must not be more than {} characters!'
                .format(max_description)
            )

        if len(form['description']) < min_description:
            error_list.append(
                'Description must not be less than {} characters!'
                .format(min_description)
            )

    # Returns errors on an empty list
    return error_list


# Index
@app.route('/')
def home():
    """ Returns the landing page """

    # Initializes page title
    page_title = 'Home'

    # Renders the landing page
    return render_template('index.html', page_title='Home')


# Register
@app.route('/register', methods=['POST', 'GET'])
def register():
    """ Creates a user in the DB """

    if request.method == 'POST':
        # Setting variables
        users = mongo.db.users
        existing_user = users.find_one({'email': request.form['email']})
        form = request.form
        error_list = validate_form(form, 'users')
        page_title = 'Register'

        # Creates a user after validating form
        if error_list == []:

            if existing_user is None:
                hashpass = bcrypt.hashpw(
                    request.form['password'].encode('utf-8'), bcrypt.gensalt())
                users.insert({'first_name': request.form.get('first_name'),
                              'last_name': request.form.get('last_name'),
                              'email': request.form.get('email'),
                              'phone': request.form.get('phone'),
                              'city': request.form.get('city'),
                              'country': request.form.get('country'),
                              'password': hashpass})
                session['email'] = request.form['email']

                # Log in the new user
                return redirect(url_for('user_interface'))

            error_list.append(
                'The email you want to register is already registered.'
            )

            # Renders the register page with error list
            return render_template('register.html',
                                   errors=error_list,
                                   page_title='Register')

        # Renders the register page with error list
        return render_template('register.html',
                               errors=error_list,
                               page_title='Register')

    # Renders the register page
    return render_template('register.html', page_title='Register')


# User Interface
@app.route('/user_interface')
def user_interface():
    """ Returns the user interface page """

    # Checks if a user is logged in
    if 'email' in session:
        # Finds user, briefs and creative ad details created by the user
        user = mongo.db.users.find_one({'email': session['email']})
        briefs = mongo.db.briefs.find({'email': session['email']})
        creatives = mongo.db.creatives.find({'email': session['email']})
        page_title = 'User Interface'

        # Renders the user interface page
        return render_template('userInterface.html',
                               user=user,
                               briefs=briefs,
                               creatives=creatives,
                               page_title='User Interface')

    # Redirects the user to the login page
    return redirect(url_for('login'))


# Login
@app.route('/login', methods=['POST', 'GET'])
def login():
    """ Logs in user """

    if request.method == 'POST':
        # Setting variables
        user = mongo.db.users
        login_user = user.find_one({'email': request.form['email']})
        form = request.form
        error_list = validate_form(form, 'login')
        page_title = 'Log in'

        # Log in user after validating form
        if error_list == []:

            if login_user:
                if bcrypt.hashpw(request.form['password'].encode('utf-8'),
                                 login_user
                                 ['password']) == login_user['password']:
                    session['email'] = request.form['email']
                    return redirect(url_for('user_interface'))

            error_list.append(
                'Invalid email/password combination.'
            )

            # Renders the login page with error list
            return render_template('login.html',
                                   errors=error_list,
                                   page_title='Log in')

        error_list.append(
            'Invalid email/password combination.'
        )

        # Renders the login page with error list
        return render_template('login.html',
                               errors=error_list,
                               page_title='Log in')

    # Renders the login page
    return render_template('login.html', page_title='Log in')


# Logout
@app.route('/logout')
def logout():
    """ Log out user """

    # Initializes page title
    page_title = 'Home'

    # Clears session
    session.clear()

    # Renders the landing page
    return render_template('index.html', page_title='Home')


# Update user
@app.route('/update_user', methods=["POST"])
def update_user():
    """ Update user details """

    # Updating user in session
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

    # Redirects to user interface
    return redirect(url_for('user_interface'))


# Get Creatives
@app.route('/get_creatives')
def get_creatives():
    """ Find creatives and render the creatives page """

    # Initializes page title
    page_title = 'Creatives'

    return render_template("creatives.html",
                           creatives=mongo.db.creatives.find(),
                           page_title='Creatives')


# Contact creative
@app.route('/contact_creative/<creative_id>', methods=['POST', 'GET'])
def contact_creative(creative_id):
    """ Find creative ad and render the contact creative page """

    # Setting variables
    page_title = 'Contact creative'
    the_creative = mongo.db.creatives.find_one({"_id": ObjectId(creative_id)})

    return render_template('contactCreative.html',
                           creative=the_creative,
                           page_title='Contact creative')


# Create creative
@app.route('/create_creative')
def create_creative():
    """ Render the create creative ad page """

    # Setting variables
    user = mongo.db.users.find_one({'email': session['email']})
    skills = mongo.db.skills.find()
    page_title = 'Create creative ad'

    return render_template('createCreative.html',
                           user=user,
                           skills=skills,
                           page_title='Create creative ad')


# Insert creative
@app.route('/insert_creative', methods=['POST'])
def insert_creative():
    """ Creates a creative ad """

    if request.method == 'POST':
        # Setting variables
        user = mongo.db.users.find_one({'email': session['email']})
        skills = mongo.db.skills.find()
        creatives = mongo.db.creatives
        form_data = request.form.to_dict()
        form_data['email'] = session['email']
        form = request.form
        error_list = validate_form(form, 'creatives')
        page_title = 'Create creative ad'

        # Creates a creative ad after validating form
        if error_list == []:
            creatives.insert_one(form_data)

            # Redirects the user to user interface
            return redirect(url_for('user_interface'))

    # Renders the create creative ad page with errors
    return render_template('createCreative.html',
                           user=user,
                           skills=skills,
                           errors=error_list,
                           page_title='Create creative ad')


# Edit creative
@app.route('/edit_user/<creative_id>')
def edit_creative(creative_id):
    """ Edit a creative ad """

    # Setting variables
    the_creative = mongo.db.creatives.find_one({"_id": ObjectId(creative_id)})
    skills = mongo.db.skills.find()
    page_title = 'Edit creative ad'

    # Renders the edit creative ad page
    return render_template('editCreative.html',
                           creative=the_creative,
                           skills=skills,
                           page_title='Edit creative ad')


# Update creative
@app.route('/update_creative/<creative_id>', methods=['POST', 'GET'])
def update_creative(creative_id):
    """ Update a creative ad """

    # Setting variables
    the_creative = mongo.db.creatives.find_one({"_id": ObjectId(creative_id)})
    creatives = mongo.db.creatives
    skills = mongo.db.skills.find()
    form = request.form
    error_list = validate_form(form, 'creatives')
    page_title = 'Edit creative ad'

    # Updates a creative ad after validating form
    if error_list == []:
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

        # Redirects the user to user interface
        return redirect(url_for('user_interface'))

    # Renders the edit creative ad page with errors
    return render_template('editCreative.html',
                           creative=the_creative,
                           skills=skills,
                           errors=error_list,
                           page_title='Edit creative ad')


# Delete creative
@app.route('/delete_creative/<creative_id>')
def delete_creative(creative_id):
    """ Delete a creative ad """

    mongo.db.creatives.remove({'_id': ObjectId(creative_id)})
    return redirect(url_for('user_interface'))


# Get briefs
@app.route('/get_briefs')
def get_briefs():
    """ Find briefs and render the briefs page """

    # Initializes page title
    page_title = 'Briefs'

    return render_template("briefs.html",
                           briefs=mongo.db.briefs.find(),
                           page_title='Briefs')


# Contact employer
@app.route('/contact_employer/<brief_id>', methods=['POST', 'GET'])
def contact_employer(brief_id):
    """ Find brief and render the contact employer page """

    # Setting variables
    page_title = 'Contact employer'
    the_brief = mongo.db.briefs.find_one({"_id": ObjectId(brief_id)})

    return render_template('contactEmployer.html',
                           brief=the_brief,
                           page_title='Contact employer')


# Create brief
@app.route('/create_brief')
def create_brief():
    """ Render the create brief page """

    # Setting variables
    user = mongo.db.users.find_one({'email': session['email']})
    skills = mongo.db.skills.find()
    page_title = 'Create brief'

    return render_template('createBrief.html',
                           user=user,
                           skills=skills,
                           page_title='Create brief')


# Insert brief
@app.route('/insert_brief', methods=['POST', 'GET'])
def insert_brief():
    """ Creates a brief """

    if request.method == 'POST':
        # Setting variables
        user = mongo.db.users.find_one({'email': session['email']})
        skills = mongo.db.skills.find()
        briefs = mongo.db.briefs
        form_data = request.form.to_dict()
        form_data['email'] = session['email']
        form = request.form
        error_list = validate_form(form, 'briefs')
        page_title = 'Create brief'

        # Creates a brief after validating form
        if error_list == []:
            briefs.insert_one(form_data)

            # Redirects the user to user interface
            return redirect(url_for('user_interface'))

    # Renders the create brief page with errors
    return render_template('createBrief.html',
                           user=user, skills=skills,
                           errors=error_list,
                           page_title='Create brief')


# Edit brief
@app.route('/edit_brief/<brief_id>')
def edit_brief(brief_id):
    """ Edit a brief """

    # Setting variables
    the_brief = mongo.db.briefs.find_one({"_id": ObjectId(brief_id)})
    skills = mongo.db.skills.find()
    page_title = 'Edit brief'

    return render_template('editBrief.html',
                           brief=the_brief,
                           skills=skills,
                           page_title='Edit brief')


# Update brief
@app.route('/update_brief/<brief_id>', methods=['POST', 'GET'])
def update_brief(brief_id):
    """ Update a creative ad """

    # Setting variables
    the_brief = mongo.db.briefs.find_one({"_id": ObjectId(brief_id)})
    briefs = mongo.db.briefs
    skills = mongo.db.skills.find()
    form = request.form
    error_list = validate_form(form, 'briefs')
    page_title = 'Edit brief'

    # Creates a brief after validating form
    if error_list == []:
        briefs.update_one({'_id': ObjectId(brief_id)},
                          {'$set':
                           {
                            'email': session['email'],
                            'email': session['email'],
                            'first_name': request.form.get('first_name'),
                            'last_name': request.form.get('last_name'),
                            'city': request.form.get('city'),
                            'country': request.form.get('country'),
                            'company_name': request.form.get('company_name'),
                            'title': request.form.get('title'),
                            'hours': request.form.get('hours'),
                            'duration': request.form.get('duration'),
                            'required_skills': request.form.get
                            ('required_skills'),
                            'budget': request.form.get('budget'),
                            'project_start': request.form.get('project_start'),
                            'description': request.form.get('description')
                           }
                           })

        # Redirects the user to user interface
        return redirect(url_for('user_interface'))

    # Renders the edit brief page with errors
    return render_template('editBrief.html',
                           brief=the_brief,
                           skills=skills,
                           errors=error_list,
                           page_title='Edit brief')


# Delete brief
@app.route('/delete_brief/<brief_id>')
def delete_brief(brief_id):
    """ Delete a creative ad """

    mongo.db.briefs.remove({'_id': ObjectId(brief_id)})
    return redirect(url_for('user_interface'))


if __name__ == '__main__':
    app.secret_key = 'mysecret'
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=False)
