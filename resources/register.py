from flask.globals import request
from flask_restful import Resource
from models.user import UserModel
from flask_jwt_extended import jwt_required




class RegisterResource(Resource):

    def post(self):

        data=request.get_json()
        print(data)
        user=UserModel(data["username"],data["registerPassword"])
        user.save_to_db()
        return {"message":"success"}

    @jwt_required()
    def get(self):

        try:

            return {"message":"test"}
        except:
            return {"message":"something went wrong"}
        # print(current_identity.json())