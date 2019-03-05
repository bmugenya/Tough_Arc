from ...db_con import database_setup


class Books():

    def __init__(self):
        self.database = database_setup()
        self.cursor = self.database.cursor

    def share(self, title, lecture, condition, comment):

        book = {
            "title": title,
            "lecture": lecture,
            "condition": condition,
            "comment": comment

        }

        query = """INSERT INTO Share(title, lecture, condition, comment)
        VALUES(%(title)s, %(lecture)s, %(condition)s,%(comment)s)"""

        self.cursor.execute(query, book)
        self.database.conn.commit()

        return book


class BuyBook():

    def __init__(self):
        self.database = database_setup()
        self.cursor = self.database.cursor

    def buy(self, title, lecture, condition):

        book = {


            "title": title,
            "lecture": lecture,
            "condition": condition

        }

        query = """INSERT INTO Orders (title,lecture,condition)
        VALUES(%(title)s, %(lecture)s,%(condition)s)"""

        self.cursor.execute(query, book)
        self.database.conn.commit()

        return book


class ViewBooks():
    def __init__(self):
        self.database = database_setup()
        self.cursor = self.database.cursor

    def get_books(self):
        self.cursor.execute("SELECT * FROM Share")
        books = self.cursor.fetchall()
        return books


class ViewBook():
    def __init__(self):
        self.database = database_setup()
        self.cursor = self.database.cursor

    def get_book(self, book_id):
        self.cursor.execute("SELECT * FROM Share WHERE book_id = (%s);" % (book_id))
        book = self.cursor.fetchall
        return book
