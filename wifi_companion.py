from machine import (
    Pin,
    UART
)

uart = UART(0, rx=Pin(1), tx=Pin(0), baudrate=115200)

print(f"Pico connected - {uart}")
uart.write("hello")
while True:
    data = bytes()
    while uart.any() > 0:
        try:
            data += uart.read(1)
            # msg = str(uart.read(), "utf-8", "ignore")
            # print(msg)
        except Exception as e:
            print(str(e))
            pass

    if len(data):
        # print(data, end="")
        output = data.decode("utf-8")
        print(f"{output}", end="")