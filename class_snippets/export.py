import os
from sqlite3.dbapi2 import Error
import sys
import csv

# get the database path in order to use the DB class
db_path = os.path.abspath(os.getcwd())
sys.path.insert(0, db_path)

from database.db import DB
from class_snippets.MessageBox import Message

def export_data(table):
    try:
        if table == "notes":
            fields = ["title", "body", "priority", "date"]
            data = DB().read(table)
            name = "notes.csv"
        else:
            fields = ["name", "path", "active", "category_name", "file_id"]
            data = DB().read("files")
            name = "apps.csv"

        filename = os.path.join(os.environ["HOMEDRIVE"], os.environ["HOMEPATH"], "Documents", name)
        
        with open(filename, "w", newline="") as notes_csv:
            notes_writer = csv.writer(notes_csv)
            notes_writer.writerow(fields)
            notes_writer.writerows(data)
    except Error as error:
        Message(f"The following error occurred: {error}", "There was an error.")

 

