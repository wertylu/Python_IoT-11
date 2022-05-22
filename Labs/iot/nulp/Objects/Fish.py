from Labs.iot.nulp.Objects.Animal import AnimalBeing


class Fish(AnimalBeing):
    def __init__(self, age: int, type_of_fish: str) -> None:
        AnimalBeing.__init__(self, age)
        self.type = type_of_fish

    def swim(self) -> str:
        return 'The fish is swimming'

    def check_if_alive(self) -> str:
        if self.is_alive:
            return "The fish is alive"
        else:
            return "The fish is dead"
