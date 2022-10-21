from machine import (
    Pin,
    UART
)

from driver.lcd_init import lcd

led = Pin(25, Pin.OUT)
uart = UART(0, rx=Pin(1), tx=Pin(0), baudrate=115200)
msg = f"Pico connected - {uart}"
print(msg)
uart.write(msg)

led.toggle()
while True:
    data = bytes()
    while uart.any() > 0:
        try:
            data += uart.read(1)
        except Exception as e:
            print(str(e))
            pass

    if len(data):
        try:
            output = data.decode("utf-8")
            print(f"{output}", end="")
            lcd.clear()
            lcd.move_to(0, 0)
            lcd.putstr(output)
        except UnicodeError as e:
            pass
