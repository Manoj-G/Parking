from Controller import *
from Vehicle import *


class Level:

    def __init__(self, levelID, vehiclesAndCount):
        self.flag = 0
        self.levelID = levelID
        self.vehiclesAndCount = vehiclesAndCount
        self.vehicles = []
        # self.controller = Controller()

    def parkVehicle(self, vehicleType, vehicleID, parkedList):

        vehicleDict = dict()
        self.flag = 0

        if self.levelID not in parkedList.keys():
            parkedList[self.levelID] = {}

        if vehicleType in parkedList[self.levelID]:

            if parkedList[self.levelID][vehicleType] >= self.vehiclesAndCount[vehicleType]:
                print(" No Space in", self.levelID)
                self.flag = 1
                # return "false"
            else:
                vehicleDict[vehicleType] = parkedList[self.levelID][vehicleType] + 1
                parkedList[self.levelID] = vehicleDict
        else:
            vehicleDict[vehicleType] = 1
            parkedList[self.levelID] = vehicleDict

        if self.flag == 0:
            parkedList[self.levelID] = vehicleDict

            # Set a class object for each vehicle
            vehicle = Vehicle(vehicleType, vehicleID)
            self.vehicles.append(vehicle)

            # In-Time Of Vehicle
            # self.controller.getParkingTime()

        return parkedList

    def unParkVehicle(self, vehicleType, vehicleID, levelID, parkedList):

        for vehicle in self.vehicles:
            if vehicle.vehicleID == vehicleID:
                parkedList[levelID][vehicleType] = parkedList[levelID][vehicleType] - 1
                print("Your Vehicle", vehicleType, "has been unParked from", levelID)

                # Out-Time Of Vehicle
                # self.controller.getParkingTime()

        return parkedList

