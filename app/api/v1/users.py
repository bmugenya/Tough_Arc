from ...db_con import database_setup


class AdminRegistration():
    def __init__(self):
        self.database = database_setup()
        self.cursor = self.database.cursor

    def save_admin(self, student_id, firstname, lastname, email, phonenumber, password):

        admin = {
            "student_id": student_id,
            "firstname": firstname,
            "lastname": lastname,
            "email": email,
            "phonenumber": phonenumber,
            "password": password,
            "isAdmin": True
        }

        query = """INSERT INTO Users (student_id,firstname, lastname,email,phonenumber,password,isAdmin)
            VALUES(%(student_id)s, %(firstname)s, %(lastname)s,
                              %(email)s, %(phonenumber)s, %(password)s,%(isAdmin)s)"""

        self.cursor.execute(query, admin)
        self.database.conn.commit()

        return admin


class UserRegistration():
    def __init__(self):
        self.database = database_setup()
        self.cursor = self.database.cursor

    def save_users(self, student_id, firstname, lastname, email, phonenumber, password):

        user = {
            "student_id": student_id,
            "firstname": firstname,
            "lastname": lastname,
            "email": email,
            "phonenumber": phonenumber,
            "password": password,
            "isAdmin": False
        }

        query = """INSERT INTO Users (student_id,firstname, lastname,email,phonenumber,password,isAdmin)
            VALUES(%(student_id)s, %(firstname)s, %(lastname)s,
                              %(email)s, %(phonenumber)s, %(password)s,%(isAdmin)s)"""

        self.cursor.execute(query, user)
        self.database.conn.commit()

        return user


class AdminLogin():

    def __init__(self):
        self.database = database_setup()
        self.cursor = self.database.cursor

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
        self.cursor = self.database.cursor

    def login(self, email, password):

        user = {
            "email": email,
            "password": password
        }

        query = "SELECT * FROM Users WHERE email = '%s' AND password = '%s';" % (email, password)
        self.cursor.execute(query, user)
        users = self.cursor.fetchall()
        return users
