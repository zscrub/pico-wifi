from machine import (
    Pin,
    UART
)

from lcd_init import lcd

uart = UART(0, rx=Pin(1), tx=Pin(0), baudrate=115200)

print(f"Pico connected - {uart}")
uart.write("hello")
while True:
    data = bytes()
    while uart.any() > 0:
        try:
            data += uart.read(1)
        except Exception as e:
            print(str(e))
            pass

    if len(data):
        output = data.decode("utf-8")
        print(f"{output}", end="")
        lcd.clear()
        lcd.move_to(0, 0)
        lcd.putstr(output)
