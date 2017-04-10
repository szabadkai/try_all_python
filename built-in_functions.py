# abs()
print(abs(-4), abs(-4.1), abs(4.1))

# all(iterable)
print(all([True, False]), all([False, False]), all([True, True]))

# any(iterable)
print(any([True, False]), any([False, False]), any([True, True]))

# ascii(object)
print(ascii(u'Ahogy várható volt, egy politikailag igazán '))

# bin(x)
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
