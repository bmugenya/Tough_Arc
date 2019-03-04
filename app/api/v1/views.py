from flask import jsonify, make_response, request
from flask_restful import Resource


from models import *


class Share(Resource, Books):
    def __init__(self):
        self.book = Books()

    def post(self):
        data = request.get_json()
        self.book_id = data['book_id']
        self.postedBy = data['postedBy']
        self.title = data['title']
        self.lecture = data['lecture']
        self.condition = data['condition']
        self.comment = data['comment']

        newBook = self.book.share(book_id, title, lecture, condition, comment)

        return make_response(jsonify({
            "message": "Book added succedfully",
            "data": newBook

        }), 201)


class Buy(Resource, BuyBook):
    def __init__(self):
        self.book = BuyBook()

    def post(self):
        data = request.get_json()
        book_id = data['book_id']
        title = data['title']
        lecture = data['lecture']
        condition = data['condition']

        book = self.book.buy(book_id, title, lecture, condition)

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
        firstName = data['firstName']
        password = data['password']
        lastName = data['lastName']
        email = data['email']
        username = data['username']

        admin = self.user.save_admin(student_id, firstName, password, lastName, email, username)

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
        firstName = data['firstName']
        password = data['password']
        lastName = data['lastName']
        email = data['email']
        username = data['username']

        user = self.user.save_users(student_id, firstName, password, lastName, email, username)

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
