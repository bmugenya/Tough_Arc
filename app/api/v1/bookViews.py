from flask import jsonify, make_response, request
from flask_restful import Resource


from book import *


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
            "message": "Book requested succesfully",
            "data": book

        }), 201)


class Available(Resource, ViewBooks):
    def __init__(self):
        self.book = ViewBooks()

    def get(self):
        book = self.book.get_books()

        return make_response(jsonify({
            "message": "Books Available",
            "data": book

        }), 200)


class View(Resource, ViewBook):
    def __init__(self):
        self.book = ViewBook()

    def get(self, book_id):
        book = self.book.get_book(book_id)

        return make_response(jsonify({
            "message": "Book added succedfully",
            "data": book

        }), 200)
