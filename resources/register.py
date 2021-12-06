from flask.globals import request
from flask_restful import Resource
from models.user import UserModel


class RegisterResource(Resource):

    def post(self):

        data=request.get_json()
        user=UserModel(**data)
        user.save_to_db()

        return {"message":"success"}

