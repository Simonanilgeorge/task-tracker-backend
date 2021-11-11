from db import db


class StockModel(db.Model):

    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(80))
    price=db.Column(db.Float)
    quantity=db.Column(db.Float)
    buyAmount=db.Column(db.Float)

    __tablename__="stocks"

    def __init__(self,name,price,quantity,buyAmount):

        self.name=name
        self.price=price
        self.quantity=quantity
        self.buyAmount=buyAmount

        

    def save_to_db(self):

        db.session.add(self)
        db.session.commit()
    
    def delete_from_db(self):

        db.session.delete(self)
        db.session.commit()

    @classmethod
    def getAllStocks(cls):
        return db.session.query(StockModel).all()
    
    @classmethod
    def getStockByName(cls,name):
        return db.session.query(StockModel).filter(StockModel.name==name).first()
    
    @classmethod
    def getStockById(cls,id):
        return db.session.query(StockModel).filter(StockModel.id==id).first()

