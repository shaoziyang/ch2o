import serial
import asyncio
import time
import os

logfile_maxsize = 500000
logfile = '/home/xxxx/ch2o/ch2o.log'
datfile = '/dev/shm/ch2o.txt'
serdev = '/dev/ttyUSB0'

def log(msg):

    try:
        r = os.stat(logfile)
        if r.st_size > logfile_maxsize:
            try:
                os.remove(logfile+'.1')
            except:
                pass
            os.rename(logfile, logfile+'.1')
    except:
        pass

    try:
        f = open(logfile, 'at')
        f.write(time.strftime('%Y-%m-%d %H:%M:%S'))
        f.write(' '+str(msg)+'\n')
        f.close()
    except Exception as e:
        print(e)

async def get_data():

    print('start monitor CH2O')

    while True:
        try:
            ser = serial.Serial(serdev, 115200)
            print('open serial success!')
            break
        except:
            print('open serial error!')
            await asyncio.sleep(2)

    n = 10000
    xs = '';
    while True:
        try:
            if ser.readable():
                d = ser.readline()
                if d[:7] == b"b'CH2O:":
                    c = d[7:][:-3]
                    x = str(c)[2:-1]
                    print('CH2O:', x)
                    f = open(datfile, 'wt')
                    f.write(time.strftime('%Y-%m-%d %H:%M:%S '))
                    f.write(x)
                    f.close()
                    xs = max(x, xs)

                    n = (n+1)%600
                    if n == 0:
                        print('log to file', xs)
                        log(xs)
                        xs = ''

            await asyncio.sleep(2)
        except Exception as e:
            print(e)

asyncio.run(get_data())

