import board
import busio
import serial

import adafruit_thermal_printer

ThermalPrinter = adafruit_thermal_printer.get_printer_class(2.69)


RX = board.RX
TX = board.TX

uart = serial.Serial("/dev/serial0", baudrate=19200, timeout=3000)

printer = ThermalPrinter(uart)

printer.print("Hello world!")

printer.feed(2)
