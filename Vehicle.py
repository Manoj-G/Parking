from enum import Enum


class VehicleType(Enum):
    CAR = 1
    BUS = 2
    VAN = 3
    BIKE = 4


class Vehicle:

    def __init__(self, vehicle, vehicleID):
        self.vehicle = VehicleType[vehicle].value
        self.vehicleID = vehicleID
