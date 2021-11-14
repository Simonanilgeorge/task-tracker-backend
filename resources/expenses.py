from flask.globals import request
from flask_restful import Resource
from models.expense import ExpenseModel
from convert import convert

class ExpensesResource(Resource):

    def get(self):

        expenses=ExpenseModel.getAllExpenses()

        res=[
           {
               "id":expense.id,
               "name":expense.name,
               "amount":expense.amount,
               "fruits":expense.fruits.split(",")
           } for expense in expenses
        ]
        return {"message":res}

    
    def post(self):

        data=request.get_json()    
        print(data)
        expense=ExpenseModel(data["name"],data["amount"],",".join(data["fruits"]))    
        expense.save_to_db()

        return {"message":"new expense added"}


    def delete(self,id):

        expense=ExpenseModel.getExpenseById(id)
        expense.delete_from_db()
        return {"message":f"expense {id} deleted"}

    def put(self,id):

        data=request.get_json()
        expense=ExpenseModel.getExpenseById(id)
        expense.name=data["name"]
        expense.amount=data["amount"]
        expense.fruits=",".join(data["fruits"])

        expense.save_to_db()

        return {"message":f"expense {id} updated"}