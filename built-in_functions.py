# abs()
print(abs(-4), abs(-4.1), abs(4.1))

# all(iterable)
print(all([True, False]), all([False, False]), all([True, True]))

# any(iterable)
print(any([True, False]), any([False, False]), any([True, True]))

# ascii(object)
print(ascii(u'Ahogy várható volt, egy politikailag igazán '))

# bin(x)b
print([bin(i) for i in range(4)])

# bool([x])
print(bool('asd'), bool(0), bool(''), bool([]))

# bytearray([source[, encoding[, errors]]])
print(bytearray("Hello World!", encoding='utf8'))
print([i for i in bytearray("Hello World!", encoding='utf8')])
a = bytearray(4)
a.append(2)
print(a)

print(bytearray([1, 2, 3, 4, 5]))
try:
    print(bytearray([1, 2, 3, 4, 257]))
except ValueError as e:
    print(repr(e))

# bytes([source[, encoding[, errors]]])
try:
    a = bytes(4)
    a[2] = 1
    print(a)
except TypeError as e:
    print(repr(e))

# callable(object)
print(callable(1))
print(callable(len))
print(callable(TypeError))

# chr(i)
print(chr(45))
print([chr(i) for i in range(500)])


# classmethod(function)
class C:
    @classmethod
    def f(cls, i):
        print(i)


C().f(1)
C.f(1)

# compile(source, filename, mode, flags=0, dont_inherit=False, optimize=-1)
exec(compile("print('hello')\n", '<string>', 'eval'))

# complex([real[, imag]])
print(complex(1, 1))


# delattr(object, name)
class Bar:
    def __init__(self):
        self.foo = 0


a = Bar()
a.foo = 231
print(a.foo)
delattr(a, 'foo')
try:
    print(a.foo)
except AttributeError as e:
    print(e)

# dict(**kwarg)
# dict(mapping, **kwarg)
# dict(iterable, **kwarg)
print(dict(foo=1, bar=2))
print(dict({'spam': 3}, foo=1, bar=2))
print(dict([('spam', 1), ('eggs', 2)]))

# dir(object)
print(dir())
print(dir("Hello"))
print(dir(TypeError))
print(dir(len))

# divmod(a, b) like (a/b, a%b)
print(divmod(11, 5))

# enumerate(iterable, start=0)
for i, animal in enumerate(["cat", "dog", "elephant"], 1):
    print(i, animal)

# eval(expression, globals=None, locals=None)
eval('print("Hello world!")')

# exec(object[, globals[, locals]])
exec('print("Hello world!")')

# filter(function, iterable)
print(list(filter(lambda x: x > 5, range(10))))

# float(object)
print(float(12))
print(float("-4234.876"))
print(float("Inf"))

# format(value[, format_spec])
print('Hello you are {0} nice fela!'.format(1))

# frozenset(iterable)
# frozenset is hashable so it can be an item in a regular set.
print({frozenset({1, 2, 3})})

# getattr(object, name[, default])
print(getattr("Hello", "upper"))

# globals()
for glob in list(globals()):
    print(glob)

# hasattr(object, name)
print(hasattr("Cirmi", "is_awesome"))
print(hasattr("Cirmi", "__len__"))

# hash(object)
print(hash(1), hash(1.0))
print(hash(""), hash("Hello"))

# help([object])
# help returns None, it is intended to used in the shell
print(help(len))

# hex(x)
print(hex(11))

# id(object) - memory address in CPython
print(id({}), id("Hello"))

# input(prompt)
# print(input("Input number:\n"))

# int(x=0)
print(int())
print(int(3.3))
print(int("16", base=30))

# isinstance(object, classinfo)
print(isinstance("World!", "".__class__))
print(isinstance("World!", TypeError))

# issubclass(class, classinfo)
print(issubclass(TypeError, "".__class__))
print(issubclass(TypeError, TypeError))
print(issubclass(TypeError, Exception))

# iter(o, sentinel)
import random


def f():
    while 1:
        yield random.randrange(0, 10)


for i in iter(f().__next__, 2):
    print(i)

print(iter([]).__class__)

# len(s)
print(len(range(5)), len("Hello World!"), len({"d": 213}), len(["Asd", "fasdf"]))

# list(iterable)
print(list("Hello World!"))
print(list([1, 2, 3]))
print(list((1, 2, 3)))
print(list({1, 2, 3}))
print(list({'H': "e", "l": "l", "o": "!"}))


# locals()
def f():
    tmp = 1
    print("locals: {}".format(repr(locals())))


print("locals: {}".format(repr(locals())))
f()


# map(function, iterable)
def f(i):
    return i ** i


print(list(map(f, [1, 2, 3])))

# max(iter) or max(*args)
print(max(5, 12, 1))
print(max([5, 12, 1]))
print(max([5, 12, 1], [5, 12, 1, 2]))

# memoryview(obj)
print(memoryview(b"Hello")[2:])

# min(iterable) / (*args)
print(min(5, 12, 1))
print(min([5, 12, 1]))
print(min([5, 12, 1], [5, 12, 1, 2]))

# next(iterator)
l = iter([1, 2, 3])
try:
    while (1):
        print(l.__next__())
except StopIteration as e:
    print("Iteration over")

# object()
print(dir(object()))

# oct(x)
print(oct(123))

# open
with open("spam.txt", "w") as f:
    print("This will be in that file", file=f)
with open("spam.txt", "r") as f:
    for i in f:
        print(i)

# ord(c)
print([ord(i) for i in "Hello"])

# pow(x,y,z) pow(x, y) % z)
print(pow(3, 2, 2))
print(pow(3, 2))

# print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
print(*[str(i) for i in range(10)], sep="^-^", end=" THE END\n", flush=True)


# property ()
class C:
    def __init__(self):
        self._x = None

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @x.deleter
    def x(self):
        del self._x


# range(start, stop, step)
print(list(range(2, 10, 3)))
print(list(range(10, 0, -2)))


class B:
    def __repr__(self):
        return "B is the best"

    def __str__(self):
        return "What is B? "


print(str(B()), repr(B()))

# reversed(seq)
print(list(reversed(range(5))))
print(reversed(range(5)))

# round(num, ndigits)
print(round(2.675, ndigits=2))
print(round(2.765, ndigits=2))
print("wat?")

# set(iterable)
print(set([1, 1, 1, 1, 1]) == {1})  # True

# setattr(object, name, value)
b = B()
setattr(b, "x", "Monkey-Patched Attribute")
print(b.x)

# slice(start, stop, step)
print([1, 2, 3].__getitem__(slice(0, 2)))
