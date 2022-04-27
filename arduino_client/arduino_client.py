from utils import arduinoRFID as arduino
from pymongo import MongoClient
from time import sleep

cluster = MongoClient("mongodb+srv://harsh-nishad:harsh123@cluster0.jlini.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db=cluster["mess"]
collection=db["details"]


MESS_TYPE="nonveg"

while True:
    rfid=arduino.read_from_arduino()
    rfid_string=arduino.convert_to_string(rfid)
    print(rfid_string)

    query={"rfid":rfid_string}
    result=collection.find_one(query)
    if result is None:
        print("No such user")
        arduino.send_to_arduino("0")
    else:
        if result["mess"]==MESS_TYPE:
            print("User is allowed")
            print("Welcome "+result["name"] + "to "+MESS_TYPE)
            arduino.send_to_arduino("1")
        else:
            print("User is not allowed")
            arduino.send_to_arduino("0")
    sleep(1)
    print("\n")

    


