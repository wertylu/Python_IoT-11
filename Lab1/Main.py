from Lab1.Fish import Fish
from Lab1.Reptile import Reptile
from Lab1.Insect import Insect
from Lab1.Bird import Bird
from Lab1.Mammal import Mammal


def main():
    fish_joe = Fish(3, "shark")
    reptile_mike = Reptile(5, "small")
    insect_dummy = Insect(1, True)
    bird_axwell = Bird(2, False)
    mammal_bober = Mammal(5, False, "bubr")

    print(fish_joe.check_years())
    print(fish_joe.swim())
    print(reptile_mike.die())
    print(insect_dummy.suck_blood())
    print(bird_axwell.sing())
    print(mammal_bober.eat_fish(fish_joe))
    print(reptile_mike.check_if_alive())

if __name__ == "__main__":
    main()
