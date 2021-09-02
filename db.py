import sqlite3

# create database class
class DB:
    def __init__(self):
        # connect to database and create cursor to interact with database
        self.db = sqlite3.connect("runner.db")
        self.cur = self.db.cursor()

        notes_table = """
            CREATE TABLE IF NOT EXISTS notes(
                title TEXT NOT NULL PRIMARY KEY, 
                body TEXT NOT NULL, 
                priority TEXT NOT NULL, 
                date TEXT NOT NULL
                )"""

        categories_table = """CREATE TABLE IF NOT EXISTS categories(name TEXT NOT NULL PRIMARY KEY, active INT NOT NULL)"""

        files_table = """
        CREATE TABLE IF NOT EXISTS files(
            name TEXT NOT NULL,
            path TEXT NOT NULL, 
            active INT NOT NULL,
            category_name TEXT NOT NULL,
            file_id INT PRIMARY KEY,
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
            values = "(?, ?, ?, ?, ?)"
        elif table == "categories":
            values = "(?, ?)"

        query = f"""
            INSERT INTO {table} VALUES {values}
        """

        # execute the query to insert the data and commit the changes
        self.cur.executemany(query, data)
        self.db.commit()
        self.db.close()

    # read method to read data from the database
    def read(self, table, field=None, value=None):

        query = ""

        if field == None and value == None:
            query = f"""
                SELECT * FROM {table}
            """
        else:
            query = f"""
                SELECT * FROM {table} WHERE {field} = '{value}'
            """
        # execute the query and get all the data
        self.cur.execute(query)
        data = self.cur.fetchall()

        # close the connection and return the data
        self.db.close()
        return data

    # delete method to delete data from the database
    def delete(self, table, name):
        # the label is used to find the relevant field in the table passed in
        label = "title" if table == "notes" else "name"

        # initialize the query
        query = ""

        # check if the table is files or notes because they will have a different query
        if table == "files" or table == "notes":       
            query = f"""DELETE FROM {table} WHERE {label} = '{name}'"""
        
        elif table == "categories":
            query = f"""DELETE FROM categories WHERE {label} = '{name}'"""

            # second query to delete all the files if the entire category is deleted
            query2 = f"""DELETE FROM files WHERE category_name = '{name}'"""
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
    
    # name refers to the old name. the name you want to delete. the new name will be in the data object
    def update(self, table, name, data):
        # Delete the data and re upload the updated data.
        # This is different from the delete method because the user can't delete a note or category from
        # their respective windows this method will only apply when the user updates the information
        
        label = "category_name" if table == "files" else "name" if table == "categories" else "title"
        query = f"""DELETE FROM {table} WHERE {label} = '{name}'"""

        self.cur.execute(query)
        
        self.save(table, data)


    def create_table(self, command):
        self.cur.execute(command)


db = DB()

# db.delete("files", "testname")

# data = db.read("files")
# print(data)

# table = "notes"
# data = [("testnote", "this is the body of the note", "Low", "2 aug 2021")]

# db.save(table, data)
