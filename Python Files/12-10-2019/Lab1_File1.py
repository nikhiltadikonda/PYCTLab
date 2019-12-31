Python 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:21:23) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a=[2,3,4,5]
>>> a
[2, 3, 4, 5]
>>> type(a)
<class 'list'>
>>> b=[1,2,3,4,5]
>>> c=[1,2,3,4,5,6]
>>> a=[[i for i in range(1,3)]]
>>> a
[[1, 2]]
>>> a=['a',[1,2],'b',c]
>>> a
['a', [1, 2], 'b', [1, 2, 3, 4, 5, 6]]
>>> a[0]
'a'
>>> a[3][1]
2
>>> type(a[0])
<class 'str'>
>>> type(a[1])
<class 'list'>
>>> type(a[1][2])
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    type(a[1][2])
IndexError: list index out of range
>>> type(a[1][1])
<class 'int'>
>>> b
[1, 2, 3, 4, 5]
>>> b[0:3]
[1, 2, 3]
>>> a=['a',[1,2],'b','c']
>>> a.append((2,3,4))
>>> a
['a', [1, 2], 'b', 'c', (2, 3, 4)]
>>> type(a[4])
<class 'tuple'>
>>> b[-1:-3]
[]
>>> b[-1:-2]
[]
>>> b[-1]
5
>>> b[-5:-1]
[1, 2, 3, 4]
>>> 

>>> if 5>2:
     print("Waste of knowing now")

     
Waste of knowing now
>>> 
b[-5:0]
[]
>>> b[-5:0]
[]
>>> b[-5:1]
[1]
>>> b[-1]
5
>>> dir(list)
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
>>> del(a)
>>> a
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    a
NameError: name 'a' is not defined
>>> a=[1,2,3,4,5]
>>> a.remove(1)
>>> a
[2, 3, 4, 5]
>>> dir(int)
['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__gt__', '__hash__', '__index__', '__init__', '__init_subclass__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'as_integer_ratio', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']
>>> 

>>> a.insert(0,3)
>>> a
[3, 2, 3, 4, 5]
>>> a=[1,2,3,4,5]
>>> a.pop(0)
1
>>> a
[2, 3, 4, 5]
>>> a.insert(0,6)
>>> a
[6, 2, 3, 4, 5]
>>> 
