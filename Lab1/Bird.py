from Lab1.Animal import AnimalBeing


class Bird(AnimalBeing):
    def __init__(self, age: int, night_bird: bool) -> None:
        AnimalBeing.__init__(self, age)
        self.__night_bird = night_bird

    def check_if_alive(self) -> str:
        if self._is_alive:
            return "The bird is alive"
        else:
            return "The bird is dead"

    def sing(self):
        return "Nobody likes your song, Mr. Bird"
