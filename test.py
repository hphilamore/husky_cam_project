from HUSKYLENSPython.HUSKYLENS.huskylib import HuskyLensLibrary
hl = HuskyLensLibrary("I2C", "", address=0x32)
#hl.algorthim("ALGORITHM_FACE_RECOGNITION")

print(hl.knock())
#print(hl.blocks())
print(hl.requestAll())

while(1):
    data=hl.requestAll()
    x = 0
    for i in data:
        x = x+1
        # x range (0, 320)
        # y range (0, 240)
        print(i.ID, i.x, i.y, i.width, i.height)
