from abc import abstractmethod


class GardenMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        """
        Possible changes to the value of the `__init__` argument do not affect
        the returned instance.
        """
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Garden(metaclass=GardenMeta):
    def __init__(self, vegetables, fruits, pests, gardener):
        self.vegetables = vegetables
        self.fruits = fruits
        self.pests = pests
        self.gardener = gardener

    def show_the_garden(self):
        print(f'I have such vegetables {self.vegetables}')
        print(f'I have such fruits {self.fruits}')

    def pest_attack(self):
        self.pests.eat(self.gardener.plants)


class Vegetables:
    def __init__(self, vegetable_type):
        self.vegetable_type = vegetable_type

    states = {"0": "None", "1": "Flowering", "2": "Green", "3": "Red"}

    @abstractmethod
    def growth(self):
        raise NotImplementedError('You missed me.')

    @abstractmethod
    def is_ripe(self):
        raise NotImplementedError("You missed me")

    @abstractmethod
    def is_eatable(self):
        raise NotImplementedError("You missed me")


class Fruits:
    def __init__(self, fruits_type):
        self.fruits_type = fruits_type

    states = {0: "None", 1: "Flowering", 2: "Green", 3: "Red"}

    @abstractmethod
    def growth(self):
        raise NotImplementedError('You missed me.')

    @abstractmethod
    def is_ripe(self):
        raise NotImplementedError("You missed me")

    @abstractmethod
    def is_eatable(self):
        raise NotImplementedError("You missed me")


class Tomato(Vegetables):
    def __init__(self, vegetable_type, number_of_tomatoes):
        Vegetables.__init__(self, vegetable_type)
        self.number_of_tomatoes = number_of_tomatoes
        self.states = 0
        self.vegetable_type = vegetable_type

    def growth(self):
        if self.states < 3:
            self.states += 1
        # self.print_state()

    def print_state(self):
        print(f"The tomato bush with tomato type: {self.vegetable_type}, {self.number_of_tomatoes}, state: {self.states}")

    def is_ripe(self):
        return self.states == 3

    def is_eatable(self):
        return self.states in [2, 3]


class Apple(Fruits):
    def __init__(self, fruits_type, number_of_apples):
        Fruits.__init__(self, fruits_type)
        self.number_of_apples = number_of_apples
        self.states = 0
        self.fruits_type = fruits_type

    def print_state(self):
        print(f"The apple tree with apple type: {self.fruits_type}, {self.number_of_apples} , state: {self.states}")

    def growth(self):
        if self.states < 3:
            self.states += 1
        # self.print_state()

    def is_ripe(self):
        return self.states == 3

    def is_eatable(self):
        return self.states in [2, 3]


class TomatoBush:
    def __init__(self, number_of_tomatoes):
        self.tomatoes = [Tomato('Cherry', index) for index in range(1, number_of_tomatoes)]

    def growth_all(self):
        for tomato in self.tomatoes:
            tomato.growth()

    def all_are_ripe(self):
        return all([tomato.is_ripe() for tomato in self.tomatoes])

    def give_away_all(self):
        self.tomatoes = []

    def pests_attack(self):
        for tomato in self.tomatoes.copy():
            if tomato.is_eatable():
                self.tomatoes.remove(tomato)
                print('Yummi')
            else:
                print('It is not tasty!')

    def check_states(self):
        for tomato in self.tomatoes:
            tomato.print_state()


class AppleTree:
    def __init__(self, number_of_apples):
        self.apples = [Apple('White', index) for index in range(1, number_of_apples)]

    def growth_all(self):
        for apple in self.apples:
            apple.growth()

    def all_are_ripe(self):
        return all([apple.is_ripe() for apple in self.apples])

    def give_away_all(self):
        self.apples = []

    def pests_attack(self):
        for apple in self.apples.copy():
            if apple.is_eatable():
                self.apples.remove(apple)
                print('Yummi')
            else:
                print('It is not tasty!')

    def check_states(self):
        for apple in self.apples:
            apple.print_state()


class Gardener:
    def __init__(self, name, plants):
        self.name = name
        self.plants = plants

    def work(self):
        for plant in self.plants:
            plant.growth_all()

    def harvest(self):
        for plant in self.plants:
            if plant.all_are_ripe():
                plant.give_away_all()
            else:
                print('Too early to harvest')

    def poison_the_pests(self):
        Garden().pests.quantity = 0
        print('I will save my garden! Watch out damn pests!!')

    def check_states(self):
        for plant in self.plants:
            plant.check_states()


class Pests:
    def __init__(self, pest_type, quantity):
        self.pest_type = pest_type
        self.quantity = quantity

    def eat(self, plants):
        if self.quantity > 10:
            for plant in plants:
                plant.pests_attack()


# Creating list of instances for vegetables and fruits, pests and gardener
tomato_bush = TomatoBush(4)
apple_tree = AppleTree(3)
tom = Gardener('Tom', [tomato_bush, apple_tree])
pests1 = Pests('worm', 11)

# creating only one garden instance with vegetables and fruits
garden = Garden(vegetables=tomato_bush.tomatoes, fruits=apple_tree.apples, pests=pests1, gardener=tom)
tom.work()
tom.check_states()
garden.pest_attack()
tom.work()
tom.check_states()
# garden.pest_attack()
tom.poison_the_pests()
tom.work()
tom.check_states()
tom.harvest()
garden.show_the_garden()

# if not state:
# gardener.handling()
# for i in range(3):
#     tom.work()
#     tom.harvest()


