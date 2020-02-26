from flask import Flask, request, jsonify, Response
import os
import socket
import uuid
import datetime
import json
from mongoengine import *
try:
    connect(db='clear_street', host='mongodb://trade_api_user:tradepassword73@ds331558.mlab.com:31558/clear_street?retryWrites=false')
    print("connetion successful")
except:
    print("not successful")

app = Flask(__name__)

basePath = "/v1"

class Error_object:
    #Contains error details, if any
    def __init__(self,message):
        self.message = message

    def return_error(self):
        return jsonify(message = self.message)    

class Trade(Document):
    # Base trade details; common amongst all trade types
    date = IntField(required=True)
    quantity = StringField(required=True)
    price = StringField(required=True)
    ticker = StringField(required=True)

    # def __init__(self,quantity, price, ticker):
    #     self.client_trade_id = uuid.uuid4()
    #     now = datetime.datetime.now()
    #     self.date = int(str(now.year) +  str(now.month) + str(now.day))
    #     self.quantity = quantity
    #     self.price = price
    #     self.ticker = ticker
class InternalTrade(Document):
    # Internal representation of a trade including internal id
    trade = ReferenceField(Trade)

class TradeSubmitted(Document):
    client_trade_id = ReferenceField(Trade)
    trade_id = ReferenceField(InternalTrade)

    # def __init__(self,client_trade_id,trade_id):
    #     self.client_trade_id = client_trade_id
    #     self.trade_id = trade_id

def trade_sanitize(trade):

    #date = str(trade.date.year) + str(trade.date.month) + trade.date.day)
    id = trade.id
    quantity = trade.quantity
    price = trade.price
    ticker = trade.ticker
    return {
        "client_trade_id":str(trade.id),
        "quantity":str(trade.quantity),
        "price":str(trade.price),
        "ticker":str(trade.ticker),
        "date":int(trade.date)
        }

@app.route("/")
def hello():
    return "<h1> API available at /v1/trades </h1>"

@app.route(basePath+'/trades', methods=['GET','POST'])
def trades_get_all():
    # Returns InternalTrades in an array called trades
    if request.method == 'GET':
        # Do something
        # sample_trade = Trade(quantity="3",price="10",ticker="AAPL")
        # sample_trade.save()
        # internal_trade = InternalTrade(trade_id="123", trade=sample_trade).save()
        try:
            trades_array = []
            for trade_obj in InternalTrade.objects:
                try:
                    trades_array.append({"id": str(trade_obj.id),
                     "trade": trade_sanitize(trade_obj.trade)})
                except:
                    print("document deleted")
            return jsonify(trades=trades_array),200

        except ValueError:
            return jsonify(message="Internal Server Error"),500
    elif request.method == 'POST':
        # Adds trades to database and returns array called trades_submitted
        try:
            if request.is_json:
                trades = request.get_json()['trades']
                trades_submitted = []
                for trade in trades:
                    trade_to_save = Trade(
                        date=trade['date'],
                        quantity=str(trade['quantity']), 
                        price=str(trade['price']),
                        ticker=trade['ticker'])
                    trade_to_save.save()
                    internal_trade = InternalTrade(trade=trade_to_save)
                    internal_trade.save()
                    trade_submitted = TradeSubmitted(client_trade_id=trade_to_save,trade_id=internal_trade)
                    trade_submitted.save()
                    trades_submitted.append({"client_trade_id":str(trade_to_save.id),
                                            "trade_id": str(internal_trade.id)})
                return jsonify(trades_submitted=trades_submitted)
            else:
                raise ValueError
        except KeyError:
            return jsonify(message="Bad Request - Improper Types Passed"),400
        
        except ValueError:
            return jsonify(message="Not processable - Missing required"), 422
        else:
            return jsonify(message="Internal Server Error"), 500
    else:
        # Request type not specified for this endpoint
        return jsonify(message="Internal Server Error"), 500


@app.route(basePath+'/trades/<tradeId>', methods=['DELETE','PUT','GET'])
def trades_id(tradeId):
    if request.method == 'GET':    
        # Get trade specified by tradeId
        try:
            internal_trade = InternalTrade.objects(pk=tradeId).first()
            if internal_trade is not None:
                return jsonify(id=tradeId,trade=trade_sanitize(internal_trade.trade))
            else:
                return jsonify(message="ID Not Found"),404
        except:
            return jsonify(message="Internal Server Error"),500

    elif request.method == 'DELETE':
        # Deletes a trade from the database
        try:
            internal_trade = InternalTrade.objects(pk=tradeId).first()
            if internal_trade is not None:
                internal_trade.trade.delete()
                internal_trade.delete()
                return "OK",204
            else:
                return jsonify(message="ID Not Found"),404
        except:
            return jsonify(message="Internal Server Error"),500

    elif request.method == 'PUT':
        # Updates a trade and returns the InternalTrade
        try:
            if request.is_json:
                new_trade = request.get_json()
                internal_trade = InternalTrade.objects(pk=tradeId).first()
                if internal_trade is not None:
                    trade = Trade.objects(pk=internal_trade.trade.id).first()
                    trade.date = int(new_trade['date']) if new_trade.get('date',False) else trade.date
                    trade.quantity = str(new_trade['quantity']) if new_trade.get('quantity',False) else trade.quantity
                    trade.price = str(new_trade['price']) if new_trade.get('price',False) else trade.price
                    trade.ticker = str(new_trade['ticker']) if new_trade.get('ticker',False) else trade.ticker
                    trade.save()
                    return jsonify(trade=trade_sanitize(trade),
                                            id=tradeId)
                else:
                    return jsonify(message="ID Not Found"),404
        except:
            return jsonify(message="Internal Server Error"),500
    else:
        return jsonify(message="Internal Server Error"),500


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080,debug=True)            
