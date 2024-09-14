import time
from machine import Pin, SPI
from mfrc522 import MFRC522

led = Pin(25, Pin.OUT)
out = Pin(15, Pin.OUT)
buzzer = Pin(14, Pin.OUT)
sda = Pin(5, Pin.OUT)
rst = Pin(22, Pin.OUT)
spi = SPI(0, baudrate=800000)

while True:
    led.value(1)
    rdr = MFRC522(spi, sda, rst)
    (stat, tag_type) = rdr.request(rdr.REQIDL)
    if stat == rdr.OK:
        (stat, raw_uid) = rdr.anticoll()
        if stat == rdr.OK:
            led.value(0)
            uid = ("0x%02x%02x%02x%02x" % (raw_uid[0], raw_uid[1], raw_uid[2], raw_uid[3]))
            print(uid)
            if uid == "":
                buzzer.value(1)
                time.sleep(0.02)
                buzzer.value(0)
                out.value(1)
                time.sleep(0.4)
                out.value(0)
                time.sleep(1)
            else:
                buzzer.value(1)
                time.sleep(0.1)
                buzzer.value(0)
                time.sleep(0.1)
                buzzer.value(1)
                time.sleep(0.1)
                buzzer.value(0)
                time.sleep(0.1)
                buzzer.value(1)
                time.sleep(0.1)
                buzzer.value(0)
                time.sleep(1)
    time.sleep(0.1)