from views import *

from flask_restful import Api, Resource
from flask import Blueprint


version_one = Blueprint('api_v1', __name__, url_prefix='/api/v1')
api = Api(version_one)
api.add_resource(Share, "/book/share")
api.add_resource(View, "/book/book_id")
api.add_resource(AdminReg, "/auth/register/admin")
api.add_resource(AdminAccess, "/auth/login/admin")
api.add_resource(UserReg, "/auth/register/user")
api.add_resource(UserAccess, "/auth/login/user")
