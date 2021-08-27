import sqlite3

# create database class


class DB:
    def __init__(self):
        # connect to database
        self.db = sqlite3.connect("runner.db")
        # create cursor to interact with database
        self.cur = self.db.cursor()

        notes_table = """
            CREATE TABLE IF NOT EXISTS notes(
                title TEXT NOT NULL PRIMARY KEY, 
                body TEXT NOT NULL, 
                priority TEXT NOT NULL, 
                date TEXT NOT NULL
                )"""

        categories_table = """CREATE TABLE IF NOT EXISTS categories(name TEXT NOT NULL PRIMARY KEY)"""

        files_table = """
        CREATE TABLE IF NOT EXISTS files(
            name TEXT NOT NULL PRIMARY KEY,
            path TEXT NOT NULL, 
            category_name TEXT NOT NULL, 
            FOREIGN KEY(category_name) REFERENCES categories(name)
            )"""

        # create the necessary tables
        self.create_table(notes_table)
        self.create_table(categories_table)
        self.create_table(files_table)

    # save methode to save to database
    def save(self, table, data):

        if type(data) != list:
            data = [data]

        # determine how many fields there are based on the table passed in
        values = ""
        if table == "notes":
            values = "(?, ?, ?, ?)"
        elif table == "files":
            values = "(?, ?, ?)"
        elif table == "categories":
            values = "(?)"

        # Query to insert data into table
        query = f"""
            INSERT INTO {table} VALUES {values}
        """

        # execute the query to insert the data
        self.cur.executemany(query, data)

        # commit the changes
        self.db.commit()
        self.db.close()

    # read method to read data from the database
    def read(self, table):

        # query to get all the data from the table passed in
        query = f"""
            SELECT * FROM {table}
        """
        # execute the query
        self.cur.execute(query)
        # get all the data
        data = self.cur.fetchall()
        # close the connection
        self.db.close()
        # return the data
        return data

    # delete method to delete data from the database
    def delete(self, table, name):
        # the label is used to find the relevant field in the table passed in
        label = "name"

        # initialize the query
        query = ""

        # check if the table is files or notes because they will have a different query
        if table == "files" or table == "notes":
            
            # if the table is notes make the label title
            if table == "notes":
                label = "title"

            # query for notes and files query
            query = f"""
                DELETE FROM {table} WHERE {label} = '{name}'
            """
        # check if the table is categories because the categories table will have a different query
        elif table == "categories":

            # query for the categories table
            query = f"""
                DELETE FROM categories WHERE {label} = '{name}'
            """
            
            # second query to delete all the files if the entire category is deleted
            query2 = f"""
                DELETE FROM files WHERE category_name = '{name}'
            """
            self.cur.execute(query2)

        self.cur.execute(query)

        self.db.commit()
        self.db.close()
    
    def get_item(self, table, name):

        label = "name" if table == "categories" else "title"

        query = f"""
            SELECT * FROM {table} WHERE {label} = '{name}'
        """

        self.cur.execute(query)
        data = self.cur.fetchone()
        self.db.close()
        return data

    def create_table(self, command):
        self.cur.execute(command)


db = DB()

# db.delete("files", "testname")

# data = db.read("files")
# print(data)

# table = "notes"
# data = [("testnote", "this is the body of the note", "Low", "2 aug 2021")]

# db.save(table, data)
