# queries.py

import sqlite3
import os

app_root = os.path.abspath(os.path.dirname(__file__))
db_path = os.path.join(app_root, 'bloo.db')

def retrieveAdmins():
    try:
        with sqlite3.connect(db_path) as conn:
            c = conn.cursor()
            c.execute("SELECT username, hash FROM admins")
            admins = c.fetchall()
            return admins
    except sqlite3.Error as e:
        print(str(e))
        return []



queries = {
    "get_flavors": "SELECT flavor_id, flavor_name FROM flavors;",
    "add_user": "INSERT INTO Users (user_name, email) VALUES (?, ?);",
    "add_vote": "INSERT INTO topflavor (user_name, user_email, flavor_id) VALUES (?, ?, ?);",
    "get_admins": "SELECT username, hash FROM Admins;",
    "get_admins_info": "SELECT id, username FROM Admins;",
    "get_users": "SELECT * FROM Users;",
    "get_all_flavors": "SELECT * FROM Flavors;",
    "get_top_flavors": "SELECT Flavors.flavor_name, topflavor.flavor_id, COUNT(*) AS count FROM topflavor JOIN Flavors ON topflavor.flavor_id = Flavors.flavor_id GROUP BY topflavor.flavor_id ORDER BY count DESC;",
    "add_flavor": "INSERT INTO Flavors (flavor_name, flavor_description) VALUES (?, ?);",
    "add_admin": "INSERT INTO Admins (username, hash) VALUES (?, ?);",
    "delete_admin": "DELETE FROM Admins WHERE id = ?;",
    "edit_admin": "UPDATE Admins SET username = ?, hash = ? WHERE id = ?;",
    "delete_flavor": "DELETE FROM Flavors WHERE id = ?;",
    "edit_flavor": "UPDATE Flavors SET username = ?, hash = ? WHERE id = ?;"


}

#My Schema.
# CREATE TABLE IF NOT EXISTS 'Admins' (id INTEGER PRIMARY KEY,username TEXT NOT NULL,'hash' INTEGER NOT NULL);CREATE TABLE IF NOT EXISTS 'Flavors' ('flavor_name' TEXT,'flavor_id' INTEGER PRIMARY KEY  , 'flavor_description' TEXT);
# CREATE TABLE IF NOT EXISTS 'topflavor' ('id' INTEGER PRIMARY KEY NOT NULL,'user_name' INTEGER, 'flavor_id' INTEGER, user_email TEXT);
# CREATE TABLE IF NOT EXISTS 'Users' ('user_id' INTEGER PRIMARY KEY NOT NULL,'user_name' TEXT, 'email' TEXT);
