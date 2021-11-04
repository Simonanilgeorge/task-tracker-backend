from flask import Flask,jsonify
from flask.globals import request
from flask_restful import Resource
from db import db
from models.stock import StockModel
import json



class StocksResource(Resource):

    def get(self):
        res=StockModel.getAllStocks()
        print(res)

        return {"message":res}



    def post(self):
        data=request.get_json()
        stock=StockModel(data["name"])
        stock.save_to_db()
        print(data)
        
        return {"message":"new stock info added"}