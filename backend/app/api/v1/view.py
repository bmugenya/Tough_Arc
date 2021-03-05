from flask import jsonify, make_response, request
from flask_restful import Resource
import os



from .model import *

class Chapters(Resource, Manga):
    def __init__(self):
        self.manga = Manga()

    def get(self):

        return make_response(jsonify({
            "message": "Book added succedfully",
            "data": "file"

        }), 200)

