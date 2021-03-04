class IAnimal():
    def power(self):
        raise NotImplementedError
    def eat(self, other):
        raise NotImplementedError

class Animal(IAnimal):
    def __init__(self, nutrition):
        self.nutrition = nutrition
        self.status = "Hungry"

    def power(self):
        raise NotImplementedError

    def eat(self, other):
        if self.status in ["Eaten", "Dead"]:
            return
        if self.power() > other.power():
            self.status = "Well Fed"
            other.status = "Eaten"


class Rabbit(Animal):
    def __init__(self, nutrition = 10):
        super().__init__(nutrition)

    def power(self):
        return 10


class Tiger(Animal):
    def __init__(self, albino = False):
        super().__init__(100)
        self.albino = albino

    def get_color(self):
        if self.albino:
            return ["white", "white"]
        return ["red", "black"]
    
    def power(self):
        return 100 if self.status == "Well Fed" else 50
        # condition ? true_value : false_value
        # true_value if condition else false_value

t1 = Tiger()
t2 = Tiger(albino=True)
r1 = Rabbit()

print(t1.get_color(), t2.get_color())
print(t1.status, ",", t2.status, r1.status)
t1.eat(r1)
print([t1.status, t2.status, r1.status])
t2.eat(t1)
print([t1.status, t2.status, r1.status])

# Interface

class Rabber(Tiger, Rabbit):
    pass

print(Rabber().nutrition)


def fn(animal1: IAnimal, animal2: IAnimal) -> bool:
    pass

class IEndangered():
    def get_position(self):
        raise NotImplementedError

class TaggedTiger(Tiger, IEndangered):
    def get_position(self):
        return (72.7, 83.1)

class RadioTransmitterMixin():
    def get_position(self):
        return (72.7, 83.1)

class TaggedTiger2(Tiger, RadioTransmitterMixin, IEndangered):
    pass

# Composition

def avg(seq):
    seq = list(seq)
    if len(seq) == 0:
        return 0
    return sum(seq) / len(seq)

class Wheel():
    def __init__(self, traction):
        self.traction = traction

class Engine():
    def __init__(self, p):
        self.p = p
    
    def produce_power(self):
        return self.p

class Car():
    def __init__(self, engine, wheels):
        self.wheels = wheels
        self.engine = engine

    def push_pedal(self):
        traction = avg(w.traction for w in self.wheels)
        power = self.engine.produce_power()
        if traction < 100:
            return "Wheels spin!"
        if power > traction:
            return "Going forward!"
        return "Sitting still!"

car_with_tractor_wheels = Car(Engine(100), [Wheel(1000), Wheel(1000)])

print(car_with_tractor_wheels.push_pedal())
print(Car(Engine(1000), [Wheel(10), Wheel(10)]).push_pedal())
print(Car(Engine(200), [Wheel(100), Wheel(100)]).push_pedal())


# Object Oriented Design Patterns

# Strategy

class IStrategy():
    def conquer(self, galaxy):
        raise NotImplementedError


class Galaxy():
    def __init__(self, size, factions):
        self.size = size
        self.factions = factions
        self.conquered = False

    def conquer(self, strategy: IStrategy):
        self.conquered = strategy.conquer(self)

    def __repr__(self):
        return "Galaxy({}, {}, {})".format(
            self.size, self.factions, self.conquered)


class Blitzkrieg(IStrategy):
    def conquer(self, galaxy):
        return galaxy.size < 10 and galaxy.factions == 1


class DivideAndConquer(IStrategy):
    def conquer(self, galaxy):
        return galaxy.factions > 1


galaxies = [Galaxy(7, 1) , Galaxy(7, 2) , Galaxy(100, 1) , Galaxy(100, 10)]

print("Initial", galaxies)
list(galaxy.conquer(Blitzkrieg()) for galaxy in galaxies)
print("Blitz", galaxies)
list(galaxy.conquer(DivideAndConquer()) for galaxy in galaxies)
print("Divide", galaxies)