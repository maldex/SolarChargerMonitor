#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import simplejson as json
from flask import Flask, request, Response, jsonify, abort, render_template, redirect, send_from_directory
from yattag import Doc
from time import time, sleep
from smbus import SMBus
from ina219 import INA219
from pprint import pprint


def read_ina219(address=0x41, shunt_ohms=0.05):
    try:
        ina = INA219(shunt_ohms, address=address)
        ina.configure()
        return {
                "Voltage": round(ina.voltage(),3),
                "Current": round(ina.current()/1000,3),
                "Power": round(ina.power()/1000,3)
                }
    except Exception as e:
        return {"ERROR": str(e)}

def read_sht31(address=0x44):
    try:
        bus = SMBus(1)
        bus.write_i2c_block_data(address, 0x2C, [0x06])
        sleep(0.1)
        data = bus.read_i2c_block_data(address, 0x00, 6)

        return {
               "Temp": round(-45 + (175 * (data[0] * 256 + data[1]) / 65535.0), 3),
               "Humid": round(100 * (data[3] * 256 + data[4]) / 65535.0, 3)
               }
    except Exception as e:
        return {"ERROR": str(e)}

def get_all_data():
    return {
        "pan_out": read_ina219(0x45),
        "bat_in": read_ina219(0x41),
        "bat_out": read_ina219(0x40),
        "env": read_sht31()
    }

##################################################
app = Flask(__name__)
app_start_time = time()
@app.route("/")
def root():
    doc, tag, text = Doc().tagtext()
    with tag('meta', ('http-equiv', 'refresh'), ('content', '1')):
        pass
    # <meta http-equiv="refresh" content="1">
    with tag('pre'):
        text(data())

    return(doc.getvalue())

@app.route("/data")
def data():
    return(json.dumps(get_all_data(), indent=4))

##################################################
if __name__ == "__main__":

    import xmltodict
    file = "~/Hotbird.0c.xml"




    app.run(host='0.0.0.0', port=4000, debug=False)


