from db import db

class ExpenseModel(db.Model):
    __tablename__="expenses"
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(80))
    amount=db.Column(db.Float)


    def __init__(self,name,amount):

        self.name=name
        self.amount=amount

    def save_to_db(self):

        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):

        db.session.delete(self)
        db.session.commit()


    @classmethod
    def getAllExpenses(cls):
        return db.session.query(ExpenseModel).all()
    
    @classmethod
    def getExpenseById(cls,id):
        return db.session.query(ExpenseModel).filter(ExpenseModel.id==id).first()
        