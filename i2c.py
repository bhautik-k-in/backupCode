from smbus import SMBus
addr=ox8
bus=SMBus(1)
n=1
print("Enter 1 For On & 0 For Off")
while n==1:
    ledstate=input(">>>> ")
    if ledstate=="1":
        bus.write_byte(addr,0x1)
        block=bus.read_byte_data(7,3)
        print(block)
    elif ledstate=="0":
        bus.write_byte(addr,0x0)
    else
        n=0