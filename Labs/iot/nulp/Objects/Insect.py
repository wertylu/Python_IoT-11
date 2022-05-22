from Labs.iot.nulp.Objects.Animal import AnimalBeing


class Insect(AnimalBeing):
    def __init__(self, age: int, blood_sucker: bool) -> None:
        AnimalBeing.__init__(self, age)
        self.blood_sucker = blood_sucker

    def check_if_alive(self) -> str:
        if self.is_alive:
            return "The insect is alive"
        else:
            return "The insect is dead"

    def suck_blood(self):
        if self.blood_sucker:
            return "You just messed up a human`s picnic"
        else:
            return "You can`t suck if you are not a sucking insect"
