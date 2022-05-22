class AnimalBeing:
    def __init__(self, age: int) -> None:
        self.age = age
        self.is_alive = True

    def die(self) -> str:
        self.is_alive = False
        return "Now it died"

    def check_if_alive(self) -> str:
        if self.is_alive:
            return "The animal is alive"
        else:
            return "The animal is dead"

    def check_years(self):
        if self.age < 2 and self.is_alive == True:
            return f"It is {self.age} year old"
        elif self.age > 1 and self.is_alive == True:
            return f"It is {self.age} years old"
        else:
            return "It`s dead, sorry"
