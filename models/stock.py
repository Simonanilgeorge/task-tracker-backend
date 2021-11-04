from db import db


class StockModel(db.Model):

    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(80))

    __tablename__="stocks"


    def __init__(self,name):
        self.name=name

    def save_to_db(self):

        db.session.add(self)
        db.session.commit()
    
    def delete_from_db(self):

        db.session.delete()
        db.session.commit()

    @classmethod
    def getAllStocks(cls):
        return db.session.query(StockModel).all()

