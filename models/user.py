from db import db
from flask_bcrypt import generate_password_hash, check_password_hash

class UserModel(db.Model):

    __tablename__="users"
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(80))
    password=db.Column(db.String(80))


    def __init__(self,username,password):

        self.username=username
        self.password =generate_password_hash(password).decode()


    def save_to_db(self):

        db.session.add(self)
        db.session.commit()
    
# check password
    def check_password(self, password):
        return check_password_hash(self.password, password)

    @classmethod  
    def getUser(cls,username):
        return db.session.query(UserModel).filter(UserModel.username==username).first()

