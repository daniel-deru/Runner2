import sqlite3


class DB:
    def __init__(self):
        self.db = sqlite3.connect("runner.db")
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

        self.create_table(notes_table)
        self.create_table(categories_table)
        self.create_table(files_table)

    def save(self, table, data):
        values = ""

        if table == "notes":
            values = "(?, ?, ?, ?)"
        elif table == "files":
            values = "(?, ?, ?)"
        elif table == "categories":
            values = "(?)"

        query = f"""
            INSERT INTO {table} VALUES {values}
        """
        self.cur.executemany(query, data)
        self.db.commit()
        self.db.close()


    def read(self, table):
        query = f"""
            SELECT * FROM {table}
        """
        self.cur.execute(query)
        data = self.cur.fetchall()
        self.db.close()
        return data

    def delete(self, table, name):
        label = "name"
        query = ""

        if (table == "files" or table == "notes"):
            
            if table == "notes": label = "title"
            query = f"""
                DELETE FROM {table} WHERE {label} = '{name}'
            """
        elif (table == "categories"):
            query = f"""
                DELETE FROM categories WHERE {label} = '{name}'
            """
            query2 = f"""
                DELETE FROM files WHERE category_name = '{name}'
            """
            self.cur.execute(query2)

        self.cur.execute(query)

        self.db.commit()
        self.db.close()


    def create_table(self, command):
        self.cur.execute(command)


db = DB()

# db.delete("files", "testname")

# data = db.read("files")
# print(data)

# table = "notes"
# data = [("testnote", "this is the body of the note", "Low", "2 aug 2021")]

# db.save(table, data)