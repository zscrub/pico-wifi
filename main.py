import gc
import uos
import esp
import network
import micropython

from time import sleep
from machine import (
    UART,
    Pin
)

# from umqttsimple import MQTTClient


from secret import (
    ssid,
    password,
    mqtt_server_ip
)

gc.collect()

# uos.dupterm(None, 1)

print("Attempting to connect to wifi...")

station = network.WLAN(network.STA_IF)

station.active(True)
station.connect(ssid, password)

print(station)

while station.isconnected() is False:
    pass

print("Connection successful!")
print(station.ifconfig())

print("Setting up serial...")

rx_pin = Pin(1)
tx_pin = Pin(0)

myserial = UART(0, 9600)
myserial.init(9600)

print("Serial setup complete!")
