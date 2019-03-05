from flask import jsonify, make_response, request
from flask_restful import Resource


from models import *


class Share(Resource, Books):
    def __init__(self):
        self.book = Books()

    def post(self):
        data = request.get_json()
        title = data['title']
        lecture = data['lecture']
        condition = data['condition']
        comment = data['comment']

        newBook = self.book.share(title, lecture, condition, comment)

        return make_response(jsonify({
            "message": "Book added succedfully",
            "data": newBook

        }), 201)


class Buy(Resource, BuyBook):
    def __init__(self):
        self.book = BuyBook()

    def post(self):
        data = request.get_json()
        title = data['title']
        lecture = data['lecture']
        condition = data['condition']

        book = self.book.buy(title, lecture, condition)

        return make_response(jsonify({
            "message": "Book added succedfully",
            "data": book

        }), 201)


class Available(Resource, ViewBooks):
    def __init__(self):
        self.book = ViewBooks()

    def get(self):
        book = self.book.get_books()

        return make_response(jsonify({
            "message": "Book added succedfully",
            "data": book

        }), 200)


class View(Resource, ViewBook):
    def __init__(self):
        self.book = ViewBook()

    def get(self):
        book = self.book.get_book()

        return make_response(jsonify({
            "message": "Book added succedfully",
            "data": book

        }), 200)


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
