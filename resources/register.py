from flask.globals import request
from flask_restful import Resource
from models.user import UserModel
# import jwt



class RegisterResource(Resource):

    def post(self):

        data=request.get_json()
        print(data)
        user=UserModel(data["username"],data["registerPassword"])
        user.save_to_db()
        return {"message":"success"}

    # @jwt_required
    def get(self):
        # token = jwt.encode({'public_id': "test"}, 'Th1s1ss3cr3t')
        # print(token)

        return {"message":"test"}
        # print(current_identity.json())