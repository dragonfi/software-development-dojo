

def recursive_one(foo: int):
    foo = []
    if foo < 5:
        recursive_one(foo)
    foo.append(1)
    print(foo)

# recursive_one(0)

# mutable
[[], {}, object()]

# immutable
[1, "string", True, (1, 2, "foo")]


def the_function(the_parameter=[]):
    the_parameter.append(1)
    print(the_parameter)


the_function()
the_function()
the_function()
the_function()

l2 = []
the_function(l2)
the_function(l2)

the_function()

