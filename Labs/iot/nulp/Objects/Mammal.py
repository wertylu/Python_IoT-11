from Labs.iot.nulp.Objects.Animal import AnimalBeing
from Labs.iot.nulp.Objects.Fish import Fish


class Mammal(AnimalBeing):
    def __init__(self, age: int, herbivorous: bool, name: str) -> None:
        AnimalBeing.__init__(self, age)
        self.__herbivorous = herbivorous
        self.__name = name
        if self.__name == "bubr":
            for i in range(0, 500):
                print("BOBER KURWA JA PIERDOLIE JAKIE BYDLE")

    def check_if_alive(self) -> str:
        if self.__is_alive:
            return "The mammal is alive"
        else:
            return "The mammal is dead"

    def eat_fish(self, fish: Fish) -> str:
        if not self.__herbivorous:
            fish.die()
            return "Fish eaten successfully"
        else:
            return "You can`t eat fish"
