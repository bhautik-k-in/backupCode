import spidev
import time
spi=spidev.SpiDev()
spi.open(0,0)
msg=0xAA
spi.max_speed_hz=115200
while 1:
    spi.writebytes([0x4])
    y=spi.readbytes(1)
    print(y)
    print("Arudino is Connected!!!")
    time.sleep(0.5)