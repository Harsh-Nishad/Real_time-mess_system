from flask import Flask, render_template, request, url_for, redirect
import pymongo
from pymongo import MongoClient
from utils import arduinoRFID as arduino
# mongodb+srv://harsh-nishad:<password>@cluster0.jlini.mongodb.net/myFirstDatabase?retryWrites=true&w=majority


cluster = MongoClient(
    "mongodb+srv://harsh-nishad:harsh123@cluster0.jlini.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = cluster["mess"]
collection = db["details"]


app = Flask(__name__)


@app.route("/", methods=["POST", "GET"])
def data():
    if request.method == "POST":
        username = request.form["name"]
        reg_no = request.form["registration_number"]
        rfid = arduino.read_from_arduino()
        mess_type = request.form["mess"]
        print(rfid)
        collection.insert_one({"_id": rfid, "name": username,
                              "regno": reg_no, "rfid": rfid,  "mess": mess_type, })
        return render_template("form.html")
    else:
        return render_template("form.html")
