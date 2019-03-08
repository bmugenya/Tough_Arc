from ...db_con import database_setup
from datetime import datetime, timedelta
import jwt
import os


class User():

    def __init__(self):
        self.database = database_setup()
        self.cursor = self.database.cursor

    def validator(self, email):

        self.cursor.execute("SELECT * FROM Users WHERE email = '%s';" % (email))
        result = self.cursor.fetchone()

        if result:
            return True

        return False

    def encode_token(self, user_id):
        try:
            payload = {
                "exp": datetime.utcnow() + timedelta(days=1),
                "iat": datetime.utcnow(),
                "user": user_id
            }
            token = jwt.encode(
                payload,
                os.getenv('SECRET_KEY'),
                algorithm='HS256'
            )

            resp = token

        except Exception as e:
            resp = e

        return resp

    def save_admin(self, firstname, lastname, email, phonenumber, password):

        self.cursor.execute("SELECT * FROM Users WHERE email = '%s';" % (email))
        result = self.cursor.fetchone()

        if result:
            return False

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

    def login(self, email):
        query = "SELECT student_id,password,firstname FROM Users WHERE email = '%s';" % (email)
        self.cursor.execute(query)
        users = self.cursor.fetchone()

        return users
