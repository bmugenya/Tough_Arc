from flask import Flask
from flask_restful import Api, Resource

from .api.v1.views import Share, Buy, View, AdminReg, UserReg, AdminAccess, UserAccess


def create_app():
    app = Flask(__name__)
    api = Api(app)
    api.add_resource(Share, "/book/share")
    api.add_resource(View, "/book/book_id")
    api.add_resource(Buy, "/books")
    api.add_resource(AdminReg, "/auth/register/admin")
    api.add_resource(AdminAccess, "/auth/login/admin")
    api.add_resource(UserReg, "/auth/register/user")
    api.add_resource(UserAccess, "/auth/login/user")

    return app
