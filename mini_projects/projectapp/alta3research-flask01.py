#!/usr/bin/env python3
"""Mini project using Flask API and jinja"""

from flask import Flask
from flask import request
from flask import redirect
from flask import jsonify
from flask import render_template
import sqlite3 as sql 
import json

app= Flask(__name__)

inventorydata= [{
    "item": "laptop",
    "brand": "samsung",
    "price": 2000
             }]

@app.route("/inventory", methods=["GET","POST"])
def index():
    if request.method == 'POST':
        data = request.json
        if data:
           data= json.loads(data)
           item = data["item"]
           brand = data["brand"]
           price = data["price"]
           inventorydata.append({"item":item,"brand":brand,"price":price})

    return jsonify(inventorydata)


@app.route("/home")
def inventory():
    
    return render_template("home.html")

@app.route('/new')
def new_entry():
    return render_template('addProduct.html')    

@app.route('/addrec', methods=['POST'])
def add_new():
    try:
        item = request.form['item']  # item
        brand = request.form['brand']  # brand
        price = request.form['price']  # price
        id = request.form['id']  # id, unconstrained -- doesn't have to be unique

        # connect to sqliteDB
        with sql.connect("inventory.db") as con:
            cursor = con.cursor()

            # place the info from our form into the sqliteDB
            cursor.execute("INSERT INTO inventory (item,brand,price,id) VALUES (?,?,?,?)", (item, brand, price, id))

            # commit the transaction to our sqliteDB
            con.commit()

        # record was successfully added to the DB
        msg = "Record successfully added"
    except:
        con.rollback()  # this undoes the commit()
        msg = "error in insert operation"  # we were NOT successful

    finally:
        # con.close()     # successful or not, close the connection to sqliteDB
        return render_template("resultadd.html", msg=msg)  # to display msg result

@app.route('/list')
def list_inventory():
    con = sql.connect("inventory.db")
    con.row_factory = sql.Row

    cursor = con.cursor()
    cursor.execute("SELECT * from inventory")  # pull all information from the table "inventory"

    rows = cursor.fetchall()
    return render_template("list.html", rows=rows)  # return all sqliteDB info as HTML




if __name__ == '__main__':
    try:
        # ensure the sqliteDB is created
        conn = sql.connect('inventory.db')
        print("inventory opened successfully")

        # ensure that the table people is ready to be written to
        conn.execute('CREATE TABLE IF NOT EXISTS inventory (item TEXT, brand TEXT, price TEXT, id TEXT)')
        print("Table created successfully")
        conn.close()

        # begin Flask Application
        app.run(host="0.0.0.0", port=2224, debug=True)

    except:
        print("App failed on boot")