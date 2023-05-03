import os
import re
import sqlite3
from email_validator import validate_email, EmailNotValidError
from flask import Flask, current_app, flash, redirect, render_template, request, session, url_for
from password_strength import PasswordPolicy
from werkzeug.exceptions import HTTPException
from werkzeug.security import check_password_hash

from queries import queries, retrieveAdmins

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'default_secret_key')
app_root = os.path.abspath(os.path.dirname(__file__))
db_path = os.path.join(app_root, 'bloo.db')
queries_path = os.path.join(app_root, 'queries.py')

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/test')
def test():
    return render_template('test.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/vote', methods=['GET', 'POST'])
def vote():
    if request.method == 'GET':
        flavors = get_flavors_from_db()
        return render_template('vote.html', flavors=flavors)
    else:
        name, email, flavor_id = process_vote_form(request.form)

        try:
            # Validate email
            valid = validate_email(email)
            email = valid.email
        except EmailNotValidError as e:
            # Log the error and show a generic error message
            current_app.logger.error(str(e))
            flash("Invalid email address.")
            return redirect(url_for('vote'))

        try:
            add_vote_to_db(name, email, flavor_id)
            flash_success_message()
            return redirect(url_for("vote"))
        except Exception as e:
            # Log the error and show a generic error message
            current_app.logger.error(str(e))
            flash_error_message(
                "An error occurred while submitting your favorite flavor.")
            return redirect(url_for('vote'))


def flash_error_message(message):
    flash(message, 'error')


def get_flavors_from_db():
    try:
        query = queries["get_flavors"]
        flavors = execute_query(query)
        return flavors
    except sqlite3.Error as e:
        current_app.logger.error(str(e))
        return []


def process_vote_form(form_data):
    name = form_data['name']
    email = form_data['email']
    flavor_id = form_data['flavor']
    return name, email, flavor_id


def add_vote_to_db(name, email, flavor_id):
    with sqlite3.connect(db_path) as conn:
        c = conn.cursor()
        c.execute(queries["add_user"], (name, email))
        c.execute(queries["add_vote"], (name, email, flavor_id))
        conn.commit()


def flash_success_message():
    flash("Thank you for submitting your favorite flavor!")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        username = request.form['username']
        hash = request.form['password']
        Admins = retrieveAdmins()
        for admin in Admins:
            if admin[0] == username and admin[1] == hash:
                session['username'] = username
                return redirect(url_for("admin"))
        error = "Invalid credentials"
        return render_template('login.html', error=error)
    else:
        error = request.args.get("error")
        return render_template('login.html', error=error)


@app.route("/admin")
def admin():
    if 'username' not in session:
        return redirect(url_for('login'))

    # Get data from database
    user_data = get_users()
    flavor_data = get_flavors()
    top_flavor = get_top_flavors()
    admins = get_admins_info()

    # Generate table HTML for user data, flavor data, and top flavor data
    user_table = generate_table(user_data, ['ID', 'Username', 'Email'])
    flavor_table = generate_table(
        flavor_data, ['Flavors', 'ID', 'Description'])
    top_flavor_table = generate_table(
        top_flavor, ['Flavor name', 'Flavor ID', 'votes'])
    admins_table = generate_table(admins, ['ID', 'Username'])

    return render_template('admin.html', user_table=user_table, flavor_table=flavor_table,
                           top_flavor_table=top_flavor_table, admins_table=admins_table)


def generate_table(data, headers):
    table_html = "<div style='overflow-x:auto;'>\n"
    # Add data-search attribute
    table_html += "<table class='table table-hover' data-search='true'>\n"
    table_html += "<thead>\n<tr>\n"
    table_html += "<th scope='col'>Checkbox</th>\n"
    for header in headers:
        table_html += f"<th scope='col'>{header}</th>\n"
    table_html += "</tr>\n</thead>\n<tbody>\n"
    for row in data:
        table_html += "<tr>\n"
        table_html += "<td><input class='form-check-input flex-shrink-0' type='checkbox'></td>\n"
        for value in row:
            table_html += f"<td>{value}</td>\n"
        table_html += "</tr>\n"
    table_html += "</tbody>\n</table>\n</div>\n"

    # Initialize the DataTable
    table_html += "<script>\n"
    table_html += "$(document).ready(function() {\n"
    table_html += "$('.table').DataTable();\n"
    table_html += "});\n"
    table_html += "</script>\n"

    return table_html


def get_connection():
    return sqlite3.connect(db_path)


def execute_query(query, *args):
    with get_connection() as conn:
        c = conn.cursor()
        c.execute(query, args)
        results = c.fetchall()
    return results


def get_users():
    query = queries["get_users"]
    results = execute_query(query)
    return results


def get_flavors():
    query = queries["get_all_flavors"]
    all_flavors = execute_query(query)
    return all_flavors


def get_top_flavors():
    query = queries["get_top_flavors"]
    top_flavors = execute_query(query)
    return top_flavors


def get_admins_info():
    query = queries["get_admins_info"]
    admins = execute_query(query)
    return admins
# Define your Flask route


@app.route('/newflavor', methods=['GET', 'POST'])
def newflavor():
    if request.method == 'POST':
        flavor_name = request.form['flavor_name']
        flavor_description = request.form['flavor_description']
        try:
            # Call the function to add flavor to the database
            add_flavor_to_db(flavor_name, flavor_description)
            flash_success_message_new_flavor()  # Call the function to flash success message
            return redirect(url_for('newflavor'))
        except Exception as e:
            # Log the error and show a generic error message
            current_app.logger.error(str(e))
            flash_error_message("An error occurred while adding a new flavor.")
            return redirect(url_for('newflavor'))

    # Render your template for the new flavor form
    return render_template('newflavor.html')


def flash_success_message_new_flavor():
    flash("New flavor added successfully!")


# Define the function to add flavor to the database
def add_flavor_to_db(flavor_name, flavor_description):
    # Replace db_path with the path to your SQLite database
    with sqlite3.connect(db_path) as conn:
        c = conn.cursor()
        # Execute your query to add flavor to the database
        c.execute(queries["add_flavor"], (flavor_name, flavor_description))
        conn.commit()


@app.route('/addnewflavor')
def new_flavor():
    return render_template('newflavor.html')


@app.route('/newadmin', methods=['GET', 'POST'])
def newadmin():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        password_confirmation = request.form['password']

        # Password strength regex pattern
        pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'

        # Validate password against regex pattern
        if re.match(pattern, password):
            if password == password_confirmation:  # Check if password and password confirmation match
                try:
                    add_admin_to_db(username, password)
                    flash_success_message_new_admin()  # Call the function to flash success message
                    return redirect(url_for('newadmin'))
                except Exception as e:
                    # Log the error and show a generic error message
                    current_app.logger.error(str(e))
                    flash_error_message(
                        "An error occurred while adding a new admin.")
                    return redirect(url_for('newadmin'))
            else:
                # Show error message for password mismatch
                flash_error_message(
                    "Password and password confirmation do not match.")
                return redirect(url_for('newadmin'))
        else:
            flash_error_message(
                "Password must meet the minimum requirements: at least 8 characters, 1 uppercase letter, 1 lowercase letter, 1 digit, and 1 special character.")
            return redirect(url_for('newadmin'))

    return render_template('newadmin.html')


def flash_success_message_new_admin():
    flash("New admin added successfully!")


def add_admin_to_db(username, hash):
    with sqlite3.connect(db_path) as conn:
        c = conn.cursor()
        c.execute(queries["add_admin"], (username, hash))
        conn.commit()
