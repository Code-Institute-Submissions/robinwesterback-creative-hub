# Megapixel Groups Creative Hub

Data Centric Development Milestone Project @ Code Institute

This project is a creative hub where creatives and employers meet.
The web application is built using flask and pymongo.
It allows you to perform CRUD operations for users, creatives, briefs and skills.
It has a form for logging in user and a form for contacting the creative/employer.
The application provides contact information and a link to Megapixels marketing services.
You can find the application [here](https://creative-hub.herokuapp.com/).

## UX

The application is designed using the [materialize](https://materializecss.com/) framework.
It is designed to be user friendly, simple and clean with the purpose to present all information in a visually appealing manner on all devices.
It is made for creatives/employers who wants to connect with one another.
They want to be able to create a user, creative ads and briefs.
They want to edit user, creative ad and brief details.
They want to be able to find creative ads and briefs.
They want to be able to delete creative ads and briefs.
To provide that information this application is a simple and straightforward web application.
It contains an index page, user interface, sections for creative ads/briefs as well as for performing CRUD operations, contact etc.
The footer provides contact information and a link to Megapixels marketing services.

### Database structure

There are 4 collection in the database:

- users:

```
{
  "_id":                   <ObjectId>,
  "first_name":            <string>,
  "last_name":             <string>,
  "email":                 <string>,
  "phone":                 <string>,
  "city":                  <string>,
  "country":               <string>,
  "password":              <Binary>
}
```

- Briefs:

```
{
  "_id":                   <ObjectId>,
  "first_name":            <string>,
  "last_name":             <string>,
  "city":                  <string>,
  "country":               <string>,
  "company_name":          <string>,
  "title":                 <string>,
  "hours":                 <string>,
  "duration":              <string>,
  "required_skills":       <string>,
  "budget":                <string>,
  "project_start":         <string>,
  "description":           <string>,
  "action":                <string>,
  "email":                 <string>
}
```

- Creatives:

```
{
  "_id":                   <ObjectId>,
  "first_name":            <string>,
  "last_name":             <string>,
  "city":                  <string>,
  "country":               <string>,
  "skills":                <string>,
  "hourly_rate":           <string>,
  "description":           <string>,
  "action":                <string>,
  "email":                 <string>
}
```

- Skills:

```
{
  "_id":                   <ObjectId>,
  "skill_name":            <string>
}
```

### User Stories

The user stories are showing pictures from an earlier stage of the project and not the deployed version.
You can access the deployed project [here](https://creative-hub.herokuapp.com/) to try the user stories yourself.

#### Story 1

As a user, I want to click on a navigation link -
![alt text](static/images/click-create-account.jpg "Click Create Account")

So that I can get navigated towards the desired link location.
![alt text](static/images/location-create-account.jpg "Location Create Account")

#### Story 2

As a user, I want to create a user account -
![alt text](static/images/create-user-account.jpg "Create User Account")

So that I can log in to my user interface
![alt text](static/images/user-interface.jpg "User Interface")

#### Story 3

As a user, I want to be able to log out -
![alt text](static/images/log-out.jpg "Log out")

And I want to be able to log in.
![alt text](static/images/log-in.jpg "Log in")

#### Story 4

As a user, I want to be able to create a brief -
![alt text](static/images/create-brief.jpg "Create Brief")

And a creative ad.
![alt text](static/images/create-creative-ad.jpg "Create Creative Ad")

#### Story 5

As a user, I want to be able to delete a brief/creative ad -
![alt text](static/images/delete-creative-ad.jpg "Delete Creative Ad")

And edit/update a brief/creative ad.
![alt text](static/images/update-brief.jpg "Update Brief")

#### Story 6

As a user, I want to be able to find briefs/creative ads -
![alt text](static/images/find-creatives.jpg "Find Creatives")

And contact the creative/employer.
![alt text](static/images/contact-employer.jpg "Contact Employer")

#### Story 7

As a user, I want to get information (social links, contact info etc.) about the owner of the site, so that I can contact the owner if I want to.
![alt text](static/images/contact-information.jpg "Contact Information")

### Strategy

The goal with the application is to provide employers and creative a way to connect.
The design should fit the purpose and coming from the [materialize](https://materializecss.com/) framework.
The foundation of the application should be solid with room for improvement for future updates/releases.

### Scope

The users should be able to use a fully functioning application for performing CRUD operations and sending an e-mail form.
At this stage the user will experience a running application with the possibility to perform CRUD operations
and let others know you are interested in connecting.

Future releases may introduce:
A wider range of functionalities and ways to interact
The possibility to rate users
Provide more valuable information and resources

### Structure

The application has a natural structure with the "home-section" giving a message, in this case welcoming the user to the application and describes how to use it.
It's easy to navigate to the different sections of the page and perform desired CRUD operations.

### Skeleton

In this [link](https://github.com/robinwesterback/creative-hub/tree/master/wireframes) you can find the wireframes for each section that serves as the skeleton for the project.

### Surface

In this [link](https://materializecss.com/) you can find Materialize.
This application is built using materialize css, components and js.

## Features

The application contains several features with a few left to be implemented.

### Existing Features

#### Navbar

A materialize [component](https://materializecss.com/navbar.html "Materialize Navbar") with a hamburger menu for mobile.

#### Footer

A materialize [component](https://materializecss.com/footer.html "Materialize Footer").

#### Icons

A materialize [component](https://materializecss.com/icons.html "Materialize Icons").

#### Forms

##### Text Inputs

Materialize [form input](https://materializecss.com/text-inputs.html "Materialize Text Inputs").

##### Select

Materialize [form select](https://materializecss.com/select.html "Materialize Select").

##### Date picker

Materialize [form date picker](https://materializecss.com/pickers.html "Materialize Pickers").

#### User login

The application allows the user to log in and out of a session.

#### CRUD Operations

The application operates to a MongoDB with 4 collections - users, briefs, creatives and skills.

##### Create document

The application allows the user to create a document in the MongoDB.

##### Read document

The application allows the user to read a document in the MongoDB.

##### Update document

The application allows the user to update a document in the MongoDB.

##### Delete document

The application allows the user to delete a document in the MongoDB.

#### Send email

I use [emailjs](https://www.emailjs.com/ "EmailJS") to let the user send emails to the site owner.
The user gets notified wether it is a success or of it fails.

### Features Left to Implement

#### Smarter interactivity for users

Make functions, collections and the exchange of information between users better.
E.g. pagination, search functions for retrieving data from the backend, categorized in a more user friendly way as the application grows larger.

#### Recourses, functions and content

Provide more information, resources and possibilities to create better ads to improve success rate for user interaction.

#### Add images, links etc.

Give users the ability to add images, documents, links etc.

#### Defensive design

Make the application more compatible with browsers other than Chrome. Customize the 404 error webpage.
More secure way to log in.

#### Livechat and chat function

I might add a livechat for contacting the site owner and a chat function for communication between users.

#### Your thoughts

Are there any features that you would like me to implement to improve the application? Please get in touch and share your thoughts.

## Technologies Used

I used HTML, CSS, Javascript, Python, Flask and MongoDB to build this project.

### HTML

This project uses semantic [HTML](https://html.com/ "HTML") to improve SEO and user friendliness.
The HTML is rendered from the templates directory.

### CSS

The project uses responsive design to improve the user experience and availability on all devices.
The [CSS](https://www.w3.org/Style/CSS/Overview.en.html "CSS") is separated using comments.
It is rendered from the static directory.

### JS

I used [JavaScript](https://www.javascript.com/ "JavaScript") for some of the functions and interactivity on the application.
Comments are provided to give an explanation of the functions.
It is rendered from the static directory.

### Python

I used [Python](https://www.python.org/ "Python") for some of the functions and interactivity on the application.
Comments are provided to give an explanation of the functions.

### Flask

I used [Flask](https://flask.palletsprojects.com/en/1.1.x/ "Flask") to create the web application.
Here is a [cheatsheet](https://s3.us-east-2.amazonaws.com/prettyprinted/flask_cheatsheet.pdf/ "Flask Cheatcheet").

### MongoDB

I used [MongoDB](https://www.mongodb.com/ "MongoDB") for the database and [PyMongo](https://pypi.org/project/pymongo/ "PyMongo") to interact with it.

## Testing

I have tested the application and looked for flaws in the design and errors in the functionality on several browsers on desktop, laptop and iPhone 7.
I have also tested the user stories to see if the application fills its purpose towards the user.
The expected outcome is that the application is responsive and functional on all browsers/devices.
Functions like links, CRUD operations and contact forms should work properly e.g "target=”\_blank"" where appropriate. Below are my findings and comments.

### Functionality

| Description                                    |                   Expected outcome                   | Pass | Comments |
| ---------------------------------------------- | :--------------------------------------------------: | ---: | -------: |
| Input 50 letters in campaign_name              |               Max input of 30 letters                |  Yes |        - |
| Post a form without filling in required fields | Shouldn't work, both backend and frontend validation |  Yes |        - |
| Log in with an e-mail that is not registered   |      Shouldn't work, error message should show       |  Yes |        - |
| Send an empty contact form                     |         Shouldn't work, fields are required          |  Yes |        - |

### User Stories

| Description                                    |                Expected outcome                 | Pass | Comments |
| ---------------------------------------------- | :---------------------------------------------: | ---: | -------: |
| Click on a navigation link                     | Get navigated towards the desired link location |  Yes |        - |
| Create user account                            |              User account created               |  Yes |        - |
| Create a user account with a registered e-mail |  It doesn't work and an error-message pops up   |  Yes |        - |
| Delete a creative ad                           |               Creative ad deleted               |  Yes |        - |
| Edit and update brief                          |            Brief edited and updated             |  Yes |        - |
| Send a message from the contact form           |                Message gets sent                |  Yes |        - |

### Different Browsers and devices

#### Desktop

| Description     |          Expected outcome           | Pass | Comments |
| --------------- | :---------------------------------: | ---: | -------: |
| Microsoft Edge  | The application works appropriately |  Yes |        - |
| Google Chrome   | The application works appropriately |  Yes |        - |
| Mozilla Firefox | The application works appropriately |  Yes |        - |
| Safari          | The application works appropriately |  Yes |        - |

#### Mobile

| Description   |          Expected outcome           | Pass | Comments |
| ------------- | :---------------------------------: | ---: | -------: |
| Google Chrome | The application works appropriately |  Yes |        - |
| Safari        | The application works appropriately |  Yes |        - |

### Responsiveness

I have tested the responsiveness of the application [here](http://ami.responsivedesign.is/# "Am I Responsive?") and it is responsive.

![alt text](src/assets/images/responsive-app.jpg "I am responsive!")

### Code validation

#### CSS

I validated my CSS with the [Jigsaw W3C Validation Service](https://jigsaw.w3.org/css-validator/ "CSS Validation").
1 error was located related to materialize. As the application works as intended it's nothing to be concerned about.
Therefore I choose to leave it for now even though jigsaw regards the CSS as an error.

#### HTML

I validated my HTML with the [W3C Markup Validation Service](https://validator.w3.org/ "HTML Validator") with no errors to show.

### Defensive design

I've implemented defensive designs throughout the application. Fields are required before submitting.
`maxLength` is applied to `input` fields. Error messages pops up where appropriate.
Email confirmation message pops up after successfully sent email.
There are more defensive design you can add to improve the user experience,
such as confirmation before deleting a creative ad/brief or adding interactive questionmarks that provide relevant information.

### Conclusion

After testing the deployed application my overall conclusion is that the application is working as intended.
It has a lot of potential to provide even more value for the user with future installations of the application.
The javascript and python works as intended.
The minor flaws that exist don’t ruin the user experience but should be corrected in the future.

## Deployment

The source code of the website is deployed to Github and the web application is hosted by Heroku. 
They both update automatically on a new commit and push to the master branch of the Github repository. 

### How to run this project locally

1. Use this [link](https://github.com/robinwesterback/creative-hub/ "Creative Hub Repository") to get to the projects repository.

2. Click "Clone or Download".

3. Click the "copy" icon.

4. Open Git Bash in your local IDE.

5. Change your current working directory to where you want the cloned directory to be made.

6. Type `$ git clone` and then paste the URL you copied earlier.

   `git clone https://github.com/USERNAME/REPOSITORY`

7. When you press enter your local clone will be ready.

## Credits

### Content

All content on the application was written by me.
The design was inspired by [Materialize](https://materializecss.com/ "Materialize").

### Media

The favicon used for this project was delivered by [Megapixel Group](https://www.megapixel.group/ "Megapixel Group").
The Icons used for this project was from [Materialize](https://materializecss.com/ "Materialize").

### Acknowledgements

Big thanks to my mentor who provided me with tips, support and some helpful resources.

## Resources

Below is a list of the resources used to create this project:

- [Log in system](https://www.youtube.com/watch?v=vVx1737auSE&ab_channel=PrettyPrinted "Log in system")
- [Materialize](https://materializecss.com/ "Materialize")
- [EmailJS](https://emailjs.com/ "EmailJS")
- [Flask Cheatcheet](https://s3.us-east-2.amazonaws.com/prettyprinted/flask_cheatsheet.pdf "Flask Cheatcheet")
