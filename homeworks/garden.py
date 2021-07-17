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
    def __init__(self, vegetables, fruits):
        self.vegetables = vegetables
        self.fruits = fruits

    def show_the_garden(self):
        print(f'I have such vegetables {self.vegetables}')
        print(f'I have such fruits {self.fruits}')


class Vegetables:
    def __init__(self, vegetable_type):
        self.vegetable_type = vegetable_type
        self.pests = []

    states = {"0": "None", "1": "Flowering", "2": "Green", "3": "Red"}

    # The method is added pests to the process
    def add_pests(self, quantity, pest_type):
        self.pests = [Pest(pest_type) for index in range(1, quantity)]

    @abstractmethod
    def growth(self):
        raise NotImplementedError('You missed me.')

    @abstractmethod
    def is_ripe(self):
        raise NotImplementedError("You missed me")

    # The method is checked whether plant is eatable (states >=2)
    @abstractmethod
    def is_eatable(self):
        raise NotImplementedError("You missed me")

    # The method is checked whether plant has been eaten
    def is_eaten(self):
        return self.is_eatable() and len(self.pests) >= self.critical_pests_limit()

    # The method is set critical pests number for corresponding plant's type
    @abstractmethod
    def critical_pests_limit(self):
        raise NotImplementedError("You missed me")

    # The method is return corresponding plant's features
    @abstractmethod
    def vegetable_name(self):
        raise NotImplementedError("You missed me")

    # The method is displayed current growth status
    def grow_process_status(self):
        if self.is_eaten():
            return f'The {self.vegetable_name()} is eaten'
        if self.is_ripe():
            return f'The {self.vegetable_name()} is ripe'
        return f'The {self.vegetable_name()} is still growing'


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
        print(f"{self.vegetable_type}, {self.number_of_tomatoes}, {self.states}")

    def vegetable_name(self):
        return f"{self.vegetable_type}, {self.number_of_tomatoes}, {self.states}"

    def is_ripe(self):
        return self.states == 3

    def is_eatable(self):
        return self.states in [2, 3]

    def critical_pests_limit(self):
        return 3


class Apple(Fruits):
    def __init__(self, fruits_type, number_of_apples):
        Fruits.__init__(self, fruits_type)
        self.number_of_apples = number_of_apples
        self.states = 0
        self.fruits_type = fruits_type

    def print_state(self):
        print(f"{self.fruits_type}, {self.number_of_apples} , {self.states}")

    def growth(self):
        if self.states < 3:
            self.states += 1
        self.print_state()

    def is_ripe(self):
        return self.states == 3


class TomatoBush:
    def __init__(self):
        self.tomatoes = []

    def growth_all(self):
        print("\nNew growing...")
        for tomato in self.tomatoes.copy():
            tomato.growth()
            print(tomato.grow_process_status())
            if tomato.is_eaten():
                self.tomatoes.remove(tomato)
                print(f'Tomato: {tomato.vegetable_name()} has been deleted from bush')

    def all_are_ripe(self):
        return all([tomato.is_ripe() for tomato in self.tomatoes])

    def give_away_all(self):
        self.tomatoes = []

    def add_tomato(self, tomato):
        self.tomatoes.append(tomato)


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


class Pest:
    def __init__(self, quantity, pest_type):
        self.pest_type = pest_type
        self.quantity = quantity


tomato1 = Tomato('Slivka1', 2)
tomato1.add_pests(2, 'Worms')

tomato2 = Tomato('Slivka2', 3)
tomato2.add_pests(4, 'Worms2')

apple_tree1 = AppleTree(2)

tomato_bush1 = TomatoBush()
tomato_bush1.add_tomato(tomato1)
tomato_bush1.add_tomato(tomato2)

garden1 = Garden(tomato_bush1, apple_tree1)
jorge = Gardener('Jorge', [tomato_bush1, apple_tree1])

jorge.work()
jorge.work()
jorge.harvest()
jorge.work()
jorge.harvest()
jorge.work()
jorge.harvest()




