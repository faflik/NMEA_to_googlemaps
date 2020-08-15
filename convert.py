# 20:42:35  $GPGLL,5016.85468,N,01649.26577,E,204235.00,A,A*64

lat = "5016.85468"
lon = "01649.26577"


def convert(data):
    split = data.split(".")

    first = split[0]
    if len(first) == 4:
        first = "0" + first
    if len(first) == 3:
        first = "00" + first

    deg = float(first[0:3])
    minutes = float(first[3:5])
    rest = float("0." + split[1])
    result = deg + (minutes / 60) + (rest / 60)
    result = float("{0:.8f}".format(result))

    return result


l1 = [convert(lat), convert(lon)]
print(l1)
print(f"Copy to GoogleMaps: {l1[0]}, {l1[1]} ")
