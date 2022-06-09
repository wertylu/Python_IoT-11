class AnimalBeing:
    def __init__(self, age: int) -> None:
        self.__age = age
        self._is_alive = True

    def die(self) -> str:
        self._is_alive = False
        return "Now it died"

    def check_if_alive(self) -> str:
        if self._is_alive:
            return "The animal is alive"
        else:
            return "The animal is dead"

    def check_years(self) -> str:
        if self.__age < 2 and self._is_alive:
            return f"It is {self.__age} year old"
        elif self.__age > 1 and self._is_alive:
            return f"It is {self.__age} years old"
        else:
            return "It`s dead, sorry"

