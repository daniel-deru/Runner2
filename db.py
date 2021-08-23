import sqlite3


class Save:
    def __init__(self):
        self.db = sqlite3.connect("runner.db")
        self.cur = self.db.cursor()

    def save(self):
        pass

    def read(self):
        pass

    def delete(self):
        pass