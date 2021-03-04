# Funkcionális

# csak konstansok vannak
# a fv is egy érték

# ebből következik: rekurziót, fv.-ket egymásba ágyazni

def my_map(fn, seq):
    if len(seq) == 0:
        return []
    return [fn(seq[0])] + my_map(fn, seq[1:])

def add1(a: int) -> int:
    return a + 1

print(my_map(add1, [1,2,3]))


def add(value: int):
    def inner_add(other_value: int):
        return value + other_value
    return inner_add

add1 = add(1)
# def add1(other_value: int):
#    value = 1
#    return value + other_value
add10 = add(10)
# def add10(other_value: int):
#    value = 10
#    return value + other_value

print(add1(100), add10(100), add(10)(20))

persons = [{'age': 10, 'name': 'Greg'}, {'age': 20, 'name': 'Michael'}]

selected = filter(lambda p: p['age'] < 18, persons)
selected2 = map(lambda p: p['name'], selected)
print(list(selected2))

# Imperative

def kid_names(persons):
    selected_person_names = []
    for person in persons:
        if person['age'] > 18:
            continue
        selected_person_names.append(person['name'])
    return selected_person_names

print(kid_names(persons))

# Strategy

from collections import namedtuple

Galaxy = namedtuple("Galaxy", "size factions conquered")

galaxies = [
    Galaxy(7, 1, False) , Galaxy(7, 2, False), 
    Galaxy(100, 1, False) , Galaxy(100, 10, False)]

def conquer(galaxy, strategy):
    return Galaxy(galaxy.size, galaxy.factions, strategy(galaxy))

def blitzkrieg(galaxy):
    return galaxy.size < 10 and galaxy.factions == 1

def divide_and_conquer(galaxy):
    return galaxy.factions > 1

from pprint import pprint

print("Initial")
pprint(galaxies)
print("Blitz")
pprint([conquer(galaxy, blitzkrieg) for galaxy in galaxies])
print("Divide")
pprint([conquer(galaxy, divide_and_conquer) for galaxy in galaxies])
