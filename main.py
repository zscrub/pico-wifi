import gc
import uos
import esp
import network
import urequests as requests
import micropython

from time import sleep
from machine import (
    UART,
    Pin
)

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

myserial = UART(0, 115200)
myserial.init(115200)

print("Serial setup complete!")

try:
    while True:
        response = requests.get("http://api.kanye.rest/")
        if response.status_code == 200:
            quote = response.json().get("quote", "")
            print(quote)
        else:
            raise Exception(f"{response.status_code}: {response.reason}")
        sleep(10)
except Exception as e:
    print(e)