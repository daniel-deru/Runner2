import os
import sys
import csv
import re

# get the database path in order to use the DB class
db_path = os.path.abspath(os.getcwd())
sys.path.insert(0, db_path)

from database.db import DB

def import_data(table, file):
    with open(file) as f:
        csv_reader = csv.reader(f)
        fields = next(csv_reader)
        categories = set()
        for row in csv_reader:
            if table == "files":
                websiteReg = "^(https?://)|(www\.).+\."
                match = re.search(websiteReg, row[1])
                categories.add(row[3])
                if match == None:
                    continue
                else:
                    DB().save(table, tuple(row))
            else:
                DB().save(table, tuple(row))
        if table == "files":
            categories = list(categories)
            for category in categories:
                DB().save("categories", (category, 1))
        
