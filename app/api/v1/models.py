from ...db_con import database_setup


class Books():

    def __init__(self):
        self.database = database_setup()
        self.cursor = self.database.cursor

    def share(self, book_id, postedBy, title, lecture, condition, comment):

        book = {
            "book_id": book_id,
            "postedBy": self.postedBy,
            "title": self.title,
            "lecture": self.lecture,
            "condition": self.condition,
            "comment": self.comment

        }

        query = """INSERT INTO Share  (book_id,postedBy, title,lecture,condition,comment)
            VALUES(%(postedBy)s, %(title)s, %(lecture)s,
                              %(condition)s, %(comment)s)"""

        self.cursor.execute(query, book)
        self.database.conn.commit()

        return book


class BuyBook():

    def __init__(self):
        self.database = database_setup()
        self.cursor = self.database.cursor

    def buy(self, book_id, title, lecture, condition):

        book = {
            "id": self.book_id,
            "title": self.title,
            "lecture": self.lecture,
            "condition": self.condition

        }

        query = """INSERT INTO Order  (postedBy, title,lecture,condition,comment)
            VALUES(%(postedBy)s, %(title)s, %(lecture)s,
                              %(condition)s, %(comment)s)"""

        self.cursor.execute(query, book)
        self.database.conn.commit()

        return book


class ViewBooks():
    def __init__(self):
        self.database = database_setup()
        self.cursor = self.database.corsor

    def get_books(self):
        self.cursor.execute("SELECT * FROM Share")
        books = self.cursor.fetchall()
        return books


class ViewBook():
    def __init__(self):
        self.database = database_setup()
        self.cursor = self.database.corsor

    def get_book(self, book_id):
        self.cursor.execute("SELECT * FROM Share WHERE book_id = (%s);" % (book_id))
        book = self.cursor.fetchall
        return book


class AdminRegistration():
    def __init__(self):
        self.database = database_setup()
        self.cursor = self.database.corsor

    def save_admin(self, student_id, firstName, lastName, userName, password, email, phoneNumber):

        admin = {
            "student_id": student_id,
            "firstName": firstName,
            "lastName": lastName,
            "username": userName,
            "password": password,
            "email": email,
            "phoneNumber": phoneNumber,
            "isAdmin": True,
        }

        query = """INSERT INTO Users (student_id,firstName, lastName,userName,password,email,phoneNumber,isAdmin)
            VALUES(%(student_id)s, %(firstName)s, %(lastName)s,
                              %(userName)s, %(password)s, %(email)s,%(phoneNumber)s,%(isAdmin)s)"""

        self.cursor.execute(query, admin)
        self.database.conn.commit()

        return admin


class UserRegistration():
    def __init__(self):
        self.database = database_setup()
        self.cursor = self.database.corsor

    def save_users(self, student_id, firstName, lastName, userName, password, email, phoneNumber):

        user = {
            "student_id": student_id,
            "firstName": firstName,
            "lastName": lastName,
            "username": userName,
            "email": email,
            "password": password,
            "isAdmin": False,
        }

        query = """INSERT INTO Users (student_id,firstName, lastName,userName,password,email,phoneNumber,isAdmin)
            VALUES(%(student_id)s, %s(firstName)s, %(lastName)s,
                              %(userName)s, %(password)s, %(email)s,%(phoneNumber)s,%(isAdmin)s)"""

        self.cursor.execute(query, user)
        self.database.conn.commit()

        return user


class AdminLogin():

    def __init__(self):
        self.database = database_setup()
        self.cursor = self.database.corsor

    def login(self, email, password):

        admin = {
            "email": email,
            "password": password
        }

        query = "SELECT * FROM Users WHERE email = '%s' AND password = '%s';" % (email, password)
        self.cursor.execute(query, admin)
        admins = self.cursor.fetchall()
        return admins


class UserLogin():

    def __init__(self):
        self.database = database_setup()
        self.cursor = self.database.corsor

    def login(self, email, password):

        user = {
            "email": email,
            "password": password
        }

        query = "SELECT * FROM Users WHERE email = '%s' AND password = '%s';" % (email, password)
        self.cursor.execute(query, user)
        users = self.cursor.fetchall()
        return users
