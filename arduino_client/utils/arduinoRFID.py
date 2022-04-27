import serial
import time


ARDUINO_PORT="/dev/ttyUSB0"
arduino = serial.Serial(port=ARDUINO_PORT, baudrate=115200, timeout=.1)


def send_to_arduino(x):
    arduino.write(bytes(x, 'utf-8'))
    time.sleep(0.05)
    data = arduino.readline()
    return data


def convert_to_string(rfid):
    rfid_string=""
    for hexcodes in rfid.split():
        rfid_string+=hexcodes
    return rfid_string

def read_from_arduino():
    while True:
        rfid=arduino.readline()
        if rfid:
            #convert rfid to sttring and check if it is in the database
            rfid=rfid.decode('utf-8').rstrip() 
            return convert_to_string(rfid)
