from flask import Flask,jsonify
from flask.globals import request
from flask_restful import Resource
from db import db
from models.stock import StockModel
import json
from sqlalchemy.sql import func
from convert import convert


class StocksResource(Resource):

    def get(self):
        stocks=StockModel.getAllStocks()
        res=[
            {
                "id":stock.id,
                "name":stock.name,
                "quantity":stock.quantity,
                "buyAmount":stock.buyAmount,
                "price":stock.price
                
            }
            for stock in stocks
        ]
        return {"message":res}



    def post(self):
        data=request.get_json()
        

        singleStock=StockModel.getStockByName(data["name"])
        if singleStock:
            singleStock.quantity+=data["quantity"]
            singleStock.buyAmount+=data["buyAmount"]
            singleStock.price=data["price"]
            singleStock.save_to_db()

            return {"message":"stock updated"}

        else:
            stock=StockModel(data["name"],data["price"],data["quantity"],data["buyAmount"])
            stock.save_to_db()
            print(data)
        
            return {"message":"new stock info added"}

    def delete(self,id):
        singleStock=StockModel.getStockById(id)

        singleStock.delete_from_db()

        return {"message":f"Stock {id} deleted"}