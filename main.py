from Controller import *
from enum import Enum


class VehicleType(Enum):
    CAR = 1
    BUS = 2
    VAN = 3
    BIKE = 4


class Choice(Enum):
    PARK = 1
    UNPARK = 2
    ADMIN = 3


def main():

    controller = Controller()
    parkedList = {}

    while 1:
        print("Do you want to Park Or UnPark Or Admin")
        for i in Choice.__members__:
            print(i)
        choice = input().upper()

        if choice == "":
            break

        if choice not in Choice.__members__:
            print("InValid Choice")
            continue

        if Choice.PARK.value == Choice[choice].value:

            print("Enter the Vehicle and it's proper ID to Park!! Choose vehicle from the below list:")
            for i in VehicleType:
                print(i.name)
            vehicleTypeAndID = input().split()

            if vehicleTypeAndID[0].upper() == "":
                break

            if vehicleTypeAndID[0].upper() not in VehicleType.__members__:
                print("This Vehicle is restricted in our System")
                continue

            parkedList = controller.checkLevel(vehicleTypeAndID[0].upper(), vehicleTypeAndID[1])

        elif Choice.UNPARK.value == Choice[choice].value:

            print("Enter the Vehicle and VehicleID(Should be CORRECT!!):")
            unPark = input().split()

            parkedList = controller.toUnParkVehicle(unPark[0].upper(), unPark[1])

    for k, v in parkedList.items():
        print(k, v)


if __name__ == '__main__':
    main()
