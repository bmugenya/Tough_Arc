from flask import jsonify, make_response, request
from flask_restful import Resource


from users import User


class AdminReg(Resource, User):
    def __init__(self):
        self.user = User()

    def post(self):
        data = request.get_json()
        firstname = data['firstname']
        lastname = data['lastname']
        email = data['email']
        phonenumber = data['phonenumber']
        password = data['password']

        if self.user.validator(email) is False:
            admin = self.user.save_admin(firstname, lastname, email, phonenumber, password)

            return make_response(jsonify({
                "message": "user added succedfully",
                "admin": admin

            }), 201)

        return make_response(jsonify({
            "message": "user exits",

        }), 401)


class UserReg(Resource, User):
    def __init__(self):
        self.user = User()

    def post(self):
        data = request.get_json()

        firstname = data['firstname']
        lastname = data['lastname']
        phonenumber = data['phonenumber']
        email = data['email']
        password = data['password']

        if self.user.validator(email) is False:
            user = self.user.save_users(firstname, lastname, email, phonenumber, password)
            token = self.user.encode_token(user)

            return make_response(jsonify({
                "message": "user added succedfully",
                "admin": user,
                "token": token

            }), 201)

        return make_response(jsonify({
            "message": "user exits",

        }), 401)


class Auth(Resource, User):
    def __init__(self):
        self.user = User()

    def post(self):
        data = request.get_json()

        new = {
            "email": data['email'],
            "password": data['password']
        }

        req = self.user.login(new['email'])

        if req:
            user_id, password, firstname = req

            if password != new['password']:
                return make_response(jsonify({
                    "message": "Invalid password",

                }), 401)

            token = self.user.encode_token(user_id)
            return make_response(jsonify({
                "message": "welcome %s" % firstname,
                "acces-token": token

            }), 200)

        else:
            return make_response(jsonify({
                "message": "user does not exit",

            }), 401)
