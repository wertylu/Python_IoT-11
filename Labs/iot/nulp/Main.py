from Labs.iot.nulp.Objects.Fish import Fish
from Labs.iot.nulp.Objects.Reptile import Reptile
from Labs.iot.nulp.Objects.Insect import Insect
from Labs.iot.nulp.Objects.Bird import Bird
from Labs.iot.nulp.Objects.Mammal import Mammal


def main():
    fish_joe = Fish(3, "shark")
    reptile_mike = Reptile(5, "small")
    insect_dummy = Insect(1, True)
    bird_axwell = Bird(2, False)
    mammal_bober = Mammal(5, True, "bubr")

    print(fish_joe.check_years())
    print(fish_joe.swim())
    print(reptile_mike.die())
    print(insect_dummy.suck_blood())
    print(bird_axwell.sing())
    print(mammal_bober.eat_fish(fish_joe))


if __name__ == "__main__":
    main()
