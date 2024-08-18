import network
import espnow
import asyncio
import neopixel

from machine import Pin
from neopixel import NeoPixel

LED= Pin(2, Pin.OUT)
SW = Pin(0, Pin.IN)
np = neopixel.NeoPixel(Pin(13), 30)

# WLAN接口必须处于活动状态才能 send()/recv()
sta = network.WLAN(network.STA_IF) # 或 network.AP_IF
sta.active(True)
sta.disconnect()

e = espnow.ESPNow()
e.active(True)

peer = b'\xbbXHYH1'
e.add_peer(peer)
e.send(peer, '123')

# 数据处理
def ch2o_dat(buf):
    try:
        if buf[:5] != b'CH2O:':
            return
        
        _t = buf[5:]
        d = float(_t)
        
        if d <= 0.05:
            n = 30
            c = (0, 30, 0)
        elif d <= 0.08:
            n = round((d - 0.05)/0.001)
            n = max(n, 5)
            c = (30, 30, 0)
        elif d < 0.11:
            n = round((d - 0.08)/0.001)
            n = max(n, 2)
            c = (30, 0, 0)
        else:
            n = 30
            c = (30, 0, 0)
        
        np.fill((0,0,0))
        for i in range(n):
            np[i] = c
        np.write()

        print(buf)
        
    except:
        return

async def e_recv():

    # 上电动画
    for i in range(15):
        np.fill((i*5+1,0,0))
        np.write()
        await asyncio.sleep_ms(20)

    for i in range(15):
        np.fill(((14-i)*5,0,0))
        np.write()
        await asyncio.sleep_ms(20)

    for i in range(15):
        np.fill((0, i*5+1,0))
        np.write()
        await asyncio.sleep_ms(20)

    for i in range(15):
        np.fill((0, (14-i)*5,0))
        np.write()
        await asyncio.sleep_ms(20)

    while True:
        host, msg = e.recv()
        if msg:
            LED(1)
            ch2o_dat(msg)
            await asyncio.sleep_ms(100)
            LED(0)
            
        await asyncio.sleep_ms(100)

asyncio.run(e_recv())
