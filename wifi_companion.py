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
            if "\r" not in (bytechar := uart.read(1)).decode("utf-8"):
                data += bytechar
        except Exception as e:
            print(str(e))
            pass
    i = 0

    if len(data):
        try:
            output = data.decode("utf-8")
            if len(output) > 32:
                print(f"Full output: {output}")
                output = output[0:32]
            lcd.clear()
            lcd.move_to(0, 0)
            print(output)
            lcd.putstr(output)
        except UnicodeError as e:
            pass
