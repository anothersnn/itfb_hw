"""
создайте класс `Plane`, наследник `Vehicle`
"""
from hw_2.base import Vehicle
from hw_2.exceptions import CargoOverload


class Plane(Vehicle):
    def __init__(self, weight=0, fuel=0, fuel_consumption=0, max_cargo=0) -> None:
        super().__init__(weight, fuel, fuel_consumption)
        self.max_cargo = max_cargo
        self.cargo = 0


    def load_cargo(self, new_cargo) -> None:   
        if self.cargo + new_cargo > self.max_cargo:
            raise CargoOverload

        self.cargo += new_cargo


    def remove_all_cargo(self) -> int:
        cur_cargo, self.cargo = self.cargo, 0
        return cur_cargo