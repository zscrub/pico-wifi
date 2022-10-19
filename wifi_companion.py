from machine import (
    Pin,
    UART
)

uart = UART(id=0, rx=Pin(1), tx=Pin(0), baudrate=9600)

print(f"Pico connected - {uart}")
uart.write("hello")
while True:
    if uart.any():
        try:
            msg = str(uart.read(), "utf-8", "ignore")
            print(msg)
        except Exception as e:
            print(str(e))
            pass
