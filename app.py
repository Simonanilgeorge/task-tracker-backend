from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from db import db
from resources.stocks import StocksResource
from resources.expenses import ExpensesResource
from models.stock import StockModel

app=Flask(__name__)
api=Api(app)
CORS(app)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+mysqlconnector://root:root@mysql/tasktracker"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False

@app.before_first_request
def create_tables():
    
    db.create_all()

api.add_resource(StocksResource,'/api/stocks','/api/stocks/<string:id>')
api.add_resource(ExpensesResource,'/api/expenses','/api/expenses/<string:id>')


if __name__=="__main__":
    db.init_app(app)
    app.run(host='0.0.0.0',debug=True) 