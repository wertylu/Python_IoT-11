from Labs.iot.nulp.Objects.Animal import AnimalBeing


class Reptile(AnimalBeing):
    def __init__(self, age: int, size: str):
        AnimalBeing.__init__(self, age)
        self.size = size

    def check_if_alive(self) -> str:
        if self.is_alive:
            return "The reptile is alive"
        else:
            return "The reptile is dead"
