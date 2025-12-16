dis = float(input("enter the distance :"))

kmToM = lambda dis :  dis * 1000

mToCm = lambda dis: dis * 100

cmToMm = lambda dis : dis * 10

ftToIch = lambda dis : dis * 12

ichToCm = lambda dis : dis * 2.54

def distanceConverter(distance, ctype, func):
    result = func(distance)
    print(f"{distance} {ctype} = {result}")

distanceConverter(dis,"km to m", kmToM)
distanceConverter(dis,"m to cm", mToCm)
distanceConverter(dis,"cm to mm", cmToMm)
distanceConverter(dis,"ft to inch", ftToIch)
distanceConverter(dis,"inch to cm", ichToCm)
