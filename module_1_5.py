immutable_var = (5, 6, True, "tuple")
print('Immutable tuple:', immutable_var)
immutable_var[1]!=10 # Объекты встроенных типов, таких как int, float, bool, str, tuple, unicode, являются неизменяемыми.
mutable_list = ([1, 2, 'a'], 'b', 'Modified')
mutable_list[0][0] = 8
print('Mutable list:', mutable_list)
