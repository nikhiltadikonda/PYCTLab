Python 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:21:23) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a=[i for i in range(1,11)]
>>> a
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> dir(a)
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
>>> a.append(11)
>>> a.insert(11,12)
>>> a
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
>>> a.count()
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    a.count()
TypeError: count() takes exactly one argument (0 given)
>>> a.count(2)
1
>>> a.extend([13,14,15])
>>> a
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
>>> a.index(13)
12
>>> a.pop(1)
2
>>> a.remove(15)
>>> a.reverse()
>>> a
[14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 1]
>>> a.sort()
>>> a.clear()
>>> a
[]
>>> 

>>> 
>>> a=[i for i in range(1,11)]
>>> hash(a)
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    hash(a)
TypeError: unhashable type: 'list'
>>> 
>>> a
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> a
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> sorted(a)
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> a.reverse()
>>> sorted(a)
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> a
[10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
>>> 
