from flask_restful import Resource
from flask.globals import request
from models.user import UserModel
from flask_jwt_extended import (create_access_token, create_refresh_token, jwt_required, get_jwt_identity)

class LoginResource(Resource):
    
    def post(self):

        data=request.get_json()
        access_token = create_access_token(identity = data['username'])
        refresh_token = create_refresh_token(identity = data['username'])
        
        print(f"access_token : {access_token} ,refresh_token : {refresh_token}")

        # get password for this user
        user=UserModel.getUser(data["username"])
        # check if password matched
        if user and user.check_password(data["password"]):
            return {
            "message":"success",
            "token":access_token
            }
        else:
            return {"message":"failed"}
        
    
