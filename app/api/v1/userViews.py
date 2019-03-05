from flask import jsonify, make_response, request
from flask_restful import Resource


from users import *


class AdminReg(Resource, AdminRegistration):
    def __init__(self):
        self.user = AdminRegistration()

    def post(self):
        data = request.get_json()
        student_id = data['student_id']
        firstname = data['firstname']
        lastname = data['lastname']
        email = data['email']
        phonenumber = data['phonenumber']
        password = data['password']

        admin = self.user.save_admin(student_id, firstname, lastname, email, phonenumber, password)

        return make_response(jsonify({
            "message": "user added succedfully",
            "admin": admin

        }), 201)


class UserReg(Resource, UserRegistration):
    def __init__(self):
        self.user = UserRegistration()

    def post(self):
        data = request.get_json()
        student_id = data['student_id']
        firstname = data['firstname']
        lastname = data['lastname']
        phonenumber = data['phonenumber']
        email = data['email']
        password = data['password']

        user = self.user.save_users(student_id, firstname, lastname, email, phonenumber, password)

        return make_response(jsonify({
            "message": "user added succedfully",
            "admin": user
        }), 201)


class AdminAccess(Resource, AdminLogin):
    def __init__(self):
        self.user = AdminLogin()

    def post(self):
        data = request.get_json()
        username = data['username']
        password = data['password']

        admin = self.user.login(username, password)

        return make_response(jsonify({
            "message": "user added succedfully",
            "admin": admin

        }), 200)


class UserAccess(Resource, UserLogin):
    def __init__(self):
        self.user = UserLogin()

    def post(self):
        data = request.get_json()
        username = data['username']
        password = data['password']

        user = self.user.login(username, password)

        return make_response(jsonify({
            "message": "user added succedfully",
            "admin": user

        }), 200)
