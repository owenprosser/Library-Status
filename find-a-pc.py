import urllib.request, json, time

with urllib.request.urlopen("https://findapc.lincoln.ac.uk/pcavailability/machinestatus") as url:
    data = json.loads(url.read().decode())

    inUse = 0
    free = 0
    other = 0

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

    print("Computers free- " + str(free))
    print("Computers in use- " + str(inUse))
    print("Library Computers are " + str("%.0f" % percentFull) + "% full." )
