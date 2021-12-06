from flask_restful import Resource
from flask.globals import request
from models.user import UserModel


class LoginResource(Resource):
    
    def post(self):

        data=request.get_json()

        # get password for this user
        user=UserModel.getUser(data["username"])
        if user.check_password(data["password"]):
            return {"message":"success"}
        else:
            return {"message":"failed"}

