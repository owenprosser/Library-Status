import urllib.request, json, sys
from datetime import datetime

with urllib.request.urlopen("https://findapc.lincoln.ac.uk/pcavailability/machinestatus") as url:
    data = json.loads(url.read().decode())

    inUse = 0
    free = 0
    other = 0
    totalGround = 0
    totalFirst = 0
    totalSecond = 0
    totalThird = 0
    inUseGround = 0
    inUseFirst = 0
    inUseSecond = 0
    inUseThird = 0

    for item in data['returned']['machines']:
        #print(item['status'])
        if (item['building'] == "UL"):
            if (item['status'] == "in use"):
                inUse += 1
            elif (item['status'] == "free"):
                free += 1
            else:
                other += 1

    totalComps = (inUse + free + other)
    percentFull = (inUse / totalComps) * 100

    lastUpdated = data['returned']['lastUpdated']
    #lastUpdated = datetime.strptime(lastUpdated, "%Y-%m-%d %H:%M:%S")
    print(lastUpdated)

    with urllib.request.urlopen("https://findapc.lincoln.ac.uk/occupancy/updatelibrary") as url:
        data = json.loads(url.read().decode())
        occupancy = data['returned']['occupancy']


    print("Computers free - " + str(free))
    print("Computers in use - " + str(inUse))
    print("Library Computers are " + str("%.0f" % percentFull) + "% capacity." )
    print("There are", str(occupancy), "people in the Library")
