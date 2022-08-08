#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from ina219 import INA219
from ina219 import DeviceRangeError
#
# # SHUNT_OHMS = 0.05
# # MAX_EXPECTED_AMPS = 3.2
# # def read():
# #     ina = INA219(SHUNT_OHMS, MAX_EXPECTED_AMPS)
# #     ina.configure(ina.RANGE_16V)
# #
# #     print("Bus Voltage: %.3f V" % ina.voltage())
# #     try:
# #         print("Bus Current: %.3f mA" % ina.current())
# #         print("Power: %.3f mW" % ina.power())
# #         print("Shunt voltage: %.3f mV" % ina.shunt_voltage())
# #     except DeviceRangeError as e:
# #         # Current out of device range with specified shunt resistor
# #         print(e)
# # if __name__ == "__main__":
# #     read()
#
#
# # import smbus
# # import time
# # # Get I2C bus
# # bus = smbus.SMBus(1)
# # # SHT31 address, 0x44(68)
# # bus.write_i2c_block_data(0x44, 0x2C, [0x06])
# # time.sleep(0.1)
# # # SHT31 address, 0x44(68)
# # # Read data back from 0x00(00), 6 bytes
# # # Temp MSB, Temp LSB, Temp CRC, Humididty MSB, Humidity LSB, Humidity CRC
# # data = bus.read_i2c_block_data(0x44, 0x00, 6)
# # # Convert the data
# # temp = data[0] * 256 + data[1]
# # cTemp = -45 + (175 * temp / 65535.0)
# # fTemp = -49 + (315 * temp / 65535.0)
# # humidity = 100 * (data[3] * 256 + data[4]) / 65535.0
# # # Output data to screen
# # print("Temperature in Celsius is : %.2f C" % cTemp)
# # print("Temperature in Fahrenheit is : %.2f F" % fTemp)
# # print("Relative Humidity is : %.2f %%RH" % humidity)
#
#
# # import bmp_sensors
# # x = bmp_sensors.BMP180(1)
# # print(x.Measure())
#
# ### https://www.sparkfun.com/qwiic#products
#
# # https://www.sparkfun.com/products/18354
# #
# # import qwiic_led_stick
# # from random import randrange
# # import time
# # import sys
# # def run_example():
# #     print("\nSparkFun Qwiic LED Stick Example 1")
# #     my_stick = qwiic_led_stick.QwiicLEDStick()
# #     if my_stick.begin() == False:
# #         print("\nThe Qwiic LED Stick isn't connected to the sytsem. Please check your connection", \
# #               file=sys.stderr)
# #         return
# #     print("\nLED Stick ready!")
# #     my_stick.set_all_LED_brightness(15)
# #     c=1
# #     while True:
# #         # Turn on all the LEDs to white
# #         c+=1
# #         if c>10: c=1
# #         my_stick.set_single_LED_color(c, randrange(0,90),randrange(0,10),randrange(0,10))
# #         time.sleep(1)
# #         print(c)
# #
# # if __name__ == '__main__':
# #     try:
# #         run_example()
# #     except (KeyboardInterrupt, SystemExit) as exErr:
# #         print("\nEnding Example 1")
# #         sys.exit(0)
#
# #
#
#
# import qwiic_relay
# import time
# import sys
#
# myRelays = qwiic_relay.QwiicRelay()
#
#
# def runExample():
#     print("\nSparkFun Qwiic Relay Example 1\n")
#
#     if myRelays.begin() == False:
#         print("The Qwiic Relay isn't connected to the system. Please check your connection", \
#               file=sys.stderr)
#         return
#
#     # Turn on relays one and three
#     myRelays.set_relay_on(1)
#     myRelays.set_relay_on(3)
#     time.sleep(1)
#
#     # Print the status of all relays
#     for relayNum in range(4):
#         current_status = None
#         if myRelays.get_relay_state(relayNum) is True:
#             current_status = "On"
#         else:
#             current_status = "Off"
#         print("Status 1: " + current_status + "\n")
#
#     # Turn off 1 and 3, turn on 2 and 4
#     myRelays.set_relay_off(1)
#     myRelays.set_relay_on(2)
#     myRelays.set_relay_off(3)
#     myRelays.set_relay_on(4)
#     time.sleep(1)
#
#     # Turn all relays on, then turn them all off
#     myRelays.set_all_relays_on()
#
#     print(myRelays.get_relay_state())
#     time.sleep(1)
#
#     myRelays.set_all_relays_off()
#     print(myRelays.get_relay_state())
#
#
# if __name__ == '__main__':
#     try:
#         while(True):
#             runExample()
#     except (KeyboardInterrupt, SystemExit) as exErr:
#         print("\nEnding Example 1")
#         sys.exit(0)

SHUNT_OHMS = 0.1


def read():
    ina = INA219(SHUNT_OHMS, address=0x40)
    ina.configure()

    print("Bus Voltage: %.3f V" % ina.voltage())
    try:
        print("Bus Current: %.3f mA" % ina.current())
        print("Power: %.3f mW" % ina.power())
        print("Shunt voltage: %.3f mV" % ina.shunt_voltage())
    except DeviceRangeError as e:
        # Current out of device range with specified shunt resistor
        print(e)


if __name__ == "__main__":
    read()