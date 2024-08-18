from machine import Pin, UART, I2C,Timer,WDT
import asyncio
import binascii
import esp32
from ssd1306 import SSD1306_I2C
from time import sleep_ms

import network
import espnow

sta = network.WLAN(network.STA_IF)
sta.active(True)
sta.disconnect()

e = espnow.ESPNow()
e.active(True)

peer = b'\xbbXHYH1'
e.add_peer(peer)

sw = Pin(9, Pin.IN)

sleep_ms(500)
DEBUG=1

if (DEBUG == 0) or (sw() == 0):
    print('WDG is disabled')
    wdt = None
else:
    print('WDG is enabled')
    wdt = WDT(timeout = 2000)

def wdt_feed():
    if wdt:
        wdt.feed()


def uart_analyse(buf):
    if buf[0] != 0xff or buf[1] != 0x17 or buf[2] != 0x04:
        return -1

    return buf[4]*256+buf[5]


async def getCH2O():

    i2c=I2C(0,sda=Pin(2), scl=Pin(10))
    oled = SSD1306_I2C(128, 64, i2c)
    oled.text('CH2O',0,0)
    oled.text('mg/m3',0,26)

    led = Pin(8, Pin.OUT, value=1)
    rxbuf = bytearray(9)
    u = UART(1, 9600, tx=Pin(4), rx=Pin(3))
    u.read()

    while 1:
        wdt_feed()
        if u.any() >= 9:
            u.readinto(rxbuf, 9)
            print(binascii.hexlify(rxbuf, ' '))
            d = uart_analyse(rxbuf)
            if d >= 0:
                led(0)
                sta.active(True)
                c = '{:.3f}'.format(d*1.34/1000)
                print(d, c, 'mg/m3')
                e.send(peer, 'CH2O:'+ c)
                sta.active(False)

                oled.text(c,0,13)
                oled.show()

            else:
                u.read()
        else:
            led(1)

        await asyncio.sleep_ms(200)

asyncio.run(getCH2O())
