from ...db_con import database_setup
from datetime import datetime, timedelta
import jwt
import os


class AdminRegistration():
    def __init__(self):
        self.database = database_setup()
        self.cursor = self.database.cursor

    def save_admin(self, firstname, lastname, email, phonenumber, password):

        admin = {

            "firstname": firstname,
            "lastname": lastname,
            "email": email,
            "phonenumber": phonenumber,
            "password": password,
            "isAdmin": True
        }

        query = """INSERT INTO Users (firstname, lastname,email,phonenumber,password,isAdmin)
            VALUES( %(firstname)s, %(lastname)s,
                              %(email)s, %(phonenumber)s, %(password)s,%(isAdmin)s)"""

        self.cursor.execute(query, admin)
        self.database.conn.commit()

        return admin


class UserRegistration():
    def __init__(self):
        self.database = database_setup()
        self.cursor = self.database.cursor

    def save_users(self, firstname, lastname, email, phonenumber, password):

        user = {

            "firstname": firstname,
            "lastname": lastname,
            "email": email,
            "phonenumber": phonenumber,
            "password": password,
            "isAdmin": False
        }

        query = """INSERT INTO Users (firstname, lastname,email,phonenumber,password,isAdmin)
            VALUES( %(firstname)s, %(lastname)s,
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
        admins = self.cursor.fetchone()

        return admins


class UserLogin():

    def __init__(self):
        self.database = database_setup()
        self.cursor = self.database.cursor

    def encode_token(self, user_id):

        try:
            payload = {
                "exp": datetime.utcnow() + timedelta(days=1),
                "iat": datetime.utcnow(),
                "user": user_id
            }
            return jwt.encode(
                payload,
                os.getenv('SECRET_KEY'),
                algorithm='HS256'
            )

        except Exception as e:
            return e

    def login(self, email):
        query = "SELECT student_id,password FROM Users WHERE email = '%s';" % (email)
        self.cursor.execute(query)

        users = self.cursor.fetchone()
        return users
