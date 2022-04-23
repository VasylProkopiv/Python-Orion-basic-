from __future__ import annotations
from typing import Dict, Any
import random
from abc import abstractmethod
import uuid
import time

# Survival
#
# 1. In the Forest (Iterable) lives Predators and Herbivores (abstract class of animal and two offspring).
# Each animal is born with the following parameters (by using random):
# - strength (from 25 to 100 points)
# - speed (from 25 to 100 points)
# The force cannot be greater than it was at birth (initialization).
#
# At each step of the game we take 1 animal from the forest (iteration):
# - If it is herbivorous, then it eats (restores its strength by 50%). *
# - If it is a predator, it hunts - randomly chooses an animal from the forest and:
#     - pulled himself out, he was unlucky and he was left without a dinner;
#     - pulled out another animal, then tries to catch up;
#     - if he can catch up, he catches up and attacks;
#     - if attacked and is stronger, then eats and restores 50% of strength;
#     - did not catch up or did not have enough strength, then he and the lucky prey lose 30% of strength
#     (Because both either ran, or fought, or all together)
#
# An animal whose power has expired dies. (You can check the strength at the time of food search)
#
# The game continues as long as predators are present in the forest.


class Animal:

    def __init__(self, power: int, speed: int):
        self.id: uuid = uuid.uuid4()
        self.max_power = power
        self.current_power = power
        self.speed = speed

    @abstractmethod
    def eat(self, forest: Forest):
        # pass
        raise NotImplementedError('You missed me.')

    def restore_power(self):
        print(f'{self.__class__.__name__}: power = {self.current_power}')
        self.current_power = round(self.current_power * 1.5, 2)
        if self.current_power >= self.max_power:
            self.current_power = self.max_power
            print(f'{self.__class__.__name__} power has been limited by {self.max_power}')
        else:
            print(f'{self.__class__.__name__} power has been recovered to {self.current_power}')

    def hunting(self):
        self.current_power = round(self.current_power * 0.7, 2)
        if self.current_power <= 1:
            forest.remove_animal(self)
            print(f'{self.__class__.__name__} died')
        else:
            print(f'{self.__class__.__name__} power has been reduced to {self.current_power}')


class Predator(Animal):
    def __init__(self):
        power = random.randint(25, 100)
        speed = random.randint(25, 100)
        Animal.__init__(self, power, speed)

    def eat(self, forest: Forest):
        victim: AnyAnimal = random.choice(list(forest.animals.values()))
        if victim.id == self.id:
            print(f'{self.__class__.__name__} left without a dinner. No power gained.')
        else:
            print(f'{self.__class__.__name__}: power = {self.current_power}, speed = {self.speed}'
                  f' is chasing the {victim.__class__.__name__}: power =  {victim.current_power}, speed = {victim.speed}')
            if self.speed > victim.speed:
                print(f'{self.__class__.__name__} caught up the {victim.__class__.__name__}')
                if self.current_power > victim.current_power:
                    print(f'{self.__class__.__name__} hunted the victim')
                    self.restore_power()
                else:
                    print(f'{victim.__class__.__name__} survived')
                    victim.hunting()
                    self.hunting()
            else:
                print(f'{self.__class__.__name__} did not caught up')
                victim.hunting()
                self.hunting()


class Herbivorous(Animal):
    def __init__(self):
        power = random.randint(25, 100)
        speed = random.randint(25, 100)
        Animal.__init__(self, power, speed)

    def eat(self, forest: Forest):
        self.restore_power()


AnyAnimal: Any[Herbivorous, Predator]


class Forest:
    def __init__(self):
        self.animals: Dict[str, AnyAnimal] = dict()

    def add_animal(self, animal: AnyAnimal):
        self.animals.update({animal.id: animal})
        print(f'The {animal.__class__.__name__} has been added {animal.id}')

    def remove_animal(self, animal: AnyAnimal):
        if animal.id in self.animals.keys():
            self.animals.pop(animal.id)
            print(f'The {animal.__class__.__name__} has not survived')

    def any_predator_left(self):
        do_exist = False
        for val in self.animals.values():
            if isinstance(val, Predator):
                do_exist = True
                break
        return do_exist


def animal_generator():
    while True:
        gen_animal = random.choice([Herbivorous(), Predator()])
        yield gen_animal


if __name__ == "__main__":
    nature = animal_generator()

    forest = Forest()
    for i in range(3):
        animal = next(nature)
        forest.add_animal(animal)

    while True:
        if not forest.any_predator_left():
            break
        for animal in forest.animals.copy().values():
            animal.eat(forest=forest)
            print('____________________________________________')
        time.sleep(1)


# Create forest
# Create few animals
# Add animals to forest
# Iterate throw forest and force animals to eat until no predators left
# animal_generator to create a random animal


# Tips:
# When a predator hunts, an animal is accidentally taken from the forest.
# This animal may be the predator itself. To check this and distinguish two animals with the same characteristics,
# use the uuid library. But when creating an animal, assign its id a unique value.
#
# You can use the random library to work with random numbers
#
# If you do not know how to create a forest and look at the survival process, here is an example of code that can
# be used for debugging




