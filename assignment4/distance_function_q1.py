dis = float(input("Enter a distance value: "))

def kmToM(km):
    return km * 1000

def mToCm(m):
    return m * 100

def cmToMm(cm):
    return cm * 10

def ftToIch(ft):
    return ft * 12

def ichToCm(inch):
    return inch * 2.54

def distanceConverter(distance, ctype, func):
    result = func(distance)
    print(f"{distance} {ctype} = {result}")

distanceConverter(dis,"km to m", kmToM)
distanceConverter(dis,"m to cm", mToCm)
distanceConverter(dis,"cm to mm", cmToMm)
distanceConverter(dis,"ft to inch", ftToIch)
distanceConverter(dis,"inch to cm", ichToCm)
