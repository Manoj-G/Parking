import time
from Level import *


class Controller:

    def __init__(self):
        self.parkedList = dict()
        self.levelCount = 1
        self.levelID = "LEVEL" + str(self.levelCount)
        self.levels = []
        self.defaultLevels()
        self.ID = dict()

    def defaultLevels(self):

        # For Level1
        vehiclesAndCount = {'CAR': 20, 'VAN': 15, 'BIKE': 10}
        level1 = Level(self.levelID, vehiclesAndCount)
        self.levels.append(level1)

        self.levelCount = self.levelCount + 1
        self.levelID = "LEVEL" + str(self.levelCount)

        # For Level2
        vehiclesAndCount = {'CAR': 20, 'VAN': 15, 'BIKE': 10, 'BUS': 2}
        level2 = Level(self.levelID, vehiclesAndCount)
        self.levels.append(level2)

        self.levelCount = self.levelCount + 1
        self.levelID = "LEVEL" + str(self.levelCount)

        # For Level3
        vehiclesAndCount = {'CAR': 20, 'VAN': 10, 'BIKE': 15, 'BUS': 2}
        level3 = Level(self.levelID, vehiclesAndCount)
        self.levels.append(level3)

        self.levelCount = self.levelCount + 1
        self.levelID = "LEVEL" + str(self.levelCount)

    def checkLevel(self, vehicleType, vehicleID):

        parkedOrNot = 1

        for level in self.levels:
            if vehicleType in level.vehiclesAndCount.keys():

                self.parkedList = level.parkVehicle(vehicleType, vehicleID, self.parkedList)

                if level.flag == 0:
                    self.ID[level] = vehicleID
                    print("Your Vehicle", vehicleType, "is parked in", level.levelID)
                    parkedOrNot = 0
                    break

        if parkedOrNot == 1:
            print("Your vehicle Can't be parked, It's Out Of Space!!!")

        return self.parkedList

    def getParkingTime(self):

        # In and Out-Time Of Vehicle
        parkTime = time.asctime(time.localtime(time.time()))
        print("UnParking Time Of vehicle is:", parkTime)

    def toUnParkVehicle(self, vehicle, vehicleID):

        if vehicle not in VehicleType.__members__:
            print("The vehicle Type is Invalid!!")
            return dict()

        for level in self.ID.keys():
            if self.ID[level] == vehicleID:
                # level = self.ID[level]
                self.parkedList = level.unParkVehicle(vehicle, vehicleID, level.levelID, self.parkedList)
                break

        return self.parkedList
