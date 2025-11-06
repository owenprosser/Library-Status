#!/usr/bin/env python3

import requests, json, ssl
from datetime import datetime

class library:
    def __init__(self):
        self.inUse = 0
        self.free = 0
        self.other = 0
        self.totalGround = 0
        self.totalFirst = 0
        self.totalSecond = 0
        self.totalThird = 0
        self.inUseGround = 0
        self.inUseFirst = 0
        self.inUseSecond = 0
        self.inUseThird = 0
        self.totalComps = 0
        self.percentFull = 0
        self.occupancy = 0
        self.lastUpdated = None
        self.timeDelta = None

        self.getJSON()
        self.getStats()
        self.getOccupancy()
        self.formatTimestamp()
        self.getJSONAge()

    def getJSON(self):
        response = requests.get("https://findapc.lincoln.ac.uk/pcavailability/machinestatus")
        data = response.json()

        for item in data['machines']:
            if (item['building'] == "UL"):
                if (item['floor'] == "Ground"):
                    self.groundFloor(item)
                elif (item['floor'] == "First"):
                    self.firstFloor(item)
                elif (item['floor'] == "Second"):
                    self.secondFloor(item)
                elif (item['floor'] == "Third"):
                    self.thirdFloor(item)

        self.lastUpdated = data['lastUpdated']
    
    def groundFloor(self, item):
        self.totalGround += 1

        if item['status'] in ["in use", "OOS", "forceOos"]:
            self.inUse += 1
            self.inUseGround += 1
        elif (item['status'] == "free"):
            self.free += 1

    def firstFloor(self, item):
        self.totalFirst += 1

        if item['status'] in ["in use", "OOS", "forceOos"]:
            self.inUse += 1
            self.inUseFirst += 1
        elif (item['status'] == "free"):
            self.free += 1

    def secondFloor(self, item):
        self.totalSecond += 1

        if item['status'] in ["in use", "OOS", "forceOos"]:
            self.inUse += 1
            self.inUseSecond += 1
        elif (item['status'] == "free"):
            self.free += 1

    def thirdFloor(self, item):
        self.totalThird += 1

        if item['status'] in ["in use", "OOS", "forceOos"]:
            self.inUse += 1
            self.inUseThird += 1
        elif (item['status'] == "free"):
            self.free += 1

    def getStats(self):
        self.totalComps = (self.inUse + self.free + self.other)
        self.percentFull = (self.inUse / self.totalComps) * 100

    def getOccupancy(self):
        response = requests.get("https://findapc.lincoln.ac.uk/occupancy/updatelibrary")
        data = response.json()
        self.occupancy = data['occupancy']

    def formatTimestamp(self):
        newString = ""
        for item in self.lastUpdated:
            if (item != 'T'):
                newString = newString + item
            else: 
                newString = newString + ' '

        self.lastUpdated = newString[:-14]

    def getJSONAge(self):
        self.lastUpdated =  datetime.strptime(self.lastUpdated, "%Y-%m-%d %X")
        self.timeDelta = (datetime.now() - self.lastUpdated).total_seconds() / 60.0

if __name__ == "__main__":
    library = library()

    print("\nLast Updated: " + str("%.2f " % library.timeDelta) + "Minutes ago at: " + str(library.lastUpdated) + "\n")
    print("Computers free - " + str(library.free))
    print("Computers in use - " + str(library.inUse))
    print("Library Computers are " + str("%.0f" % library.percentFull) + "% capacity." )
    print("There are", str(library.occupancy), "people in the Library \n")