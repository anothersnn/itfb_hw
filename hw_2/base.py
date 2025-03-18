from abc import ABC
from hw_2.exceptions import LowFuelError, NotEnoughFuel


class Vehicle(ABC):
    def __init__(self, weight=0, fuel=0, fuel_consumption=0) -> None:
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption
        self.started = False


    def start(self) -> None:
        if not self.started:
            if self.fuel > 0:
                self.started = True
            else:
                raise LowFuelError


    def move(self, distance) -> None:
        check_fuel = self.fuel - distance * self.fuel_consumption

        if check_fuel >= 0:
            self.fuel = check_fuel
        else:
            raise NotEnoughFuel
