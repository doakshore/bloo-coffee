Project Overview
This project is a website made with Flask, where users can vote for their favorite flavor. It uses a database management system called SQLite, and a templating engine called Jinja2 to create HTML pages. Below are the main parts and features of the project.

app.py
app.py is the main file for the Flask application. It defines the different web pages and what should happen when users interact with them. It uses Flask and other libraries depending on what the page needs to do.

Templates
Templates are the code that determines how the website looks and what content it has. Here are the different templates used in this project:

index.html
index.html is the template used for the homepage of the Bloo Coffee website. It uses HTML and CSS to create the structure and style of the page.

base.html
base.html is a template that serves as the base for other templates in the project. It contains the basic structure and style that all pages share.

about.html
about.html is a template for a page that tells the story of the company. It includes sections about the team and company values, and it uses CSS to create a visually appealing layout.

vote.html
vote.html is the template for the page where users can vote for their favorite flavor. It includes a form for submitting a vote and a checkbox to agree to terms and conditions. When users submit their vote, the form sends data using the HTTP POST method, and the page displays a message confirming the vote was successful.

admin.html
admin.html is a template for a page where administrators can manage data in the database.

newadmin.html
newadmin.html is a template for a page where administrators can add new administrators to the database. It includes a form for entering the new admin's name and password, and JavaScript code to toggle the visibility of the password.

newflavor.html
newflavor.html is the template for a page where administrators can add new flavors to the database. It includes a form for entering the new flavor's name and description.

login.html
login.html is the template for the login page. It includes a form for entering a username and password, and a message is displayed if the login is unsuccessful.

Overall, this project is a web application that allows users to vote for their favorite flavor and administrators to manage the database. The different templates create the pages and styles that make up the website.

Components
This is a Flask web application that serves several routes. It uses SQLite as its database management system and the Jinja2 templating engine to render HTML templates. Here's a summary of the main components:

Import statements: Import required libraries and modules.
app object: Initialize the Flask application instance and set a secret key for session management.
@app.route('/'), @app.route('/about'), @app.route('/vote'), @app.route('/success'), @app.route('/login'), @app.route('/admin'): These are decorators that define URL routes for the web application. When a user visits a URL corresponding to one of these routes, Flask will call the associated function and render the appropriate template.
render_template(): Renders an HTML template with the given arguments.
request: Provides information about the incoming HTTP request.
redirect(): Redirects the user to a different URL.
url_for(): Generates a URL for a given function.
`session`: Stores data across requests.
flash(): Provides a way to show one-time messages to the user on a subsequent request.
sqlite: Provides a Python interface to SQLite.
queries: Defines the SQL queries used by the application.
validate_email: Validates that an email address is valid.
werkzeug.security: Provides password hashing and verification functionality.
