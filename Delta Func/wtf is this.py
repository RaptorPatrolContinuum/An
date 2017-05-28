Python 3.4.3 (v3.4.3:9b73f1c3e601, Feb 24 2015, 22:43:06) [MSC v.1600 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> ================================ RESTART ================================
>>> 
Exit or logout to leave 
test
char is missing [1, 2]
char is missing ['A', 'B']
char is missing [[3, 4], [5, 6]]
char is missing [7, ['yuku yo']]
i is missing 5
char is missing ['so transiently', 'Kotoko']
input []
char is missing ['subversively', [1, 5]]
char is missing [[1, 2], [1, 2]]
char is missing ['B', 'D']
char is missing ['B', 'F']
i is missing 5
char is missing ['Kotoko', 'works with strings']
i is missing 6
char is missing [9, 10]
i is missing 7
char is missing [11, 5]
i is missing 8
char is missing ['Dwarf fortress', 'wtf']
input []
[]
the issue is that I haven't implemented lemma 1.5.1/2 (? this actually might be its own theorem) because address is complaining but each element is part of the basis so basically I just have to bump up the L-value and return the address properly
really need to fix address so that it inputs the right Lvalues
input [3, 6, 11]
pair is 3
LVal is  1
pair is 6
LVal is  1
pair is 11
LVal is  1
[]
input [[3, 6, 11]]
pair is [3, 6, 11]
[3, 6, 11] is not int!
LVal is  2
[]
Exit or logout to leave 

>>> ================================ RESTART ================================
>>> 
Exit or logout to leave 

i is missing 1
char is missing [1, 2]
i is missing 2
char is missing ['A', 'B']
i is missing 3
char is missing [[3, 4], [5, 6]]
i is missing 4
char is missing [7, ['yuku yo']]
i is missing 5
char is missing ['so transiently', 'Kotoko']
input []
i is missing 1
char is missing ['subversively', [1, 5]]
i is missing 2
char is missing [[1, 2], [1, 2]]
i is missing 3
char is missing ['B', 'D']
i is missing 4
char is missing ['B', 'F']
i is missing 5
char is missing ['Kotoko', 'works with strings']
i is missing 6
char is missing [9, 10]
i is missing 7
char is missing [11, 5]
i is missing 8
char is missing ['Dwarf fortress', 'wtf']
input []
[]
the issue is that I haven't implemented lemma 1.5.1/2 (? this actually might be its own theorem) because address is complaining but each element is part of the basis so basically I just have to bump up the L-value and return the address properly
really need to fix address so that it inputs the right Lvalues
input [3, 6, 11]
pair is 3
LVal is  1
pair is 6
LVal is  1
pair is 11
LVal is  1
[]
input [[3, 6, 11]]
pair is [3, 6, 11]
[3, 6, 11] is not int!
LVal is  2
[]
Exit or logout to leave 

>>> ================================ RESTART ================================
>>> 
Traceback (most recent call last):
  File "C:/An/Delta Func/powerset testing.py", line 6, in <module>
    print(powerset([1,2,3]))
  File "C:/An/Delta Func/powerset testing.py", line 4, in powerset
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))
NameError: name 'chain' is not defined
>>> ================================ RESTART ================================
>>> 
Traceback (most recent call last):
  File "C:/An/Delta Func/powerset testing.py", line 8, in <module>
    print(powerset([1,2,3]))
  File "C:/An/Delta Func/powerset testing.py", line 6, in powerset
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))
NameError: name 'chain' is not defined
>>> ================================ RESTART ================================
>>> 
Traceback (most recent call last):
  File "C:/An/Delta Func/powerset testing.py", line 8, in <module>
    print(powerset(123))
  File "C:/An/Delta Func/powerset testing.py", line 5, in powerset
    s = list(iterable)
TypeError: 'int' object is not iterable
>>> ================================ RESTART ================================
>>> 
Traceback (most recent call last):
  File "C:/An/Delta Func/powerset testing.py", line 8, in <module>
    print(list(powerset(123)))
  File "C:/An/Delta Func/powerset testing.py", line 5, in powerset
    s = list(iterable)
TypeError: 'int' object is not iterable
>>> ================================ RESTART ================================
>>> 
Traceback (most recent call last):
  File "C:/An/Delta Func/powerset testing.py", line 8, in <module>
    print(list(powerset(123)))
  File "C:/An/Delta Func/powerset testing.py", line 5, in powerset
    s = list(iterable)
TypeError: 'int' object is not iterable
>>> ================================ RESTART ================================
>>> 
Traceback (most recent call last):
  File "C:/An/Delta Func/powerset testing.py", line 6, in <module>
    print(list(powerset(123)))
  File "C:/An/Delta Func/powerset testing.py", line 3, in powerset
    s = list(iterable)
TypeError: 'int' object is not iterable
>>> ================================ RESTART ================================
>>> 
Traceback (most recent call last):
  File "C:/An/Delta Func/powerset testing.py", line 6, in <module>
    print(list(powerset([123])))
  File "C:/An/Delta Func/powerset testing.py", line 4, in powerset
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))
NameError: name 'chain' is not defined
>>> ================================ RESTART ================================
>>> 
Traceback (most recent call last):
  File "C:/An/Delta Func/powerset testing.py", line 8, in <module>
    print(list(powerset(123)))
  File "C:/An/Delta Func/powerset testing.py", line 5, in powerset
    s = list(iterable)
TypeError: 'int' object is not iterable
>>> ================================ RESTART ================================
>>> 
Traceback (most recent call last):
  File "C:/An/Delta Func/powerset testing.py", line 8, in <module>
    print(list(powerset([123])))
  File "C:/An/Delta Func/powerset testing.py", line 6, in powerset
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))
NameError: name 'chain' is not defined
>>> ================================ RESTART ================================
>>> 
Traceback (most recent call last):
  File "C:/An/Delta Func/powerset testing.py", line 8, in <module>
    print(list(powerset([123])))
  File "C:/An/Delta Func/powerset testing.py", line 6, in powerset
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))
NameError: name 'chain' is not defined
>>> ================================ RESTART ================================
>>> 
Traceback (most recent call last):
  File "C:/An/Delta Func/powerset testing.py", line 8, in <module>
    print(list(powerset([123])))
  File "C:/An/Delta Func/powerset testing.py", line 6, in powerset
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))
NameError: name 'chain' is not defined
>>> ================================ RESTART ================================
>>> 
Traceback (most recent call last):
  File "C:/An/Delta Func/powerset testing.py", line 9, in <module>
    print(list(powerset([123])))
  File "C:/An/Delta Func/powerset testing.py", line 7, in <genexpr>
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))
NameError: name 'combinations' is not defined
>>> ================================ RESTART ================================
>>> 
Traceback (most recent call last):
  File "C:/An/Delta Func/powerset testing.py", line 8, in <module>
    print(list(powerset([123])))
  File "C:/An/Delta Func/powerset testing.py", line 6, in powerset
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))
NameError: name 'chain' is not defined
>>> ================================ RESTART ================================
>>> 
<generator object powerset at 0x03AAE828>
>>> ================================ RESTART ================================
>>> 
[[], [4], [5], [4, 5], [6], [4, 6], [5, 6], [4, 5, 6]]
>>> ================================ RESTART ================================
>>> 
0
1
10
11
100
101
110
111
1000
1001
1010
1011
1100
1101
1110
1111
>>> ================================ RESTART ================================
>>> 
0
1
01
11
001
101
011
111
0001
1001
0101
1101
0011
1011
0111
1111
>>> ================================ RESTART ================================
>>> 
0000
0001
0001
0011
0001
0101
0011
0111
0001
1001
0101
1101
0011
1011
0111
1111
>>> ================================ RESTART ================================
>>> 
0000
Traceback (most recent call last):
  File "C:/An/Delta Func/powerset testing.py", line 10, in <module>
    print("{0:b}".format(x).zfill(4))[::-1]
TypeError: 'NoneType' object is not subscriptable
>>> ================================ RESTART ================================
>>> 
0000
1000
0100
1100
0010
1010
0110
1110
0001
1001
0101
1101
0011
1011
0111
1111
>>> ================================ RESTART ================================
>>> 
Traceback (most recent call last):
  File "C:/An/Delta Func/powerset testing.py", line 7, in <module>
    print(list(powerset([[0,0],[1,0],[0,1][1,1]])))
TypeError: list indices must be integers, not tuple
>>> ================================ RESTART ================================
>>> 
Traceback (most recent call last):
  File "C:/An/Delta Func/powerset testing.py", line 7, in <module>
    print(list(powerset([[0,0],[1,0],[0,1][1,1]])))
TypeError: list indices must be integers, not tuple
>>> ================================ RESTART ================================
>>> 
Traceback (most recent call last):
  File "C:/An/Delta Func/powerset testing.py", line 6, in <module>
    print(list(powerset([[0,0],[1,0],[0,1][1,1]])))
TypeError: list indices must be integers, not tuple
>>> ================================ RESTART ================================
>>> 
Traceback (most recent call last):
  File "C:/An/Delta Func/powerset testing.py", line 6, in <module>
    list(powerset("abcd"))
  File "C:/An/Delta Func/powerset testing.py", line 4, in powerset
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))
NameError: name 'chain' is not defined
>>> ================================ RESTART ================================
>>> 
Traceback (most recent call last):
  File "C:/An/Delta Func/powerset testing.py", line 6, in <module>
    list(powerset("abcd"))
  File "C:/An/Delta Func/powerset testing.py", line 4, in powerset
    return itertools.chain.from_iterable(combinations(s, r) for r in range(len(s)+1))
NameError: name 'itertools' is not defined
>>> ================================ RESTART ================================
>>> 
Traceback (most recent call last):
  File "C:/An/Delta Func/powerset testing.py", line 8, in <module>
    list(powerset("abcd"))
  File "C:/An/Delta Func/powerset testing.py", line 6, in <genexpr>
    return itertools.chain.from_iterable(combinations(s, r) for r in range(len(s)+1))
NameError: name 'combinations' is not defined
>>> ================================ RESTART ================================
>>> 
>>> ================================ RESTART ================================
>>> 
[(), ('a',), ('b',), ('c',), ('d',), ('a', 'b'), ('a', 'c'), ('a', 'd'), ('b', 'c'), ('b', 'd'), ('c', 'd'), ('a', 'b', 'c'), ('a', 'b', 'd'), ('a', 'c', 'd'), ('b', 'c', 'd'), ('a', 'b', 'c', 'd')]
>>> ================================ RESTART ================================
>>> 
<itertools.chain object at 0x0374CEF0>
>>> ================================ RESTART ================================
>>> 
[(), ('a',), ('b',), ('c',), ('d',), ('a', 'b'), ('a', 'c'), ('a', 'd'), ('b', 'c'), ('b', 'd'), ('c', 'd'), ('a', 'b', 'c'), ('a', 'b', 'd'), ('a', 'c', 'd'), ('b', 'c', 'd'), ('a', 'b', 'c', 'd')]
>>> ================================ RESTART ================================
>>> 
()
('a',)
('b',)
('c',)
('d',)
('a', 'b')
('a', 'c')
('a', 'd')
('b', 'c')
('b', 'd')
('c', 'd')
('a', 'b', 'c')
('a', 'b', 'd')
('a', 'c', 'd')
('b', 'c', 'd')
('a', 'b', 'c', 'd')
>>> ================================ RESTART ================================
>>> 
Traceback (most recent call last):
  File "C:\An\Delta Func\powerset testing.py", line 7, in <module>
    for x in powerset(list(powerset([0,0],[[1,1]]))):
TypeError: powerset() takes 1 positional argument but 2 were given
>>> ================================ RESTART ================================
>>> 
()
((),)
(([0, 0],),)
(([1, 1],),)
(([0, 0], [1, 1]),)
((), ([0, 0],))
((), ([1, 1],))
((), ([0, 0], [1, 1]))
(([0, 0],), ([1, 1],))
(([0, 0],), ([0, 0], [1, 1]))
(([1, 1],), ([0, 0], [1, 1]))
((), ([0, 0],), ([1, 1],))
((), ([0, 0],), ([0, 0], [1, 1]))
((), ([1, 1],), ([0, 0], [1, 1]))
(([0, 0],), ([1, 1],), ([0, 0], [1, 1]))
((), ([0, 0],), ([1, 1],), ([0, 0], [1, 1]))
>>> ================================ RESTART ================================
>>> 
()
((),)
(('a',),)
(('b',),)
(('a', 'b'),)
((), ('a',))
((), ('b',))
((), ('a', 'b'))
(('a',), ('b',))
(('a',), ('a', 'b'))
(('b',), ('a', 'b'))
((), ('a',), ('b',))
((), ('a',), ('a', 'b'))
((), ('b',), ('a', 'b'))
(('a',), ('b',), ('a', 'b'))
((), ('a',), ('b',), ('a', 'b'))
>>> ================================ RESTART ================================
>>> 
()
((),)
(('a',),)
(('b',),)
(('a', 'b'),)
((), ('a',))
((), ('b',))
((), ('a', 'b'))
(('a',), ('b',))
(('a',), ('a', 'b'))
(('b',), ('a', 'b'))
((), ('a',), ('b',))
((), ('a',), ('a', 'b'))
((), ('b',), ('a', 'b'))
(('a',), ('b',), ('a', 'b'))
((), ('a',), ('b',), ('a', 'b'))
>>> ================================ RESTART ================================
>>> 
()
('a',)
('b',)
('a', 'b')
>>> ================================ RESTART ================================
>>> 
[1, 2]
['A', 'B']
[[3, 4], [5, 6]]
[7, ['yuku yo']]
['so transiently', 'Kotoko']
>>> ================================ RESTART ================================
>>> 
Traceback (most recent call last):
  File "C:/An/Testing/fixing address2.py", line 1, in <module>
    basis = [1,2,A,B,3]
NameError: name 'A' is not defined
>>> ================================ RESTART ================================
>>> 
[1, 2]
['A', 'B']
[[3, 4], [5, 6]]
[7, ['yuku yo']]
['so transiently', 'Kotoko']
>>> ================================ RESTART ================================
>>> 
i is missing 1
char is missing [1, 2]
i is missing 2
char is missing ['A', 'B']
i is missing 3
char is missing [[3, 4], [5, 6]]
i is missing 4
char is missing [7, ['yuku yo']]
i is missing 5
char is missing ['so transiently', 'Kotoko']
[[[[1, 2, 'A', 'B', 3, 4, 5, 6, 7, 'y', 'u', 'k', 'o', 's', 't', 'r', 'a', 'n', 'i', 'e', 'n', 'l'], 1, []], [[1, [1, 2]], [2, ['A', 'B']], [3, [[3, 4], [5, 6]]], [4, [7, ['yuku yo']]], [5, ['so transiently', 'Kotoko']]]]]
>>> ================================ RESTART ================================
>>> 
>>> ================================ RESTART ================================
>>> 
Traceback (most recent call last):
  File "C:/An/Testing/fixing address2.py", line 50, in <module>
    x = basis.index(str("35"))
ValueError: '35' is not in list

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:/An/Testing/fixing address2.py", line 52, in <module>
    print("i is missing", i)
NameError: name 'i' is not defined
>>> ================================ RESTART ================================
>>> 
Traceback (most recent call last):
  File "C:/An/Testing/fixing address2.py", line 50, in <module>
    x = basis.index(str(3))
ValueError: '3' is not in list

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:/An/Testing/fixing address2.py", line 52, in <module>
    print("i is missing", i)
NameError: name 'i' is not defined
>>> ================================ RESTART ================================
>>> 
Traceback (most recent call last):
  File "C:/An/Testing/fixing address2.py", line 58, in <module>
    x = basis.index(str(3))
ValueError: '3' is not in list
>>> ================================ RESTART ================================
>>> 
Traceback (most recent call last):
  File "C:/An/Testing/fixing address2.py", line 58, in <module>
    x = basis.index(str(k))
NameError: name 'k' is not defined
>>> ================================ RESTART ================================
>>> 
>>> ================================ RESTART ================================
>>> 
>>> ================================ RESTART ================================
>>> 
err is caught
>>> ================================ RESTART ================================
>>> 
[1, 2, 'A', 'B', 3, 4, 5, 6, 7, 'y', 'u', 'k', 'o', 's', 't', 'r', 'a', 'n', 'i', 'e', 'n', 'l']
>>> ================================ RESTART ================================
>>> 
Traceback (most recent call last):
  File "C:/An/Testing/fixing address2.py", line 51, in <module>
    print(basis.replace["[",""].replace["]",""])
AttributeError: 'list' object has no attribute 'replace'
>>> ================================ RESTART ================================
>>> 
Traceback (most recent call last):
  File "C:/An/Testing/fixing address2.py", line 51, in <module>
    print(str(basis).replace["[",""].replace["]",""])
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> ================================ RESTART ================================
>>> 
Traceback (most recent call last):
  File "C:/An/Testing/fixing address2.py", line 51, in <module>
    print(str(basis).replace["[",""])
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> ================================ RESTART ================================
>>> 
[1, 2, 'A', 'B', 3, 4, 5, 6, 7, 'y', 'u', 'k', 'o', 's', 't', 'r', 'a', 'n', 'i', 'e', 'n', 'l']
>>> ================================ RESTART ================================
>>> 
Traceback (most recent call last):
  File "C:/An/Testing/fixing address2.py", line 53, in <module>
    print(testy.replace["[",""].replace["]",""])
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> ================================ RESTART ================================
>>> 
[1, 2, 'A', 'B', 3, 4, 5, 6, 7, 'y', 'u', 'k', 'o', 's', 't', 'r', 'a', 'n', 'i', 'e', 'n', 'l']
>>> ================================ RESTART ================================
>>> 
1, 2, 'A', 'B', 3, 4, 5, 6, 7, 'y', 'u', 'k', 'o', 's', 't', 'r', 'a', 'n', 'i', 'e', 'n', 'l'
>>> ================================ RESTART ================================
>>> 
1, 2, 'A', 'B', 3, 4, 5, 6, 7, 'yuku yo', 'so transiently', 'Kotoko'
>>> ================================ RESTART ================================
>>> 
1
,
 
2
,
 
'
A
'
,
 
'
B
'
,
 
3
,
 
4
,
 
5
,
 
6
,
 
7
,
 
'
y
u
k
u
 
y
o
'
,
 
'
s
o
 
t
r
a
n
s
i
e
n
t
l
y
'
,
 
'
K
o
t
o
k
o
'
>>> ================================ RESTART ================================
>>> 
()
((),)
(('1',),)
(('2',),)
(('1', '2'),)
((), ('1',))
((), ('2',))
((), ('1', '2'))
(('1',), ('2',))
(('1',), ('1', '2'))
(('2',), ('1', '2'))
((), ('1',), ('2',))
((), ('1',), ('1', '2'))
((), ('2',), ('1', '2'))
(('1',), ('2',), ('1', '2'))
((), ('1',), ('2',), ('1', '2'))
>>> ================================ RESTART ================================
>>> 
()
('1',)
('2',)
('1', '2')
>>> ================================ RESTART ================================
>>> 
1
,
 
2
,
 
'
A
'
,
 
'
B
'
,
 
3
,
 
4
,
 
5
,
 
6
,
 
7
,
 
'
y
u
k
u
 
y
o
'
,
 
'
s
o
 
t
r
a
n
s
i
e
n
t
l
y
'
,
 
'
K
o
t
o
k
o
'
>>> ================================ RESTART ================================
>>> 
1
,
 
2
,
 
'
A
'
,
 
'
B
'
,
 
3
,
 
4
,
 
5
,
 
6
,
 
7
,
 
'
y
u
k
u
 
y
o
'
,
 
'
s
o
 
t
r
a
n
s
i
e
n
t
l
y
'
,
 
'
K
o
t
o
k
o
'
Traceback (most recent call last):
  File "C:/An/Testing/fixing address2.py", line 62, in <module>
    for x in pairdepth2:
NameError: name 'pairdepth2' is not defined
>>> ================================ RESTART ================================
>>> 
1
,
 
2
,
 
'
A
'
,
 
'
B
'
,
 
3
,
 
4
,
 
5
,
 
6
,
 
7
,
 
'
y
u
k
u
 
y
o
'
,
 
'
s
o
 
t
r
a
n
s
i
e
n
t
l
y
'
,
 
'
K
o
t
o
k
o
'
>>> ================================ RESTART ================================
>>> 
1
,
 
2
,
 
'
A
'
,
 
'
B
'
,
 
3
,
 
4
,
 
5
,
 
6
,
 
7
,
 
'
y
u
k
u
 
y
o
'
,
 
'
s
o
 
t
r
a
n
s
i
e
n
t
l
y
'
,
 
'
K
o
t
o
k
o
'
1
>>> ================================ RESTART ================================
>>> 
1
>>> ================================ RESTART ================================
>>> 
1
>>> ================================ RESTART ================================
>>> 
pls work []
1
>>> ================================ RESTART ================================
>>> 
[[], [[], [1], [2]], [[], 'superhard']] ???
pls work []
1
>>> ================================ RESTART ================================
>>> 
[[], [[], [1], [2]], [[], 'superhard']] ???
pls work []
1
>>> ================================ RESTART ================================'
,

'
K
o
t
o
k
o
'
Traceback (most recent call last):
  File "C:/An/Testing/fixing address2.py", line 62, in <module>
    for x in pairdepth2:
NameError: name 'pairdepth2' is not defined
>>> 
[[], [[], [1], [2]], [[], 'superhard']] ???
pls work []
pls work [[], [1], [2]]
pls work [[], 'superhard']
[[], [[], [1], [2]], [[], 'superhard']] ???
pls work []
pls work [[], [1], [2]]
pls work [[], 'superhard']
[[], [[], [1], [2]], [[], 'superhard']] ???
pls work []
pls work [[], [1], [2]]
pls work [[], 'superhard']
[[], [[], [1], [2]], [[], 'superhard']] ???
pls work []
pls work [[], [1], [2]]
pls work [[], 'superhard']
[[], [[], [1], [2]], [[], 'superhard']] ???
pls work []
pls work [[], [1], [2]]
pls work [[], 'superhard']
[[], [[], [1], [2]], [[], 'superhard']] ???
pls work []
pls work [[], [1], [2]]
pls work [[], 'superhard']
[[], [[], [1], [2]], [[], 'superhard']] ???
pls work []
pls work [[], [1], [2]]
pls work [[], 'superhard']
[[], [[], [1], [2]], [[], 'superhard']] ???
pls work []
pls work [[], [1], [2]]
pls work [[], 'superhard']
[[], [[], [1], [2]], [[], 'superhard']] ???
pls work []
pls work [[], [1], [2]]
pls work [[], 'superhard']
[[], [[], [1], [2]], [[], 'superhard']] ???
pls work []
pls work [[], [1], [2]]
pls work [[], 'superhard']
[[], [[], [1], [2]], [[], 'superhard']] ???
pls work []
pls work [[], [1], [2]]
pls work [[], 'superhard']
[[], [[], [1], [2]], [[], 'superhard']] ???
pls work []
pls work [[], [1], [2]]
pls work [[], 'superhard']
[[], [[], [1], [2]], [[], 'superhard']] ???
pls work []
pls work [[], [1], [2]]
pls work [[], 'superhard']
[[], [[], [1], [2]], [[], 'superhard']] ???
pls work []
pls work [[], [1], [2]]
pls work [[], 'superhard']
[[], [[], [1], [2]], [[], 'superhard']] ???
pls work []
pls work [[], [1], [2]]
pls work [[], 'superhard']
[[], [[], [1], [2]], [[], 'superhard']] ???
pls work []
pls work [[], [1], [2]]
pls work [[], 'superhard']
[[], [[], [1], [2]], [[], 'superhard']] ???
pls work []
pls work [[], [1], [2]]
pls work [[], 'superhard']
[[], [[], [1], [2]], [[], 'superhard']] ???
pls work []
pls work [[], [1], [2]]
pls work [[], 'superhard']
[[], [[], [1], [2]], [[], 'superhard']] ???
pls work []
pls work [[], [1], [2]]
pls work [[], 'superhard']
[[], [[], [1], [2]], [[], 'superhard']] ???
pls work []
pls work [[], [1], [2]]
pls work [[], 'superhard']
[[], [[], [1], [2]], [[], 'superhard']] ???
pls work []
pls work [[], [1], [2]]
pls work [[], 'superhard']
[[], [[], [1], [2]], [[], 'superhard']] ???
pls work []
pls work [[], [1], [2]]
pls work [[], 'superhard']
[[], [[], [1], [2]], [[], 'superhard']] ???
pls work []
pls work [[], [1], [2]]
pls work [[], 'superhard']
[[], [[], [1], [2]], [[], 'superhard']] ???
pls work []
pls work [[], [1], [2]]
pls work [[], 'superhard']
[[], [[], [1], [2]], [[], 'superhard']] ???
pls work []
pls work [[], [1], [2]]
pls work [[], 'superhard']
[[], [[], [1], [2]], [[], 'superhard']] ???
pls work []
pls work [[], [1], [2]]
pls work [[], 'superhard']
[[], [[], [1], [2]], [[], 'superhard']] ???
pls work []
pls work [[], [1], [2]]
pls work [[], 'superhard']
[[], [[], [1], [2]], [[], 'superhard']] ???
pls work []
pls work [[], [1], [2]]
pls work [[], 'superhard']
[[], [[], [1], [2]], [[], 'superhard']] ???
pls work []
pls work [[], [1], [2]]
pls work [[], 'superhard']
[[], [[], [1], [2]], [[], 'superhard']] ???
pls work []
pls work [[], [1], [2]]
pls work [[], 'superhard']
[[], [[], [1], [2]], [[], 'superhard']] ???
pls work []
pls work [[], [1], [2]]
pls work [[], 'superhard']
[[], [[], [1], [2]], [[], 'superhard']] ???
pls work []
pls work [[], [1], [2]]
pls work [[], 'superhard']
[[], [[], [1], [2]], [[], 'superhard']] ???
pls work []
pls work [[], [1], [2]]
pls work [[], 'superhard']
[[], [[], [1], [2]], [[], 'superhard']] ???
pls work []
pls work [[], [1], [2]]
pls work [[], 'superhard']
[[], [[], [1], [2]], [[], 'superhard']] ???
pls work []
pls work [[], [1], [2]]
pls work [[], 'superhard']
[[], [[], [1], [2]], [[], 'superhard']] ???
pls work []
pls work [[], [1], [2]]
pls work [[], 'superhard']
[[], [[], [1], [2]], [[], 'superhard']] ???
pls work []
pls work [[], [1], [2]]
pls work [[], 'superhard']
[[], [[], [1], [2]], [[], 'superhard']] ???
pls work []
pls work [[], [1], [2]]
pls work [[], 'superhard']
[[], [[], [1], [2]], [[], 'superhard']] ???
pls work []
pls work [[], [1], [2]]
pls work Traceback (most recent call last):
  File "C:/An/Testing/fixing address2.py", line 85, in <module>
    print(depthtest(pairdepth,1))
  File "C:/An/Testing/fixing address2.py", line 83, in depthtest
    depthtest(string,currentL)
  File "C:/An/Testing/fixing address2.py", line 83, in depthtest
    depthtest(string,currentL)
  File "C:/An/Testing/fixing address2.py", line 83, in depthtest
    depthtest(string,currentL)
  File "C:/An/Testing/fixing address2.py", line 83, in depthtest
    depthtest(string,currentL)
  File "C:/An/Testing/fixing address2.py", line 83, in depthtest
    depthtest(string,currentL)
  File "C:/An/Testing/fixing address2.py", line 83, in depthtest
    depthtest(string,currentL)
  File "C:/An/Testing/fixing address2.py", line 83, in depthtest
    depthtest(string,currentL)
  File "C:/An/Testing/fixing address2.py", line 83, in depthtest
    depthtest(string,currentL)
  File "C:/An/Testing/fixing address2.py", line 83, in depthtest
    depthtest(string,currentL)
  File "C:/An/Testing/fixing address2.py", line 83, in depthtest
    depthtest(string,currentL)
  File "C:/An/Testing/fixing address2.py", line 83, in depthtest
    depthtest(string,currentL)
  File "C:/An/Testing/fixing address2.py", line 83, in depthtest
    depthtest(string,currentL)
  File "C:/An/Testing/fixing address2.py", line 83, in depthtest
    depthtest(string,currentL)
  File "C:/An/Testing/fixing address2.py", line 83, in depthtest
    depthtest(string,currentL)
  File "C:/An/Testing/fixing address2.py", line 83, in depthtest
    depthtest(string,currentL)
  File "C:/An/Testing/fixing address2.py", line 83, in depthtest
    depthtest(string,currentL)
  File "C:/An/Testing/fixing address2.py", line 83, in depthtest
    depthtest(string,currentL)
  File "C:/An/Testing/fixing address2.py", line 83, in depthtest
    depthtest(string,currentL)
  File "C:/An/Testing/fixing address2.py", line 83, in depthtest
    depthtest(string,currentL)
  File "C:/An/Testing/fixing address2.py", line 83, in depthtest
    depthtest(string,currentL)
  File "C:/An/Testing/fixing address2.py", line 83, in depthtest
    depthtest(string,currentL)
  File "C:/An/Testing/fixing address2.py", line 83, in depthtest
    depthtest(string,currentL)
  File "C:/An/Testing/fixing address2.py", line 83, in depthtest
    depthtest(string,currentL)
  File "C:/An/Testing/fixing address2.py", line 83, in depthtest
    depthtest(string,currentL)
  File "C:/An/Testing/fixing address2.py", line 83, in depthtest
    depthtest(string,currentL)
  File "C:/An/Testing/fixing address2.py", line 83, in depthtest
    depthtest(string,currentL)
  File "C:/An/Testing/fixing address2.py", line 83, in depthtest
    depthtest(string,currentL)
  File "C:/An/Testing/fixing address2.py", line 83, in depthtest
    depthtest(string,currentL)
  File "C:/An/Testing/fixing address2.py", line 83, in depthtest
    depthtest(string,currentL)
  File "C:/An/Testing/fixing address2.py", line 83, in depthtest
    depthtest(string,currentL)
  File "C:/An/Testing/fixing address2.py", line 83, in depthtest
    depthtest(string,currentL)
  File "C:/An/Testing/fixing address2.py", line 83, in depthtest
    depthtest(string,currentL)
  File "C:/An/Testing/fixing address2.py", line 83, in depthtest
    depthtest(string,currentL)
  File "C:/An/Testing/fixing address2.py", line 83, in depthtest
    depthtest(string,currentL)
  File "C:/An/Testing/fixing address2.py", line 83, in depthtest
    depthtest(string,currentL)
  File "C:/An/Testing/fixing address2.py", line 83, in depthtest
    depthtest(string,currentL)
  File "C:/An/Testing/fixing address2.py", line 83, in depthtest
    depthtest(string,currentL)
  File "C:/An/Testing/fixing address2.py", line 83, in depthtest
    depthtest(string,currentL)
  File "C:/An/Testing/fixing address2.py", line 80, in depthtest
    print("pls work",x)
  File "C:\Personalize\Python\lib\idlelib\PyShell.py", line 1347, in write
    return self.shell.write(s, self.tags)
KeyboardInterrupt
>>> 
KeyboardInterrupt
>>> ================================ RESTART ================================
>>> 
[[], [[], [1], [2]], [[], 'superhard']] ???
pls work []
1
>>> ================================ RESTART ================================
>>> 
[[], [[], [1], [2]], [[], 'superhard']] ???
pls work []
pls work [[], [1], [2]]
[[], [1], [2]] changed our minds about L =  1
[[], [[], [1], [2]], [[], 'superhard']] ???
pls work []
pls work [[], [1], [2]]
[[], [1], [2]] changed our minds about L =  2
[[], [[], [1], [2]], [[], 'superhard']] ???
pls work []
pls work [[], [1], [2]]
[[], [1], [2]] changed our minds about L =  3
[[], [[], [1], [2]], [[], 'superhard']] ???
pls work []
pls work [[], [1], [2]]
[[], [1], [2]] changed our minds about L =  4
[[], [[], [1], [2]], [[], 'superhard']] ???
pls work []
pls work [[], [1], [2]]
[[], [1], [2]] changed our minds about L =  5
[[], [[], [1], [2]], [[], 'superhard']] ???
pls work []
pls work [[], [1], [2]]
[[], [1], [2]] changed our minds about L =  6
[[], [[], [1], [2]], [[], 'superhard']] ???
pls work []
pls work [[], [1], [2]]
[[], [1], [2]] changed our minds about L =  7
[[], [[], [1], [2]], [[], 'superhard']] ???
pls work []
pls work [[], [1], [2]]
[[], [1], [2]] changed our minds about L =  8
[[], [[], [1], [2]], [[], 'superhard']] ???
pls work []
pls work [[], [1], [2]]
[[], [1], [2]] changed our minds about L =  9
[[], [[], [1], [2]], [[], 'superhard']] ???
pls work []
pls work [[], [1], [2]]
[[], [1], [2]] changed our minds about L =  10
[[], [[], [1], [2]], [[], 'superhard']] ???
pls work []
pls work [[], [1], [2]]
[[], [1], [2]] changed our minds about L =  11
[[], [[], [1], [2]], [[], 'superhard']] ???
pls work []
pls work [[], [1], [2]]
[[], [1], [2]] changed our minds about L =  12
[[], [[], [1], [2]], [[], 'superhard']] ???
pls work []
pls work [[], [1], [2]]
[[], [1], [2]] changed our minds about L =  13
[[], [[], [1], [2]], [[], 'superhard']] ???
pls work []
pls work [[], [1], [2]]
[[], [1], [2]] changed our minds about L =  14
[[], [[], [1], [2]], [[], 'superhard']] ???
pls work []
pls work [[], [1], [2]]
[[], [1], [2]] changed our minds about L =  15
[[], [[], [1], [2]], [[], 'superhard']] ???
pls work []
pls work [[], [1], [2]]
[[], [1], [2]] changed our minds about L =  16
[[], [[], [1], [2]], [[], 'superhard']] ???
pls work []
pls work [[], [1], [2]]
[[], [1], [2]] changed our minds about L =  17
[[], [[], [1], [2]], [[], 'superhard']] ???
pls work []
pls work [[], [1], [2]]
[[], [1], [2]] changed our minds about L =  18
[[], [[], [1], [2]], [[], 'superhard']] ???
pls work []
pls work [[], [1], [2]]
[[], [1], [2]] changed our minds about L =  19
[[], [[], [1], [2]], [[], 'superhard']] ???
pls work []
pls work [[], [1], [2]]
[[], [1], [2]] changed our minds about L =  20
[[], [[], [1], [2]], [[], 'superhard']] ???
pls work []
pls work [[], [1], [2]]
[[], [1], [2]] changed our minds about L =  21
[[], [[], [1], [2]], [[], 'superhard']] ???
pls work []
pls work [[], [1], [2]]
[[], [1], [2]] changed our minds about L =  22
[[], [[], [1], [2]], [[], 'superhard']] ???
pls work []
pls work [[], [1], [2]]
[[], [1], [2]] changed our minds about L =  23
[[], [[], [1], [2]], [[], 'superhard']] ???
pls work []
pls work [[], [1], [2]]
[[], [1], [2]] changed our minds about L =  24
[[], [[], [1], [2]], [[], 'superhard']] ???
pls work []
pls work [[], [1], [2]]
[[], [1], [2]] changed our minds about L =  25
[[], [[], [1], [2]], [[], 'superhard']] ???
pls work []
pls work [[], [1], [2]]
[[], [1], [2]] changed our minds about L =  26
[[], [[], [1], [2]], [[], 'superhard']] ???
pls work []
pls work [[], [1], [2]]
[[], [1], [2]] changed our minds about L =  27
[[], [[], [1], [2]], [[], 'superhard']] ???
pls work []
pls work [[], [1], [2]]
[[], [1], [2]] changed our minds about L =  28
[[], [[], [1], [2]], [[], 'superhard']] ???
pls work []
pls work [[], [1], [2]]
[[], [1], [2]] changed our minds about L =  29
[[], [[], [1], [2]], [[], 'superhard']] ???
pls work []
pls work [[], [1], [2]]
[[], [1], [2]] changed our minds about L =  30
[[], [[], [1], [2]], [[], 'superhard']] ???
pls work []
pls work [[], [1], [2]]
[[], [1], [2]] changed our minds about L =  31
[[], [[], [1], [2]], [[], 'superhard']] ???
pls work []
pls work [[], [1], [2]]
[[], [1], [2]] changed our minds about L =  32
[[], [[], [1], [2]], [[], 'superhard']] ???
pls work []
pls work [[], [1], [2]]
[[], [1], [2]] changed our minds about L =  33
[[], [[], [1], [2]], [[], 'superhard']] ???
pls work []
pls work [[], [1], [2]]
[[], [1], [2]] changed our minds about L =  34
[[], [[], [1], [2]], [[], 'superhard']] ???
pls work []
pls work [[], [1], [2]]
[[], [1], [2]] changed our minds about L =  35
[[], [[], [1], [2]], [[], 'superhard']] ???
pls work []
pls work [[], [1], [2]]
[[], [1], [2]] changed our minds about L =  36
[[], [[], [1], [2]], [[], 'superhard']] ???
pls work []
pls work [[], [1], [2]]
[[], [1], [2]] changed our minds about L =  37
[[], [[], [1], [2]], [[], 'superhard']] ???
pls work []
pls work [[], [1], [2]]
[[], [1], [2]] changed our minds about L =  38
[[], [[], [1], [2]], [[], 'superhard']] ???
pls work []
pls work [[], [1], [2]]
[[], [1], [2]] changed our minds about L =  39
[[], [[], [1], [2]], [[], 'superhard']] ???
pls work []
pls work [[], [1], [2]]
[[], [1], [2]] changed our minds about L =  40
[[], [[], [1], [2]], [[], 'superhard']] ???
pls work []
pls work [[], [1], [2]]
[[], [1], [2]] changed our minds about L =  41
[[], [[], [1], [2]], [[], 'superhard']] ???
pls work []
pls work [[], [1], [2]]
[[], [1], [2]] changed our minds about L =  42
[[], [[], [1], [2]], [[], 'superhard']] ???
pls work []
pls work [[], [1], [2]]
[[], [1], [2]] changed our minds about L =  43
[[], [[], [1], [2]], [[], 'superhard']] ???
pls work []
pls work [[], [1], [2]]
[[], [1], [2]] changed our minds about L =  44
[[], [[], [1], [2]], [[], 'superhard']] ???
pls work []
pls work [[], [1], [2]]
[[], [1], [2]] changed our minds about L =  45
[[], [[], [1], [2]], [[], 'superhard']] ???
pls work []
pls work [[], [1], [2]]
[[], [1], [2]] changed our minds about L =  46
[[], [[], [1], [2]], [[], 'superhard']] ???
pls work []
pls work [[], [1], [2]]
[[], [1], [2]] changed our minds about L =  47
[[], [[], [1], [2]], [[], 'superhard']] ???
pls work []
pls work [[], [1], [2]]
[[], [1], [2]] changed our minds about L =  48
[[], [[], [1], [2]], [[], 'superhard']] ???
pls work []
pls work [[], [1], [2]]
[[], [1], [2]] changed our minds about L =  49
[[], [[], [1], [2]], [[], 'superhard']] ???Traceback (most recent call last):
  File "C:/An/Testing/fixing address2.py", line 91, in <module>
    print(depthtest(pairdepth,1))
  File "C:/An/Testing/fixing address2.py", line 89, in depthtest
    depthtest(string,currentL)
  File "C:/An/Testing/fixing address2.py", line 89, in depthtest
    depthtest(string,currentL)
  File "C:/An/Testing/fixing address2.py", line 89, in depthtest
    depthtest(string,currentL)
  File "C:/An/Testing/fixing address2.py", line 89, in depthtest
    depthtest(string,currentL)
  File "C:/An/Testing/fixing address2.py", line 89, in depthtest
    depthtest(string,currentL)
  File "C:/An/Testing/fixing address2.py", line 89, in depthtest
    depthtest(string,currentL)
  File "C:/An/Testing/fixing address2.py", line 89, in depthtest
    depthtest(string,currentL)
  File "C:/An/Testing/fixing address2.py", line 89, in depthtest
    depthtest(string,currentL)
  File "C:/An/Testing/fixing address2.py", line 89, in depthtest
    depthtest(string,currentL)
  File "C:/An/Testing/fixing address2.py", line 89, in depthtest
    depthtest(string,currentL)
  File "C:/An/Testing/fixing address2.py", line 89, in depthtest
    depthtest(string,currentL)
  File "C:/An/Testing/fixing address2.py", line 89, in depthtest
    depthtest(string,currentL)
  File "C:/An/Testing/fixing address2.py", line 89, in depthtest
    depthtest(string,currentL)
  File "C:/An/Testing/fixing address2.py", line 89, in depthtest
    depthtest(string,currentL)
  File "C:/An/Testing/fixing address2.py", line 89, in depthtest
    depthtest(string,currentL)
  File "C:/An/Testing/fixing address2.py", line 89, in depthtest
    depthtest(string,currentL)
  File "C:/An/Testing/fixing address2.py", line 89, in depthtest
    depthtest(string,currentL)
  File "C:/An/Testing/fixing address2.py", line 89, in depthtest
    depthtest(string,currentL)
  File "C:/An/Testing/fixing address2.py", line 89, in depthtest
    depthtest(string,currentL)
  File "C:/An/Testing/fixing address2.py", line 89, in depthtest
    depthtest(string,currentL)
  File "C:/An/Testing/fixing address2.py", line 89, in depthtest
    depthtest(string,currentL)
  File "C:/An/Testing/fixing address2.py", line 89, in depthtest
    depthtest(string,currentL)
  File "C:/An/Testing/fixing address2.py", line 89, in depthtest
    depthtest(string,currentL)
  File "C:/An/Testing/fixing address2.py", line 89, in depthtest
    depthtest(string,currentL)
  File "C:/An/Testing/fixing address2.py", line 89, in depthtest
    depthtest(string,currentL)
  File "C:/An/Testing/fixing address2.py", line 89, in depthtest
    depthtest(string,currentL)
  File "C:/An/Testing/fixing address2.py", line 89, in depthtest
    depthtest(string,currentL)
  File "C:/An/Testing/fixing address2.py", line 89, in depthtest
    depthtest(string,currentL)
  File "C:/An/Testing/fixing address2.py", line 89, in depthtest
    depthtest(string,currentL)
  File "C:/An/Testing/fixing address2.py", line 89, in depthtest
    depthtest(string,currentL)
  File "C:/An/Testing/fixing address2.py", line 89, in depthtest
    depthtest(string,currentL)
  File "C:/An/Testing/fixing address2.py", line 89, in depthtest
    depthtest(string,currentL)
  File "C:/An/Testing/fixing address2.py", line 89, in depthtest
    depthtest(string,currentL)
  File "C:/An/Testing/fixing address2.py", line 89, in depthtest
    depthtest(string,currentL)
  File "C:/An/Testing/fixing address2.py", line 89, in depthtest
    depthtest(string,currentL)
  File "C:/An/Testing/fixing address2.py", line 89, in depthtest
    depthtest(string,currentL)
  File "C:/An/Testing/fixing address2.py", line 89, in depthtest
    depthtest(string,currentL)
  File "C:/An/Testing/fixing address2.py", line 89, in depthtest
    depthtest(string,currentL)
  File "C:/An/Testing/fixing address2.py", line 89, in depthtest
    depthtest(string,currentL)
  File "C:/An/Testing/fixing address2.py", line 89, in depthtest
    depthtest(string,currentL)
  File "C:/An/Testing/fixing address2.py", line 89, in depthtest
    depthtest(string,currentL)
  File "C:/An/Testing/fixing address2.py", line 89, in depthtest
    depthtest(string,currentL)
  File "C:/An/Testing/fixing address2.py", line 89, in depthtest
    depthtest(string,currentL)
  File "C:/An/Testing/fixing address2.py", line 89, in depthtest
    depthtest(string,currentL)
  File "C:/An/Testing/fixing address2.py", line 89, in depthtest
    depthtest(string,currentL)
  File "C:/An/Testing/fixing address2.py", line 89, in depthtest
    depthtest(string,currentL)
  File "C:/An/Testing/fixing address2.py", line 89, in depthtest
    depthtest(string,currentL)
  File "C:/An/Testing/fixing address2.py", line 89, in depthtest
    depthtest(string,currentL)
  File "C:/An/Testing/fixing address2.py", line 89, in depthtest
    depthtest(string,currentL)
  File "C:/An/Testing/fixing address2.py", line 77, in depthtest
    print(string, "???")
  File "C:\Personalize\Python\lib\idlelib\PyShell.py", line 1347, in write
    return self.shell.write(s, self.tags)
KeyboardInterrupt
>>> ================================ RESTART ================================
>>> 
None
>>> ================================ RESTART ================================
>>> 
[[1, 1], [2, 1], [3, 1]]
>>> ================================ RESTART ================================
>>> 
[[1, 1], [2, 1], [3, 1]]
>>> ================================ RESTART ================================
>>> 
[[1, 1], [2, 1], [3, 1]] [[], [[], [1], [2]], [[], 'superhard']]
>>> ================================ RESTART ================================
>>> 
[[1, 1], [2, 1], [3, 1]] 
 [[], [[], [1], [2]], [[], 'superhard']]
>>> ================================ RESTART ================================
>>> 
[[1, 2], [2, 3], [3, 2], [4, 2], [5, 2], [6, 3], [7, 4], [8, 3], [9, 3], [10, 3], [11, 4], [12, 4], [13, 3], [14, 3], [15, 3], [16, 4], [17, 4], [18, 3], [19, 2], [20, 2], [21, 2], [22, 3], [23, 4], [24, 3], [25, 3], [26, 3], [27, 3], [28, 3], [29, 3], [30, 3], [31, 3], [32, 3], [33, 3], [34, 3], [35, 3], [36, 3], [37, 3], [38, 2], [39, 1]] 
 [[], [[], [1], [2]], [[], 'superhard']]
>>> ================================ RESTART ================================
>>> 
[[1, 1], [2, 2], [3, 1], [4, 1], [5, 1], [6, 2], [7, 3], [8, 2], [9, 2], [10, 2], [11, 3], [12, 3], [13, 2], [14, 2], [15, 2], [16, 3], [17, 3], [18, 2], [19, 1], [20, 1], [21, 1], [22, 2], [23, 3], [24, 2], [25, 2], [26, 2], [27, 2], [28, 2], [29, 2], [30, 2], [31, 2], [32, 2], [33, 2], [34, 2], [35, 2], [36, 2], [37, 2], [38, 1], [39, 0]] 
 [[], [[], [1], [2]], [[], 'superhard']]
>>> ================================ RESTART ================================
>>> 
[[], [[], [1], [2]], [[], 'superhard']]
>>> ================================ RESTART ================================
>>> 
[[], [[], [1], [2]], [[], 'superhard']]
>>> ================================ RESTART ================================
>>> 
[[1, 1], [2, 2], [3, 1], [6, 2], [7, 3], [8, 2], [11, 3], [13, 2], [16, 3], [18, 2], [19, 1], [22, 2], [23, 3], [24, 2], [38, 1], [39, 0]] 
 [[], [[], [1], [2]], [[], 'superhard']]
>>> ================================ RESTART ================================
>>> 
3 
 [[], [[], [1], [2]], [[], 'superhard']]
>>> ================================ RESTART ================================
>>> 
1 
 [[], [[], [1], [2]], [[], 'superhard']]
>>> ================================ RESTART ================================
>>> 
3
>>> ================================ RESTART ================================
>>> 
4
>>> ================================ RESTART ================================
>>> 
>>> ================================ RESTART ================================
>>> 
i is missing 1
char is missing 1
i is missing 2
char is missing ,
i is missing 3
char is missing  
i is missing 4
char is missing 2
i is missing 5
char is missing ,
i is missing 6
char is missing  
i is missing 7
char is missing '
i is missing 8
i is missing 9
char is missing '
i is missing 10
char is missing ,
i is missing 11
char is missing  
i is missing 12
char is missing '
i is missing 13
i is missing 14
char is missing '
i is missing 15
char is missing ,
i is missing 16
char is missing  
i is missing 17
char is missing 3
i is missing 18
char is missing ,
i is missing 19
char is missing  
i is missing 20
char is missing 4
i is missing 21
char is missing ,
i is missing 22
char is missing  
i is missing 23
char is missing 5
i is missing 24
char is missing ,
i is missing 25
char is missing  
i is missing 26
char is missing 6
i is missing 27
char is missing ,
i is missing 28
char is missing  
i is missing 29
char is missing 7
i is missing 30
char is missing ,
i is missing 31
char is missing  
i is missing 32
char is missing '
i is missing 33
i is missing 34
i is missing 35
i is missing 36
i is missing 37
char is missing  
i is missing 38
i is missing 39
i is missing 40
char is missing '
i is missing 41
char is missing ,
i is missing 42
char is missing  
i is missing 43
char is missing '
i is missing 44
i is missing 45
i is missing 46
char is missing  
i is missing 47
i is missing 48
i is missing 49
i is missing 50
i is missing 51
i is missing 52
i is missing 53
i is missing 54
i is missing 55
i is missing 56
i is missing 57
i is missing 58
char is missing '
i is missing 59
char is missing ,
i is missing 60
char is missing  
i is missing 61
char is missing '
i is missing 62
char is missing K
i is missing 63
i is missing 64
i is missing 65
i is missing 66
i is missing 67
i is missing 68
char is missing '
[[[[1, 2, 'A', 'B', 3, 4, 5, 6, 7, 'y', 'u', 'k', 'o', 's', 't', 'r', 'a', 'n', 'i', 'e', 'n', 'l'], 0, []], [[1, '1'], [2, ','], [3, ' '], [4, '2'], [5, ','], [6, ' '], [7, "'"], [8, 'A'], [9, "'"], [10, ','], [11, ' '], [12, "'"], [13, 'B'], [14, "'"], [15, ','], [16, ' '], [17, '3'], [18, ','], [19, ' '], [20, '4'], [21, ','], [22, ' '], [23, '5'], [24, ','], [25, ' '], [26, '6'], [27, ','], [28, ' '], [29, '7'], [30, ','], [31, ' '], [32, "'"], [33, 'y'], [34, 'u'], [35, 'k'], [36, 'u'], [37, ' '], [38, 'y'], [39, 'o'], [40, "'"], [41, ','], [42, ' '], [43, "'"], [44, 's'], [45, 'o'], [46, ' '], [47, 't'], [48, 'r'], [49, 'a'], [50, 'n'], [51, 's'], [52, 'i'], [53, 'e'], [54, 'n'], [55, 't'], [56, 'l'], [57, 'y'], [58, "'"], [59, ','], [60, ' '], [61, "'"], [62, 'K'], [63, 'o'], [64, 't'], [65, 'o'], [66, 'k'], [67, 'o'], [68, "'"]]]]
>>> ================================ RESTART ================================
>>> 
char is missing  
char is missing  
char is missing '
char is missing '
char is missing  
char is missing '
char is missing '
char is missing  
char is missing  
char is missing  
char is missing  
char is missing  
char is missing  
char is missing '
char is missing  
char is missing '
char is missing  
char is missing '
char is missing  
char is missing '
char is missing  
char is missing '
char is missing K
char is missing '
[[[['1', '2', 'A', 'B', '3', '4', '5', '6', '7', 'y', 'u', 'k', 'o', 's', 't', 'r', 'a', 'n', 'i', 'e', 'n', 'l', ','], 0, [0.0, 298.0, 22.0, 428.0]], [[3, ' '], [6, ' '], [7, "'"], [8, 'A'], [9, "'"], [10, ','], [11, ' '], [12, "'"], [13, 'B'], [14, "'"], [15, ','], [16, ' '], [17, '3'], [18, ','], [19, ' '], [20, '4'], [21, ','], [22, ' '], [23, '5'], [24, ','], [25, ' '], [26, '6'], [27, ','], [28, ' '], [29, '7'], [30, ','], [31, ' '], [32, "'"], [33, 'y'], [34, 'u'], [35, 'k'], [36, 'u'], [37, ' '], [38, 'y'], [39, 'o'], [40, "'"], [41, ','], [42, ' '], [43, "'"], [44, 's'], [45, 'o'], [46, ' '], [47, 't'], [48, 'r'], [49, 'a'], [50, 'n'], [51, 's'], [52, 'i'], [53, 'e'], [54, 'n'], [55, 't'], [56, 'l'], [57, 'y'], [58, "'"], [59, ','], [60, ' '], [61, "'"], [62, 'K'], [63, 'o'], [64, 't'], [65, 'o'], [66, 'k'], [67, 'o'], [68, "'"]]]]
>>> ================================ RESTART ================================
>>> 
-===== 1, 2, 'A', 'B', 3, 4, 5, 6, 7, 'yuku yo', 'so transiently', 'Kotoko'
char is missing  
char is missing  
char is missing '
char is missing '
char is missing  
char is missing '
char is missing '
char is missing  
char is missing  
char is missing  
char is missing  
char is missing  
char is missing  
char is missing '
char is missing  
char is missing '
char is missing  
char is missing '
char is missing  
char is missing '
char is missing  
char is missing '
char is missing K
char is missing '
[[[['1', '2', 'A', 'B', '3', '4', '5', '6', '7', 'y', 'u', 'k', 'o', 's', 't', 'r', 'a', 'n', 'i', 'e', 'n', 'l', ','], 0, [0.0, 298.0, 22.0, 428.0]], [[3, ' '], [6, ' '], [7, "'"], [8, 'A'], [9, "'"], [10, ','], [11, ' '], [12, "'"], [13, 'B'], [14, "'"], [15, ','], [16, ' '], [17, '3'], [18, ','], [19, ' '], [20, '4'], [21, ','], [22, ' '], [23, '5'], [24, ','], [25, ' '], [26, '6'], [27, ','], [28, ' '], [29, '7'], [30, ','], [31, ' '], [32, "'"], [33, 'y'], [34, 'u'], [35, 'k'], [36, 'u'], [37, ' '], [38, 'y'], [39, 'o'], [40, "'"], [41, ','], [42, ' '], [43, "'"], [44, 's'], [45, 'o'], [46, ' '], [47, 't'], [48, 'r'], [49, 'a'], [50, 'n'], [51, 's'], [52, 'i'], [53, 'e'], [54, 'n'], [55, 't'], [56, 'l'], [57, 'y'], [58, "'"], [59, ','], [60, ' '], [61, "'"], [62, 'K'], [63, 'o'], [64, 't'], [65, 'o'], [66, 'k'], [67, 'o'], [68, "'"]]]]
>>> ================================ RESTART ================================
>>> 
-===== 1, 2, 'A', 'B', 3, 4, 5, 6, 7, 'yuku yo', 'so transiently', 'Kotoko'
char is missing  
char is missing  
char is missing  
char is missing  
char is missing  
char is missing  
char is missing  
char is missing  
char is missing  
char is missing  
char is missing  
char is missing  
char is missing  
char is missing K
[[[['1', '2', 'A', 'B', '3', '4', '5', '6', '7', 'y', 'u', 'k', 'o', 's', 't', 'r', 'a', 'n', 'i', 'e', 'n', 'l', ',', "'"], 0, [0.0, 298.0, 22.0, 428.0, 519.0]], [[3, ' '], [6, ' '], [8, 'A'], [9, "'"], [10, ','], [11, ' '], [12, "'"], [13, 'B'], [14, "'"], [15, ','], [16, ' '], [17, '3'], [18, ','], [19, ' '], [20, '4'], [21, ','], [22, ' '], [23, '5'], [24, ','], [25, ' '], [26, '6'], [27, ','], [28, ' '], [29, '7'], [30, ','], [31, ' '], [32, "'"], [33, 'y'], [34, 'u'], [35, 'k'], [36, 'u'], [37, ' '], [38, 'y'], [39, 'o'], [40, "'"], [41, ','], [42, ' '], [43, "'"], [44, 's'], [45, 'o'], [46, ' '], [47, 't'], [48, 'r'], [49, 'a'], [50, 'n'], [51, 's'], [52, 'i'], [53, 'e'], [54, 'n'], [55, 't'], [56, 'l'], [57, 'y'], [58, "'"], [59, ','], [60, ' '], [61, "'"], [62, 'K'], [63, 'o'], [64, 't'], [65, 'o'], [66, 'k'], [67, 'o'], [68, "'"]]]]
>>> ================================ RESTART ================================
>>> 
0
0
1
2
3
4
1
0
1
2
3
4
2
0
1
2
3
4
3
0
1
2
3
4
4
0
1
2
3
4
>>> ================================ RESTART ================================
>>> 
0 0
0 1
0 2
0 3
0 4
1 0
1 1
1 2
1 3
1 4
2 0
2 1
2 2
2 3
2 4
3 0
3 1
3 2
3 3
3 4
4 0
4 1
4 2
4 3
4 4
>>> ================================ RESTART ================================
>>> 
0000
1000
0100
1100
0010
1010
0110
1110
0001
1001
0101
1101
0011
1011
0111
1111
>>> ================================ RESTART ================================
>>> 
()
('1',)
('2',)
('1', '2')
0
1
01
11
001
101
011
111
0001
1001
0101
1101
0011
1011
0111
1111
>>> ================================ RESTART ================================
>>> 
>>> 
()
('1',)
('2',)
('1', '2')
0000
1000
0100
1100
0010
1010
0110
1110
0001
1001
0101
1101
0011
1011
0111
1111
>>> ================================ RESTART ================================
>>> 
1
>>> ================================ RESTART ================================
>>> 
00000001
>>> ================================ RESTART ================================
>>> 
1 0
2 0
3 0
4 0
5 0
6 0
7 0
8 1
>>> ================================ RESTART ================================
>>> 
>>> ================================ RESTART ================================
>>> 
wtf man 0
wtf man 0
wtf man 0
wtf man 0
wtf man 0
wtf man 0
wtf man 0
wtf man 1
>>> ================================ RESTART ================================
>>> 
wtf man 0
wtf man 0
wtf man 0
wtf man 0
wtf man 0
wtf man 0
wtf man 0
wtf man 1
yes at 8
>>> ================================ RESTART ================================
>>> 
Traceback (most recent call last):
  File "C:/An/Delta Func/autocomposer.py", line 112, in <module>
    AutoVision(128,1)
  File "C:/An/Delta Func/autocomposer.py", line 106, in AutoVision
    w = floor((sqrt(8*z+1)-1)/2)
NameError: name 'floor' is not defined
>>> ================================ RESTART ================================
>>> 
>>> ================================ RESTART ================================
>>> 
[[7.0, 8.0]]
>>> ================================ RESTART ================================
>>> 
[]
>>> ================================ RESTART ================================
>>> 
wtf?
wtf?
wtf?
wtf?
wtf?
wtf?
wtf?
wtf?
[]
>>> ================================ RESTART ================================
>>> 
yes at 0
[]
>>> ================================ RESTART ================================
>>> 
yes at 0
[]
>>> ================================ RESTART ================================
>>> 
yes at 0
[]
>>> ================================ RESTART ================================
>>> 
bin is 00000001
bin is 00000001
bin is 00000001
bin is 00000001
bin is 00000001
bin is 00000001
bin is 00000001
bin is 00000001
yes at 0
[]
>>> ================================ RESTART ================================
>>> 
bin is 00000001 0
bin is 00000001 0
bin is 00000001 0
bin is 00000001 0
bin is 00000001 0
bin is 00000001 0
bin is 00000001 0
bin is 00000001 1
yes at 0
[]
>>> ================================ RESTART ================================
>>> 
bin is 00000001 0 False True
bin is 00000001 0 False True
bin is 00000001 0 False True
bin is 00000001 0 False True
bin is 00000001 0 False True
bin is 00000001 0 False True
bin is 00000001 0 False True
bin is 00000001 1 False False
yes at 0
[]
>>> ================================ RESTART ================================
>>> 
bin is 00000001 0 False True
bin is 00000001 0 False True
bin is 00000001 0 False True
bin is 00000001 0 False True
bin is 00000001 0 False True
bin is 00000001 0 False True
bin is 00000001 0 False True
bin is 00000001 1 False False
yes at 7
[]
>>> ================================ RESTART ================================
>>> 
yes at 7
[[[2.0, 1.0]]]
>>> ================================ RESTART ================================
>>> 
[[2.0, 0.0]]
>>> ================================ RESTART ================================
>>> 
()
((),)
(([1, 1],),)
((), ([1, 1],))
>>> ================================ RESTART ================================
>>> 
()
((),)
(([0, 0],),)
(([0, 1],),)
(([1, 0],),)
(([2, 0],),)
(([0, 0], [0, 1]),)
(([0, 0], [1, 0]),)
(([0, 0], [2, 0]),)
(([0, 1], [1, 0]),)
(([0, 1], [2, 0]),)
(([1, 0], [2, 0]),)
(([0, 0], [0, 1], [1, 0]),)
(([0, 0], [0, 1], [2, 0]),)
(([0, 0], [1, 0], [2, 0]),)
(([0, 1], [1, 0], [2, 0]),)
(([0, 0], [0, 1], [1, 0], [2, 0]),)
((), ([0, 0],))
((), ([0, 1],))
((), ([1, 0],))
((), ([2, 0],))
((), ([0, 0], [0, 1]))
((), ([0, 0], [1, 0]))
((), ([0, 0], [2, 0]))
((), ([0, 1], [1, 0]))
((), ([0, 1], [2, 0]))
((), ([1, 0], [2, 0]))
((), ([0, 0], [0, 1], [1, 0]))
((), ([0, 0], [0, 1], [2, 0]))
((), ([0, 0], [1, 0], [2, 0]))
((), ([0, 1], [1, 0], [2, 0]))
((), ([0, 0], [0, 1], [1, 0], [2, 0]))
(([0, 0],), ([0, 1],))
(([0, 0],), ([1, 0],))
(([0, 0],), ([2, 0],))
(([0, 0],), ([0, 0], [0, 1]))
(([0, 0],), ([0, 0], [1, 0]))
(([0, 0],), ([0, 0], [2, 0]))
(([0, 0],), ([0, 1], [1, 0]))
(([0, 0],), ([0, 1], [2, 0]))
(([0, 0],), ([1, 0], [2, 0]))
(([0, 0],), ([0, 0], [0, 1], [1, 0]))
(([0, 0],), ([0, 0], [0, 1], [2, 0]))
(([0, 0],), ([0, 0], [1, 0], [2, 0]))
(([0, 0],), ([0, 1], [1, 0], [2, 0]))
(([0, 0],), ([0, 0], [0, 1], [1, 0], [2, 0]))
(([0, 1],), ([1, 0],))
(([0, 1],), ([2, 0],))
(([0, 1],), ([0, 0], [0, 1]))
(([0, 1],), ([0, 0], [1, 0]))
(([0, 1],), ([0, 0], [2, 0]))
(([0, 1],), ([0, 1], [1, 0]))
(([0, 1],), ([0, 1], [2, 0]))
(([0, 1],), ([1, 0], [2, 0]))
(([0, 1],), ([0, 0], [0, 1], [1, 0]))
(([0, 1],), ([0, 0], [0, 1], [2, 0]))
(([0, 1],), ([0, 0], [1, 0], [2, 0]))
(([0, 1],), ([0, 1], [1, 0], [2, 0]))
(([0, 1],), ([0, 0], [0, 1], [1, 0], [2, 0]))
(([1, 0],), ([2, 0],))
(([1, 0],), ([0, 0], [0, 1]))
(([1, 0],), ([0, 0], [1, 0]))
(([1, 0],), ([0, 0], [2, 0]))
(([1, 0],), ([0, 1], [1, 0]))
(([1, 0],), ([0, 1], [2, 0]))
(([1, 0],), ([1, 0], [2, 0]))
(([1, 0],), ([0, 0], [0, 1], [1, 0]))
(([1, 0],), ([0, 0], [0, 1], [2, 0]))
(([1, 0],), ([0, 0], [1, 0], [2, 0]))
(([1, 0],), ([0, 1], [1, 0], [2, 0]))
(([1, 0],), ([0, 0], [0, 1], [1, 0], [2, 0]))
(([2, 0],), ([0, 0], [0, 1]))
(([2, 0],), ([0, 0], [1, 0]))
(([2, 0],), ([0, 0], [2, 0]))
(([2, 0],), ([0, 1], [1, 0]))
(([2, 0],), ([0, 1], [2, 0]))
(([2, 0],), ([1, 0], [2, 0]))
(([2, 0],), ([0, 0], [0, 1], [1, 0]))
(([2, 0],), ([0, 0], [0, 1], [2, 0]))
(([2, 0],), ([0, 0], [1, 0], [2, 0]))
(([2, 0],), ([0, 1], [1, 0], [2, 0]))
(([2, 0],), ([0, 0], [0, 1], [1, 0], [2, 0]))
(([0, 0], [0, 1]), ([0, 0], [1, 0]))
(([0, 0], [0, 1]), ([0, 0], [2, 0]))
(([0, 0], [0, 1]), ([0, 1], [1, 0]))
(([0, 0], [0, 1]), ([0, 1], [2, 0]))
(([0, 0], [0, 1]), ([1, 0], [2, 0]))
(([0, 0], [0, 1]), ([0, 0], [0, 1], [1, 0]))
(([0, 0], [0, 1]), ([0, 0], [0, 1], [2, 0]))
(([0, 0], [0, 1]), ([0, 0], [1, 0], [2, 0]))
(([0, 0], [0, 1]), ([0, 1], [1, 0], [2, 0]))
(([0, 0], [0, 1]), ([0, 0], [0, 1], [1, 0], [2, 0]))
(([0, 0], [1, 0]), ([0, 0], [2, 0]))
(([0, 0], [1, 0]), ([0, 1], [1, 0]))
(([0, 0], [1, 0]), ([0, 1], [2, 0]))
(([0, 0], [1, 0]), ([1, 0], [2, 0]))
(([0, 0], [1, 0]), ([0, 0], [0, 1], [1, 0]))
(([0, 0], [1, 0]), ([0, 0], [0, 1], [2, 0]))
(([0, 0], [1, 0]), ([0, 0], [1, 0], [2, 0]))
(([0, 0], [1, 0]), ([0, 1], [1, 0], [2, 0]))
(([0, 0], [1, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
(([0, 0], [2, 0]), ([0, 1], [1, 0]))
(([0, 0], [2, 0]), ([0, 1], [2, 0]))
(([0, 0], [2, 0]), ([1, 0], [2, 0]))
(([0, 0], [2, 0]), ([0, 0], [0, 1], [1, 0]))
(([0, 0], [2, 0]), ([0, 0], [0, 1], [2, 0]))
(([0, 0], [2, 0]), ([0, 0], [1, 0], [2, 0]))
(([0, 0], [2, 0]), ([0, 1], [1, 0], [2, 0]))
(([0, 0], [2, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
(([0, 1], [1, 0]), ([0, 1], [2, 0]))
(([0, 1], [1, 0]), ([1, 0], [2, 0]))
(([0, 1], [1, 0]), ([0, 0], [0, 1], [1, 0]))
(([0, 1], [1, 0]), ([0, 0], [0, 1], [2, 0]))
(([0, 1], [1, 0]), ([0, 0], [1, 0], [2, 0]))
(([0, 1], [1, 0]), ([0, 1], [1, 0], [2, 0]))
(([0, 1], [1, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
(([0, 1], [2, 0]), ([1, 0], [2, 0]))
(([0, 1], [2, 0]), ([0, 0], [0, 1], [1, 0]))
(([0, 1], [2, 0]), ([0, 0], [0, 1], [2, 0]))
(([0, 1], [2, 0]), ([0, 0], [1, 0], [2, 0]))
(([0, 1], [2, 0]), ([0, 1], [1, 0], [2, 0]))
(([0, 1], [2, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
(([1, 0], [2, 0]), ([0, 0], [0, 1], [1, 0]))
(([1, 0], [2, 0]), ([0, 0], [0, 1], [2, 0]))
(([1, 0], [2, 0]), ([0, 0], [1, 0], [2, 0]))
(([1, 0], [2, 0]), ([0, 1], [1, 0], [2, 0]))
(([1, 0], [2, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
(([0, 0], [0, 1], [1, 0]), ([0, 0], [0, 1], [2, 0]))
(([0, 0], [0, 1], [1, 0]), ([0, 0], [1, 0], [2, 0]))
(([0, 0], [0, 1], [1, 0]), ([0, 1], [1, 0], [2, 0]))
(([0, 0], [0, 1], [1, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
(([0, 0], [0, 1], [2, 0]), ([0, 0], [1, 0], [2, 0]))
(([0, 0], [0, 1], [2, 0]), ([0, 1], [1, 0], [2, 0]))
(([0, 0], [0, 1], [2, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
(([0, 0], [1, 0], [2, 0]), ([0, 1], [1, 0], [2, 0]))
(([0, 0], [1, 0], [2, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
(([0, 1], [1, 0], [2, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
((), ([0, 0],), ([0, 1],))
((), ([0, 0],), ([1, 0],))
((), ([0, 0],), ([2, 0],))
((), ([0, 0],), ([0, 0], [0, 1]))
((), ([0, 0],), ([0, 0], [1, 0]))
((), ([0, 0],), ([0, 0], [2, 0]))
((), ([0, 0],), ([0, 1], [1, 0]))
((), ([0, 0],), ([0, 1], [2, 0]))
((), ([0, 0],), ([1, 0], [2, 0]))
((), ([0, 0],), ([0, 0], [0, 1], [1, 0]))
((), ([0, 0],), ([0, 0], [0, 1], [2, 0]))
((), ([0, 0],), ([0, 0], [1, 0], [2, 0]))
((), ([0, 0],), ([0, 1], [1, 0], [2, 0]))
((), ([0, 0],), ([0, 0], [0, 1], [1, 0], [2, 0]))
((), ([0, 1],), ([1, 0],))
((), ([0, 1],), ([2, 0],))
((), ([0, 1],), ([0, 0], [0, 1]))
((), ([0, 1],), ([0, 0], [1, 0]))
((), ([0, 1],), ([0, 0], [2, 0]))
((), ([0, 1],), ([0, 1], [1, 0]))
((), ([0, 1],), ([0, 1], [2, 0]))
((), ([0, 1],), ([1, 0], [2, 0]))
((), ([0, 1],), ([0, 0], [0, 1], [1, 0]))
((), ([0, 1],), ([0, 0], [0, 1], [2, 0]))
((), ([0, 1],), ([0, 0], [1, 0], [2, 0]))
((), ([0, 1],), ([0, 1], [1, 0], [2, 0]))
((), ([0, 1],), ([0, 0], [0, 1], [1, 0], [2, 0]))
((), ([1, 0],), ([2, 0],))
((), ([1, 0],), ([0, 0], [0, 1]))
((), ([1, 0],), ([0, 0], [1, 0]))
((), ([1, 0],), ([0, 0], [2, 0]))
((), ([1, 0],), ([0, 1], [1, 0]))
((), ([1, 0],), ([0, 1], [2, 0]))
((), ([1, 0],), ([1, 0], [2, 0]))
((), ([1, 0],), ([0, 0], [0, 1], [1, 0]))
((), ([1, 0],), ([0, 0], [0, 1], [2, 0]))
((), ([1, 0],), ([0, 0], [1, 0], [2, 0]))
((), ([1, 0],), ([0, 1], [1, 0], [2, 0]))
((), ([1, 0],), ([0, 0], [0, 1], [1, 0], [2, 0]))
((), ([2, 0],), ([0, 0], [0, 1]))
((), ([2, 0],), ([0, 0], [1, 0]))
((), ([2, 0],), ([0, 0], [2, 0]))
((), ([2, 0],), ([0, 1], [1, 0]))
((), ([2, 0],), ([0, 1], [2, 0]))
((), ([2, 0],), ([1, 0], [2, 0]))
((), ([2, 0],), ([0, 0], [0, 1], [1, 0]))
((), ([2, 0],), ([0, 0], [0, 1], [2, 0]))
((), ([2, 0],), ([0, 0], [1, 0], [2, 0]))
((), ([2, 0],), ([0, 1], [1, 0], [2, 0]))
((), ([2, 0],), ([0, 0], [0, 1], [1, 0], [2, 0]))
((), ([0, 0], [0, 1]), ([0, 0], [1, 0]))
((), ([0, 0], [0, 1]), ([0, 0], [2, 0]))
((), ([0, 0], [0, 1]), ([0, 1], [1, 0]))
((), ([0, 0], [0, 1]), ([0, 1], [2, 0]))
((), ([0, 0], [0, 1]), ([1, 0], [2, 0]))
((), ([0, 0], [0, 1]), ([0, 0], [0, 1], [1, 0]))
((), ([0, 0], [0, 1]), ([0, 0], [0, 1], [2, 0]))
((), ([0, 0], [0, 1]), ([0, 0], [1, 0], [2, 0]))
((), ([0, 0], [0, 1]), ([0, 1], [1, 0], [2, 0]))
((), ([0, 0], [0, 1]), ([0, 0], [0, 1], [1, 0], [2, 0]))
((), ([0, 0], [1, 0]), ([0, 0], [2, 0]))
((), ([0, 0], [1, 0]), ([0, 1], [1, 0]))
((), ([0, 0], [1, 0]), ([0, 1], [2, 0]))
((), ([0, 0], [1, 0]), ([1, 0], [2, 0]))
((), ([0, 0], [1, 0]), ([0, 0], [0, 1], [1, 0]))
((), ([0, 0], [1, 0]), ([0, 0], [0, 1], [2, 0]))
((), ([0, 0], [1, 0]), ([0, 0], [1, 0], [2, 0]))
((), ([0, 0], [1, 0]), ([0, 1], [1, 0], [2, 0]))
((), ([0, 0], [1, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
((), ([0, 0], [2, 0]), ([0, 1], [1, 0]))
((), ([0, 0], [2, 0]), ([0, 1], [2, 0]))
((), ([0, 0], [2, 0]), ([1, 0], [2, 0]))
((), ([0, 0], [2, 0]), ([0, 0], [0, 1], [1, 0]))
((), ([0, 0], [2, 0]), ([0, 0], [0, 1], [2, 0]))
((), ([0, 0], [2, 0]), ([0, 0], [1, 0], [2, 0]))
((), ([0, 0], [2, 0]), ([0, 1], [1, 0], [2, 0]))
((), ([0, 0], [2, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
((), ([0, 1], [1, 0]), ([0, 1], [2, 0]))
((), ([0, 1], [1, 0]), ([1, 0], [2, 0]))
((), ([0, 1], [1, 0]), ([0, 0], [0, 1], [1, 0]))
((), ([0, 1], [1, 0]), ([0, 0], [0, 1], [2, 0]))
((), ([0, 1], [1, 0]), ([0, 0], [1, 0], [2, 0]))
((), ([0, 1], [1, 0]), ([0, 1], [1, 0], [2, 0]))
((), ([0, 1], [1, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
((), ([0, 1], [2, 0]), ([1, 0], [2, 0]))
((), ([0, 1], [2, 0]), ([0, 0], [0, 1], [1, 0]))
((), ([0, 1], [2, 0]), ([0, 0], [0, 1], [2, 0]))
((), ([0, 1], [2, 0]), ([0, 0], [1, 0], [2, 0]))
((), ([0, 1], [2, 0]), ([0, 1], [1, 0], [2, 0]))
((), ([0, 1], [2, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
((), ([1, 0], [2, 0]), ([0, 0], [0, 1], [1, 0]))
((), ([1, 0], [2, 0]), ([0, 0], [0, 1], [2, 0]))
((), ([1, 0], [2, 0]), ([0, 0], [1, 0], [2, 0]))
((), ([1, 0], [2, 0]), ([0, 1], [1, 0], [2, 0]))
((), ([1, 0], [2, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
((), ([0, 0], [0, 1], [1, 0]), ([0, 0], [0, 1], [2, 0]))
((), ([0, 0], [0, 1], [1, 0]), ([0, 0], [1, 0], [2, 0]))
((), ([0, 0], [0, 1], [1, 0]), ([0, 1], [1, 0], [2, 0]))
((), ([0, 0], [0, 1], [1, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
((), ([0, 0], [0, 1], [2, 0]), ([0, 0], [1, 0], [2, 0]))
((), ([0, 0], [0, 1], [2, 0]), ([0, 1], [1, 0], [2, 0]))
((), ([0, 0], [0, 1], [2, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
((), ([0, 0], [1, 0], [2, 0]), ([0, 1], [1, 0], [2, 0]))
((), ([0, 0], [1, 0], [2, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
((), ([0, 1], [1, 0], [2, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
(([0, 0],), ([0, 1],), ([1, 0],))
(([0, 0],), ([0, 1],), ([2, 0],))
(([0, 0],), ([0, 1],), ([0, 0], [0, 1]))
(([0, 0],), ([0, 1],), ([0, 0], [1, 0]))
(([0, 0],), ([0, 1],), ([0, 0], [2, 0]))
(([0, 0],), ([0, 1],), ([0, 1], [1, 0]))
(([0, 0],), ([0, 1],), ([0, 1], [2, 0]))
(([0, 0],), ([0, 1],), ([1, 0], [2, 0]))
(([0, 0],), ([0, 1],), ([0, 0], [0, 1], [1, 0]))
(([0, 0],), ([0, 1],), ([0, 0], [0, 1], [2, 0]))
(([0, 0],), ([0, 1],), ([0, 0], [1, 0], [2, 0]))
(([0, 0],), ([0, 1],), ([0, 1], [1, 0], [2, 0]))
(([0, 0],), ([0, 1],), ([0, 0], [0, 1], [1, 0], [2, 0]))
(([0, 0],), ([1, 0],), ([2, 0],))
(([0, 0],), ([1, 0],), ([0, 0], [0, 1]))
(([0, 0],), ([1, 0],), ([0, 0], [1, 0]))
(([0, 0],), ([1, 0],), ([0, 0], [2, 0]))
(([0, 0],), ([1, 0],), ([0, 1], [1, 0]))
(([0, 0],), ([1, 0],), ([0, 1], [2, 0]))
(([0, 0],), ([1, 0],), ([1, 0], [2, 0]))
(([0, 0],), ([1, 0],), ([0, 0], [0, 1], [1, 0]))
(([0, 0],), ([1, 0],), ([0, 0], [0, 1], [2, 0]))
(([0, 0],), ([1, 0],), ([0, 0], [1, 0], [2, 0]))
(([0, 0],), ([1, 0],), ([0, 1], [1, 0], [2, 0]))
(([0, 0],), ([1, 0],), ([0, 0], [0, 1], [1, 0], [2, 0]))
(([0, 0],), ([2, 0],), ([0, 0], [0, 1]))
(([0, 0],), ([2, 0],), ([0, 0], [1, 0]))
(([0, 0],), ([2, 0],), ([0, 0], [2, 0]))
(([0, 0],), ([2, 0],), ([0, 1], [1, 0]))
(([0, 0],), ([2, 0],), ([0, 1], [2, 0]))
(([0, 0],), ([2, 0],), ([1, 0], [2, 0]))
(([0, 0],), ([2, 0],), ([0, 0], [0, 1], [1, 0]))
(([0, 0],), ([2, 0],), ([0, 0], [0, 1], [2, 0]))
(([0, 0],), ([2, 0],), ([0, 0], [1, 0], [2, 0]))
(([0, 0],), ([2, 0],), ([0, 1], [1, 0], [2, 0]))
(([0, 0],), ([2, 0],), ([0, 0], [0, 1], [1, 0], [2, 0]))
(([0, 0],), ([0, 0], [0, 1]), ([0, 0], [1, 0]))
(([0, 0],), ([0, 0], [0, 1]), ([0, 0], [2, 0]))
(([0, 0],), ([0, 0], [0, 1]), ([0, 1], [1, 0]))
(([0, 0],), ([0, 0], [0, 1]), ([0, 1], [2, 0]))
(([0, 0],), ([0, 0], [0, 1]), ([1, 0], [2, 0]))
(([0, 0],), ([0, 0], [0, 1]), ([0, 0], [0, 1], [1, 0]))
(([0, 0],), ([0, 0], [0, 1]), ([0, 0], [0, 1], [2, 0]))
(([0, 0],), ([0, 0], [0, 1]), ([0, 0], [1, 0], [2, 0]))
(([0, 0],), ([0, 0], [0, 1]), ([0, 1], [1, 0], [2, 0]))
(([0, 0],), ([0, 0], [0, 1]), ([0, 0], [0, 1], [1, 0], [2, 0]))
(([0, 0],), ([0, 0], [1, 0]), ([0, 0], [2, 0]))
(([0, 0],), ([0, 0], [1, 0]), ([0, 1], [1, 0]))
(([0, 0],), ([0, 0], [1, 0]), ([0, 1], [2, 0]))
(([0, 0],), ([0, 0], [1, 0]), ([1, 0], [2, 0]))
(([0, 0],), ([0, 0], [1, 0]), ([0, 0], [0, 1], [1, 0]))
(([0, 0],), ([0, 0], [1, 0]), ([0, 0], [0, 1], [2, 0]))
(([0, 0],), ([0, 0], [1, 0]), ([0, 0], [1, 0], [2, 0]))
(([0, 0],), ([0, 0], [1, 0]), ([0, 1], [1, 0], [2, 0]))
(([0, 0],), ([0, 0], [1, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
(([0, 0],), ([0, 0], [2, 0]), ([0, 1], [1, 0]))
(([0, 0],), ([0, 0], [2, 0]), ([0, 1], [2, 0]))
(([0, 0],), ([0, 0], [2, 0]), ([1, 0], [2, 0]))
(([0, 0],), ([0, 0], [2, 0]), ([0, 0], [0, 1], [1, 0]))
(([0, 0],), ([0, 0], [2, 0]), ([0, 0], [0, 1], [2, 0]))
(([0, 0],), ([0, 0], [2, 0]), ([0, 0], [1, 0], [2, 0]))
(([0, 0],), ([0, 0], [2, 0]), ([0, 1], [1, 0], [2, 0]))
(([0, 0],), ([0, 0], [2, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
(([0, 0],), ([0, 1], [1, 0]), ([0, 1], [2, 0]))
(([0, 0],), ([0, 1], [1, 0]), ([1, 0], [2, 0]))
(([0, 0],), ([0, 1], [1, 0]), ([0, 0], [0, 1], [1, 0]))
(([0, 0],), ([0, 1], [1, 0]), ([0, 0], [0, 1], [2, 0]))
(([0, 0],), ([0, 1], [1, 0]), ([0, 0], [1, 0], [2, 0]))
(([0, 0],), ([0, 1], [1, 0]), ([0, 1], [1, 0], [2, 0]))
(([0, 0],), ([0, 1], [1, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
(([0, 0],), ([0, 1], [2, 0]), ([1, 0], [2, 0]))
(([0, 0],), ([0, 1], [2, 0]), ([0, 0], [0, 1], [1, 0]))
(([0, 0],), ([0, 1], [2, 0]), ([0, 0], [0, 1], [2, 0]))
(([0, 0],), ([0, 1], [2, 0]), ([0, 0], [1, 0], [2, 0]))
(([0, 0],), ([0, 1], [2, 0]), ([0, 1], [1, 0], [2, 0]))
(([0, 0],), ([0, 1], [2, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
(([0, 0],), ([1, 0], [2, 0]), ([0, 0], [0, 1], [1, 0]))
(([0, 0],), ([1, 0], [2, 0]), ([0, 0], [0, 1], [2, 0]))
(([0, 0],), ([1, 0], [2, 0]), ([0, 0], [1, 0], [2, 0]))
(([0, 0],), ([1, 0], [2, 0]), ([0, 1], [1, 0], [2, 0]))
(([0, 0],), ([1, 0], [2, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
(([0, 0],), ([0, 0], [0, 1], [1, 0]), ([0, 0], [0, 1], [2, 0]))
(([0, 0],), ([0, 0], [0, 1], [1, 0]), ([0, 0], [1, 0], [2, 0]))
(([0, 0],), ([0, 0], [0, 1], [1, 0]), ([0, 1], [1, 0], [2, 0]))
(([0, 0],), ([0, 0], [0, 1], [1, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
(([0, 0],), ([0, 0], [0, 1], [2, 0]), ([0, 0], [1, 0], [2, 0]))
(([0, 0],), ([0, 0], [0, 1], [2, 0]), ([0, 1], [1, 0], [2, 0]))
(([0, 0],), ([0, 0], [0, 1], [2, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
(([0, 0],), ([0, 0], [1, 0], [2, 0]), ([0, 1], [1, 0], [2, 0]))
(([0, 0],), ([0, 0], [1, 0], [2, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
(([0, 0],), ([0, 1], [1, 0], [2, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
(([0, 1],), ([1, 0],), ([2, 0],))
(([0, 1],), ([1, 0],), ([0, 0], [0, 1]))
(([0, 1],), ([1, 0],), ([0, 0], [1, 0]))
(([0, 1],), ([1, 0],), ([0, 0], [2, 0]))
(([0, 1],), ([1, 0],), ([0, 1], [1, 0]))
(([0, 1],), ([1, 0],), ([0, 1], [2, 0]))
(([0, 1],), ([1, 0],), ([1, 0], [2, 0]))
(([0, 1],), ([1, 0],), ([0, 0], [0, 1], [1, 0]))
(([0, 1],), ([1, 0],), ([0, 0], [0, 1], [2, 0]))
(([0, 1],), ([1, 0],), ([0, 0], [1, 0], [2, 0]))
(([0, 1],), ([1, 0],), ([0, 1], [1, 0], [2, 0]))
(([0, 1],), ([1, 0],), ([0, 0], [0, 1], [1, 0], [2, 0]))
(([0, 1],), ([2, 0],), ([0, 0], [0, 1]))
(([0, 1],), ([2, 0],), ([0, 0], [1, 0]))
(([0, 1],), ([2, 0],), ([0, 0], [2, 0]))
(([0, 1],), ([2, 0],), ([0, 1], [1, 0]))
(([0, 1],), ([2, 0],), ([0, 1], [2, 0]))
(([0, 1],), ([2, 0],), ([1, 0], [2, 0]))
(([0, 1],), ([2, 0],), ([0, 0], [0, 1], [1, 0]))
(([0, 1],), ([2, 0],), ([0, 0], [0, 1], [2, 0]))
(([0, 1],), ([2, 0],), ([0, 0], [1, 0], [2, 0]))
(([0, 1],), ([2, 0],), ([0, 1], [1, 0], [2, 0]))
(([0, 1],), ([2, 0],), ([0, 0], [0, 1], [1, 0], [2, 0]))
(([0, 1],), ([0, 0], [0, 1]), ([0, 0], [1, 0]))
(([0, 1],), ([0, 0], [0, 1]), ([0, 0], [2, 0]))
(([0, 1],), ([0, 0], [0, 1]), ([0, 1], [1, 0]))
(([0, 1],), ([0, 0], [0, 1]), ([0, 1], [2, 0]))
(([0, 1],), ([0, 0], [0, 1]), ([1, 0], [2, 0]))
(([0, 1],), ([0, 0], [0, 1]), ([0, 0], [0, 1], [1, 0]))
(([0, 1],), ([0, 0], [0, 1]), ([0, 0], [0, 1], [2, 0]))
(([0, 1],), ([0, 0], [0, 1]), ([0, 0], [1, 0], [2, 0]))
(([0, 1],), ([0, 0], [0, 1]), ([0, 1], [1, 0], [2, 0]))
(([0, 1],), ([0, 0], [0, 1]), ([0, 0], [0, 1], [1, 0], [2, 0]))
(([0, 1],), ([0, 0], [1, 0]), ([0, 0], [2, 0]))
(([0, 1],), ([0, 0], [1, 0]), ([0, 1], [1, 0]))
(([0, 1],), ([0, 0], [1, 0]), ([0, 1], [2, 0]))
(([0, 1],), ([0, 0], [1, 0]), ([1, 0], [2, 0]))
(([0, 1],), ([0, 0], [1, 0]), ([0, 0], [0, 1], [1, 0]))
(([0, 1],), ([0, 0], [1, 0]), ([0, 0], [0, 1], [2, 0]))
(([0, 1],), ([0, 0], [1, 0]), ([0, 0], [1, 0], [2, 0]))
(([0, 1],), ([0, 0], [1, 0]), ([0, 1], [1, 0], [2, 0]))
(([0, 1],), ([0, 0], [1, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
(([0, 1],), ([0, 0], [2, 0]), ([0, 1], [1, 0]))
(([0, 1],), ([0, 0], [2, 0]), ([0, 1], [2, 0]))
(([0, 1],), ([0, 0], [2, 0]), ([1, 0], [2, 0]))
(([0, 1],), ([0, 0], [2, 0]), ([0, 0], [0, 1], [1, 0]))
(([0, 1],), ([0, 0], [2, 0]), ([0, 0], [0, 1], [2, 0]))
(([0, 1],), ([0, 0], [2, 0]), ([0, 0], [1, 0], [2, 0]))
(([0, 1],), ([0, 0], [2, 0]), ([0, 1], [1, 0], [2, 0]))
(([0, 1],), ([0, 0], [2, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
(([0, 1],), ([0, 1], [1, 0]), ([0, 1], [2, 0]))
(([0, 1],), ([0, 1], [1, 0]), ([1, 0], [2, 0]))
(([0, 1],), ([0, 1], [1, 0]), ([0, 0], [0, 1], [1, 0]))
(([0, 1],), ([0, 1], [1, 0]), ([0, 0], [0, 1], [2, 0]))
(([0, 1],), ([0, 1], [1, 0]), ([0, 0], [1, 0], [2, 0]))
(([0, 1],), ([0, 1], [1, 0]), ([0, 1], [1, 0], [2, 0]))
(([0, 1],), ([0, 1], [1, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
(([0, 1],), ([0, 1], [2, 0]), ([1, 0], [2, 0]))
(([0, 1],), ([0, 1], [2, 0]), ([0, 0], [0, 1], [1, 0]))
(([0, 1],), ([0, 1], [2, 0]), ([0, 0], [0, 1], [2, 0]))
(([0, 1],), ([0, 1], [2, 0]), ([0, 0], [1, 0], [2, 0]))
(([0, 1],), ([0, 1], [2, 0]), ([0, 1], [1, 0], [2, 0]))
(([0, 1],), ([0, 1], [2, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
(([0, 1],), ([1, 0], [2, 0]), ([0, 0], [0, 1], [1, 0]))
(([0, 1],), ([1, 0], [2, 0]), ([0, 0], [0, 1], [2, 0]))
(([0, 1],), ([1, 0], [2, 0]), ([0, 0], [1, 0], [2, 0]))
(([0, 1],), ([1, 0], [2, 0]), ([0, 1], [1, 0], [2, 0]))
(([0, 1],), ([1, 0], [2, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
(([0, 1],), ([0, 0], [0, 1], [1, 0]), ([0, 0], [0, 1], [2, 0]))
(([0, 1],), ([0, 0], [0, 1], [1, 0]), ([0, 0], [1, 0], [2, 0]))
(([0, 1],), ([0, 0], [0, 1], [1, 0]), ([0, 1], [1, 0], [2, 0]))
(([0, 1],), ([0, 0], [0, 1], [1, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
(([0, 1],), ([0, 0], [0, 1], [2, 0]), ([0, 0], [1, 0], [2, 0]))
(([0, 1],), ([0, 0], [0, 1], [2, 0]), ([0, 1], [1, 0], [2, 0]))
(([0, 1],), ([0, 0], [0, 1], [2, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
(([0, 1],), ([0, 0], [1, 0], [2, 0]), ([0, 1], [1, 0], [2, 0]))
(([0, 1],), ([0, 0], [1, 0], [2, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
(([0, 1],), ([0, 1], [1, 0], [2, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
(([1, 0],), ([2, 0],), ([0, 0], [0, 1]))
(([1, 0],), ([2, 0],), ([0, 0], [1, 0]))
(([1, 0],), ([2, 0],), ([0, 0], [2, 0]))
(([1, 0],), ([2, 0],), ([0, 1], [1, 0]))
(([1, 0],), ([2, 0],), ([0, 1], [2, 0]))
(([1, 0],), ([2, 0],), ([1, 0], [2, 0]))
(([1, 0],), ([2, 0],), ([0, 0], [0, 1], [1, 0]))
(([1, 0],), ([2, 0],), ([0, 0], [0, 1], [2, 0]))
(([1, 0],), ([2, 0],), ([0, 0], [1, 0], [2, 0]))
(([1, 0],), ([2, 0],), ([0, 1], [1, 0], [2, 0]))
(([1, 0],), ([2, 0],), ([0, 0], [0, 1], [1, 0], [2, 0]))
(([1, 0],), ([0, 0], [0, 1]), ([0, 0], [1, 0]))
(([1, 0],), ([0, 0], [0, 1]), ([0, 0], [2, 0]))
(([1, 0],), ([0, 0], [0, 1]), ([0, 1], [1, 0]))
(([1, 0],), ([0, 0], [0, 1]), ([0, 1], [2, 0]))
(([1, 0],), ([0, 0], [0, 1]), ([1, 0], [2, 0]))
(([1, 0],), ([0, 0], [0, 1]), ([0, 0], [0, 1], [1, 0]))
(([1, 0],), ([0, 0], [0, 1]), ([0, 0], [0, 1], [2, 0]))
(([1, 0],), ([0, 0], [0, 1]), ([0, 0], [1, 0], [2, 0]))
(([1, 0],), ([0, 0], [0, 1]), ([0, 1], [1, 0], [2, 0]))
(([1, 0],), ([0, 0], [0, 1]), ([0, 0], [0, 1], [1, 0], [2, 0]))
(([1, 0],), ([0, 0], [1, 0]), ([0, 0], [2, 0]))
(([1, 0],), ([0, 0], [1, 0]), ([0, 1], [1, 0]))
(([1, 0],), ([0, 0], [1, 0]), ([0, 1], [2, 0]))
(([1, 0],), ([0, 0], [1, 0]), ([1, 0], [2, 0]))
(([1, 0],), ([0, 0], [1, 0]), ([0, 0], [0, 1], [1, 0]))
(([1, 0],), ([0, 0], [1, 0]), ([0, 0], [0, 1], [2, 0]))
(([1, 0],), ([0, 0], [1, 0]), ([0, 0], [1, 0], [2, 0]))
(([1, 0],), ([0, 0], [1, 0]), ([0, 1], [1, 0], [2, 0]))
(([1, 0],), ([0, 0], [1, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
(([1, 0],), ([0, 0], [2, 0]), ([0, 1], [1, 0]))
(([1, 0],), ([0, 0], [2, 0]), ([0, 1], [2, 0]))
(([1, 0],), ([0, 0], [2, 0]), ([1, 0], [2, 0]))
(([1, 0],), ([0, 0], [2, 0]), ([0, 0], [0, 1], [1, 0]))
(([1, 0],), ([0, 0], [2, 0]), ([0, 0], [0, 1], [2, 0]))
(([1, 0],), ([0, 0], [2, 0]), ([0, 0], [1, 0], [2, 0]))
(([1, 0],), ([0, 0], [2, 0]), ([0, 1], [1, 0], [2, 0]))
(([1, 0],), ([0, 0], [2, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
(([1, 0],), ([0, 1], [1, 0]), ([0, 1], [2, 0]))
(([1, 0],), ([0, 1], [1, 0]), ([1, 0], [2, 0]))
(([1, 0],), ([0, 1], [1, 0]), ([0, 0], [0, 1], [1, 0]))
(([1, 0],), ([0, 1], [1, 0]), ([0, 0], [0, 1], [2, 0]))
(([1, 0],), ([0, 1], [1, 0]), ([0, 0], [1, 0], [2, 0]))
(([1, 0],), ([0, 1], [1, 0]), ([0, 1], [1, 0], [2, 0]))
(([1, 0],), ([0, 1], [1, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
(([1, 0],), ([0, 1], [2, 0]), ([1, 0], [2, 0]))
(([1, 0],), ([0, 1], [2, 0]), ([0, 0], [0, 1], [1, 0]))
(([1, 0],), ([0, 1], [2, 0]), ([0, 0], [0, 1], [2, 0]))
(([1, 0],), ([0, 1], [2, 0]), ([0, 0], [1, 0], [2, 0]))
(([1, 0],), ([0, 1], [2, 0]), ([0, 1], [1, 0], [2, 0]))
(([1, 0],), ([0, 1], [2, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
(([1, 0],), ([1, 0], [2, 0]), ([0, 0], [0, 1], [1, 0]))
(([1, 0],), ([1, 0], [2, 0]), ([0, 0], [0, 1], [2, 0]))
(([1, 0],), ([1, 0], [2, 0]), ([0, 0], [1, 0], [2, 0]))
(([1, 0],), ([1, 0], [2, 0]), ([0, 1], [1, 0], [2, 0]))
(([1, 0],), ([1, 0], [2, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
(([1, 0],), ([0, 0], [0, 1], [1, 0]), ([0, 0], [0, 1], [2, 0]))
(([1, 0],), ([0, 0], [0, 1], [1, 0]), ([0, 0], [1, 0], [2, 0]))
(([1, 0],), ([0, 0], [0, 1], [1, 0]), ([0, 1], [1, 0], [2, 0]))
(([1, 0],), ([0, 0], [0, 1], [1, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
(([1, 0],), ([0, 0], [0, 1], [2, 0]), ([0, 0], [1, 0], [2, 0]))
(([1, 0],), ([0, 0], [0, 1], [2, 0]), ([0, 1], [1, 0], [2, 0]))
(([1, 0],), ([0, 0], [0, 1], [2, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
(([1, 0],), ([0, 0], [1, 0], [2, 0]), ([0, 1], [1, 0], [2, 0]))
(([1, 0],), ([0, 0], [1, 0], [2, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
(([1, 0],), ([0, 1], [1, 0], [2, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
(([2, 0],), ([0, 0], [0, 1]), ([0, 0], [1, 0]))
(([2, 0],), ([0, 0], [0, 1]), ([0, 0], [2, 0]))
(([2, 0],), ([0, 0], [0, 1]), ([0, 1], [1, 0]))
(([2, 0],), ([0, 0], [0, 1]), ([0, 1], [2, 0]))
(([2, 0],), ([0, 0], [0, 1]), ([1, 0], [2, 0]))
(([2, 0],), ([0, 0], [0, 1]), ([0, 0], [0, 1], [1, 0]))
(([2, 0],), ([0, 0], [0, 1]), ([0, 0], [0, 1], [2, 0]))
(([2, 0],), ([0, 0], [0, 1]), ([0, 0], [1, 0], [2, 0]))
(([2, 0],), ([0, 0], [0, 1]), ([0, 1], [1, 0], [2, 0]))
(([2, 0],), ([0, 0], [0, 1]), ([0, 0], [0, 1], [1, 0], [2, 0]))
(([2, 0],), ([0, 0], [1, 0]), ([0, 0], [2, 0]))
(([2, 0],), ([0, 0], [1, 0]), ([0, 1], [1, 0]))
(([2, 0],), ([0, 0], [1, 0]), ([0, 1], [2, 0]))
(([2, 0],), ([0, 0], [1, 0]), ([1, 0], [2, 0]))
(([2, 0],), ([0, 0], [1, 0]), ([0, 0], [0, 1], [1, 0]))
(([2, 0],), ([0, 0], [1, 0]), ([0, 0], [0, 1], [2, 0]))
(([2, 0],), ([0, 0], [1, 0]), ([0, 0], [1, 0], [2, 0]))
(([2, 0],), ([0, 0], [1, 0]), ([0, 1], [1, 0], [2, 0]))
(([2, 0],), ([0, 0], [1, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
(([2, 0],), ([0, 0], [2, 0]), ([0, 1], [1, 0]))
(([2, 0],), ([0, 0], [2, 0]), ([0, 1], [2, 0]))
(([2, 0],), ([0, 0], [2, 0]), ([1, 0], [2, 0]))
(([2, 0],), ([0, 0], [2, 0]), ([0, 0], [0, 1], [1, 0]))
(([2, 0],), ([0, 0], [2, 0]), ([0, 0], [0, 1], [2, 0]))
(([2, 0],), ([0, 0], [2, 0]), ([0, 0], [1, 0], [2, 0]))
(([2, 0],), ([0, 0], [2, 0]), ([0, 1], [1, 0], [2, 0]))
(([2, 0],), ([0, 0], [2, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
(([2, 0],), ([0, 1], [1, 0]), ([0, 1], [2, 0]))
(([2, 0],), ([0, 1], [1, 0]), ([1, 0], [2, 0]))
(([2, 0],), ([0, 1], [1, 0]), ([0, 0], [0, 1], [1, 0]))
(([2, 0],), ([0, 1], [1, 0]), ([0, 0], [0, 1], [2, 0]))
(([2, 0],), ([0, 1], [1, 0]), ([0, 0], [1, 0], [2, 0]))
(([2, 0],), ([0, 1], [1, 0]), ([0, 1], [1, 0], [2, 0]))
(([2, 0],), ([0, 1], [1, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
(([2, 0],), ([0, 1], [2, 0]), ([1, 0], [2, 0]))
(([2, 0],), ([0, 1], [2, 0]), ([0, 0], [0, 1], [1, 0]))
(([2, 0],), ([0, 1], [2, 0]), ([0, 0], [0, 1], [2, 0]))
(([2, 0],), ([0, 1], [2, 0]), ([0, 0], [1, 0], [2, 0]))
(([2, 0],), ([0, 1], [2, 0]), ([0, 1], [1, 0], [2, 0]))
(([2, 0],), ([0, 1], [2, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
(([2, 0],), ([1, 0], [2, 0]), ([0, 0], [0, 1], [1, 0]))
(([2, 0],), ([1, 0], [2, 0]), ([0, 0], [0, 1], [2, 0]))
(([2, 0],), ([1, 0], [2, 0]), ([0, 0], [1, 0], [2, 0]))
(([2, 0],), ([1, 0], [2, 0]), ([0, 1], [1, 0], [2, 0]))
(([2, 0],), ([1, 0], [2, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
(([2, 0],), ([0, 0], [0, 1], [1, 0]), ([0, 0], [0, 1], [2, 0]))
(([2, 0],), ([0, 0], [0, 1], [1, 0]), ([0, 0], [1, 0], [2, 0]))
(([2, 0],), ([0, 0], [0, 1], [1, 0]), ([0, 1], [1, 0], [2, 0]))
(([2, 0],), ([0, 0], [0, 1], [1, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
(([2, 0],), ([0, 0], [0, 1], [2, 0]), ([0, 0], [1, 0], [2, 0]))
(([2, 0],), ([0, 0], [0, 1], [2, 0]), ([0, 1], [1, 0], [2, 0]))
(([2, 0],), ([0, 0], [0, 1], [2, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
(([2, 0],), ([0, 0], [1, 0], [2, 0]), ([0, 1], [1, 0], [2, 0]))
(([2, 0],), ([0, 0], [1, 0], [2, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
(([2, 0],), ([0, 1], [1, 0], [2, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
(([0, 0], [0, 1]), ([0, 0], [1, 0]), ([0, 0], [2, 0]))
(([0, 0], [0, 1]), ([0, 0], [1, 0]), ([0, 1], [1, 0]))
(([0, 0], [0, 1]), ([0, 0], [1, 0]), ([0, 1], [2, 0]))
(([0, 0], [0, 1]), ([0, 0], [1, 0]), ([1, 0], [2, 0]))
(([0, 0], [0, 1]), ([0, 0], [1, 0]), ([0, 0], [0, 1], [1, 0]))
(([0, 0], [0, 1]), ([0, 0], [1, 0]), ([0, 0], [0, 1], [2, 0]))
(([0, 0], [0, 1]), ([0, 0], [1, 0]), ([0, 0], [1, 0], [2, 0]))
(([0, 0], [0, 1]), ([0, 0], [1, 0]), ([0, 1], [1, 0], [2, 0]))
(([0, 0], [0, 1]), ([0, 0], [1, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
(([0, 0], [0, 1]), ([0, 0], [2, 0]), ([0, 1], [1, 0]))
(([0, 0], [0, 1]), ([0, 0], [2, 0]), ([0, 1], [2, 0]))
(([0, 0], [0, 1]), ([0, 0], [2, 0]), ([1, 0], [2, 0]))
(([0, 0], [0, 1]), ([0, 0], [2, 0]), ([0, 0], [0, 1], [1, 0]))
(([0, 0], [0, 1]), ([0, 0], [2, 0]), ([0, 0], [0, 1], [2, 0]))
(([0, 0], [0, 1]), ([0, 0], [2, 0]), ([0, 0], [1, 0], [2, 0]))
(([0, 0], [0, 1]), ([0, 0], [2, 0]), ([0, 1], [1, 0], [2, 0]))
(([0, 0], [0, 1]), ([0, 0], [2, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
(([0, 0], [0, 1]), ([0, 1], [1, 0]), ([0, 1], [2, 0]))
(([0, 0], [0, 1]), ([0, 1], [1, 0]), ([1, 0], [2, 0]))
(([0, 0], [0, 1]), ([0, 1], [1, 0]), ([0, 0], [0, 1], [1, 0]))
(([0, 0], [0, 1]), ([0, 1], [1, 0]), ([0, 0], [0, 1], [2, 0]))
(([0, 0], [0, 1]), ([0, 1], [1, 0]), ([0, 0], [1, 0], [2, 0]))
(([0, 0], [0, 1]), ([0, 1], [1, 0]), ([0, 1], [1, 0], [2, 0]))
(([0, 0], [0, 1]), ([0, 1], [1, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
(([0, 0], [0, 1]), ([0, 1], [2, 0]), ([1, 0], [2, 0]))
(([0, 0], [0, 1]), ([0, 1], [2, 0]), ([0, 0], [0, 1], [1, 0]))
(([0, 0], [0, 1]), ([0, 1], [2, 0]), ([0, 0], [0, 1], [2, 0]))
(([0, 0], [0, 1]), ([0, 1], [2, 0]), ([0, 0], [1, 0], [2, 0]))
(([0, 0], [0, 1]), ([0, 1], [2, 0]), ([0, 1], [1, 0], [2, 0]))
(([0, 0], [0, 1]), ([0, 1], [2, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
(([0, 0], [0, 1]), ([1, 0], [2, 0]), ([0, 0], [0, 1], [1, 0]))
(([0, 0], [0, 1]), ([1, 0], [2, 0]), ([0, 0], [0, 1], [2, 0]))
(([0, 0], [0, 1]), ([1, 0], [2, 0]), ([0, 0], [1, 0], [2, 0]))
(([0, 0], [0, 1]), ([1, 0], [2, 0]), ([0, 1], [1, 0], [2, 0]))
(([0, 0], [0, 1]), ([1, 0], [2, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
(([0, 0], [0, 1]), ([0, 0], [0, 1], [1, 0]), ([0, 0], [0, 1], [2, 0]))
(([0, 0], [0, 1]), ([0, 0], [0, 1], [1, 0]), ([0, 0], [1, 0], [2, 0]))
(([0, 0], [0, 1]), ([0, 0], [0, 1], [1, 0]), ([0, 1], [1, 0], [2, 0]))
(([0, 0], [0, 1]), ([0, 0], [0, 1], [1, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
(([0, 0], [0, 1]), ([0, 0], [0, 1], [2, 0]), ([0, 0], [1, 0], [2, 0]))
(([0, 0], [0, 1]), ([0, 0], [0, 1], [2, 0]), ([0, 1], [1, 0], [2, 0]))
(([0, 0], [0, 1]), ([0, 0], [0, 1], [2, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
(([0, 0], [0, 1]), ([0, 0], [1, 0], [2, 0]), ([0, 1], [1, 0], [2, 0]))
(([0, 0], [0, 1]), ([0, 0], [1, 0], [2, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
(([0, 0], [0, 1]), ([0, 1], [1, 0], [2, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
(([0, 0], [1, 0]), ([0, 0], [2, 0]), ([0, 1], [1, 0]))
(([0, 0], [1, 0]), ([0, 0], [2, 0]), ([0, 1], [2, 0]))
(([0, 0], [1, 0]), ([0, 0], [2, 0]), ([1, 0], [2, 0]))
(([0, 0], [1, 0]), ([0, 0], [2, 0]), ([0, 0], [0, 1], [1, 0]))
(([0, 0], [1, 0]), ([0, 0], [2, 0]), ([0, 0], [0, 1], [2, 0]))
(([0, 0], [1, 0]), ([0, 0], [2, 0]), ([0, 0], [1, 0], [2, 0]))
(([0, 0], [1, 0]), ([0, 0], [2, 0]), ([0, 1], [1, 0], [2, 0]))
(([0, 0], [1, 0]), ([0, 0], [2, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
(([0, 0], [1, 0]), ([0, 1], [1, 0]), ([0, 1], [2, 0]))
(([0, 0], [1, 0]), ([0, 1], [1, 0]), ([1, 0], [2, 0]))
(([0, 0], [1, 0]), ([0, 1], [1, 0]), ([0, 0], [0, 1], [1, 0]))
(([0, 0], [1, 0]), ([0, 1], [1, 0]), ([0, 0], [0, 1], [2, 0]))
(([0, 0], [1, 0]), ([0, 1], [1, 0]), ([0, 0], [1, 0], [2, 0]))
(([0, 0], [1, 0]), ([0, 1], [1, 0]), ([0, 1], [1, 0], [2, 0]))
(([0, 0], [1, 0]), ([0, 1], [1, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
(([0, 0], [1, 0]), ([0, 1], [2, 0]), ([1, 0], [2, 0]))
(([0, 0], [1, 0]), ([0, 1], [2, 0]), ([0, 0], [0, 1], [1, 0]))
(([0, 0], [1, 0]), ([0, 1], [2, 0]), ([0, 0], [0, 1], [2, 0]))
(([0, 0], [1, 0]), ([0, 1], [2, 0]), ([0, 0], [1, 0], [2, 0]))
(([0, 0], [1, 0]), ([0, 1], [2, 0]), ([0, 1], [1, 0], [2, 0]))
(([0, 0], [1, 0]), ([0, 1], [2, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
(([0, 0], [1, 0]), ([1, 0], [2, 0]), ([0, 0], [0, 1], [1, 0]))
(([0, 0], [1, 0]), ([1, 0], [2, 0]), ([0, 0], [0, 1], [2, 0]))
(([0, 0], [1, 0]), ([1, 0], [2, 0]), ([0, 0], [1, 0], [2, 0]))
(([0, 0], [1, 0]), ([1, 0], [2, 0]), ([0, 1], [1, 0], [2, 0]))
(([0, 0], [1, 0]), ([1, 0], [2, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
(([0, 0], [1, 0]), ([0, 0], [0, 1], [1, 0]), ([0, 0], [0, 1], [2, 0]))
(([0, 0], [1, 0]), ([0, 0], [0, 1], [1, 0]), ([0, 0], [1, 0], [2, 0]))
(([0, 0], [1, 0]), ([0, 0], [0, 1], [1, 0]), ([0, 1], [1, 0], [2, 0]))
(([0, 0], [1, 0]), ([0, 0], [0, 1], [1, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
(([0, 0], [1, 0]), ([0, 0], [0, 1], [2, 0]), ([0, 0], [1, 0], [2, 0]))
(([0, 0], [1, 0]), ([0, 0], [0, 1], [2, 0]), ([0, 1], [1, 0], [2, 0]))
(([0, 0], [1, 0]), ([0, 0], [0, 1], [2, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
(([0, 0], [1, 0]), ([0, 0], [1, 0], [2, 0]), ([0, 1], [1, 0], [2, 0]))
(([0, 0], [1, 0]), ([0, 0], [1, 0], [2, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
(([0, 0], [1, 0]), ([0, 1], [1, 0], [2, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
(([0, 0], [2, 0]), ([0, 1], [1, 0]), ([0, 1], [2, 0]))
(([0, 0], [2, 0]), ([0, 1], [1, 0]), ([1, 0], [2, 0]))
(([0, 0], [2, 0]), ([0, 1], [1, 0]), ([0, 0], [0, 1], [1, 0]))
(([0, 0], [2, 0]), ([0, 1], [1, 0]), ([0, 0], [0, 1], [2, 0]))
(([0, 0], [2, 0]), ([0, 1], [1, 0]), ([0, 0], [1, 0], [2, 0]))
(([0, 0], [2, 0]), ([0, 1], [1, 0]), ([0, 1], [1, 0], [2, 0]))
(([0, 0], [2, 0]), ([0, 1], [1, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
(([0, 0], [2, 0]), ([0, 1], [2, 0]), ([1, 0], [2, 0]))
(([0, 0], [2, 0]), ([0, 1], [2, 0]), ([0, 0], [0, 1], [1, 0]))
(([0, 0], [2, 0]), ([0, 1], [2, 0]), ([0, 0], [0, 1], [2, 0]))
(([0, 0], [2, 0]), ([0, 1], [2, 0]), ([0, 0], [1, 0], [2, 0]))
(([0, 0], [2, 0]), ([0, 1], [2, 0]), ([0, 1], [1, 0], [2, 0]))
(([0, 0], [2, 0]), ([0, 1], [2, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
(([0, 0], [2, 0]), ([1, 0], [2, 0]), ([0, 0], [0, 1], [1, 0]))
(([0, 0], [2, 0]), ([1, 0], [2, 0]), ([0, 0], [0, 1], [2, 0]))
(([0, 0], [2, 0]), ([1, 0], [2, 0]), ([0, 0], [1, 0], [2, 0]))
(([0, 0], [2, 0]), ([1, 0], [2, 0]), ([0, 1], [1, 0], [2, 0]))
(([0, 0], [2, 0]), ([1, 0], [2, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
(([0, 0], [2, 0]), ([0, 0], [0, 1], [1, 0]), ([0, 0], [0, 1], [2, 0]))
(([0, 0], [2, 0]), ([0, 0], [0, 1], [1, 0]), ([0, 0], [1, 0], [2, 0]))
(([0, 0], [2, 0]), ([0, 0], [0, 1], [1, 0]), ([0, 1], [1, 0], [2, 0]))
(([0, 0], [2, 0]), ([0, 0], [0, 1], [1, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
(([0, 0], [2, 0]), ([0, 0], [0, 1], [2, 0]), ([0, 0], [1, 0], [2, 0]))
(([0, 0], [2, 0]), ([0, 0], [0, 1], [2, 0]), ([0, 1], [1, 0], [2, 0]))
(([0, 0], [2, 0]), ([0, 0], [0, 1], [2, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
(([0, 0], [2, 0]), ([0, 0], [1, 0], [2, 0]), ([0, 1], [1, 0], [2, 0]))
(([0, 0], [2, 0]), ([0, 0], [1, 0], [2, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
(([0, 0], [2, 0]), ([0, 1], [1, 0], [2, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
(([0, 1], [1, 0]), ([0, 1], [2, 0]), ([1, 0], [2, 0]))
(([0, 1], [1, 0]), ([0, 1], [2, 0]), ([0, 0], [0, 1], [1, 0]))
(([0, 1], [1, 0]), ([0, 1], [2, 0]), ([0, 0], [0, 1], [2, 0]))
(([0, 1], [1, 0]), ([0, 1], [2, 0]), ([0, 0], [1, 0], [2, 0]))
(([0, 1], [1, 0]), ([0, 1], [2, 0]), ([0, 1], [1, 0], [2, 0]))
(([0, 1], [1, 0]), ([0, 1], [2, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
(([0, 1], [1, 0]), ([1, 0], [2, 0]), ([0, 0], [0, 1], [1, 0]))
(([0, 1], [1, 0]), ([1, 0], [2, 0]), ([0, 0], [0, 1], [2, 0]))
(([0, 1], [1, 0]), ([1, 0], [2, 0]), ([0, 0], [1, 0], [2, 0]))
(([0, 1], [1, 0]), ([1, 0], [2, 0]), ([0, 1], [1, 0], [2, 0]))
(([0, 1], [1, 0]), ([1, 0], [2, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
(([0, 1], [1, 0]), ([0, 0], [0, 1], [1, 0]), ([0, 0], [0, 1], [2, 0]))
(([0, 1], [1, 0]), ([0, 0], [0, 1], [1, 0]), ([0, 0], [1, 0], [2, 0]))
(([0, 1], [1, 0]), ([0, 0], [0, 1], [1, 0]), ([0, 1], [1, 0], [2, 0]))
(([0, 1], [1, 0]), ([0, 0], [0, 1], [1, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
(([0, 1], [1, 0]), ([0, 0], [0, 1], [2, 0]), ([0, 0], [1, 0], [2, 0]))
(([0, 1], [1, 0]), ([0, 0], [0, 1], [2, 0]), ([0, 1], [1, 0], [2, 0]))
(([0, 1], [1, 0]), ([0, 0], [0, 1], [2, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
(([0, 1], [1, 0]), ([0, 0], [1, 0], [2, 0]), ([0, 1], [1, 0], [2, 0]))
(([0, 1], [1, 0]), ([0, 0], [1, 0], [2, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
(([0, 1], [1, 0]), ([0, 1], [1, 0], [2, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
(([0, 1], [2, 0]), ([1, 0], [2, 0]), ([0, 0], [0, 1], [1, 0]))
(([0, 1], [2, 0]), ([1, 0], [2, 0]), ([0, 0], [0, 1], [2, 0]))
(([0, 1], [2, 0]), ([1, 0], [2, 0]), ([0, 0], [1, 0], [2, 0]))
(([0, 1], [2, 0]), ([1, 0], [2, 0]), ([0, 1], [1, 0], [2, 0]))
(([0, 1], [2, 0]), ([1, 0], [2, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
(([0, 1], [2, 0]), ([0, 0], [0, 1], [1, 0]), ([0, 0], [0, 1], [2, 0]))
(([0, 1], [2, 0]), ([0, 0], [0, 1], [1, 0]), ([0, 0], [1, 0], [2, 0]))
(([0, 1], [2, 0]), ([0, 0], [0, 1], [1, 0]), ([0, 1], [1, 0], [2, 0]))
(([0, 1], [2, 0]), ([0, 0], [0, 1], [1, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
(([0, 1], [2, 0]), ([0, 0], [0, 1], [2, 0]), ([0, 0], [1, 0], [2, 0]))
(([0, 1], [2, 0]), ([0, 0], [0, 1], [2, 0]), ([0, 1], [1, 0], [2, 0]))
(([0, 1], [2, 0]), ([0, 0], [0, 1], [2, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
(([0, 1], [2, 0]), ([0, 0], [1, 0], [2, 0]), ([0, 1], [1, 0], [2, 0]))
(([0, 1], [2, 0]), ([0, 0], [1, 0], [2, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
(([0, 1], [2, 0]), ([0, 1], [1, 0], [2, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
(([1, 0], [2, 0]), ([0, 0], [0, 1], [1, 0]), ([0, 0], [0, 1], [2, 0]))
(([1, 0], [2, 0]), ([0, 0], [0, 1], [1, 0]), ([0, 0], [1, 0], [2, 0]))
(([1, 0], [2, 0]), ([0, 0], [0, 1], [1, 0]), ([0, 1], [1, 0], [2, 0]))
(([1, 0], [2, 0]), ([0, 0], [0, 1], [1, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
(([1, 0], [2, 0]), ([0, 0], [0, 1], [2, 0]), ([0, 0], [1, 0], [2, 0]))
(([1, 0], [2, 0]), ([0, 0], [0, 1], [2, 0]), ([0, 1], [1, 0], [2, 0]))
(([1, 0], [2, 0]), ([0, 0], [0, 1], [2, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
(([1, 0], [2, 0]), ([0, 0], [1, 0], [2, 0]), ([0, 1], [1, 0], [2, 0]))
(([1, 0], [2, 0]), ([0, 0], [1, 0], [2, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
(([1, 0], [2, 0]), ([0, 1], [1, 0], [2, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
(([0, 0], [0, 1], [1, 0]), ([0, 0], [0, 1], [2, 0]), ([0, 0], [1, 0], [2, 0]))
(([0, 0], [0, 1], [1, 0]), ([0, 0], [0, 1], [2, 0]), ([0, 1], [1, 0], [2, 0]))
(([0, 0], [0, 1], [1, 0]), ([0, 0], [0, 1], [2, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
(([0, 0], [0, 1], [1, 0]), ([0, 0], [1, 0], [2, 0]), ([0, 1], [1, 0], [2, 0]))
(([0, 0], [0, 1], [1, 0]), ([0, 0], [1, 0], [2, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
(([0, 0], [0, 1], [1, 0]), ([0, 1], [1, 0], [2, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
(([0, 0], [0, 1], [2, 0]), ([0, 0], [1, 0], [2, 0]), ([0, 1], [1, 0], [2, 0]))
(([0, 0], [0, 1], [2, 0]), ([0, 0], [1, 0], [2, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
(([0, 0], [0, 1], [2, 0]), ([0, 1], [1, 0], [2, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
(([0, 0], [1, 0], [2, 0]), ([0, 1], [1, 0], [2, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
((), ([0, 0],), ([0, 1],), ([1, 0],))
((), ([0, 0],), ([0, 1],), ([2, 0],))
((), ([0, 0],), ([0, 1],), ([0, 0], [0, 1]))
((), ([0, 0],), ([0, 1],), ([0, 0], [1, 0]))
((), ([0, 0],), ([0, 1],), ([0, 0], [2, 0]))
((), ([0, 0],), ([0, 1],), ([0, 1], [1, 0]))
((), ([0, 0],), ([0, 1],), ([0, 1], [2, 0]))
((), ([0, 0],), ([0, 1],), ([1, 0], [2, 0]))
((), ([0, 0],), ([0, 1],), ([0, 0], [0, 1], [1, 0]))
((), ([0, 0],), ([0, 1],), ([0, 0], [0, 1], [2, 0]))
((), ([0, 0],), ([0, 1],), ([0, 0], [1, 0], [2, 0]))
((), ([0, 0],), ([0, 1],), ([0, 1], [1, 0], [2, 0]))
((), ([0, 0],), ([0, 1],), ([0, 0], [0, 1], [1, 0], [2, 0]))
((), ([0, 0],), ([1, 0],), ([2, 0],))
((), ([0, 0],), ([1, 0],), ([0, 0], [0, 1]))
((), ([0, 0],), ([1, 0],), ([0, 0], [1, 0]))
((), ([0, 0],), ([1, 0],), ([0, 0], [2, 0]))
((), ([0, 0],), ([1, 0],), ([0, 1], [1, 0]))
((), ([0, 0],), ([1, 0],), ([0, 1], [2, 0]))
((), ([0, 0],), ([1, 0],), ([1, 0], [2, 0]))
((), ([0, 0],), ([1, 0],), ([0, 0], [0, 1], [1, 0]))
((), ([0, 0],), ([1, 0],), ([0, 0], [0, 1], [2, 0]))
((), ([0, 0],), ([1, 0],), ([0, 0], [1, 0], [2, 0]))
((), ([0, 0],), ([1, 0],), ([0, 1], [1, 0], [2, 0]))
((), ([0, 0],), ([1, 0],), ([0, 0], [0, 1], [1, 0], [2, 0]))
((), ([0, 0],), ([2, 0],), ([0, 0], [0, 1]))
((), ([0, 0],), ([2, 0],), ([0, 0], [1, 0]))
((), ([0, 0],), ([2, 0],), ([0, 0], [2, 0]))
((), ([0, 0],), ([2, 0],), ([0, 1], [1, 0]))
((), ([0, 0],), ([2, 0],), ([0, 1], [2, 0]))
((), ([0, 0],), ([2, 0],), ([1, 0], [2, 0]))
((), ([0, 0],), ([2, 0],), ([0, 0], [0, 1], [1, 0]))
((), ([0, 0],), ([2, 0],), ([0, 0], [0, 1], [2, 0]))
((), ([0, 0],), ([2, 0],), ([0, 0], [1, 0], [2, 0]))
((), ([0, 0],), ([2, 0],), ([0, 1], [1, 0], [2, 0]))
((), ([0, 0],), ([2, 0],), ([0, 0], [0, 1], [1, 0], [2, 0]))
((), ([0, 0],), ([0, 0], [0, 1]), ([0, 0], [1, 0]))
((), ([0, 0],), ([0, 0], [0, 1]), ([0, 0], [2, 0]))
((), ([0, 0],), ([0, 0], [0, 1]), ([0, 1], [1, 0]))
((), ([0, 0],), ([0, 0], [0, 1]), ([0, 1], [2, 0]))
((), ([0, 0],), ([0, 0], [0, 1]), ([1, 0], [2, 0]))
((), ([0, 0],), ([0, 0], [0, 1]), ([0, 0], [0, 1], [1, 0]))
((), ([0, 0],), ([0, 0], [0, 1]), ([0, 0], [0, 1], [2, 0]))
((), ([0, 0],), ([0, 0], [0, 1]), ([0, 0], [1, 0], [2, 0]))
((), ([0, 0],), ([0, 0], [0, 1]), ([0, 1], [1, 0], [2, 0]))
((), ([0, 0],), ([0, 0], [0, 1]), ([0, 0], [0, 1], [1, 0], [2, 0]))
((), ([0, 0],), ([0, 0], [1, 0]), ([0, 0], [2, 0]))
((), ([0, 0],), ([0, 0], [1, 0]), ([0, 1], [1, 0]))
((), ([0, 0],), ([0, 0], [1, 0]), ([0, 1], [2, 0]))
((), ([0, 0],), ([0, 0], [1, 0]), ([1, 0], [2, 0]))
((), ([0, 0],), ([0, 0], [1, 0]), ([0, 0], [0, 1], [1, 0]))
((), ([0, 0],), ([0, 0], [1, 0]), ([0, 0], [0, 1], [2, 0]))
((), ([0, 0],), ([0, 0], [1, 0]), ([0, 0], [1, 0], [2, 0]))
((), ([0, 0],), ([0, 0], [1, 0]), ([0, 1], [1, 0], [2, 0]))
((), ([0, 0],), ([0, 0], [1, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
((), ([0, 0],), ([0, 0], [2, 0]), ([0, 1], [1, 0]))
((), ([0, 0],), ([0, 0], [2, 0]), ([0, 1], [2, 0]))
((), ([0, 0],), ([0, 0], [2, 0]), ([1, 0], [2, 0]))
((), ([0, 0],), ([0, 0], [2, 0]), ([0, 0], [0, 1], [1, 0]))
((), ([0, 0],), ([0, 0], [2, 0]), ([0, 0], [0, 1], [2, 0]))
((), ([0, 0],), ([0, 0], [2, 0]), ([0, 0], [1, 0], [2, 0]))
((), ([0, 0],), ([0, 0], [2, 0]), ([0, 1], [1, 0], [2, 0]))
((), ([0, 0],), ([0, 0], [2, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
((), ([0, 0],), ([0, 1], [1, 0]), ([0, 1], [2, 0]))
((), ([0, 0],), ([0, 1], [1, 0]), ([1, 0], [2, 0]))
((), ([0, 0],), ([0, 1], [1, 0]), ([0, 0], [0, 1], [1, 0]))
((), ([0, 0],), ([0, 1], [1, 0]), ([0, 0], [0, 1], [2, 0]))
((), ([0, 0],), ([0, 1], [1, 0]), ([0, 0], [1, 0], [2, 0]))
((), ([0, 0],), ([0, 1], [1, 0]), ([0, 1], [1, 0], [2, 0]))
((), ([0, 0],), ([0, 1], [1, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
((), ([0, 0],), ([0, 1], [2, 0]), ([1, 0], [2, 0]))
((), ([0, 0],), ([0, 1], [2, 0]), ([0, 0], [0, 1], [1, 0]))
((), ([0, 0],), ([0, 1], [2, 0]), ([0, 0], [0, 1], [2, 0]))
((), ([0, 0],), ([0, 1], [2, 0]), ([0, 0], [1, 0], [2, 0]))
((), ([0, 0],), ([0, 1], [2, 0]), ([0, 1], [1, 0], [2, 0]))
((), ([0, 0],), ([0, 1], [2, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
((), ([0, 0],), ([1, 0], [2, 0]), ([0, 0], [0, 1], [1, 0]))
((), ([0, 0],), ([1, 0], [2, 0]), ([0, 0], [0, 1], [2, 0]))
((), ([0, 0],), ([1, 0], [2, 0]), ([0, 0], [1, 0], [2, 0]))
((), ([0, 0],), ([1, 0], [2, 0]), ([0, 1], [1, 0], [2, 0]))
((), ([0, 0],), ([1, 0], [2, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
((), ([0, 0],), ([0, 0], [0, 1], [1, 0]), ([0, 0], [0, 1], [2, 0]))
((), ([0, 0],), ([0, 0], [0, 1], [1, 0]), ([0, 0], [1, 0], [2, 0]))
((), ([0, 0],), ([0, 0], [0, 1], [1, 0]), ([0, 1], [1, 0], [2, 0]))
((), ([0, 0],), ([0, 0], [0, 1], [1, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
((), ([0, 0],), ([0, 0], [0, 1], [2, 0]), ([0, 0], [1, 0], [2, 0]))
((), ([0, 0],), ([0, 0], [0, 1], [2, 0]), ([0, 1], [1, 0], [2, 0]))
((), ([0, 0],), ([0, 0], [0, 1], [2, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
((), ([0, 0],), ([0, 0], [1, 0], [2, 0]), ([0, 1], [1, 0], [2, 0]))
((), ([0, 0],), ([0, 0], [1, 0], [2, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
((), ([0, 0],), ([0, 1], [1, 0], [2, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
((), ([0, 1],), ([1, 0],), ([2, 0],))
((), ([0, 1],), ([1, 0],), ([0, 0], [0, 1]))
((), ([0, 1],), ([1, 0],), ([0, 0], [1, 0]))
((), ([0, 1],), ([1, 0],), ([0, 0], [2, 0]))
((), ([0, 1],), ([1, 0],), ([0, 1], [1, 0]))
((), ([0, 1],), ([1, 0],), ([0, 1], [2, 0]))
((), ([0, 1],), ([1, 0],), ([1, 0], [2, 0]))
((), ([0, 1],), ([1, 0],), ([0, 0], [0, 1], [1, 0]))
((), ([0, 1],), ([1, 0],), ([0, 0], [0, 1], [2, 0]))
((), ([0, 1],), ([1, 0],), ([0, 0], [1, 0], [2, 0]))
((), ([0, 1],), ([1, 0],), ([0, 1], [1, 0], [2, 0]))
((), ([0, 1],), ([1, 0],), ([0, 0], [0, 1], [1, 0], [2, 0]))
((), ([0, 1],), ([2, 0],), ([0, 0], [0, 1]))
((), ([0, 1],), ([2, 0],), ([0, 0], [1, 0]))
((), ([0, 1],), ([2, 0],), ([0, 0], [2, 0]))
((), ([0, 1],), ([2, 0],), ([0, 1], [1, 0]))
((), ([0, 1],), ([2, 0],), ([0, 1], [2, 0]))
((), ([0, 1],), ([2, 0],), ([1, 0], [2, 0]))
((), ([0, 1],), ([2, 0],), ([0, 0], [0, 1], [1, 0]))
((), ([0, 1],), ([2, 0],), ([0, 0], [0, 1], [2, 0]))
((), ([0, 1],), ([2, 0],), ([0, 0], [1, 0], [2, 0]))
((), ([0, 1],), ([2, 0],), ([0, 1], [1, 0], [2, 0]))
((), ([0, 1],), ([2, 0],), ([0, 0], [0, 1], [1, 0], [2, 0]))
((), ([0, 1],), ([0, 0], [0, 1]), ([0, 0], [1, 0]))
((), ([0, 1],), ([0, 0], [0, 1]), ([0, 0], [2, 0]))
((), ([0, 1],), ([0, 0], [0, 1]), ([0, 1], [1, 0]))
((), ([0, 1],), ([0, 0], [0, 1]), ([0, 1], [2, 0]))
((), ([0, 1],), ([0, 0], [0, 1]), ([1, 0], [2, 0]))
((), ([0, 1],), ([0, 0], [0, 1]), ([0, 0], [0, 1], [1, 0]))
((), ([0, 1],), ([0, 0], [0, 1]), ([0, 0], [0, 1], [2, 0]))
((), ([0, 1],), ([0, 0], [0, 1]), ([0, 0], [1, 0], [2, 0]))
((), ([0, 1],), ([0, 0], [0, 1]), ([0, 1], [1, 0], [2, 0]))
((), ([0, 1],), ([0, 0], [0, 1]), ([0, 0], [0, 1], [1, 0], [2, 0]))
((), ([0, 1],), ([0, 0], [1, 0]), ([0, 0], [2, 0]))
((), ([0, 1],), ([0, 0], [1, 0]), ([0, 1], [1, 0]))
((), ([0, 1],), ([0, 0], [1, 0]), ([0, 1], [2, 0]))
((), ([0, 1],), ([0, 0], [1, 0]), ([1, 0], [2, 0]))
((), ([0, 1],), ([0, 0], [1, 0]), ([0, 0], [0, 1], [1, 0]))
((), ([0, 1],), ([0, 0], [1, 0]), ([0, 0], [0, 1], [2, 0]))
((), ([0, 1],), ([0, 0], [1, 0]), ([0, 0], [1, 0], [2, 0]))
((), ([0, 1],), ([0, 0], [1, 0]), ([0, 1], [1, 0], [2, 0]))
((), ([0, 1],), ([0, 0], [1, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
((), ([0, 1],), ([0, 0], [2, 0]), ([0, 1], [1, 0]))
((), ([0, 1],), ([0, 0], [2, 0]), ([0, 1], [2, 0]))
((), ([0, 1],), ([0, 0], [2, 0]), ([1, 0], [2, 0]))
((), ([0, 1],), ([0, 0], [2, 0]), ([0, 0], [0, 1], [1, 0]))
((), ([0, 1],), ([0, 0], [2, 0]), ([0, 0], [0, 1], [2, 0]))
((), ([0, 1],), ([0, 0], [2, 0]), ([0, 0], [1, 0], [2, 0]))
((), ([0, 1],), ([0, 0], [2, 0]), ([0, 1], [1, 0], [2, 0]))
((), ([0, 1],), ([0, 0], [2, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
((), ([0, 1],), ([0, 1], [1, 0]), ([0, 1], [2, 0]))
((), ([0, 1],), ([0, 1], [1, 0]), ([1, 0], [2, 0]))
((), ([0, 1],), ([0, 1], [1, 0]), ([0, 0], [0, 1], [1, 0]))
((), ([0, 1],), ([0, 1], [1, 0]), ([0, 0], [0, 1], [2, 0]))
((), ([0, 1],), ([0, 1], [1, 0]), ([0, 0], [1, 0], [2, 0]))
((), ([0, 1],), ([0, 1], [1, 0]), ([0, 1], [1, 0], [2, 0]))
((), ([0, 1],), ([0, 1], [1, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
((), ([0, 1],), ([0, 1], [2, 0]), ([1, 0], [2, 0]))
((), ([0, 1],), ([0, 1], [2, 0]), ([0, 0], [0, 1], [1, 0]))
((), ([0, 1],), ([0, 1], [2, 0]), ([0, 0], [0, 1], [2, 0]))
((), ([0, 1],), ([0, 1], [2, 0]), ([0, 0], [1, 0], [2, 0]))
((), ([0, 1],), ([0, 1], [2, 0]), ([0, 1], [1, 0], [2, 0]))
((), ([0, 1],), ([0, 1], [2, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
((), ([0, 1],), ([1, 0], [2, 0]), ([0, 0], [0, 1], [1, 0]))
((), ([0, 1],), ([1, 0], [2, 0]), ([0, 0], [0, 1], [2, 0]))
((), ([0, 1],), ([1, 0], [2, 0]), ([0, 0], [1, 0], [2, 0]))
((), ([0, 1],), ([1, 0], [2, 0]), ([0, 1], [1, 0], [2, 0]))
((), ([0, 1],), ([1, 0], [2, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
((), ([0, 1],), ([0, 0], [0, 1], [1, 0]), ([0, 0], [0, 1], [2, 0]))
((), ([0, 1],), ([0, 0], [0, 1], [1, 0]), ([0, 0], [1, 0], [2, 0]))
((), ([0, 1],), ([0, 0], [0, 1], [1, 0]), ([0, 1], [1, 0], [2, 0]))
((), ([0, 1],), ([0, 0], [0, 1], [1, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
((), ([0, 1],), ([0, 0], [0, 1], [2, 0]), ([0, 0], [1, 0], [2, 0]))
((), ([0, 1],), ([0, 0], [0, 1], [2, 0]), ([0, 1], [1, 0], [2, 0]))
((), ([0, 1],), ([0, 0], [0, 1], [2, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
((), ([0, 1],), ([0, 0], [1, 0], [2, 0]), ([0, 1], [1, 0], [2, 0]))
((), ([0, 1],), ([0, 0], [1, 0], [2, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
((), ([0, 1],), ([0, 1], [1, 0], [2, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
((), ([1, 0],), ([2, 0],), ([0, 0], [0, 1]))
((), ([1, 0],), ([2, 0],), ([0, 0], [1, 0]))
((), ([1, 0],), ([2, 0],), ([0, 0], [2, 0]))
((), ([1, 0],), ([2, 0],), ([0, 1], [1, 0]))
((), ([1, 0],), ([2, 0],), ([0, 1], [2, 0]))
((), ([1, 0],), ([2, 0],), ([1, 0], [2, 0]))
((), ([1, 0],), ([2, 0],), ([0, 0], [0, 1], [1, 0]))
((), ([1, 0],), ([2, 0],), ([0, 0], [0, 1], [2, 0]))
((), ([1, 0],), ([2, 0],), ([0, 0], [1, 0], [2, 0]))
((), ([1, 0],), ([2, 0],), ([0, 1], [1, 0], [2, 0]))
((), ([1, 0],), ([2, 0],), ([0, 0], [0, 1], [1, 0], [2, 0]))
((), ([1, 0],), ([0, 0], [0, 1]), ([0, 0], [1, 0]))
((), ([1, 0],), ([0, 0], [0, 1]), ([0, 0], [2, 0]))
((), ([1, 0],), ([0, 0], [0, 1]), ([0, 1], [1, 0]))
((), ([1, 0],), ([0, 0], [0, 1]), ([0, 1], [2, 0]))
((), ([1, 0],), ([0, 0], [0, 1]), ([1, 0], [2, 0]))
((), ([1, 0],), ([0, 0], [0, 1]), ([0, 0], [0, 1], [1, 0]))
((), ([1, 0],), ([0, 0], [0, 1]), ([0, 0], [0, 1], [2, 0]))
((), ([1, 0],), ([0, 0], [0, 1]), ([0, 0], [1, 0], [2, 0]))
((), ([1, 0],), ([0, 0], [0, 1]), ([0, 1], [1, 0], [2, 0]))
((), ([1, 0],), ([0, 0], [0, 1]), ([0, 0], [0, 1], [1, 0], [2, 0]))
((), ([1, 0],), ([0, 0], [1, 0]), ([0, 0], [2, 0]))
((), ([1, 0],), ([0, 0], [1, 0]), ([0, 1], [1, 0]))
((), ([1, 0],), ([0, 0], [1, 0]), ([0, 1], [2, 0]))
((), ([1, 0],), ([0, 0], [1, 0]), ([1, 0], [2, 0]))
((), ([1, 0],), ([0, 0], [1, 0]), ([0, 0], [0, 1], [1, 0]))
((), ([1, 0],), ([0, 0], [1, 0]), ([0, 0], [0, 1], [2, 0]))
((), ([1, 0],), ([0, 0], [1, 0]), ([0, 0], [1, 0], [2, 0]))
((), ([1, 0],), ([0, 0], [1, 0]), ([0, 1], [1, 0], [2, 0]))
((), ([1, 0],), ([0, 0], [1, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
((), ([1, 0],), ([0, 0], [2, 0]), ([0, 1], [1, 0]))
((), ([1, 0],), ([0, 0], [2, 0]), ([0, 1], [2, 0]))
((), ([1, 0],), ([0, 0], [2, 0]), ([1, 0], [2, 0]))
((), ([1, 0],), ([0, 0], [2, 0]), ([0, 0], [0, 1], [1, 0]))
((), ([1, 0],), ([0, 0], [2, 0]), ([0, 0], [0, 1], [2, 0]))
((), ([1, 0],), ([0, 0], [2, 0]), ([0, 0], [1, 0], [2, 0]))
((), ([1, 0],), ([0, 0], [2, 0]), ([0, 1], [1, 0], [2, 0]))
((), ([1, 0],), ([0, 0], [2, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
((), ([1, 0],), ([0, 1], [1, 0]), ([0, 1], [2, 0]))
((), ([1, 0],), ([0, 1], [1, 0]), ([1, 0], [2, 0]))
((), ([1, 0],), ([0, 1], [1, 0]), ([0, 0], [0, 1], [1, 0]))
((), ([1, 0],), ([0, 1], [1, 0]), ([0, 0], [0, 1], [2, 0]))
((), ([1, 0],), ([0, 1], [1, 0]), ([0, 0], [1, 0], [2, 0]))
((), ([1, 0],), ([0, 1], [1, 0]), ([0, 1], [1, 0], [2, 0]))
((), ([1, 0],), ([0, 1], [1, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
((), ([1, 0],), ([0, 1], [2, 0]), ([1, 0], [2, 0]))
((), ([1, 0],), ([0, 1], [2, 0]), ([0, 0], [0, 1], [1, 0]))
((), ([1, 0],), ([0, 1], [2, 0]), ([0, 0], [0, 1], [2, 0]))
((), ([1, 0],), ([0, 1], [2, 0]), ([0, 0], [1, 0], [2, 0]))
((), ([1, 0],), ([0, 1], [2, 0]), ([0, 1], [1, 0], [2, 0]))
((), ([1, 0],), ([0, 1], [2, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
((), ([1, 0],), ([1, 0], [2, 0]), ([0, 0], [0, 1], [1, 0]))
((), ([1, 0],), ([1, 0], [2, 0]), ([0, 0], [0, 1], [2, 0]))
((), ([1, 0],), ([1, 0], [2, 0]), ([0, 0], [1, 0], [2, 0]))
((), ([1, 0],), ([1, 0], [2, 0]), ([0, 1], [1, 0], [2, 0]))
((), ([1, 0],), ([1, 0], [2, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
((), ([1, 0],), ([0, 0], [0, 1], [1, 0]), ([0, 0], [0, 1], [2, 0]))
((), ([1, 0],), ([0, 0], [0, 1], [1, 0]), ([0, 0], [1, 0], [2, 0]))
((), ([1, 0],), ([0, 0], [0, 1], [1, 0]), ([0, 1], [1, 0], [2, 0]))
((), ([1, 0],), ([0, 0], [0, 1], [1, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
((), ([1, 0],), ([0, 0], [0, 1], [2, 0]), ([0, 0], [1, 0], [2, 0]))
((), ([1, 0],), ([0, 0], [0, 1], [2, 0]), ([0, 1], [1, 0], [2, 0]))
((), ([1, 0],), ([0, 0], [0, 1], [2, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
((), ([1, 0],), ([0, 0], [1, 0], [2, 0]), ([0, 1], [1, 0], [2, 0]))
((), ([1, 0],), ([0, 0], [1, 0], [2, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
((), ([1, 0],), ([0, 1], [1, 0], [2, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
((), ([2, 0],), ([0, 0], [0, 1]), ([0, 0], [1, 0]))
((), ([2, 0],), ([0, 0], [0, 1]), ([0, 0], [2, 0]))
((), ([2, 0],), ([0, 0], [0, 1]), ([0, 1], [1, 0]))
((), ([2, 0],), ([0, 0], [0, 1]), ([0, 1], [2, 0]))
((), ([2, 0],), ([0, 0], [0, 1]), ([1, 0], [2, 0]))
((), ([2, 0],), ([0, 0], [0, 1]), ([0, 0], [0, 1], [1, 0]))
((), ([2, 0],), ([0, 0], [0, 1]), ([0, 0], [0, 1], [2, 0]))
((), ([2, 0],), ([0, 0], [0, 1]), ([0, 0], [1, 0], [2, 0]))
((), ([2, 0],), ([0, 0], [0, 1]), ([0, 1], [1, 0], [2, 0]))
((), ([2, 0],), ([0, 0], [0, 1]), ([0, 0], [0, 1], [1, 0], [2, 0]))
((), ([2, 0],), ([0, 0], [1, 0]), ([0, 0], [2, 0]))
((), ([2, 0],), ([0, 0], [1, 0]), ([0, 1], [1, 0]))
((), ([2, 0],), ([0, 0], [1, 0]), ([0, 1], [2, 0]))
((), ([2, 0],), ([0, 0], [1, 0]), ([1, 0], [2, 0]))
((), ([2, 0],), ([0, 0], [1, 0]), ([0, 0], [0, 1], [1, 0]))
((), ([2, 0],), ([0, 0], [1, 0]), ([0, 0], [0, 1], [2, 0]))
((), ([2, 0],), ([0, 0], [1, 0]), ([0, 0], [1, 0], [2, 0]))
((), ([2, 0],), ([0, 0], [1, 0]), ([0, 1], [1, 0], [2, 0]))
((), ([2, 0],), ([0, 0], [1, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
((), ([2, 0],), ([0, 0], [2, 0]), ([0, 1], [1, 0]))
((), ([2, 0],), ([0, 0], [2, 0]), ([0, 1], [2, 0]))
((), ([2, 0],), ([0, 0], [2, 0]), ([1, 0], [2, 0]))
((), ([2, 0],), ([0, 0], [2, 0]), ([0, 0], [0, 1], [1, 0]))
((), ([2, 0],), ([0, 0], [2, 0]), ([0, 0], [0, 1], [2, 0]))
((), ([2, 0],), ([0, 0], [2, 0]), ([0, 0], [1, 0], [2, 0]))
((), ([2, 0],), ([0, 0], [2, 0]), ([0, 1], [1, 0], [2, 0]))
((), ([2, 0],), ([0, 0], [2, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
((), ([2, 0],), ([0, 1], [1, 0]), ([0, 1], [2, 0]))
((), ([2, 0],), ([0, 1], [1, 0]), ([1, 0], [2, 0]))
((), ([2, 0],), ([0, 1], [1, 0]), ([0, 0], [0, 1], [1, 0]))
((), ([2, 0],), ([0, 1], [1, 0]), ([0, 0], [0, 1], [2, 0]))
((), ([2, 0],), ([0, 1], [1, 0]), ([0, 0], [1, 0], [2, 0]))
((), ([2, 0],), ([0, 1], [1, 0]), ([0, 1], [1, 0], [2, 0]))
((), ([2, 0],), ([0, 1], [1, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
((), ([2, 0],), ([0, 1], [2, 0]), ([1, 0], [2, 0]))
((), ([2, 0],), ([0, 1], [2, 0]), ([0, 0], [0, 1], [1, 0]))
((), ([2, 0],), ([0, 1], [2, 0]), ([0, 0], [0, 1], [2, 0]))
((), ([2, 0],), ([0, 1], [2, 0]), ([0, 0], [1, 0], [2, 0]))
((), ([2, 0],), ([0, 1], [2, 0]), ([0, 1], [1, 0], [2, 0]))
((), ([2, 0],), ([0, 1], [2, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
((), ([2, 0],), ([1, 0], [2, 0]), ([0, 0], [0, 1], [1, 0]))
((), ([2, 0],), ([1, 0], [2, 0]), ([0, 0], [0, 1], [2, 0]))
((), ([2, 0],), ([1, 0], [2, 0]), ([0, 0], [1, 0], [2, 0]))
((), ([2, 0],), ([1, 0], [2, 0]), ([0, 1], [1, 0], [2, 0]))
((), ([2, 0],), ([1, 0], [2, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
((), ([2, 0],), ([0, 0], [0, 1], [1, 0]), ([0, 0], [0, 1], [2, 0]))
((), ([2, 0],), ([0, 0], [0, 1], [1, 0]), ([0, 0], [1, 0], [2, 0]))
((), ([2, 0],), ([0, 0], [0, 1], [1, 0]), ([0, 1], [1, 0], [2, 0]))
((), ([2, 0],), ([0, 0], [0, 1], [1, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
((), ([2, 0],), ([0, 0], [0, 1], [2, 0]), ([0, 0], [1, 0], [2, 0]))
((), ([2, 0],), ([0, 0], [0, 1], [2, 0]), ([0, 1], [1, 0], [2, 0]))
((), ([2, 0],), ([0, 0], [0, 1], [2, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
((), ([2, 0],), ([0, 0], [1, 0], [2, 0]), ([0, 1], [1, 0], [2, 0]))
((), ([2, 0],), ([0, 0], [1, 0], [2, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
((), ([2, 0],), ([0, 1], [1, 0], [2, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
((), ([0, 0], [0, 1]), ([0, 0], [1, 0]), ([0, 0], [2, 0]))
((), ([0, 0], [0, 1]), ([0, 0], [1, 0]), ([0, 1], [1, 0]))
((), ([0, 0], [0, 1]), ([0, 0], [1, 0]), ([0, 1], [2, 0]))
((), ([0, 0], [0, 1]), ([0, 0], [1, 0]), ([1, 0], [2, 0]))
((), ([0, 0], [0, 1]), ([0, 0], [1, 0]), ([0, 0], [0, 1], [1, 0]))
((), ([0, 0], [0, 1]), ([0, 0], [1, 0]), ([0, 0], [0, 1], [2, 0]))
((), ([0, 0], [0, 1]), ([0, 0], [1, 0]), ([0, 0], [1, 0], [2, 0]))
((), ([0, 0], [0, 1]), ([0, 0], [1, 0]), ([0, 1], [1, 0], [2, 0]))
((), ([0, 0], [0, 1]), ([0, 0], [1, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
((), ([0, 0], [0, 1]), ([0, 0], [2, 0]), ([0, 1], [1, 0]))
((), ([0, 0], [0, 1]), ([0, 0], [2, 0]), ([0, 1], [2, 0]))
((), ([0, 0], [0, 1]), ([0, 0], [2, 0]), ([1, 0], [2, 0]))
((), ([0, 0], [0, 1]), ([0, 0], [2, 0]), ([0, 0], [0, 1], [1, 0]))
((), ([0, 0], [0, 1]), ([0, 0], [2, 0]), ([0, 0], [0, 1], [2, 0]))
((), ([0, 0], [0, 1]), ([0, 0], [2, 0]), ([0, 0], [1, 0], [2, 0]))
((), ([0, 0], [0, 1]), ([0, 0], [2, 0]), ([0, 1], [1, 0], [2, 0]))
((), ([0, 0], [0, 1]), ([0, 0], [2, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
((), ([0, 0], [0, 1]), ([0, 1], [1, 0]), ([0, 1], [2, 0]))
((), ([0, 0], [0, 1]), ([0, 1], [1, 0]), ([1, 0], [2, 0]))
((), ([0, 0], [0, 1]), ([0, 1], [1, 0]), ([0, 0], [0, 1], [1, 0]))
((), ([0, 0], [0, 1]), ([0, 1], [1, 0]), ([0, 0], [0, 1], [2, 0]))
((), ([0, 0], [0, 1]), ([0, 1], [1, 0]), ([0, 0], [1, 0], [2, 0]))
((), ([0, 0], [0, 1]), ([0, 1], [1, 0]), ([0, 1], [1, 0], [2, 0]))
((), ([0, 0], [0, 1]), ([0, 1], [1, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
((), ([0, 0], [0, 1]), ([0, 1], [2, 0]), ([1, 0], [2, 0]))
((), ([0, 0], [0, 1]), ([0, 1], [2, 0]), ([0, 0], [0, 1], [1, 0]))
((), ([0, 0], [0, 1]), ([0, 1], [2, 0]), ([0, 0], [0, 1], [2, 0]))
((), ([0, 0], [0, 1]), ([0, 1], [2, 0]), ([0, 0], [1, 0], [2, 0]))
((), ([0, 0], [0, 1]), ([0, 1], [2, 0]), ([0, 1], [1, 0], [2, 0]))
((), ([0, 0], [0, 1]), ([0, 1], [2, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
((), ([0, 0], [0, 1]), ([1, 0], [2, 0]), ([0, 0], [0, 1], [1, 0]))
((), ([0, 0], [0, 1]), ([1, 0], [2, 0]), ([0, 0], [0, 1], [2, 0]))
((), ([0, 0], [0, 1]), ([1, 0], [2, 0]), ([0, 0], [1, 0], [2, 0]))
((), ([0, 0], [0, 1]), ([1, 0], [2, 0]), ([0, 1], [1, 0], [2, 0]))
((), ([0, 0], [0, 1]), ([1, 0], [2, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
((), ([0, 0], [0, 1]), ([0, 0], [0, 1], [1, 0]), ([0, 0], [0, 1], [2, 0]))
((), ([0, 0], [0, 1]), ([0, 0], [0, 1], [1, 0]), ([0, 0], [1, 0], [2, 0]))
((), ([0, 0], [0, 1]), ([0, 0], [0, 1], [1, 0]), ([0, 1], [1, 0], [2, 0]))
((), ([0, 0], [0, 1]), ([0, 0], [0, 1], [1, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
((), ([0, 0], [0, 1]), ([0, 0], [0, 1], [2, 0]), ([0, 0], [1, 0], [2, 0]))
((), ([0, 0], [0, 1]), ([0, 0], [0, 1], [2, 0]), ([0, 1], [1, 0], [2, 0]))
((), ([0, 0], [0, 1]), ([0, 0], [0, 1], [2, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
((), ([0, 0], [0, 1]), ([0, 0], [1, 0], [2, 0]), ([0, 1], [1, 0], [2, 0]))
((), ([0, 0], [0, 1]), ([0, 0], [1, 0], [2, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
((), ([0, 0], [0, 1]), ([0, 1], [1, 0], [2, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
((), ([0, 0], [1, 0]), ([0, 0], [2, 0]), ([0, 1], [1, 0]))
((), ([0, 0], [1, 0]), ([0, 0], [2, 0]), ([0, 1], [2, 0]))
((), ([0, 0], [1, 0]), ([0, 0], [2, 0]), ([1, 0], [2, 0]))
((), ([0, 0], [1, 0]), ([0, 0], [2, 0]), ([0, 0], [0, 1], [1, 0]))
((), ([0, 0], [1, 0]), ([0, 0], [2, 0]), ([0, 0], [0, 1], [2, 0]))
((), ([0, 0], [1, 0]), ([0, 0], [2, 0]), ([0, 0], [1, 0], [2, 0]))
((), ([0, 0], [1, 0]), ([0, 0], [2, 0]), ([0, 1], [1, 0], [2, 0]))
((), ([0, 0], [1, 0]), ([0, 0], [2, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
((), ([0, 0], [1, 0]), ([0, 1], [1, 0]), ([0, 1], [2, 0]))
((), ([0, 0], [1, 0]), ([0, 1], [1, 0]), ([1, 0], [2, 0]))
((), ([0, 0], [1, 0]), ([0, 1], [1, 0]), ([0, 0], [0, 1], [1, 0]))
((), ([0, 0], [1, 0]), ([0, 1], [1, 0]), ([0, 0], [0, 1], [2, 0]))
((), ([0, 0], [1, 0]), ([0, 1], [1, 0]), ([0, 0], [1, 0], [2, 0]))
((), ([0, 0], [1, 0]), ([0, 1], [1, 0]), ([0, 1], [1, 0], [2, 0]))
((), ([0, 0], [1, 0]), ([0, 1], [1, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
((), ([0, 0], [1, 0]), ([0, 1], [2, 0]), ([1, 0], [2, 0]))
((), ([0, 0], [1, 0]), ([0, 1], [2, 0]), ([0, 0], [0, 1], [1, 0]))
((), ([0, 0], [1, 0]), ([0, 1], [2, 0]), ([0, 0], [0, 1], [2, 0]))
((), ([0, 0], [1, 0]), ([0, 1], [2, 0]), ([0, 0], [1, 0], [2, 0]))
((), ([0, 0], [1, 0]), ([0, 1], [2, 0]), ([0, 1], [1, 0], [2, 0]))
((), ([0, 0], [1, 0]), ([0, 1], [2, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
((), ([0, 0], [1, 0]), ([1, 0], [2, 0]), ([0, 0], [0, 1], [1, 0]))
((), ([0, 0], [1, 0]), ([1, 0], [2, 0]), ([0, 0], [0, 1], [2, 0]))
((), ([0, 0], [1, 0]), ([1, 0], [2, 0]), ([0, 0], [1, 0], [2, 0]))
((), ([0, 0], [1, 0]), ([1, 0], [2, 0]), ([0, 1], [1, 0], [2, 0]))
((), ([0, 0], [1, 0]), ([1, 0], [2, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
((), ([0, 0], [1, 0]), ([0, 0], [0, 1], [1, 0]), ([0, 0], [0, 1], [2, 0]))
((), ([0, 0], [1, 0]), ([0, 0], [0, 1], [1, 0]), ([0, 0], [1, 0], [2, 0]))
((), ([0, 0], [1, 0]), ([0, 0], [0, 1], [1, 0]), ([0, 1], [1, 0], [2, 0]))
((), ([0, 0], [1, 0]), ([0, 0], [0, 1], [1, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
((), ([0, 0], [1, 0]), ([0, 0], [0, 1], [2, 0]), ([0, 0], [1, 0], [2, 0]))
((), ([0, 0], [1, 0]), ([0, 0], [0, 1], [2, 0]), ([0, 1], [1, 0], [2, 0]))
((), ([0, 0], [1, 0]), ([0, 0], [0, 1], [2, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
((), ([0, 0], [1, 0]), ([0, 0], [1, 0], [2, 0]), ([0, 1], [1, 0], [2, 0]))
((), ([0, 0], [1, 0]), ([0, 0], [1, 0], [2, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
((), ([0, 0], [1, 0]), ([0, 1], [1, 0], [2, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
((), ([0, 0], [2, 0]), ([0, 1], [1, 0]), ([0, 1], [2, 0]))
((), ([0, 0], [2, 0]), ([0, 1], [1, 0]), ([1, 0], [2, 0]))
((), ([0, 0], [2, 0]), ([0, 1], [1, 0]), ([0, 0], [0, 1], [1, 0]))
((), ([0, 0], [2, 0]), ([0, 1], [1, 0]), ([0, 0], [0, 1], [2, 0]))
((), ([0, 0], [2, 0]), ([0, 1], [1, 0]), ([0, 0], [1, 0], [2, 0]))
((), ([0, 0], [2, 0]), ([0, 1], [1, 0]), ([0, 1], [1, 0], [2, 0]))
((), ([0, 0], [2, 0]), ([0, 1], [1, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
((), ([0, 0], [2, 0]), ([0, 1], [2, 0]), ([1, 0], [2, 0]))
((), ([0, 0], [2, 0]), ([0, 1], [2, 0]), ([0, 0], [0, 1], [1, 0]))
((), ([0, 0], [2, 0]), ([0, 1], [2, 0]), ([0, 0], [0, 1], [2, 0]))
((), ([0, 0], [2, 0]), ([0, 1], [2, 0]), ([0, 0], [1, 0], [2, 0]))
((), ([0, 0], [2, 0]), ([0, 1], [2, 0]), ([0, 1], [1, 0], [2, 0]))
((), ([0, 0], [2, 0]), ([0, 1], [2, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
((), ([0, 0], [2, 0]), ([1, 0], [2, 0]), ([0, 0], [0, 1], [1, 0]))
((), ([0, 0], [2, 0]), ([1, 0], [2, 0]), ([0, 0], [0, 1], [2, 0]))
((), ([0, 0], [2, 0]), ([1, 0], [2, 0]), ([0, 0], [1, 0], [2, 0]))
((), ([0, 0], [2, 0]), ([1, 0], [2, 0]), ([0, 1], [1, 0], [2, 0]))
((), ([0, 0], [2, 0]), ([1, 0], [2, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
((), ([0, 0], [2, 0]), ([0, 0], [0, 1], [1, 0]), ([0, 0], [0, 1], [2, 0]))
((), ([0, 0], [2, 0]), ([0, 0], [0, 1], [1, 0]), ([0, 0], [1, 0], [2, 0]))
((), ([0, 0], [2, 0]), ([0, 0], [0, 1], [1, 0]), ([0, 1], [1, 0], [2, 0]))
((), ([0, 0], [2, 0]), ([0, 0], [0, 1], [1, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
((), ([0, 0], [2, 0]), ([0, 0], [0, 1], [2, 0]), ([0, 0], [1, 0], [2, 0]))
((), ([0, 0], [2, 0]), ([0, 0], [0, 1], [2, 0]), ([0, 1], [1, 0], [2, 0]))
((), ([0, 0], [2, 0]), ([0, 0], [0, 1], [2, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
((), ([0, 0], [2, 0]), ([0, 0], [1, 0], [2, 0]), ([0, 1], [1, 0], [2, 0]))
((), ([0, 0], [2, 0]), ([0, 0], [1, 0], [2, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
((), ([0, 0], [2, 0]), ([0, 1], [1, 0], [2, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
((), ([0, 1], [1, 0]), ([0, 1], [2, 0]), ([1, 0], [2, 0]))
((), ([0, 1], [1, 0]), ([0, 1], [2, 0]), ([0, 0], [0, 1], [1, 0]))
((), ([0, 1], [1, 0]), ([0, 1], [2, 0]), ([0, 0], [0, 1], [2, 0]))
((), ([0, 1], [1, 0]), ([0, 1], [2, 0]), ([0, 0], [1, 0], [2, 0]))
((), ([0, 1], [1, 0]), ([0, 1], [2, 0]), ([0, 1], [1, 0], [2, 0]))
((), ([0, 1], [1, 0]), ([0, 1], [2, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
((), ([0, 1], [1, 0]), ([1, 0], [2, 0]), ([0, 0], [0, 1], [1, 0]))
((), ([0, 1], [1, 0]), ([1, 0], [2, 0]), ([0, 0], [0, 1], [2, 0]))
((), ([0, 1], [1, 0]), ([1, 0], [2, 0]), ([0, 0], [1, 0], [2, 0]))
((), ([0, 1], [1, 0]), ([1, 0], [2, 0]), ([0, 1], [1, 0], [2, 0]))
((), ([0, 1], [1, 0]), ([1, 0], [2, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
((), ([0, 1], [1, 0]), ([0, 0], [0, 1], [1, 0]), ([0, 0], [0, 1], [2, 0]))
((), ([0, 1], [1, 0]), ([0, 0], [0, 1], [1, 0]), ([0, 0], [1, 0], [2, 0]))
((), ([0, 1], [1, 0]), ([0, 0], [0, 1], [1, 0]), ([0, 1], [1, 0], [2, 0]))
((), ([0, 1], [1, 0]), ([0, 0], [0, 1], [1, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
((), ([0, 1], [1, 0]), ([0, 0], [0, 1], [2, 0]), ([0, 0], [1, 0], [2, 0]))
((), ([0, 1], [1, 0]), ([0, 0], [0, 1], [2, 0]), ([0, 1], [1, 0], [2, 0]))
((), ([0, 1], [1, 0]), ([0, 0], [0, 1], [2, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
((), ([0, 1], [1, 0]), ([0, 0], [1, 0], [2, 0]), ([0, 1], [1, 0], [2, 0]))
((), ([0, 1], [1, 0]), ([0, 0], [1, 0], [2, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
((), ([0, 1], [1, 0]), ([0, 1], [1, 0], [2, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
((), ([0, 1], [2, 0]), ([1, 0], [2, 0]), ([0, 0], [0, 1], [1, 0]))
((), ([0, 1], [2, 0]), ([1, 0], [2, 0]), ([0, 0], [0, 1], [2, 0]))
((), ([0, 1], [2, 0]), ([1, 0], [2, 0]), ([0, 0], [1, 0], [2, 0]))
((), ([0, 1], [2, 0]), ([1, 0], [2, 0]), ([0, 1], [1, 0], [2, 0]))
((), ([0, 1], [2, 0]), ([1, 0], [2, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
((), ([0, 1], [2, 0]), ([0, 0], [0, 1], [1, 0]), ([0, 0], [0, 1], [2, 0]))
((), ([0, 1], [2, 0]), ([0, 0], [0, 1], [1, 0]), ([0, 0], [1, 0], [2, 0]))
((), ([0, 1], [2, 0]), ([0, 0], [0, 1], [1, 0]), ([0, 1], [1, 0], [2, 0]))
((), ([0, 1], [2, 0]), ([0, 0], [0, 1], [1, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
((), ([0, 1], [2, 0]), ([0, 0], [0, 1], [2, 0]), ([0, 0], [1, 0], [2, 0]))
((), ([0, 1], [2, 0]), ([0, 0], [0, 1], [2, 0]), ([0, 1], [1, 0], [2, 0]))
((), ([0, 1], [2, 0]), ([0, 0], [0, 1], [2, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
((), ([0, 1], [2, 0]), ([0, 0], [1, 0], [2, 0]), ([0, 1], [1, 0], [2, 0]))
((), ([0, 1], [2, 0]), ([0, 0], [1, 0], [2, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
((), ([0, 1], [2, 0]), ([0, 1], [1, 0], [2, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
((), ([1, 0], [2, 0]), ([0, 0], [0, 1], [1, 0]), ([0, 0], [0, 1], [2, 0]))
((), ([1, 0], [2, 0]), ([0, 0], [0, 1], [1, 0]), ([0, 0], [1, 0], [2, 0]))
((), ([1, 0], [2, 0]), ([0, 0], [0, 1], [1, 0]), ([0, 1], [1, 0], [2, 0]))
((), ([1, 0], [2, 0]), ([0, 0], [0, 1], [1, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
((), ([1, 0], [2, 0]), ([0, 0], [0, 1], [2, 0]), ([0, 0], [1, 0], [2, 0]))
((), ([1, 0], [2, 0]), ([0, 0], [0, 1], [2, 0]), ([0, 1], [1, 0], [2, 0]))
((), ([1, 0], [2, 0]), ([0, 0], [0, 1], [2, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
((), ([1, 0], [2, 0]), ([0, 0], [1, 0], [2, 0]), ([0, 1], [1, 0], [2, 0]))
((), ([1, 0], [2, 0]), ([0, 0], [1, 0], [2, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
((), ([1, 0], [2, 0]), ([0, 1], [1, 0], [2, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
((), ([0, 0], [0, 1], [1, 0]), ([0, 0], [0, 1], [2, 0]), ([0, 0], [1, 0], [2, 0]))
((), ([0, 0], [0, 1], [1, 0]), ([0, 0], [0, 1], [2, 0]), ([0, 1], [1, 0], [2, 0]))
((), ([0, 0], [0, 1], [1, 0]), ([0, 0], [0, 1], [2, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
((), ([0, 0], [0, 1], [1, 0]), ([0, 0], [1, 0], [2, 0]), ([0, 1], [1, 0], [2, 0]))
((), ([0, 0], [0, 1], [1, 0]), ([0, 0], [1, 0], [2, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
((), ([0, 0], [0, 1], [1, 0]), ([0, 1], [1, 0], [2, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
((), ([0, 0], [0, 1], [2, 0]), ([0, 0], [1, 0], [2, 0]), ([0, 1], [1, 0], [2, 0]))
((), ([0, 0], [0, 1], [2, 0]), ([0, 0], [1, 0], [2, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
((), ([0, 0], [0, 1], [2, 0]), ([0, 1], [1, 0], [2, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
((), ([0, 0], [1, 0], [2, 0]), ([0, 1], [1, 0], [2, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
(([0, 0],), ([0, 1],), ([1, 0],), ([2, 0],))
(([0, 0],), ([0, 1],), ([1, 0],), ([0, 0], [0, 1]))
(([0, 0],), ([0, 1],), ([1, 0],), ([0, 0], [1, 0]))
(([0, 0],), ([0, 1],), ([1, 0],), ([0, 0], [2, 0]))
(([0, 0],), ([0, 1],), ([1, 0],), ([0, 1], [1, 0]))
(([0, 0],), ([0, 1],), ([1, 0],), ([0, 1], [2, 0]))
(([0, 0],), ([0, 1],), ([1, 0],), ([1, 0], [2, 0]))
(([0, 0],), ([0, 1],), ([1, 0],), ([0, 0], [0, 1], [1, 0]))
(([0, 0],), ([0, 1],), ([1, 0],), ([0, 0], [0, 1], [2, 0]))
(([0, 0],), ([0, 1],), ([1, 0],), ([0, 0], [1, 0], [2, 0]))
(([0, 0],), ([0, 1],), ([1, 0],), ([0, 1], [1, 0], [2, 0]))
(([0, 0],), ([0, 1],), ([1, 0],), ([0, 0], [0, 1], [1, 0], [2, 0]))
(([0, 0],), ([0, 1],), ([2, 0],), ([0, 0], [0, 1]))
(([0, 0],), ([0, 1],), ([2, 0],), ([0, 0], [1, 0]))
(([0, 0],), ([0, 1],), ([2, 0],), ([0, 0], [2, 0]))
(([0, 0],), ([0, 1],), ([2, 0],), ([0, 1], [1, 0]))
(([0, 0],), ([0, 1],), ([2, 0],), ([0, 1], [2, 0]))
(([0, 0],), ([0, 1],), ([2, 0],), ([1, 0], [2, 0]))
(([0, 0],), ([0, 1],), ([2, 0],), ([0, 0], [0, 1], [1, 0]))
(([0, 0],), ([0, 1],), ([2, 0],), ([0, 0], [0, 1], [2, 0]))
(([0, 0],), ([0, 1],), ([2, 0],), ([0, 0], [1, 0], [2, 0]))
(([0, 0],), ([0, 1],), ([2, 0],), ([0, 1], [1, 0], [2, 0]))
(([0, 0],), ([0, 1],), ([2, 0],), ([0, 0], [0, 1], [1, 0], [2, 0]))
(([0, 0],), ([0, 1],), ([0, 0], [0, 1]), ([0, 0], [1, 0]))
(([0, 0],), ([0, 1],), ([0, 0], [0, 1]), ([0, 0], [2, 0]))
(([0, 0],), ([0, 1],), ([0, 0], [0, 1]), ([0, 1], [1, 0]))
(([0, 0],), ([0, 1],), ([0, 0], [0, 1]), ([0, 1], [2, 0]))
(([0, 0],), ([0, 1],), ([0, 0], [0, 1]), ([1, 0], [2, 0]))
(([0, 0],), ([0, 1],), ([0, 0], [0, 1]), ([0, 0], [0, 1], [1, 0]))
(([0, 0],), ([0, 1],), ([0, 0], [0, 1]), ([0, 0], [0, 1], [2, 0]))
(([0, 0],), ([0, 1],), ([0, 0], [0, 1]), ([0, 0], [1, 0], [2, 0]))
(([0, 0],), ([0, 1],), ([0, 0], [0, 1]), ([0, 1], [1, 0], [2, 0]))
(([0, 0],), ([0, 1],), ([0, 0], [0, 1]), ([0, 0], [0, 1], [1, 0], [2, 0]))
(([0, 0],), ([0, 1],), ([0, 0], [1, 0]), ([0, 0], [2, 0]))
(([0, 0],), ([0, 1],), ([0, 0], [1, 0]), ([0, 1], [1, 0]))
(([0, 0],), ([0, 1],), ([0, 0], [1, 0]), ([0, 1], [2, 0]))
(([0, 0],), ([0, 1],), ([0, 0], [1, 0]), ([1, 0], [2, 0]))
(([0, 0],), ([0, 1],), ([0, 0], [1, 0]), ([0, 0], [0, 1], [1, 0]))
(([0, 0],), ([0, 1],), ([0, 0], [1, 0]), ([0, 0], [0, 1], [2, 0]))
(([0, 0],), ([0, 1],), ([0, 0], [1, 0]), ([0, 0], [1, 0], [2, 0]))
(([0, 0],), ([0, 1],), ([0, 0], [1, 0]), ([0, 1], [1, 0], [2, 0]))
(([0, 0],), ([0, 1],), ([0, 0], [1, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
(([0, 0],), ([0, 1],), ([0, 0], [2, 0]), ([0, 1], [1, 0]))
(([0, 0],), ([0, 1],), ([0, 0], [2, 0]), ([0, 1], [2, 0]))
(([0, 0],), ([0, 1],), ([0, 0], [2, 0]), ([1, 0], [2, 0]))
(([0, 0],), ([0, 1],), ([0, 0], [2, 0]), ([0, 0], [0, 1], [1, 0]))
(([0, 0],), ([0, 1],), ([0, 0], [2, 0]), ([0, 0], [0, 1], [2, 0]))
(([0, 0],), ([0, 1],), ([0, 0], [2, 0]), ([0, 0], [1, 0], [2, 0]))
(([0, 0],), ([0, 1],), ([0, 0], [2, 0]), ([0, 1], [1, 0], [2, 0]))
(([0, 0],), ([0, 1],), ([0, 0], [2, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
(([0, 0],), ([0, 1],), ([0, 1], [1, 0]), ([0, 1], [2, 0]))
(([0, 0],), ([0, 1],), ([0, 1], [1, 0]), ([1, 0], [2, 0]))
(([0, 0],), ([0, 1],), ([0, 1], [1, 0]), ([0, 0], [0, 1], [1, 0]))
(([0, 0],), ([0, 1],), ([0, 1], [1, 0]), ([0, 0], [0, 1], [2, 0]))
(([0, 0],), ([0, 1],), ([0, 1], [1, 0]), ([0, 0], [1, 0], [2, 0]))
(([0, 0],), ([0, 1],), ([0, 1], [1, 0]), ([0, 1], [1, 0], [2, 0]))
(([0, 0],), ([0, 1],), ([0, 1], [1, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
(([0, 0],), ([0, 1],), ([0, 1], [2, 0]), ([1, 0], [2, 0]))
(([0, 0],), ([0, 1],), ([0, 1], [2, 0]), ([0, 0], [0, 1], [1, 0]))
(([0, 0],), ([0, 1],), ([0, 1], [2, 0]), ([0, 0], [0, 1], [2, 0]))
(([0, 0],), ([0, 1],), ([0, 1], [2, 0]), ([0, 0], [1, 0], [2, 0]))
(([0, 0],), ([0, 1],), ([0, 1], [2, 0]), ([0, 1], [1, 0], [2, 0]))
(([0, 0],), ([0, 1],), ([0, 1], [2, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
(([0, 0],), ([0, 1],), ([1, 0], [2, 0]), ([0, 0], [0, 1], [1, 0]))
(([0, 0],), ([0, 1],), ([1, 0], [2, 0]), ([0, 0], [0, 1], [2, 0]))
(([0, 0],), ([0, 1],), ([1, 0], [2, 0]), ([0, 0], [1, 0], [2, 0]))
(([0, 0],), ([0, 1],), ([1, 0], [2, 0]), ([0, 1], [1, 0], [2, 0]))
(([0, 0],), ([0, 1],), ([1, 0], [2, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
(([0, 0],), ([0, 1],), ([0, 0], [0, 1], [1, 0]), ([0, 0], [0, 1], [2, 0]))
(([0, 0],), ([0, 1],), ([0, 0], [0, 1], [1, 0]), ([0, 0], [1, 0], [2, 0]))
(([0, 0],), ([0, 1],), ([0, 0], [0, 1], [1, 0]), ([0, 1], [1, 0], [2, 0]))
(([0, 0],), ([0, 1],), ([0, 0], [0, 1], [1, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
(([0, 0],), ([0, 1],), ([0, 0], [0, 1], [2, 0]), ([0, 0], [1, 0], [2, 0]))
(([0, 0],), ([0, 1],), ([0, 0], [0, 1], [2, 0]), ([0, 1], [1, 0], [2, 0]))
(([0, 0],), ([0, 1],), ([0, 0], [0, 1], [2, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
(([0, 0],), ([0, 1],), ([0, 0], [1, 0], [2, 0]), ([0, 1], [1, 0], [2, 0]))
(([0, 0],), ([0, 1],), ([0, 0], [1, 0], [2, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
(([0, 0],), ([0, 1],), ([0, 1], [1, 0], [2, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
(([0, 0],), ([1, 0],), ([2, 0],), ([0, 0], [0, 1]))
(([0, 0],), ([1, 0],), ([2, 0],), ([0, 0], [1, 0]))
(([0, 0],), ([1, 0],), ([2, 0],), ([0, 0], [2, 0]))
(([0, 0],), ([1, 0],), ([2, 0],), ([0, 1], [1, 0]))
(([0, 0],), ([1, 0],), ([2, 0],), ([0, 1], [2, 0]))
(([0, 0],), ([1, 0],), ([2, 0],), ([1, 0], [2, 0]))
(([0, 0],), ([1, 0],), ([2, 0],), ([0, 0], [0, 1], [1, 0]))
(([0, 0],), ([1, 0],), ([2, 0],), ([0, 0], [0, 1], [2, 0]))
(([0, 0],), ([1, 0],), ([2, 0],), ([0, 0], [1, 0], [2, 0]))
(([0, 0],), ([1, 0],), ([2, 0],), ([0, 1], [1, 0], [2, 0]))
(([0, 0],), ([1, 0],), ([2, 0],), ([0, 0], [0, 1], [1, 0], [2, 0]))
(([0, 0],), ([1, 0],), ([0, 0], [0, 1]), ([0, 0], [1, 0]))
(([0, 0],), ([1, 0],), ([0, 0], [0, 1]), ([0, 0], [2, 0]))
(([0, 0],), ([1, 0],), ([0, 0], [0, 1]), ([0, 1], [1, 0]))
(([0, 0],), ([1, 0],), ([0, 0], [0, 1]), ([0, 1], [2, 0]))
(([0, 0],), ([1, 0],), ([0, 0], [0, 1]), ([1, 0], [2, 0]))
(([0, 0],), ([1, 0],), ([0, 0], [0, 1]), ([0, 0], [0, 1], [1, 0]))
(([0, 0],), ([1, 0],), ([0, 0], [0, 1]), ([0, 0], [0, 1], [2, 0]))
(([0, 0],), ([1, 0],), ([0, 0], [0, 1]), ([0, 0], [1, 0], [2, 0]))
(([0, 0],), ([1, 0],), ([0, 0], [0, 1]), ([0, 1], [1, 0], [2, 0]))
(([0, 0],), ([1, 0],), ([0, 0], [0, 1]), ([0, 0], [0, 1], [1, 0], [2, 0]))
(([0, 0],), ([1, 0],), ([0, 0], [1, 0]), ([0, 0], [2, 0]))
(([0, 0],), ([1, 0],), ([0, 0], [1, 0]), ([0, 1], [1, 0]))
(([0, 0],), ([1, 0],), ([0, 0], [1, 0]), ([0, 1], [2, 0]))
(([0, 0],), ([1, 0],), ([0, 0], [1, 0]), ([1, 0], [2, 0]))
(([0, 0],), ([1, 0],), ([0, 0], [1, 0]), ([0, 0], [0, 1], [1, 0]))
(([0, 0],), ([1, 0],), ([0, 0], [1, 0]), ([0, 0], [0, 1], [2, 0]))
(([0, 0],), ([1, 0],), ([0, 0], [1, 0]), ([0, 0], [1, 0], [2, 0]))
(([0, 0],), ([1, 0],), ([0, 0], [1, 0]), ([0, 1], [1, 0], [2, 0]))
(([0, 0],), ([1, 0],), ([0, 0], [1, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
(([0, 0],), ([1, 0],), ([0, 0], [2, 0]), ([0, 1], [1, 0]))
(([0, 0],), ([1, 0],), ([0, 0], [2, 0]), ([0, 1], [2, 0]))
(([0, 0],), ([1, 0],), ([0, 0], [2, 0]), ([1, 0], [2, 0]))
(([0, 0],), ([1, 0],), ([0, 0], [2, 0]), ([0, 0], [0, 1], [1, 0]))
(([0, 0],), ([1, 0],), ([0, 0], [2, 0]), ([0, 0], [0, 1], [2, 0]))
(([0, 0],), ([1, 0],), ([0, 0], [2, 0]), ([0, 0], [1, 0], [2, 0]))
(([0, 0],), ([1, 0],), ([0, 0], [2, 0]), ([0, 1], [1, 0], [2, 0]))
(([0, 0],), ([1, 0],), ([0, 0], [2, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
(([0, 0],), ([1, 0],), ([0, 1], [1, 0]), ([0, 1], [2, 0]))
(([0, 0],), ([1, 0],), ([0, 1], [1, 0]), ([1, 0], [2, 0]))
(([0, 0],), ([1, 0],), ([0, 1], [1, 0]), ([0, 0], [0, 1], [1, 0]))
(([0, 0],), ([1, 0],), ([0, 1], [1, 0]), ([0, 0], [0, 1], [2, 0]))
(([0, 0],), ([1, 0],), ([0, 1], [1, 0]), ([0, 0], [1, 0], [2, 0]))
(([0, 0],), ([1, 0],), ([0, 1], [1, 0]), ([0, 1], [1, 0], [2, 0]))
(([0, 0],), ([1, 0],), ([0, 1], [1, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
(([0, 0],), ([1, 0],), ([0, 1], [2, 0]), ([1, 0], [2, 0]))
(([0, 0],), ([1, 0],), ([0, 1], [2, 0]), ([0, 0], [0, 1], [1, 0]))
(([0, 0],), ([1, 0],), ([0, 1], [2, 0]), ([0, 0], [0, 1], [2, 0]))
(([0, 0],), ([1, 0],), ([0, 1], [2, 0]), ([0, 0], [1, 0], [2, 0]))
(([0, 0],), ([1, 0],), ([0, 1], [2, 0]), ([0, 1], [1, 0], [2, 0]))
(([0, 0],), ([1, 0],), ([0, 1], [2, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
(([0, 0],), ([1, 0],), ([1, 0], [2, 0]), ([0, 0], [0, 1], [1, 0]))
(([0, 0],), ([1, 0],), ([1, 0], [2, 0]), ([0, 0], [0, 1], [2, 0]))
(([0, 0],), ([1, 0],), ([1, 0], [2, 0]), ([0, 0], [1, 0], [2, 0]))
(([0, 0],), ([1, 0],), ([1, 0], [2, 0]), ([0, 1], [1, 0], [2, 0]))
(([0, 0],), ([1, 0],), ([1, 0], [2, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
(([0, 0],), ([1, 0],), ([0, 0], [0, 1], [1, 0]), ([0, 0], [0, 1], [2, 0]))
(([0, 0],), ([1, 0],), ([0, 0], [0, 1], [1, 0]), ([0, 0], [1, 0], [2, 0]))
(([0, 0],), ([1, 0],), ([0, 0], [0, 1], [1, 0]), ([0, 1], [1, 0], [2, 0]))
(([0, 0],), ([1, 0],), ([0, 0], [0, 1], [1, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
(([0, 0],), ([1, 0],), ([0, 0], [0, 1], [2, 0]), ([0, 0], [1, 0], [2, 0]))
(([0, 0],), ([1, 0],), ([0, 0], [0, 1], [2, 0]), ([0, 1], [1, 0], [2, 0]))
(([0, 0],), ([1, 0],), ([0, 0], [0, 1], [2, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
(([0, 0],), ([1, 0],), ([0, 0], [1, 0], [2, 0]), ([0, 1], [1, 0], [2, 0]))
(([0, 0],), ([1, 0],), ([0, 0], [1, 0], [2, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
(([0, 0],), ([1, 0],), ([0, 1], [1, 0], [2, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
(([0, 0],), ([2, 0],), ([0, 0], [0, 1]), ([0, 0], [1, 0]))
(([0, 0],), ([2, 0],), ([0, 0], [0, 1]), ([0, 0], [2, 0]))
(([0, 0],), ([2, 0],), ([0, 0], [0, 1]), ([0, 1], [1, 0]))
(([0, 0],), ([2, 0],), ([0, 0], [0, 1]), ([0, 1], [2, 0]))
(([0, 0],), ([2, 0],), ([0, 0], [0, 1]), ([1, 0], [2, 0]))
(([0, 0],), ([2, 0],), ([0, 0], [0, 1]), ([0, 0], [0, 1], [1, 0]))
(([0, 0],), ([2, 0],), ([0, 0], [0, 1]), ([0, 0], [0, 1], [2, 0]))
(([0, 0],), ([2, 0],), ([0, 0], [0, 1]), ([0, 0], [1, 0], [2, 0]))
(([0, 0],), ([2, 0],), ([0, 0], [0, 1]), ([0, 1], [1, 0], [2, 0]))
(([0, 0],), ([2, 0],), ([0, 0], [0, 1]), ([0, 0], [0, 1], [1, 0], [2, 0]))
(([0, 0],), ([2, 0],), ([0, 0], [1, 0]), ([0, 0], [2, 0]))
(([0, 0],), ([2, 0],), ([0, 0], [1, 0]), ([0, 1], [1, 0]))
(([0, 0],), ([2, 0],), ([0, 0], [1, 0]), ([0, 1], [2, 0]))
(([0, 0],), ([2, 0],), ([0, 0], [1, 0]), ([1, 0], [2, 0]))
(([0, 0],), ([2, 0],), ([0, 0], [1, 0]), ([0, 0], [0, 1], [1, 0]))
(([0, 0],), ([2, 0],), ([0, 0], [1, 0]), ([0, 0], [0, 1], [2, 0]))
(([0, 0],), ([2, 0],), ([0, 0], [1, 0]), ([0, 0], [1, 0], [2, 0]))
(([0, 0],), ([2, 0],), ([0, 0], [1, 0]), ([0, 1], [1, 0], [2, 0]))
(([0, 0],), ([2, 0],), ([0, 0], [1, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
(([0, 0],), ([2, 0],), ([0, 0], [2, 0]), ([0, 1], [1, 0]))
(([0, 0],), ([2, 0],), ([0, 0], [2, 0]), ([0, 1], [2, 0]))
(([0, 0],), ([2, 0],), ([0, 0], [2, 0]), ([1, 0], [2, 0]))
(([0, 0],), ([2, 0],), ([0, 0], [2, 0]), ([0, 0], [0, 1], [1, 0]))
(([0, 0],), ([2, 0],), ([0, 0], [2, 0]), ([0, 0], [0, 1], [2, 0]))
(([0, 0],), ([2, 0],), ([0, 0], [2, 0]), ([0, 0], [1, 0], [2, 0]))
(([0, 0],), ([2, 0],), ([0, 0], [2, 0]), ([0, 1], [1, 0], [2, 0]))
(([0, 0],), ([2, 0],), ([0, 0], [2, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
(([0, 0],), ([2, 0],), ([0, 1], [1, 0]), ([0, 1], [2, 0]))
(([0, 0],), ([2, 0],), ([0, 1], [1, 0]), ([1, 0], [2, 0]))
(([0, 0],), ([2, 0],), ([0, 1], [1, 0]), ([0, 0], [0, 1], [1, 0]))
(([0, 0],), ([2, 0],), ([0, 1], [1, 0]), ([0, 0], [0, 1], [2, 0]))
(([0, 0],), ([2, 0],), ([0, 1], [1, 0]), ([0, 0], [1, 0], [2, 0]))
(([0, 0],), ([2, 0],), ([0, 1], [1, 0]), ([0, 1], [1, 0], [2, 0]))
(([0, 0],), ([2, 0],), ([0, 1], [1, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
(([0, 0],), ([2, 0],), ([0, 1], [2, 0]), ([1, 0], [2, 0]))
(([0, 0],), ([2, 0],), ([0, 1], [2, 0]), ([0, 0], [0, 1], [1, 0]))
(([0, 0],), ([2, 0],), ([0, 1], [2, 0]), ([0, 0], [0, 1], [2, 0]))
(([0, 0],), ([2, 0],), ([0, 1], [2, 0]), ([0, 0], [1, 0], [2, 0]))
(([0, 0],), ([2, 0],), ([0, 1], [2, 0]), ([0, 1], [1, 0], [2, 0]))
(([0, 0],), ([2, 0],), ([0, 1], [2, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
(([0, 0],), ([2, 0],), ([1, 0], [2, 0]), ([0, 0], [0, 1], [1, 0]))
(([0, 0],), ([2, 0],), ([1, 0], [2, 0]), ([0, 0], [0, 1], [2, 0]))
(([0, 0],), ([2, 0],), ([1, 0], [2, 0]), ([0, 0], [1, 0], [2, 0]))
(([0, 0],), ([2, 0],), ([1, 0], [2, 0]), ([0, 1], [1, 0], [2, 0]))
(([0, 0],), ([2, 0],), ([1, 0], [2, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
(([0, 0],), ([2, 0],), ([0, 0], [0, 1], [1, 0]), ([0, 0], [0, 1], [2, 0]))
(([0, 0],), ([2, 0],), ([0, 0], [0, 1], [1, 0]), ([0, 0], [1, 0], [2, 0]))
(([0, 0],), ([2, 0],), ([0, 0], [0, 1], [1, 0]), ([0, 1], [1, 0], [2, 0]))
(([0, 0],), ([2, 0],), ([0, 0], [0, 1], [1, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
(([0, 0],), ([2, 0],), ([0, 0], [0, 1], [2, 0]), ([0, 0], [1, 0], [2, 0]))
(([0, 0],), ([2, 0],), ([0, 0], [0, 1], [2, 0]), ([0, 1], [1, 0], [2, 0]))
(([0, 0],), ([2, 0],), ([0, 0], [0, 1], [2, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
(([0, 0],), ([2, 0],), ([0, 0], [1, 0], [2, 0]), ([0, 1], [1, 0], [2, 0]))
(([0, 0],), ([2, 0],), ([0, 0], [1, 0], [2, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
(([0, 0],), ([2, 0],), ([0, 1], [1, 0], [2, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
(([0, 0],), ([0, 0], [0, 1]), ([0, 0], [1, 0]), ([0, 0], [2, 0]))
(([0, 0],), ([0, 0], [0, 1]), ([0, 0], [1, 0]), ([0, 1], [1, 0]))
(([0, 0],), ([0, 0], [0, 1]), ([0, 0], [1, 0]), ([0, 1], [2, 0]))
(([0, 0],), ([0, 0], [0, 1]), ([0, 0], [1, 0]), ([1, 0], [2, 0]))
(([0, 0],), ([0, 0], [0, 1]), ([0, 0], [1, 0]), ([0, 0], [0, 1], [1, 0]))
(([0, 0],), ([0, 0], [0, 1]), ([0, 0], [1, 0]), ([0, 0], [0, 1], [2, 0]))
(([0, 0],), ([0, 0], [0, 1]), ([0, 0], [1, 0]), ([0, 0], [1, 0], [2, 0]))
(([0, 0],), ([0, 0], [0, 1]), ([0, 0], [1, 0]), ([0, 1], [1, 0], [2, 0]))
(([0, 0],), ([0, 0], [0, 1]), ([0, 0], [1, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
(([0, 0],), ([0, 0], [0, 1]), ([0, 0], [2, 0]), ([0, 1], [1, 0]))
(([0, 0],), ([0, 0], [0, 1]), ([0, 0], [2, 0]), ([0, 1], [2, 0]))
(([0, 0],), ([0, 0], [0, 1]), ([0, 0], [2, 0]), ([1, 0], [2, 0]))
(([0, 0],), ([0, 0], [0, 1]), ([0, 0], [2, 0]), ([0, 0], [0, 1], [1, 0]))
(([0, 0],), ([0, 0], [0, 1]), ([0, 0], [2, 0]), ([0, 0], [0, 1], [2, 0]))
(([0, 0],), ([0, 0], [0, 1]), ([0, 0], [2, 0]), ([0, 0], [1, 0], [2, 0]))
(([0, 0],), ([0, 0], [0, 1]), ([0, 0], [2, 0]), ([0, 1], [1, 0], [2, 0]))
(([0, 0],), ([0, 0], [0, 1]), ([0, 0], [2, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
(([0, 0],), ([0, 0], [0, 1]), ([0, 1], [1, 0]), ([0, 1], [2, 0]))
(([0, 0],), ([0, 0], [0, 1]), ([0, 1], [1, 0]), ([1, 0], [2, 0]))
(([0, 0],), ([0, 0], [0, 1]), ([0, 1], [1, 0]), ([0, 0], [0, 1], [1, 0]))
(([0, 0],), ([0, 0], [0, 1]), ([0, 1], [1, 0]), ([0, 0], [0, 1], [2, 0]))
(([0, 0],), ([0, 0], [0, 1]), ([0, 1], [1, 0]), ([0, 0], [1, 0], [2, 0]))
(([0, 0],), ([0, 0], [0, 1]), ([0, 1], [1, 0]), ([0, 1], [1, 0], [2, 0]))
(([0, 0],), ([0, 0], [0, 1]), ([0, 1], [1, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
(([0, 0],), ([0, 0], [0, 1]), ([0, 1], [2, 0]), ([1, 0], [2, 0]))
(([0, 0],), ([0, 0], [0, 1]), ([0, 1], [2, 0]), ([0, 0], [0, 1], [1, 0]))
(([0, 0],), ([0, 0], [0, 1]), ([0, 1], [2, 0]), ([0, 0], [0, 1], [2, 0]))
(([0, 0],), ([0, 0], [0, 1]), ([0, 1], [2, 0]), ([0, 0], [1, 0], [2, 0]))
(([0, 0],), ([0, 0], [0, 1]), ([0, 1], [2, 0]), ([0, 1], [1, 0], [2, 0]))
(([0, 0],), ([0, 0], [0, 1]), ([0, 1], [2, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
(([0, 0],), ([0, 0], [0, 1]), ([1, 0], [2, 0]), ([0, 0], [0, 1], [1, 0]))
(([0, 0],), ([0, 0], [0, 1]), ([1, 0], [2, 0]), ([0, 0], [0, 1], [2, 0]))
(([0, 0],), ([0, 0], [0, 1]), ([1, 0], [2, 0]), ([0, 0], [1, 0], [2, 0]))
(([0, 0],), ([0, 0], [0, 1]), ([1, 0], [2, 0]), ([0, 1], [1, 0], [2, 0]))
(([0, 0],), ([0, 0], [0, 1]), ([1, 0], [2, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
(([0, 0],), ([0, 0], [0, 1]), ([0, 0], [0, 1], [1, 0]), ([0, 0], [0, 1], [2, 0]))
(([0, 0],), ([0, 0], [0, 1]), ([0, 0], [0, 1], [1, 0]), ([0, 0], [1, 0], [2, 0]))
(([0, 0],), ([0, 0], [0, 1]), ([0, 0], [0, 1], [1, 0]), ([0, 1], [1, 0], [2, 0]))
(([0, 0],), ([0, 0], [0, 1]), ([0, 0], [0, 1], [1, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
(([0, 0],), ([0, 0], [0, 1]), ([0, 0], [0, 1], [2, 0]), ([0, 0], [1, 0], [2, 0]))
(([0, 0],), ([0, 0], [0, 1]), ([0, 0], [0, 1], [2, 0]), ([0, 1], [1, 0], [2, 0]))
(([0, 0],), ([0, 0], [0, 1]), ([0, 0], [0, 1], [2, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
(([0, 0],), ([0, 0], [0, 1]), ([0, 0], [1, 0], [2, 0]), ([0, 1], [1, 0], [2, 0]))
(([0, 0],), ([0, 0], [0, 1]), ([0, 0], [1, 0], [2, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
(([0, 0],), ([0, 0], [0, 1]), ([0, 1], [1, 0], [2, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
(([0, 0],), ([0, 0], [1, 0]), ([0, 0], [2, 0]), ([0, 1], [1, 0]))
(([0, 0],), ([0, 0], [1, 0]), ([0, 0], [2, 0]), ([0, 1], [2, 0]))
(([0, 0],), ([0, 0], [1, 0]), ([0, 0], [2, 0]), ([1, 0], [2, 0]))
(([0, 0],), ([0, 0], [1, 0]), ([0, 0], [2, 0]), ([0, 0], [0, 1], [1, 0]))
(([0, 0],), ([0, 0], [1, 0]), ([0, 0], [2, 0]), ([0, 0], [0, 1], [2, 0]))
(([0, 0],), ([0, 0], [1, 0]), ([0, 0], [2, 0]), ([0, 0], [1, 0], [2, 0]))
(([0, 0],), ([0, 0], [1, 0]), ([0, 0], [2, 0]), ([0, 1], [1, 0], [2, 0]))
(([0, 0],), ([0, 0], [1, 0]), ([0, 0], [2, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
(([0, 0],), ([0, 0], [1, 0]), ([0, 1], [1, 0]), ([0, 1], [2, 0]))
(([0, 0],), ([0, 0], [1, 0]), ([0, 1], [1, 0]), ([1, 0], [2, 0]))
(([0, 0],), ([0, 0], [1, 0]), ([0, 1], [1, 0]), ([0, 0], [0, 1], [1, 0]))
(([0, 0],), ([0, 0], [1, 0]), ([0, 1], [1, 0]), ([0, 0], [0, 1], [2, 0]))
(([0, 0],), ([0, 0], [1, 0]), ([0, 1], [1, 0]), ([0, 0], [1, 0], [2, 0]))
(([0, 0],), ([0, 0], [1, 0]), ([0, 1], [1, 0]), ([0, 1], [1, 0], [2, 0]))
(([0, 0],), ([0, 0], [1, 0]), ([0, 1], [1, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
(([0, 0],), ([0, 0], [1, 0]), ([0, 1], [2, 0]), ([1, 0], [2, 0]))
(([0, 0],), ([0, 0], [1, 0]), ([0, 1], [2, 0]), ([0, 0], [0, 1], [1, 0]))
(([0, 0],), ([0, 0], [1, 0]), ([0, 1], [2, 0]), ([0, 0], [0, 1], [2, 0]))
(([0, 0],), ([0, 0], [1, 0]), ([0, 1], [2, 0]), ([0, 0], [1, 0], [2, 0]))
(([0, 0],), ([0, 0], [1, 0]), ([0, 1], [2, 0]), ([0, 1], [1, 0], [2, 0]))
(([0, 0],), ([0, 0], [1, 0]), ([0, 1], [2, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
(([0, 0],), ([0, 0], [1, 0]), ([1, 0], [2, 0]), ([0, 0], [0, 1], [1, 0]))
(([0, 0],), ([0, 0], [1, 0]), ([1, 0], [2, 0]), ([0, 0], [0, 1], [2, 0]))
(([0, 0],), ([0, 0], [1, 0]), ([1, 0], [2, 0]), ([0, 0], [1, 0], [2, 0]))
(([0, 0],), ([0, 0], [1, 0]), ([1, 0], [2, 0]), ([0, 1], [1, 0], [2, 0]))
(([0, 0],), ([0, 0], [1, 0]), ([1, 0], [2, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
(([0, 0],), ([0, 0], [1, 0]), ([0, 0], [0, 1], [1, 0]), ([0, 0], [0, 1], [2, 0]))
(([0, 0],), ([0, 0], [1, 0]), ([0, 0], [0, 1], [1, 0]), ([0, 0], [1, 0], [2, 0]))
(([0, 0],), ([0, 0], [1, 0]), ([0, 0], [0, 1], [1, 0]), ([0, 1], [1, 0], [2, 0]))
(([0, 0],), ([0, 0], [1, 0]), ([0, 0], [0, 1], [1, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
(([0, 0],), ([0, 0], [1, 0]), ([0, 0], [0, 1], [2, 0]), ([0, 0], [1, 0], [2, 0]))
(([0, 0],), ([0, 0], [1, 0]), ([0, 0], [0, 1], [2, 0]), ([0, 1], [1, 0], [2, 0]))
(([0, 0],), ([0, 0], [1, 0]), ([0, 0], [0, 1], [2, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
(([0, 0],), ([0, 0], [1, 0]), ([0, 0], [1, 0], [2, 0]), ([0, 1], [1, 0], [2, 0]))
(([0, 0],), ([0, 0], [1, 0]), ([0, 0], [1, 0], [2, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
(([0, 0],), ([0, 0], [1, 0]), ([0, 1], [1, 0], [2, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
(([0, 0],), ([0, 0], [2, 0]), ([0, 1], [1, 0]), ([0, 1], [2, 0]))
(([0, 0],), ([0, 0], [2, 0]), ([0, 1], [1, 0]), ([1, 0], [2, 0]))
(([0, 0],), ([0, 0], [2, 0]), ([0, 1], [1, 0]), ([0, 0], [0, 1], [1, 0]))
(([0, 0],), ([0, 0], [2, 0]), ([0, 1], [1, 0]), ([0, 0], [0, 1], [2, 0]))
(([0, 0],), ([0, 0], [2, 0]), ([0, 1], [1, 0]), ([0, 0], [1, 0], [2, 0]))
(([0, 0],), ([0, 0], [2, 0]), ([0, 1], [1, 0]), ([0, 1], [1, 0], [2, 0]))
(([0, 0],), ([0, 0], [2, 0]), ([0, 1], [1, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
(([0, 0],), ([0, 0], [2, 0]), ([0, 1], [2, 0]), ([1, 0], [2, 0]))
(([0, 0],), ([0, 0], [2, 0]), ([0, 1], [2, 0]), ([0, 0], [0, 1], [1, 0]))
(([0, 0],), ([0, 0], [2, 0]), ([0, 1], [2, 0]), ([0, 0], [0, 1], [2, 0]))
(([0, 0],), ([0, 0], [2, 0]), ([0, 1], [2, 0]), ([0, 0], [1, 0], [2, 0]))
(([0, 0],), ([0, 0], [2, 0]), ([0, 1], [2, 0]), ([0, 1], [1, 0], [2, 0]))
(([0, 0],), ([0, 0], [2, 0]), ([0, 1], [2, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
(([0, 0],), ([0, 0], [2, 0]), ([1, 0], [2, 0]), ([0, 0], [0, 1], [1, 0]))
(([0, 0],), ([0, 0], [2, 0]), ([1, 0], [2, 0]), ([0, 0], [0, 1], [2, 0]))
(([0, 0],), ([0, 0], [2, 0]), ([1, 0], [2, 0]), ([0, 0], [1, 0], [2, 0]))
(([0, 0],), ([0, 0], [2, 0]), ([1, 0], [2, 0]), ([0, 1], [1, 0], [2, 0]))
(([0, 0],), ([0, 0], [2, 0]), ([1, 0], [2, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
(([0, 0],), ([0, 0], [2, 0]), ([0, 0], [0, 1], [1, 0]), ([0, 0], [0, 1], [2, 0]))
(([0, 0],), ([0, 0], [2, 0]), ([0, 0], [0, 1], [1, 0]), ([0, 0], [1, 0], [2, 0]))
(([0, 0],), ([0, 0], [2, 0]), ([0, 0], [0, 1], [1, 0]), ([0, 1], [1, 0], [2, 0]))
(([0, 0],), ([0, 0], [2, 0]), ([0, 0], [0, 1], [1, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
(([0, 0],), ([0, 0], [2, 0]), ([0, 0], [0, 1], [2, 0]), ([0, 0], [1, 0], [2, 0]))
(([0, 0],), ([0, 0], [2, 0]), ([0, 0], [0, 1], [2, 0]), ([0, 1], [1, 0], [2, 0]))
(([0, 0],), ([0, 0], [2, 0]), ([0, 0], [0, 1], [2, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
(([0, 0],), ([0, 0], [2, 0]), ([0, 0], [1, 0], [2, 0]), ([0, 1], [1, 0], [2, 0]))
(([0, 0],), ([0, 0], [2, 0]), ([0, 0], [1, 0], [2, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
(([0, 0],), ([0, 0], [2, 0]), ([0, 1], [1, 0], [2, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
(([0, 0],), ([0, 1], [1, 0]), ([0, 1], [2, 0]), ([1, 0], [2, 0]))
(([0, 0],), ([0, 1], [1, 0]), ([0, 1], [2, 0]), ([0, 0], [0, 1], [1, 0]))
(([0, 0],), ([0, 1], [1, 0]), ([0, 1], [2, 0]), ([0, 0], [0, 1], [2, 0]))
(([0, 0],), ([0, 1], [1, 0]), ([0, 1], [2, 0]), ([0, 0], [1, 0], [2, 0]))
(([0, 0],), ([0, 1], [1, 0]), ([0, 1], [2, 0]), ([0, 1], [1, 0], [2, 0]))
(([0, 0],), ([0, 1], [1, 0]), ([0, 1], [2, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
(([0, 0],), ([0, 1], [1, 0]), ([1, 0], [2, 0]), ([0, 0], [0, 1], [1, 0]))
(([0, 0],), ([0, 1], [1, 0]), ([1, 0], [2, 0]), ([0, 0], [0, 1], [2, 0]))
(([0, 0],), ([0, 1], [1, 0]), ([1, 0], [2, 0]), ([0, 0], [1, 0], [2, 0]))
(([0, 0],), ([0, 1], [1, 0]), ([1, 0], [2, 0]), ([0, 1], [1, 0], [2, 0]))
(([0, 0],), ([0, 1], [1, 0]), ([1, 0], [2, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
(([0, 0],), ([0, 1], [1, 0]), ([0, 0], [0, 1], [1, 0]), ([0, 0], [0, 1], [2, 0]))
(([0, 0],), ([0, 1], [1, 0]), ([0, 0], [0, 1], [1, 0]), ([0, 0], [1, 0], [2, 0]))
(([0, 0],), ([0, 1], [1, 0]), ([0, 0], [0, 1], [1, 0]), ([0, 1], [1, 0], [2, 0]))
(([0, 0],), ([0, 1], [1, 0]), ([0, 0], [0, 1], [1, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
(([0, 0],), ([0, 1], [1, 0]), ([0, 0], [0, 1], [2, 0]), ([0, 0], [1, 0], [2, 0]))
(([0, 0],), ([0, 1], [1, 0]), ([0, 0], [0, 1], [2, 0]), ([0, 1], [1, 0], [2, 0]))
(([0, 0],), ([0, 1], [1, 0]), ([0, 0], [0, 1], [2, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
(([0, 0],), ([0, 1], [1, 0]), ([0, 0], [1, 0], [2, 0]), ([0, 1], [1, 0], [2, 0]))
(([0, 0],), ([0, 1], [1, 0]), ([0, 0], [1, 0], [2, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
(([0, 0],), ([0, 1], [1, 0]), ([0, 1], [1, 0], [2, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
(([0, 0],), ([0, 1], [2, 0]), ([1, 0], [2, 0]), ([0, 0], [0, 1], [1, 0]))
(([0, 0],), ([0, 1], [2, 0]), ([1, 0], [2, 0]), ([0, 0], [0, 1], [2, 0]))
(([0, 0],), ([0, 1], [2, 0]), ([1, 0], [2, 0]), ([0, 0], [1, 0], [2, 0]))
(([0, 0],), ([0, 1], [2, 0]), ([1, 0], [2, 0]), ([0, 1], [1, 0], [2, 0]))
(([0, 0],), ([0, 1], [2, 0]), ([1, 0], [2, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
(([0, 0],), ([0, 1], [2, 0]), ([0, 0], [0, 1], [1, 0]), ([0, 0], [0, 1], [2, 0]))
(([0, 0],), ([0, 1], [2, 0]), ([0, 0], [0, 1], [1, 0]), ([0, 0], [1, 0], [2, 0]))
(([0, 0],), ([0, 1], [2, 0]), ([0, 0], [0, 1], [1, 0]), ([0, 1], [1, 0], [2, 0]))
(([0, 0],), ([0, 1], [2, 0]), ([0, 0], [0, 1], [1, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
(([0, 0],), ([0, 1], [2, 0]), ([0, 0], [0, 1], [2, 0]), ([0, 0], [1, 0], [2, 0]))
(([0, 0],), ([0, 1], [2, 0]), ([0, 0], [0, 1], [2, 0]), ([0, 1], [1, 0], [2, 0]))
(([0, 0],), ([0, 1], [2, 0]), ([0, 0], [0, 1], [2, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
(([0, 0],), ([0, 1], [2, 0]), ([0, 0], [1, 0], [2, 0]), ([0, 1], [1, 0], [2, 0]))
(([0, 0],), ([0, 1], [2, 0]), ([0, 0], [1, 0], [2, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
(([0, 0],), ([0, 1], [2, 0]), ([0, 1], [1, 0], [2, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
(([0, 0],), ([1, 0], [2, 0]), ([0, 0], [0, 1], [1, 0]), ([0, 0], [0, 1], [2, 0]))
(([0, 0],), ([1, 0], [2, 0]), ([0, 0], [0, 1], [1, 0]), ([0, 0], [1, 0], [2, 0]))
(([0, 0],), ([1, 0], [2, 0]), ([0, 0], [0, 1], [1, 0]), ([0, 1], [1, 0], [2, 0]))
(([0, 0],), ([1, 0], [2, 0]), ([0, 0], [0, 1], [1, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
(([0, 0],), ([1, 0], [2, 0]), ([0, 0], [0, 1], [2, 0]), ([0, 0], [1, 0], [2, 0]))
(([0, 0],), ([1, 0], [2, 0]), ([0, 0], [0, 1], [2, 0]), ([0, 1], [1, 0], [2, 0]))
(([0, 0],), ([1, 0], [2, 0]), ([0, 0], [0, 1], [2, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
(([0, 0],), ([1, 0], [2, 0]), ([0, 0], [1, 0], [2, 0]), ([0, 1], [1, 0], [2, 0]))
(([0, 0],), ([1, 0], [2, 0]), ([0, 0], [1, 0], [2, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
(([0, 0],), ([1, 0], [2, 0]), ([0, 1], [1, 0], [2, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
(([0, 0],), ([0, 0], [0, 1], [1, 0]), ([0, 0], [0, 1], [2, 0]), ([0, 0], [1, 0], [2, 0]))
(([0, 0],), ([0, 0], [0, 1], [1, 0]), ([0, 0], [0, 1], [2, 0]), ([0, 1], [1, 0], [2, 0]))
(([0, 0],), ([0, 0], [0, 1], [1, 0]), ([0, 0], [0, 1], [2, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
(([0, 0],), ([0, 0], [0, 1], [1, 0]), ([0, 0], [1, 0], [2, 0]), ([0, 1], [1, 0], [2, 0]))
(([0, 0],), ([0, 0], [0, 1], [1, 0]), ([0, 0], [1, 0], [2, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
(([0, 0],), ([0, 0], [0, 1], [1, 0]), ([0, 1], [1, 0], [2, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
(([0, 0],), ([0, 0], [0, 1], [2, 0]), ([0, 0], [1, 0], [2, 0]), ([0, 1], [1, 0], [2, 0]))
(([0, 0],), ([0, 0], [0, 1], [2, 0]), ([0, 0], [1, 0], [2, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
(([0, 0],), ([0, 0], [0, 1], [2, 0]), ([0, 1], [1, 0], [2, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
(([0, 0],), ([0, 0], [1, 0], [2, 0]), ([0, 1], [1, 0], [2, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
(([0, 1],), ([1, 0],), ([2, 0],), ([0, 0], [0, 1]))
(([0, 1],), ([1, 0],), ([2, 0],), ([0, 0], [1, 0]))
(([0, 1],), ([1, 0],), ([2, 0],), ([0, 0], [2, 0]))
(([0, 1],), ([1, 0],), ([2, 0],), ([0, 1], [1, 0]))
(([0, 1],), ([1, 0],), ([2, 0],), ([0, 1], [2, 0]))
(([0, 1],), ([1, 0],), ([2, 0],), ([1, 0], [2, 0]))
(([0, 1],), ([1, 0],), ([2, 0],), ([0, 0], [0, 1], [1, 0]))
(([0, 1],), ([1, 0],), ([2, 0],), ([0, 0], [0, 1], [2, 0]))
(([0, 1],), ([1, 0],), ([2, 0],), ([0, 0], [1, 0], [2, 0]))
(([0, 1],), ([1, 0],), ([2, 0],), ([0, 1], [1, 0], [2, 0]))
(([0, 1],), ([1, 0],), ([2, 0],), ([0, 0], [0, 1], [1, 0], [2, 0]))
(([0, 1],), ([1, 0],), ([0, 0], [0, 1]), ([0, 0], [1, 0]))
(([0, 1],), ([1, 0],), ([0, 0], [0, 1]), ([0, 0], [2, 0]))
(([0, 1],), ([1, 0],), ([0, 0], [0, 1]), ([0, 1], [1, 0]))
(([0, 1],), ([1, 0],), ([0, 0], [0, 1]), ([0, 1], [2, 0]))
(([0, 1],), ([1, 0],), ([0, 0], [0, 1]), ([1, 0], [2, 0]))
(([0, 1],), ([1, 0],), ([0, 0], [0, 1]), ([0, 0], [0, 1], [1, 0]))
(([0, 1],), ([1, 0],), ([0, 0], [0, 1]), ([0, 0], [0, 1], [2, 0]))
(([0, 1],), ([1, 0],), ([0, 0], [0, 1]), ([0, 0], [1, 0], [2, 0]))
(([0, 1],), ([1, 0],), ([0, 0], [0, 1]), ([0, 1], [1, 0], [2, 0]))
(([0, 1],), ([1, 0],), ([0, 0], [0, 1]), ([0, 0], [0, 1], [1, 0], [2, 0]))
(([0, 1],), ([1, 0],), ([0, 0], [1, 0]), ([0, 0], [2, 0]))
(([0, 1],), ([1, 0],), ([0, 0], [1, 0]), ([0, 1], [1, 0]))
(([0, 1],), ([1, 0],), ([0, 0], [1, 0]), ([0, 1], [2, 0]))
(([0, 1],), ([1, 0],), ([0, 0], [1, 0]), ([1, 0], [2, 0]))
(([0, 1],), ([1, 0],), ([0, 0], [1, 0]), ([0, 0], [0, 1], [1, 0]))
(([0, 1],), ([1, 0],), ([0, 0], [1, 0]), ([0, 0], [0, 1], [2, 0]))
(([0, 1],), ([1, 0],), ([0, 0], [1, 0]), ([0, 0], [1, 0], [2, 0]))
(([0, 1],), ([1, 0],), ([0, 0], [1, 0]), ([0, 1], [1, 0], [2, 0]))
(([0, 1],), ([1, 0],), ([0, 0], [1, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
(([0, 1],), ([1, 0],), ([0, 0], [2, 0]), ([0, 1], [1, 0]))
(([0, 1],), ([1, 0],), ([0, 0], [2, 0]), ([0, 1], [2, 0]))
(([0, 1],), ([1, 0],), ([0, 0], [2, 0]), ([1, 0], [2, 0]))
(([0, 1],), ([1, 0],), ([0, 0], [2, 0]), ([0, 0], [0, 1], [1, 0]))
(([0, 1],), ([1, 0],), ([0, 0], [2, 0]), ([0, 0], [0, 1], [2, 0]))
(([0, 1],), ([1, 0],), ([0, 0], [2, 0]), ([0, 0], [1, 0], [2, 0]))
(([0, 1],), ([1, 0],), ([0, 0], [2, 0]), ([0, 1], [1, 0], [2, 0]))
(([0, 1],), ([1, 0],), ([0, 0], [2, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
(([0, 1],), ([1, 0],), ([0, 1], [1, 0]), ([0, 1], [2, 0]))
(([0, 1],), ([1, 0],), ([0, 1], [1, 0]), ([1, 0], [2, 0]))
(([0, 1],), ([1, 0],), ([0, 1], [1, 0]), ([0, 0], [0, 1], [1, 0]))
(([0, 1],), ([1, 0],), ([0, 1], [1, 0]), ([0, 0], [0, 1], [2, 0]))
(([0, 1],), ([1, 0],), ([0, 1], [1, 0]), ([0, 0], [1, 0], [2, 0]))
(([0, 1],), ([1, 0],), ([0, 1], [1, 0]), ([0, 1], [1, 0], [2, 0]))
(([0, 1],), ([1, 0],), ([0, 1], [1, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
(([0, 1],), ([1, 0],), ([0, 1], [2, 0]), ([1, 0], [2, 0]))
(([0, 1],), ([1, 0],), ([0, 1], [2, 0]), ([0, 0], [0, 1], [1, 0]))
(([0, 1],), ([1, 0],), ([0, 1], [2, 0]), ([0, 0], [0, 1], [2, 0]))
(([0, 1],), ([1, 0],), ([0, 1], [2, 0]), ([0, 0], [1, 0], [2, 0]))
(([0, 1],), ([1, 0],), ([0, 1], [2, 0]), ([0, 1], [1, 0], [2, 0]))
(([0, 1],), ([1, 0],), ([0, 1], [2, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
(([0, 1],), ([1, 0],), ([1, 0], [2, 0]), ([0, 0], [0, 1], [1, 0]))
(([0, 1],), ([1, 0],), ([1, 0], [2, 0]), ([0, 0], [0, 1], [2, 0]))
(([0, 1],), ([1, 0],), ([1, 0], [2, 0]), ([0, 0], [1, 0], [2, 0]))
(([0, 1],), ([1, 0],), ([1, 0], [2, 0]), ([0, 1], [1, 0], [2, 0]))
(([0, 1],), ([1, 0],), ([1, 0], [2, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
(([0, 1],), ([1, 0],), ([0, 0], [0, 1], [1, 0]), ([0, 0], [0, 1], [2, 0]))
(([0, 1],), ([1, 0],), ([0, 0], [0, 1], [1, 0]), ([0, 0], [1, 0], [2, 0]))
(([0, 1],), ([1, 0],), ([0, 0], [0, 1], [1, 0]), ([0, 1], [1, 0], [2, 0]))
(([0, 1],), ([1, 0],), ([0, 0], [0, 1], [1, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
(([0, 1],), ([1, 0],), ([0, 0], [0, 1], [2, 0]), ([0, 0], [1, 0], [2, 0]))
(([0, 1],), ([1, 0],), ([0, 0], [0, 1], [2, 0]), ([0, 1], [1, 0], [2, 0]))
(([0, 1],), ([1, 0],), ([0, 0], [0, 1], [2, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
(([0, 1],), ([1, 0],), ([0, 0], [1, 0], [2, 0]), ([0, 1], [1, 0], [2, 0]))
(([0, 1],), ([1, 0],), ([0, 0], [1, 0], [2, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
(([0, 1],), ([1, 0],), ([0, 1], [1, 0], [2, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
(([0, 1],), ([2, 0],), ([0, 0], [0, 1]), ([0, 0], [1, 0]))
(([0, 1],), ([2, 0],), ([0, 0], [0, 1]), ([0, 0], [2, 0]))
(([0, 1],), ([2, 0],), ([0, 0], [0, 1]), ([0, 1], [1, 0]))
(([0, 1],), ([2, 0],), ([0, 0], [0, 1]), ([0, 1], [2, 0]))
(([0, 1],), ([2, 0],), ([0, 0], [0, 1]), ([1, 0], [2, 0]))
(([0, 1],), ([2, 0],), ([0, 0], [0, 1]), ([0, 0], [0, 1], [1, 0]))
(([0, 1],), ([2, 0],), ([0, 0], [0, 1]), ([0, 0], [0, 1], [2, 0]))
(([0, 1],), ([2, 0],), ([0, 0], [0, 1]), ([0, 0], [1, 0], [2, 0]))
(([0, 1],), ([2, 0],), ([0, 0], [0, 1]), ([0, 1], [1, 0], [2, 0]))
(([0, 1],), ([2, 0],), ([0, 0], [0, 1]), ([0, 0], [0, 1], [1, 0], [2, 0]))
(([0, 1],), ([2, 0],), ([0, 0], [1, 0]), ([0, 0], [2, 0]))
(([0, 1],), ([2, 0],), ([0, 0], [1, 0]), ([0, 1], [1, 0]))
(([0, 1],), ([2, 0],), ([0, 0], [1, 0]), ([0, 1], [2, 0]))
(([0, 1],), ([2, 0],), ([0, 0], [1, 0]), ([1, 0], [2, 0]))
(([0, 1],), ([2, 0],), ([0, 0], [1, 0]), ([0, 0], [0, 1], [1, 0]))
(([0, 1],), ([2, 0],), ([0, 0], [1, 0]), ([0, 0], [0, 1], [2, 0]))
(([0, 1],), ([2, 0],), ([0, 0], [1, 0]), ([0, 0], [1, 0], [2, 0]))
(([0, 1],), ([2, 0],), ([0, 0], [1, 0]), ([0, 1], [1, 0], [2, 0]))
(([0, 1],), ([2, 0],), ([0, 0], [1, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
(([0, 1],), ([2, 0],), ([0, 0], [2, 0]), ([0, 1], [1, 0]))
(([0, 1],), ([2, 0],), ([0, 0], [2, 0]), ([0, 1], [2, 0]))
(([0, 1],), ([2, 0],), ([0, 0], [2, 0]), ([1, 0], [2, 0]))
(([0, 1],), ([2, 0],), ([0, 0], [2, 0]), ([0, 0], [0, 1], [1, 0]))
(([0, 1],), ([2, 0],), ([0, 0], [2, 0]), ([0, 0], [0, 1], [2, 0]))
(([0, 1],), ([2, 0],), ([0, 0], [2, 0]), ([0, 0], [1, 0], [2, 0]))
(([0, 1],), ([2, 0],), ([0, 0], [2, 0]), ([0, 1], [1, 0], [2, 0]))
(([0, 1],), ([2, 0],), ([0, 0], [2, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
(([0, 1],), ([2, 0],), ([0, 1], [1, 0]), ([0, 1], [2, 0]))
(([0, 1],), ([2, 0],), ([0, 1], [1, 0]), ([1, 0], [2, 0]))
(([0, 1],), ([2, 0],), ([0, 1], [1, 0]), ([0, 0], [0, 1], [1, 0]))
(([0, 1],), ([2, 0],), ([0, 1], [1, 0]), ([0, 0], [0, 1], [2, 0]))
(([0, 1],), ([2, 0],), ([0, 1], [1, 0]), ([0, 0], [1, 0], [2, 0]))
(([0, 1],), ([2, 0],), ([0, 1], [1, 0]), ([0, 1], [1, 0], [2, 0]))
(([0, 1],), ([2, 0],), ([0, 1], [1, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
(([0, 1],), ([2, 0],), ([0, 1], [2, 0]), ([1, 0], [2, 0]))
(([0, 1],), ([2, 0],), ([0, 1], [2, 0]), ([0, 0], [0, 1], [1, 0]))
(([0, 1],), ([2, 0],), ([0, 1], [2, 0]), ([0, 0], [0, 1], [2, 0]))
(([0, 1],), ([2, 0],), ([0, 1], [2, 0]), ([0, 0], [1, 0], [2, 0]))
(([0, 1],), ([2, 0],), ([0, 1], [2, 0]), ([0, 1], [1, 0], [2, 0]))
(([0, 1],), ([2, 0],), ([0, 1], [2, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
(([0, 1],), ([2, 0],), ([1, 0], [2, 0]), ([0, 0], [0, 1], [1, 0]))
(([0, 1],), ([2, 0],), ([1, 0], [2, 0]), ([0, 0], [0, 1], [2, 0]))
(([0, 1],), ([2, 0],), ([1, 0], [2, 0]), ([0, 0], [1, 0], [2, 0]))
(([0, 1],), ([2, 0],), ([1, 0], [2, 0]), ([0, 1], [1, 0], [2, 0]))
(([0, 1],), ([2, 0],), ([1, 0], [2, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
(([0, 1],), ([2, 0],), ([0, 0], [0, 1], [1, 0]), ([0, 0], [0, 1], [2, 0]))
(([0, 1],), ([2, 0],), ([0, 0], [0, 1], [1, 0]), ([0, 0], [1, 0], [2, 0]))
(([0, 1],), ([2, 0],), ([0, 0], [0, 1], [1, 0]), ([0, 1], [1, 0], [2, 0]))
(([0, 1],), ([2, 0],), ([0, 0], [0, 1], [1, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
(([0, 1],), ([2, 0],), ([0, 0], [0, 1], [2, 0]), ([0, 0], [1, 0], [2, 0]))
(([0, 1],), ([2, 0],), ([0, 0], [0, 1], [2, 0]), ([0, 1], [1, 0], [2, 0]))
(([0, 1],), ([2, 0],), ([0, 0], [0, 1], [2, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
(([0, 1],), ([2, 0],), ([0, 0], [1, 0], [2, 0]), ([0, 1], [1, 0], [2, 0]))
(([0, 1],), ([2, 0],), ([0, 0], [1, 0], [2, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
(([0, 1],), ([2, 0],), ([0, 1], [1, 0], [2, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
(([0, 1],), ([0, 0], [0, 1]), ([0, 0], [1, 0]), ([0, 0], [2, 0]))
(([0, 1],), ([0, 0], [0, 1]), ([0, 0], [1, 0]), ([0, 1], [1, 0]))
(([0, 1],), ([0, 0], [0, 1]), ([0, 0], [1, 0]), ([0, 1], [2, 0]))
(([0, 1],), ([0, 0], [0, 1]), ([0, 0], [1, 0]), ([1, 0], [2, 0]))
(([0, 1],), ([0, 0], [0, 1]), ([0, 0], [1, 0]), ([0, 0], [0, 1], [1, 0]))
(([0, 1],), ([0, 0], [0, 1]), ([0, 0], [1, 0]), ([0, 0], [0, 1], [2, 0]))
(([0, 1],), ([0, 0], [0, 1]), ([0, 0], [1, 0]), ([0, 0], [1, 0], [2, 0]))
(([0, 1],), ([0, 0], [0, 1]), ([0, 0], [1, 0]), ([0, 1], [1, 0], [2, 0]))
(([0, 1],), ([0, 0], [0, 1]), ([0, 0], [1, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
(([0, 1],), ([0, 0], [0, 1]), ([0, 0], [2, 0]), ([0, 1], [1, 0]))
(([0, 1],), ([0, 0], [0, 1]), ([0, 0], [2, 0]), ([0, 1], [2, 0]))
(([0, 1],), ([0, 0], [0, 1]), ([0, 0], [2, 0]), ([1, 0], [2, 0]))
(([0, 1],), ([0, 0], [0, 1]), ([0, 0], [2, 0]), ([0, 0], [0, 1], [1, 0]))
(([0, 1],), ([0, 0], [0, 1]), ([0, 0], [2, 0]), ([0, 0], [0, 1], [2, 0]))
(([0, 1],), ([0, 0], [0, 1]), ([0, 0], [2, 0]), ([0, 0], [1, 0], [2, 0]))
(([0, 1],), ([0, 0], [0, 1]), ([0, 0], [2, 0]), ([0, 1], [1, 0], [2, 0]))
(([0, 1],), ([0, 0], [0, 1]), ([0, 0], [2, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
(([0, 1],), ([0, 0], [0, 1]), ([0, 1], [1, 0]), ([0, 1], [2, 0]))
(([0, 1],), ([0, 0], [0, 1]), ([0, 1], [1, 0]), ([1, 0], [2, 0]))
(([0, 1],), ([0, 0], [0, 1]), ([0, 1], [1, 0]), ([0, 0], [0, 1], [1, 0]))
(([0, 1],), ([0, 0], [0, 1]), ([0, 1], [1, 0]), ([0, 0], [0, 1], [2, 0]))
(([0, 1],), ([0, 0], [0, 1]), ([0, 1], [1, 0]), ([0, 0], [1, 0], [2, 0]))
(([0, 1],), ([0, 0], [0, 1]), ([0, 1], [1, 0]), ([0, 1], [1, 0], [2, 0]))
(([0, 1],), ([0, 0], [0, 1]), ([0, 1], [1, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
(([0, 1],), ([0, 0], [0, 1]), ([0, 1], [2, 0]), ([1, 0], [2, 0]))
(([0, 1],), ([0, 0], [0, 1]), ([0, 1], [2, 0]), ([0, 0], [0, 1], [1, 0]))
(([0, 1],), ([0, 0], [0, 1]), ([0, 1], [2, 0]), ([0, 0], [0, 1], [2, 0]))
(([0, 1],), ([0, 0], [0, 1]), ([0, 1], [2, 0]), ([0, 0], [1, 0], [2, 0]))
(([0, 1],), ([0, 0], [0, 1]), ([0, 1], [2, 0]), ([0, 1], [1, 0], [2, 0]))
(([0, 1],), ([0, 0], [0, 1]), ([0, 1], [2, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
(([0, 1],), ([0, 0], [0, 1]), ([1, 0], [2, 0]), ([0, 0], [0, 1], [1, 0]))
(([0, 1],), ([0, 0], [0, 1]), ([1, 0], [2, 0]), ([0, 0], [0, 1], [2, 0]))
(([0, 1],), ([0, 0], [0, 1]), ([1, 0], [2, 0]), ([0, 0], [1, 0], [2, 0]))
(([0, 1],), ([0, 0], [0, 1]), ([1, 0], [2, 0]), ([0, 1], [1, 0], [2, 0]))
(([0, 1],), ([0, 0], [0, 1]), ([1, 0], [2, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
(([0, 1],), ([0, 0], [0, 1]), ([0, 0], [0, 1], [1, 0]), ([0, 0], [0, 1], [2, 0]))
(([0, 1],), ([0, 0], [0, 1]), ([0, 0], [0, 1], [1, 0]), ([0, 0], [1, 0], [2, 0]))
(([0, 1],), ([0, 0], [0, 1]), ([0, 0], [0, 1], [1, 0]), ([0, 1], [1, 0], [2, 0]))
(([0, 1],), ([0, 0], [0, 1]), ([0, 0], [0, 1], [1, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
(([0, 1],), ([0, 0], [0, 1]), ([0, 0], [0, 1], [2, 0]), ([0, 0], [1, 0], [2, 0]))
(([0, 1],), ([0, 0], [0, 1]), ([0, 0], [0, 1], [2, 0]), ([0, 1], [1, 0], [2, 0]))
(([0, 1],), ([0, 0], [0, 1]), ([0, 0], [0, 1], [2, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
(([0, 1],), ([0, 0], [0, 1]), ([0, 0], [1, 0], [2, 0]), ([0, 1], [1, 0], [2, 0]))
(([0, 1],), ([0, 0], [0, 1]), ([0, 0], [1, 0], [2, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
(([0, 1],), ([0, 0], [0, 1]), ([0, 1], [1, 0], [2, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
(([0, 1],), ([0, 0], [1, 0]), ([0, 0], [2, 0]), ([0, 1], [1, 0]))
(([0, 1],), ([0, 0], [1, 0]), ([0, 0], [2, 0]), ([0, 1], [2, 0]))
(([0, 1],), ([0, 0], [1, 0]), ([0, 0], [2, 0]), ([1, 0], [2, 0]))
(([0, 1],), ([0, 0], [1, 0]), ([0, 0], [2, 0]), ([0, 0], [0, 1], [1, 0]))
(([0, 1],), ([0, 0], [1, 0]), ([0, 0], [2, 0]), ([0, 0], [0, 1], [2, 0]))
(([0, 1],), ([0, 0], [1, 0]), ([0, 0], [2, 0]), ([0, 0], [1, 0], [2, 0]))
(([0, 1],), ([0, 0], [1, 0]), ([0, 0], [2, 0]), ([0, 1], [1, 0], [2, 0]))
(([0, 1],), ([0, 0], [1, 0]), ([0, 0], [2, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
(([0, 1],), ([0, 0], [1, 0]), ([0, 1], [1, 0]), ([0, 1], [2, 0]))
(([0, 1],), ([0, 0], [1, 0]), ([0, 1], [1, 0]), ([1, 0], [2, 0]))
(([0, 1],), ([0, 0], [1, 0]), ([0, 1], [1, 0]), ([0, 0], [0, 1], [1, 0]))
(([0, 1],), ([0, 0], [1, 0]), ([0, 1], [1, 0]), ([0, 0], [0, 1], [2, 0]))
(([0, 1],), ([0, 0], [1, 0]), ([0, 1], [1, 0]), ([0, 0], [1, 0], [2, 0]))
(([0, 1],), ([0, 0], [1, 0]), ([0, 1], [1, 0]), ([0, 1], [1, 0], [2, 0]))
(([0, 1],), ([0, 0], [1, 0]), ([0, 1], [1, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
(([0, 1],), ([0, 0], [1, 0]), ([0, 1], [2, 0]), ([1, 0], [2, 0]))
(([0, 1],), ([0, 0], [1, 0]), ([0, 1], [2, 0]), ([0, 0], [0, 1], [1, 0]))
(([0, 1],), ([0, 0], [1, 0]), ([0, 1], [2, 0]), ([0, 0], [0, 1], [2, 0]))
(([0, 1],), ([0, 0], [1, 0]), ([0, 1], [2, 0]), ([0, 0], [1, 0], [2, 0]))
(([0, 1],), ([0, 0], [1, 0]), ([0, 1], [2, 0]), ([0, 1], [1, 0], [2, 0]))
(([0, 1],), ([0, 0], [1, 0]), ([0, 1], [2, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
(([0, 1],), ([0, 0], [1, 0]), ([1, 0], [2, 0]), ([0, 0], [0, 1], [1, 0]))
(([0, 1],), ([0, 0], [1, 0]), ([1, 0], [2, 0]), ([0, 0], [0, 1], [2, 0]))
(([0, 1],), ([0, 0], [1, 0]), ([1, 0], [2, 0]), ([0, 0], [1, 0], [2, 0]))
(([0, 1],), ([0, 0], [1, 0]), ([1, 0], [2, 0]), ([0, 1], [1, 0], [2, 0]))
(([0, 1],), ([0, 0], [1, 0]), ([1, 0], [2, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
(([0, 1],), ([0, 0], [1, 0]), ([0, 0], [0, 1], [1, 0]), ([0, 0], [0, 1], [2, 0]))
(([0, 1],), ([0, 0], [1, 0]), ([0, 0], [0, 1], [1, 0]), ([0, 0], [1, 0], [2, 0]))
(([0, 1],), ([0, 0], [1, 0]), ([0, 0], [0, 1], [1, 0]), ([0, 1], [1, 0], [2, 0]))
(([0, 1],), ([0, 0], [1, 0]), ([0, 0], [0, 1], [1, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
(([0, 1],), ([0, 0], [1, 0]), ([0, 0], [0, 1], [2, 0]), ([0, 0], [1, 0], [2, 0]))
(([0, 1],), ([0, 0], [1, 0]), ([0, 0], [0, 1], [2, 0]), ([0, 1], [1, 0], [2, 0]))
(([0, 1],), ([0, 0], [1, 0]), ([0, 0], [0, 1], [2, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
(([0, 1],), ([0, 0], [1, 0]), ([0, 0], [1, 0], [2, 0]), ([0, 1], [1, 0], [2, 0]))
(([0, 1],), ([0, 0], [1, 0]), ([0, 0], [1, 0], [2, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
(([0, 1],), ([0, 0], [1, 0]), ([0, 1], [1, 0], [2, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
(([0, 1],), ([0, 0], [2, 0]), ([0, 1], [1, 0]), ([0, 1], [2, 0]))
(([0, 1],), ([0, 0], [2, 0]), ([0, 1], [1, 0]), ([1, 0], [2, 0]))
(([0, 1],), ([0, 0], [2, 0]), ([0, 1], [1, 0]), ([0, 0], [0, 1], [1, 0]))
(([0, 1],), ([0, 0], [2, 0]), ([0, 1], [1, 0]), ([0, 0], [0, 1], [2, 0]))
(([0, 1],), ([0, 0], [2, 0]), ([0, 1], [1, 0]), ([0, 0], [1, 0], [2, 0]))
(([0, 1],), ([0, 0], [2, 0]), ([0, 1], [1, 0]), ([0, 1], [1, 0], [2, 0]))
(([0, 1],), ([0, 0], [2, 0]), ([0, 1], [1, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))
(([0, 1],), ([0, 0], [2, 0]), ([0, 1], [2, 0]), ([1, 0], [2, 0]))
(([0, 1],), ([0, 0], [2, 0]), ([0, 1], [2, 0]), ([0, 0], [0, 1], [1, 0]))
(([0, 1],), ([0, 0], [2, 0]), ([0, 1], [2, 0]), ([0, 0], [0, 1], [2, 0]))
(([0, 1],), ([0, 0], [2, 0]), ([0, 1], [2, 0]), ([0, 0], [1, 0], [2, 0]))
(([0, 1],), ([0, 0], [2, 0]), ([0, 1], [2, 0]), ([0, 1], [1, 0], [2, 0]))
(([0, 1],), ([0, 0], [2, 0]), ([0, 1], [2, 0]), ([0, 0], [0, 1], [1, 0], [2, 0]))Traceback (most recent call last):
  File "C:\An\Delta Func\powerset testing.py", line 9, in <module>
    print(x)
  File "C:\Personalize\Python\lib\idlelib\PyShell.py", line 1347, in write
    return self.shell.write(s, self.tags)
KeyboardInterrupt
>>> ================================ RESTART ================================
>>> 
()
((),)
(('a',),)
(('b',),)
(('a', 'b'),)
((), ('a',))
((), ('b',))
((), ('a', 'b'))
(('a',), ('b',))
(('a',), ('a', 'b'))
(('b',), ('a', 'b'))
((), ('a',), ('b',))
((), ('a',), ('a', 'b'))
((), ('b',), ('a', 'b'))
(('a',), ('b',), ('a', 'b'))
((), ('a',), ('b',), ('a', 'b'))
>>> ================================ RESTART ================================
>>> 
()
('1',)
('2',)
('1', '2')
>>> ================================ RESTART ================================
>>> 
[]
>>> ================================ RESTART ================================
>>> 
[[0.0, 0.0]]
>>> ================================ RESTART ================================
>>> 
[]
>>> ================================ RESTART ================================
>>> 
[[0.0, 0.0]]
>>> ================================ RESTART ================================
>>> 
[[1.0, 0.0]]
>>> ================================ RESTART ================================
>>> 
yes at 0
[[[0.0, 0.0]]]
>>> ================================ RESTART ================================
>>> 
yes at 0
[[[0.0, 0.0]]]
yes at 1
yes at 2
yes at 3
yes at 6
[[[1.0, 0.0]], [[0.0, 1.0]], [[2.0, 0.0]], [[3.0, 0.0]]]
>>> ================================ RESTART ================================
>>> 
[[1.0, 1.0]]
>>> ================================ RESTART ================================
>>> 
yes at 1
[]
>>> ================================ RESTART ================================
>>> 
yes at 1
[]
Traceback (most recent call last):
  File "C:/An/Delta Func/autocomposer.py", line 141, in <module>
    file = open('Auto.txt', 'r+')
FileNotFoundError: [Errno 2] No such file or directory: 'Auto.txt'
>>> ================================ RESTART ================================
>>> 
yes at 1
[]
Traceback (most recent call last):
  File "C:/An/Delta Func/autocomposer.py", line 147, in <module>
    f.write(
NameError: name 'f' is not defined
>>> ================================ RESTART ================================
>>> 
yes at 1
[]
yes at 1
yes at 1
Traceback (most recent call last):
  File "C:/An/Delta Func/autocomposer.py", line 149, in <module>
    [AutoVision(1,1),AutoVision(2,2)],gcomposition(AutoVision(1,1),AutoVision(2,2))]
TypeError: must be str, not list
>>> ================================ RESTART ================================
>>> 
yes at 1
[]
yes at 1
yes at 1
yes at 1
yes at 1
yes at 1
yes at 1
yes at 1
yes at 1
yes at 1
yes at 1
yes at 1
yes at 1
yes at 1
yes at 1
yes at 1
yes at 1
yes at 1
yes at 1
yes at 1
yes at 1
yes at 1
yes at 1
yes at 1
yes at 1
yes at 1
yes at 1
yes at 1
yes at 1
yes at 1
yes at 1
yes at 1
yes at 1
yes at 1
yes at 1
yes at 1
yes at 1
yes at 1
yes at 1
yes at 1
yes at 1
yes at 1
yes at 1
yes at 1
yes at 1
yes at 1
yes at 1
yes at 1
yes at 1
yes at 1
yes at 1
>>> ================================ RESTART ================================
>>> 
[]
>>> ================================ RESTART ================================
>>> 
[]
>>> ================================ RESTART ================================
>>> 
[]
Traceback (most recent call last):
  File "C:/An/Delta Func/autocomposer.py", line 146, in <module>
    file.write(str([[AutoVision(x,top),AutoVision(y,top)],gcomposition(AutoVision(x,top),AutoVision(y,top))]))
  File "C:/An/Delta Func/autocomposer.py", line 135, in gcomposition
    if y[0] == x[1]:
IndexError: list index out of range
>>> ================================ RESTART ================================
>>> 
[]
>>> ================================ RESTART ================================
>>> 
[]
Traceback (most recent call last):
  File "C:/An/Delta Func/autocomposer.py", line 146, in <module>
    file.write(str([[AutoVision(x,top),AutoVision(y,top)],gcomposition(AutoVision(x,top),AutoVision(y,top))]))
  File "C:/An/Delta Func/autocomposer.py", line 135, in gcomposition
    if y[0] == x[1]:
IndexError: list index out of range
>>> ================================ RESTART ================================
>>> 
[1.0, 0.0] 0.0
[]
Traceback (most recent call last):
  File "C:/An/Delta Func/autocomposer.py", line 147, in <module>
    file.write(str([[AutoVision(x,top),AutoVision(y,top)],gcomposition(AutoVision(x,top),AutoVision(y,top))]))
  File "C:/An/Delta Func/autocomposer.py", line 135, in gcomposition
    print(y[0],x[1])
IndexError: list index out of range
>>> ================================ RESTART ================================
>>> 
[1.0, 0.0] [[1.0, 0.0]] [1.0, 0.0] 0.0
[]
Traceback (most recent call last):
  File "C:/An/Delta Func/autocomposer.py", line 147, in <module>
    file.write(str([[AutoVision(x,top),AutoVision(y,top)],gcomposition(AutoVision(x,top),AutoVision(y,top))]))
  File "C:/An/Delta Func/autocomposer.py", line 135, in gcomposition
    print(x,y,y[0],x[1])
IndexError: list index out of range
>>> ================================ RESTART ================================
>>> 
[1.0, 0.0] wtf [[1.0, 0.0]] [1.0, 0.0] 0.0
[]
Traceback (most recent call last):
  File "C:/An/Delta Func/autocomposer.py", line 147, in <module>
    file.write(str([[AutoVision(x,top),AutoVision(y,top)],gcomposition(AutoVision(x,top),AutoVision(y,top))]))
  File "C:/An/Delta Func/autocomposer.py", line 135, in gcomposition
    print(x,"wtf",y,y[0],x[1])
IndexError: list index out of range
>>> ================================ RESTART ================================
>>> 
[1.0, 0.0] [[1.0, 0.0]]
[]
[[0.0, 0.0]] [[0.0, 0.0]]
Traceback (most recent call last):
  File "C:/An/Delta Func/autocomposer.py", line 148, in <module>
    file.write(str([[AutoVision(x,top),AutoVision(y,top)],gcomposition(AutoVision(x,top),AutoVision(y,top))]))
  File "C:/An/Delta Func/autocomposer.py", line 137, in gcomposition
    if y[0] == x[1]:
IndexError: list index out of range
>>> ================================ RESTART ================================
>>> 
[1.0, 0.0] [[1.0, 0.0]]
[]
what [] []
what [] [[[0.0, 0.0]]]
what [[[0.0, 0.0]]] []
what [[[0.0, 0.0]]] [[[0.0, 0.0]]]
[[0.0, 0.0]] [[0.0, 0.0]]
Traceback (most recent call last):
  File "C:/An/Delta Func/autocomposer.py", line 149, in <module>
    file.write(str([[AutoVision(x,top),AutoVision(y,top)],gcomposition(AutoVision(x,top),AutoVision(y,top))]))
  File "C:/An/Delta Func/autocomposer.py", line 137, in gcomposition
    if y[0] == x[1]:
IndexError: list index out of range
>>> ================================ RESTART ================================
>>> 
[1.0, 0.0] [[1.0, 0.0]]
[]
0 0 2
what [] []
0 1 2
what [] [[[0.0, 0.0]]]
1 0 2
what [[[0.0, 0.0]]] []
1 1 2
what [[[0.0, 0.0]]] [[[0.0, 0.0]]]
[[0.0, 0.0]] [[0.0, 0.0]]
Traceback (most recent call last):
  File "C:/An/Delta Func/autocomposer.py", line 150, in <module>
    file.write(str([[AutoVision(x,top),AutoVision(y,top)],gcomposition(AutoVision(x,top),AutoVision(y,top))]))
  File "C:/An/Delta Func/autocomposer.py", line 137, in gcomposition
    if y[0] == x[1]:
IndexError: list index out of range
>>> ================================ RESTART ================================
>>> 
[1.0, 0.0] [[1.0, 0.0]]
[]
0 0 1
what [[0.0, 0.0]] [[0.0, 0.0]]
[0.0, 0.0] [0.0, 0.0]
0 0 2
what [] []
0 1 2
what [] [[[0.0, 0.0]]]
1 0 2
what [[[0.0, 0.0]]] []
1 1 2
what [[[0.0, 0.0]]] [[[0.0, 0.0]]]
[[0.0, 0.0]] [[0.0, 0.0]]
Traceback (most recent call last):
  File "C:/An/Delta Func/autocomposer.py", line 150, in <module>
    file.write(str([[AutoVision(x,top),AutoVision(y,top)],gcomposition(AutoVision(x,top),AutoVision(y,top))]))
  File "C:/An/Delta Func/autocomposer.py", line 137, in gcomposition
    if y[0] == x[1]:
IndexError: list index out of range
>>> ================================ RESTART ================================
>>> 
[1.0, 0.0] [[1.0, 0.0]]
[]
0 0 1
what [[0.0, 0.0]] [[0.0, 0.0]]
0 0 2
what [] []
0 1 2
what [] [[[0.0, 0.0]]]
1 0 2
what [[[0.0, 0.0]]] []
1 1 2
what [[[0.0, 0.0]]] [[[0.0, 0.0]]]
0 0 3
what [] []
0 1 3
what [] [[]]
0 2 3
what [] [[[[0.0, 0.0]]]]
1 0 3
what [[]] []
1 1 3
what [[]] [[]]
1 2 3
what [[]] [[[[0.0, 0.0]]]]
2 0 3
what [[[[0.0, 0.0]]]] []
2 1 3
what [[[[0.0, 0.0]]]] [[]]
2 2 3
what [[[[0.0, 0.0]]]] [[[[0.0, 0.0]]]]
0 0 4
what [] []
0 1 4
what [] [[]]
0 2 4
what [] [[[]]]
0 3 4
what [] [[], [[]]]
1 0 4
what [[]] []
1 1 4
what [[]] [[]]
1 2 4
what [[]] [[[]]]
1 3 4
what [[]] [[], [[]]]
2 0 4
what [[[]]] []
2 1 4
what [[[]]] [[]]
2 2 4
what [[[]]] [[[]]]
2 3 4
what [[[]]] [[], [[]]]
3 0 4
what [[], [[]]] []
3 1 4
what [[], [[]]] [[]]
3 2 4
what [[], [[]]] [[[]]]
3 3 4
what [[], [[]]] [[], [[]]]
>>> ================================ RESTART ================================
>>> 
[1.0, 0.0] [[1.0, 0.0]]
[]
0 0 0
what [] []
0 0 1
what [[0.0, 0.0]] [[0.0, 0.0]]
0 1 1
what [[0.0, 0.0]] [[1.0, 0.0]]
1 0 1
what [[1.0, 0.0]] [[0.0, 0.0]]
1 1 1
what [[1.0, 0.0]] [[1.0, 0.0]]
0 0 2
what [] []
0 1 2
what [] [[[0.0, 0.0]]]
0 2 2
what [] [[[1.0, 0.0]]]
1 0 2
what [[[0.0, 0.0]]] []
1 1 2
what [[[0.0, 0.0]]] [[[0.0, 0.0]]]
1 2 2
what [[[0.0, 0.0]]] [[[1.0, 0.0]]]
2 0 2
what [[[1.0, 0.0]]] []
2 1 2
what [[[1.0, 0.0]]] [[[0.0, 0.0]]]
2 2 2
what [[[1.0, 0.0]]] [[[1.0, 0.0]]]
0 0 3
what [] []
0 1 3
what [] [[]]
0 2 3
what [] [[[[0.0, 0.0]]]]
0 3 3
what [] [[], [[[0.0, 0.0]]]]
1 0 3
what [[]] []
1 1 3
what [[]] [[]]
1 2 3
what [[]] [[[[0.0, 0.0]]]]
1 3 3
what [[]] [[], [[[0.0, 0.0]]]]
2 0 3
what [[[[0.0, 0.0]]]] []
2 1 3
what [[[[0.0, 0.0]]]] [[]]
2 2 3
what [[[[0.0, 0.0]]]] [[[[0.0, 0.0]]]]
2 3 3
what [[[[0.0, 0.0]]]] [[], [[[0.0, 0.0]]]]
3 0 3
what [[], [[[0.0, 0.0]]]] []
3 1 3
what [[], [[[0.0, 0.0]]]] [[]]
3 2 3
what [[], [[[0.0, 0.0]]]] [[[[0.0, 0.0]]]]
3 3 3
what [[], [[[0.0, 0.0]]]] [[], [[[0.0, 0.0]]]]
0 0 4
what [] []
0 1 4
what [] [[]]
0 2 4
what [] [[[]]]
0 3 4
what [] [[], [[]]]
0 4 4
what [] [[[[[0.0, 0.0]]]]]
1 0 4
what [[]] []
1 1 4
what [[]] [[]]
1 2 4
what [[]] [[[]]]
1 3 4
what [[]] [[], [[]]]
1 4 4
what [[]] [[[[[0.0, 0.0]]]]]
2 0 4
what [[[]]] []
2 1 4
what [[[]]] [[]]
2 2 4
what [[[]]] [[[]]]
2 3 4
what [[[]]] [[], [[]]]
2 4 4
what [[[]]] [[[[[0.0, 0.0]]]]]
3 0 4
what [[], [[]]] []
3 1 4
what [[], [[]]] [[]]
3 2 4
what [[], [[]]] [[[]]]
3 3 4
what [[], [[]]] [[], [[]]]
3 4 4
what [[], [[]]] [[[[[0.0, 0.0]]]]]
4 0 4
what [[[[[0.0, 0.0]]]]] []
4 1 4
what [[[[[0.0, 0.0]]]]] [[]]
4 2 4
what [[[[[0.0, 0.0]]]]] [[[]]]
4 3 4
what [[[[[0.0, 0.0]]]]] [[], [[]]]
4 4 4
what [[[[[0.0, 0.0]]]]] [[[[[0.0, 0.0]]]]]
>>> ================================ RESTART ================================
>>> 
[1.0, 0.0] [[1.0, 0.0]]
[]
0 0 0
what [] []
0 0 1
what [[0.0, 0.0]] [[0.0, 0.0]]
[0.0, 0.0] [0.0, 0.0]
0 1 1
what [[0.0, 0.0]] [[1.0, 0.0]]
[0.0, 0.0] [1.0, 0.0]
1 0 1
what [[1.0, 0.0]] [[0.0, 0.0]]
[1.0, 0.0] [0.0, 0.0]
1 1 1
what [[1.0, 0.0]] [[1.0, 0.0]]
[1.0, 0.0] [1.0, 0.0]
0 0 2
what [] []
0 1 2
what [] [[[0.0, 0.0]]]
0 2 2
what [] [[[1.0, 0.0]]]
1 0 2
what [[[0.0, 0.0]]] []
1 1 2
what [[[0.0, 0.0]]] [[[0.0, 0.0]]]
[[0.0, 0.0]] [[0.0, 0.0]]
Traceback (most recent call last):
  File "C:/An/Delta Func/autocomposer.py", line 150, in <module>
    file.write(str([[AutoVision(x,top),AutoVision(y,top)],gcomposition(AutoVision(x,top),AutoVision(y,top))]))
  File "C:/An/Delta Func/autocomposer.py", line 137, in gcomposition
    if y[0] == x[1]:
IndexError: list index out of range
>>> ================================ RESTART ================================
>>> 
x,y [1.0, 0.0] [[1.0, 0.0]]
[1.0, 0.0] wtf [[1.0, 0.0]] [1.0, 0.0] 0.0
[]
0 0 0
what [] []
0 0 1
what [[0.0, 0.0]] [[0.0, 0.0]]
x,y [0.0, 0.0] [0.0, 0.0]
[0.0, 0.0] wtf [0.0, 0.0] 0.0 0.0
0 1 1
what [[0.0, 0.0]] [[1.0, 0.0]]
x,y [0.0, 0.0] [1.0, 0.0]
[0.0, 0.0] wtf [1.0, 0.0] 1.0 0.0
1 0 1
what [[1.0, 0.0]] [[0.0, 0.0]]
x,y [1.0, 0.0] [0.0, 0.0]
[1.0, 0.0] wtf [0.0, 0.0] 0.0 0.0
1 1 1
what [[1.0, 0.0]] [[1.0, 0.0]]
x,y [1.0, 0.0] [1.0, 0.0]
[1.0, 0.0] wtf [1.0, 0.0] 1.0 0.0
0 0 2
what [] []
0 1 2
what [] [[[0.0, 0.0]]]
0 2 2
what [] [[[1.0, 0.0]]]
1 0 2
what [[[0.0, 0.0]]] []
1 1 2
what [[[0.0, 0.0]]] [[[0.0, 0.0]]]
x,y [[0.0, 0.0]] [[0.0, 0.0]]
Traceback (most recent call last):
  File "C:/An/Delta Func/autocomposer.py", line 150, in <module>
    file.write(str([[AutoVision(x,top),AutoVision(y,top)],gcomposition(AutoVision(x,top),AutoVision(y,top))]))
  File "C:/An/Delta Func/autocomposer.py", line 136, in gcomposition
    print(x,"wtf",y,y[0],x[1])
IndexError: list index out of range
>>> ================================ RESTART ================================
>>> 
x,y [1.0, 0.0] [[1.0, 0.0]]
[1.0, 0.0] wtf [[1.0, 0.0]] [1.0, 0.0] 0.0
[]
0 0 0
input first:  [] []
0 0 1
input first:  [[0.0, 0.0]] [[0.0, 0.0]]
x,y [0.0, 0.0] [0.0, 0.0]
[0.0, 0.0] wtf [0.0, 0.0] 0.0 0.0
0 1 1
input first:  [[0.0, 0.0]] [[1.0, 0.0]]
x,y [0.0, 0.0] [1.0, 0.0]
[0.0, 0.0] wtf [1.0, 0.0] 1.0 0.0
1 0 1
input first:  [[1.0, 0.0]] [[0.0, 0.0]]
x,y [1.0, 0.0] [0.0, 0.0]
[1.0, 0.0] wtf [0.0, 0.0] 0.0 0.0
1 1 1
input first:  [[1.0, 0.0]] [[1.0, 0.0]]
x,y [1.0, 0.0] [1.0, 0.0]
[1.0, 0.0] wtf [1.0, 0.0] 1.0 0.0
0 0 2
input first:  [] []
0 1 2
input first:  [] [[[0.0, 0.0]]]
0 2 2
input first:  [] [[[1.0, 0.0]]]
1 0 2
input first:  [[[0.0, 0.0]]] []
1 1 2
input first:  [[[0.0, 0.0]]] [[[0.0, 0.0]]]
x,y [[0.0, 0.0]] [[0.0, 0.0]]
Traceback (most recent call last):
  File "C:/An/Delta Func/autocomposer.py", line 150, in <module>
    file.write(str([[AutoVision(x,top),AutoVision(y,top)],gcomposition(AutoVision(x,top),AutoVision(y,top))]))
  File "C:/An/Delta Func/autocomposer.py", line 136, in gcomposition
    print(x,"wtf",y,y[0],x[1])
IndexError: list index out of range
>>> ================================ RESTART ================================
>>> 
x,y [1.0, 0.0] [[1.0, 0.0]]
[1.0, 0.0] wtf [[1.0, 0.0]] [1.0, 0.0] 0.0
[]
0 0 0
input first: 
input pls:  [] []
0 0 1
input first: 
input pls:  [[0.0, 0.0]] [[0.0, 0.0]]
x,y [0.0, 0.0] [0.0, 0.0]
[0.0, 0.0] wtf [0.0, 0.0] 0.0 0.0
0 1 1
input first: 
input pls:  [[0.0, 0.0]] [[1.0, 0.0]]
x,y [0.0, 0.0] [1.0, 0.0]
[0.0, 0.0] wtf [1.0, 0.0] 1.0 0.0
1 0 1
input first: 
input pls:  [[1.0, 0.0]] [[0.0, 0.0]]
x,y [1.0, 0.0] [0.0, 0.0]
[1.0, 0.0] wtf [0.0, 0.0] 0.0 0.0
1 1 1
input first: 
input pls:  [[1.0, 0.0]] [[1.0, 0.0]]
x,y [1.0, 0.0] [1.0, 0.0]
[1.0, 0.0] wtf [1.0, 0.0] 1.0 0.0
0 0 2
input first: 
input pls:  [] []
0 1 2
input first: 
input pls:  [] [[[0.0, 0.0]]]
0 2 2
input first: 
input pls:  [] [[[1.0, 0.0]]]
1 0 2
input first: 
input pls:  [[[0.0, 0.0]]] []
1 1 2
input first: 
input pls:  [[[0.0, 0.0]]] [[[0.0, 0.0]]]
x,y [[0.0, 0.0]] [[0.0, 0.0]]
Traceback (most recent call last):
  File "C:/An/Delta Func/autocomposer.py", line 152, in <module>
    file.write(str([[AutoVision(x,top),AutoVision(y,top)],gcomposition(AutoVision(x,top),AutoVision(y,top))]))
  File "C:/An/Delta Func/autocomposer.py", line 136, in gcomposition
    print(x,"wtf",y,y[0],x[1])
IndexError: list index out of range
>>> ================================ RESTART ================================
>>> 
0 0 0
input first: 
input pls:  [] []
0 0 1
input first: 
input pls:  [[0.0, 0.0]] [[0.0, 0.0]]
x,y [0.0, 0.0] [0.0, 0.0]
[0.0, 0.0] wtf [0.0, 0.0] 0.0 0.0
0 1 1
input first: 
input pls:  [[0.0, 0.0]] [[1.0, 0.0]]
x,y [0.0, 0.0] [1.0, 0.0]
[0.0, 0.0] wtf [1.0, 0.0] 1.0 0.0
1 0 1
input first: 
input pls:  [[1.0, 0.0]] [[0.0, 0.0]]
x,y [1.0, 0.0] [0.0, 0.0]
[1.0, 0.0] wtf [0.0, 0.0] 0.0 0.0
1 1 1
input first: 
input pls:  [[1.0, 0.0]] [[1.0, 0.0]]
x,y [1.0, 0.0] [1.0, 0.0]
[1.0, 0.0] wtf [1.0, 0.0] 1.0 0.0
0 0 2
input first: 
input pls:  [] []
0 1 2
input first: 
input pls:  [] [[[0.0, 0.0]]]
0 2 2
input first: 
input pls:  [] [[[1.0, 0.0]]]
1 0 2
input first: 
input pls:  [[[0.0, 0.0]]] []
1 1 2
input first: 
input pls:  [[[0.0, 0.0]]] [[[0.0, 0.0]]]
x,y [[0.0, 0.0]] [[0.0, 0.0]]
Traceback (most recent call last):
  File "C:/An/Delta Func/autocomposer.py", line 152, in <module>
    file.write(str([[AutoVision(x,top),AutoVision(y,top)],gcomposition(AutoVision(x,top),AutoVision(y,top))]))
  File "C:/An/Delta Func/autocomposer.py", line 136, in gcomposition
    print(x,"wtf",y,y[0],x[1])
IndexError: list index out of range
>>> ================================ RESTART ================================
>>> 
0 0 0
input first:  [] []
0 0 1
input first:  [[0.0, 0.0]] [[0.0, 0.0]]
x,y [0.0, 0.0] [0.0, 0.0]
[0.0, 0.0] wtf [0.0, 0.0] 0.0 0.0
0 1 1
input first:  [[0.0, 0.0]] [[1.0, 0.0]]
x,y [0.0, 0.0] [1.0, 0.0]
[0.0, 0.0] wtf [1.0, 0.0] 1.0 0.0
1 0 1
input first:  [[1.0, 0.0]] [[0.0, 0.0]]
x,y [1.0, 0.0] [0.0, 0.0]
[1.0, 0.0] wtf [0.0, 0.0] 0.0 0.0
1 1 1
input first:  [[1.0, 0.0]] [[1.0, 0.0]]
x,y [1.0, 0.0] [1.0, 0.0]
[1.0, 0.0] wtf [1.0, 0.0] 1.0 0.0
0 0 2
input first:  [] []
0 1 2
input first:  [] [[[0.0, 0.0]]]
0 2 2
input first:  [] [[[1.0, 0.0]]]
1 0 2
input first:  [[[0.0, 0.0]]] []
1 1 2
input first:  [[[0.0, 0.0]]] [[[0.0, 0.0]]]
x,y [[0.0, 0.0]] [[0.0, 0.0]]
Traceback (most recent call last):
  File "C:/An/Delta Func/autocomposer.py", line 151, in <module>
    file.write(str([[AutoVision(x,top),AutoVision(y,top)],gcomposition(AutoVision(x,top),AutoVision(y,top))]))
  File "C:/An/Delta Func/autocomposer.py", line 136, in gcomposition
    print(x,"wtf",y,y[0],x[1])
IndexError: list index out of range
>>> ================================ RESTART ================================
>>> 
0 0 0
input first:  [] []
0 0 1
input first:  [[0.0, 0.0]] [[0.0, 0.0]]
x,y [0.0, 0.0] [0.0, 0.0]
[0.0, 0.0] wtf [0.0, 0.0] 0.0 0.0
0 1 1
input first:  [[0.0, 0.0]] [[1.0, 0.0]]
x,y [0.0, 0.0] [1.0, 0.0]
[0.0, 0.0] wtf [1.0, 0.0] 1.0 0.0
1 0 1
input first:  [[1.0, 0.0]] [[0.0, 0.0]]
x,y [1.0, 0.0] [0.0, 0.0]
[1.0, 0.0] wtf [0.0, 0.0] 0.0 0.0
1 1 1
input first:  [[1.0, 0.0]] [[1.0, 0.0]]
x,y [1.0, 0.0] [1.0, 0.0]
[1.0, 0.0] wtf [1.0, 0.0] 1.0 0.0
0 0 2
input first:  [] []
0 1 2
input first:  [] [[[0.0, 0.0]]]
0 2 2
input first:  [] [[[1.0, 0.0]]]
1 0 2
input first:  [[[0.0, 0.0]]] []
1 1 2
input first:  [[[0.0, 0.0]]] [[[0.0, 0.0]]]
x,y [[0.0, 0.0]] [[0.0, 0.0]]
Traceback (most recent call last):
  File "C:/An/Delta Func/autocomposer.py", line 151, in <module>
    file.write(str([[AutoVision(x,top),AutoVision(y,top)],gcomposition(AutoVision(x,top),AutoVision(y,top))]))
  File "C:/An/Delta Func/autocomposer.py", line 136, in gcomposition
    print(x,"wtf",y,y[0],x[1])
IndexError: list index out of range
>>> ================================ RESTART ================================
>>> 
0 0 0
input first:  [] []
0 0 1
input first:  [[0.0, 0.0]] [[0.0, 0.0]]
x,y [0.0, 0.0] [0.0, 0.0]
0 1 1
input first:  [[0.0, 0.0]] [[1.0, 0.0]]
x,y [0.0, 0.0] [1.0, 0.0]
1 0 1
input first:  [[1.0, 0.0]] [[0.0, 0.0]]
x,y [1.0, 0.0] [0.0, 0.0]
1 1 1
input first:  [[1.0, 0.0]] [[1.0, 0.0]]
x,y [1.0, 0.0] [1.0, 0.0]
0 0 2
input first:  [] []
0 1 2
input first:  [] [[[0.0, 0.0]]]
0 2 2
input first:  [] [[[1.0, 0.0]]]
1 0 2
input first:  [[[0.0, 0.0]]] []
1 1 2
input first:  [[[0.0, 0.0]]] [[[0.0, 0.0]]]
x,y [[0.0, 0.0]] [[0.0, 0.0]]
1 2 2
input first:  [[[0.0, 0.0]]] [[[1.0, 0.0]]]
x,y [[0.0, 0.0]] [[1.0, 0.0]]
2 0 2
input first:  [[[1.0, 0.0]]] []
2 1 2
input first:  [[[1.0, 0.0]]] [[[0.0, 0.0]]]
x,y [[1.0, 0.0]] [[0.0, 0.0]]
2 2 2
input first:  [[[1.0, 0.0]]] [[[1.0, 0.0]]]
x,y [[1.0, 0.0]] [[1.0, 0.0]]
0 0 3
input first:  [] []
0 1 3
input first:  [] [[]]
0 2 3
input first:  [] [[[[0.0, 0.0]]]]
0 3 3
input first:  [] [[], [[[0.0, 0.0]]]]
1 0 3
input first:  [[]] []
1 1 3
input first:  [[]] [[]]
x,y [] []
1 2 3
input first:  [[]] [[[[0.0, 0.0]]]]
x,y [] [[[0.0, 0.0]]]
1 3 3
input first:  [[]] [[], [[[0.0, 0.0]]]]
x,y [] []
x,y [] [[[0.0, 0.0]]]
2 0 3
input first:  [[[[0.0, 0.0]]]] []
2 1 3
input first:  [[[[0.0, 0.0]]]] [[]]
x,y [[[0.0, 0.0]]] []
2 2 3
input first:  [[[[0.0, 0.0]]]] [[[[0.0, 0.0]]]]
x,y [[[0.0, 0.0]]] [[[0.0, 0.0]]]
2 3 3
input first:  [[[[0.0, 0.0]]]] [[], [[[0.0, 0.0]]]]
x,y [[[0.0, 0.0]]] []
x,y [[[0.0, 0.0]]] [[[0.0, 0.0]]]
3 0 3
input first:  [[], [[[0.0, 0.0]]]] []
3 1 3
input first:  [[], [[[0.0, 0.0]]]] [[]]
x,y [] []
x,y [[[0.0, 0.0]]] []
3 2 3
input first:  [[], [[[0.0, 0.0]]]] [[[[0.0, 0.0]]]]
x,y [] [[[0.0, 0.0]]]
x,y [[[0.0, 0.0]]] [[[0.0, 0.0]]]
3 3 3
input first:  [[], [[[0.0, 0.0]]]] [[], [[[0.0, 0.0]]]]
x,y [] []
x,y [] [[[0.0, 0.0]]]
x,y [[[0.0, 0.0]]] []
x,y [[[0.0, 0.0]]] [[[0.0, 0.0]]]
0 0 4
input first:  [] []
0 1 4
input first:  [] [[]]
0 2 4
input first:  [] [[[]]]
0 3 4
input first:  [] [[], [[]]]
0 4 4
input first:  [] [[[[[0.0, 0.0]]]]]
1 0 4
input first:  [[]] []
1 1 4
input first:  [[]] [[]]
x,y [] []
1 2 4
input first:  [[]] [[[]]]
x,y [] [[]]
1 3 4
input first:  [[]] [[], [[]]]
x,y [] []
x,y [] [[]]
1 4 4
input first:  [[]] [[[[[0.0, 0.0]]]]]
x,y [] [[[[0.0, 0.0]]]]
2 0 4
input first:  [[[]]] []
2 1 4
input first:  [[[]]] [[]]
x,y [[]] []
2 2 4
input first:  [[[]]] [[[]]]
x,y [[]] [[]]
2 3 4
input first:  [[[]]] [[], [[]]]
x,y [[]] []
x,y [[]] [[]]
2 4 4
input first:  [[[]]] [[[[[0.0, 0.0]]]]]
x,y [[]] [[[[0.0, 0.0]]]]
3 0 4
input first:  [[], [[]]] []
3 1 4
input first:  [[], [[]]] [[]]
x,y [] []
x,y [[]] []
3 2 4
input first:  [[], [[]]] [[[]]]
x,y [] [[]]
x,y [[]] [[]]
3 3 4
input first:  [[], [[]]] [[], [[]]]
x,y [] []
x,y [] [[]]
x,y [[]] []
x,y [[]] [[]]
3 4 4
input first:  [[], [[]]] [[[[[0.0, 0.0]]]]]
x,y [] [[[[0.0, 0.0]]]]
x,y [[]] [[[[0.0, 0.0]]]]
4 0 4
input first:  [[[[[0.0, 0.0]]]]] []
4 1 4
input first:  [[[[[0.0, 0.0]]]]] [[]]
x,y [[[[0.0, 0.0]]]] []
4 2 4
input first:  [[[[[0.0, 0.0]]]]] [[[]]]
x,y [[[[0.0, 0.0]]]] [[]]
4 3 4
input first:  [[[[[0.0, 0.0]]]]] [[], [[]]]
x,y [[[[0.0, 0.0]]]] []
x,y [[[[0.0, 0.0]]]] [[]]
4 4 4
input first:  [[[[[0.0, 0.0]]]]] [[[[[0.0, 0.0]]]]]
x,y [[[[0.0, 0.0]]]] [[[[0.0, 0.0]]]]
>>> ================================ RESTART ================================
>>> 
0 0 0
input first:  [] []
0 0 1
input first:  [[0.0, 0.0]] [[0.0, 0.0]]
x,y [0.0, 0.0] [0.0, 0.0]
[0.0, 0.0] wtf [0.0, 0.0] 0.0 0.0
0 1 1
input first:  [[0.0, 0.0]] [[1.0, 0.0]]
x,y [0.0, 0.0] [1.0, 0.0]
[0.0, 0.0] wtf [1.0, 0.0] 1.0 0.0
1 0 1
input first:  [[1.0, 0.0]] [[0.0, 0.0]]
x,y [1.0, 0.0] [0.0, 0.0]
[1.0, 0.0] wtf [0.0, 0.0] 0.0 0.0
1 1 1
input first:  [[1.0, 0.0]] [[1.0, 0.0]]
x,y [1.0, 0.0] [1.0, 0.0]
[1.0, 0.0] wtf [1.0, 0.0] 1.0 0.0
0 0 2
input first:  [] []
0 1 2
input first:  [] [[[0.0, 0.0]]]
0 2 2
input first:  [] [[[1.0, 0.0]]]
1 0 2
input first:  [[[0.0, 0.0]]] []
1 1 2
input first:  [[[0.0, 0.0]]] [[[0.0, 0.0]]]
x,y [[0.0, 0.0]] [[0.0, 0.0]]
Traceback (most recent call last):
  File "C:/An/Delta Func/autocomposer.py", line 151, in <module>
    file.write(str([[AutoVision(x,top),AutoVision(y,top)],gcomposition(AutoVision(x,top),AutoVision(y,top))]))
  File "C:/An/Delta Func/autocomposer.py", line 136, in gcomposition
    print(x,"wtf",y,y[0],x[1])
IndexError: list index out of range
>>> ================================ RESTART ================================
>>> 
0 0 0
input first:  [] []
0 0 1
input first:  [[0.0, 0.0]] [[0.0, 0.0]]
x,y [0.0, 0.0] [0.0, 0.0]
[0.0, 0.0] wtf [0.0, 0.0] 0.0 0.0
0 1 1
input first:  [[0.0, 0.0]] [[1.0, 0.0]]
x,y [0.0, 0.0] [1.0, 0.0]
[0.0, 0.0] wtf [1.0, 0.0] 1.0 0.0
1 0 1
input first:  [[1.0, 0.0]] [[0.0, 0.0]]
x,y [1.0, 0.0] [0.0, 0.0]
[1.0, 0.0] wtf [0.0, 0.0] 0.0 0.0
1 1 1
input first:  [[1.0, 0.0]] [[1.0, 0.0]]
x,y [1.0, 0.0] [1.0, 0.0]
[1.0, 0.0] wtf [1.0, 0.0] 1.0 0.0
0 0 2
input first:  [] []
0 1 2
input first:  [] [[[0.0, 0.0]]]
0 2 2
input first:  [] [[[1.0, 0.0]]]
1 0 2
input first:  [[[0.0, 0.0]]] []
1 1 2
input first:  [[[0.0, 0.0]]] [[[0.0, 0.0]]]
x,y [[0.0, 0.0]] [[0.0, 0.0]]
Traceback (most recent call last):
  File "C:/An/Delta Func/autocomposer.py", line 151, in <module>
    file.write(str([[AutoVision(x,top),AutoVision(y,top)],gcomposition(AutoVision(x,top),AutoVision(y,top))]))
  File "C:/An/Delta Func/autocomposer.py", line 136, in gcomposition
    print(x,"wtf",y,y[0],x[1])
IndexError: list index out of range
>>> ================================ RESTART ================================
>>> 
0 0 0
input first:  [] []
0 0 1
input first:  [[0.0, 0.0]] [[0.0, 0.0]]
x,y [0.0, 0.0] [0.0, 0.0]
[0.0, 0.0] wtf [0.0, 0.0]
0.0
0.0
0 1 1
input first:  [[0.0, 0.0]] [[1.0, 0.0]]
x,y [0.0, 0.0] [1.0, 0.0]
[0.0, 0.0] wtf [1.0, 0.0]
1.0
0.0
1 0 1
input first:  [[1.0, 0.0]] [[0.0, 0.0]]
x,y [1.0, 0.0] [0.0, 0.0]
[1.0, 0.0] wtf [0.0, 0.0]
0.0
0.0
1 1 1
input first:  [[1.0, 0.0]] [[1.0, 0.0]]
x,y [1.0, 0.0] [1.0, 0.0]
[1.0, 0.0] wtf [1.0, 0.0]
1.0
0.0
0 0 2
input first:  [] []
0 1 2
input first:  [] [[[0.0, 0.0]]]
0 2 2
input first:  [] [[[1.0, 0.0]]]
1 0 2
input first:  [[[0.0, 0.0]]] []
1 1 2
input first:  [[[0.0, 0.0]]] [[[0.0, 0.0]]]
x,y [[0.0, 0.0]] [[0.0, 0.0]]
[[0.0, 0.0]] wtf [[0.0, 0.0]]
[0.0, 0.0]
Traceback (most recent call last):
  File "C:/An/Delta Func/autocomposer.py", line 153, in <module>
    file.write(str([[AutoVision(x,top),AutoVision(y,top)],gcomposition(AutoVision(x,top),AutoVision(y,top))]))
  File "C:/An/Delta Func/autocomposer.py", line 138, in gcomposition
    print(x[1])
IndexError: list index out of range
>>> ================================ RESTART ================================
>>> 
0 0 0
input first:  [] []
0 0 1
input first:  [[0.0, 0.0]] [[0.0, 0.0]]
x,y [0.0, 0.0] [0.0, 0.0]
[0.0, 0.0] wtf [0.0, 0.0]
0 1 1
input first:  [[0.0, 0.0]] [[1.0, 0.0]]
x,y [0.0, 0.0] [1.0, 0.0]
[0.0, 0.0] wtf [1.0, 0.0]
1 0 1
input first:  [[1.0, 0.0]] [[0.0, 0.0]]
x,y [1.0, 0.0] [0.0, 0.0]
[1.0, 0.0] wtf [0.0, 0.0]
1 1 1
input first:  [[1.0, 0.0]] [[1.0, 0.0]]
x,y [1.0, 0.0] [1.0, 0.0]
[1.0, 0.0] wtf [1.0, 0.0]
0 0 2
input first:  [] []
0 1 2
input first:  [] [[[0.0, 0.0]]]
0 2 2
input first:  [] [[[1.0, 0.0]]]
1 0 2
input first:  [[[0.0, 0.0]]] []
1 1 2
input first:  [[[0.0, 0.0]]] [[[0.0, 0.0]]]
x,y [[0.0, 0.0]] [[0.0, 0.0]]
[[0.0, 0.0]] wtf [[0.0, 0.0]]
x failed
1 2 2
input first:  [[[0.0, 0.0]]] [[[1.0, 0.0]]]
x,y [[0.0, 0.0]] [[1.0, 0.0]]
[[0.0, 0.0]] wtf [[1.0, 0.0]]
x failed
2 0 2
input first:  [[[1.0, 0.0]]] []
2 1 2
input first:  [[[1.0, 0.0]]] [[[0.0, 0.0]]]
x,y [[1.0, 0.0]] [[0.0, 0.0]]
[[1.0, 0.0]] wtf [[0.0, 0.0]]
x failed
2 2 2
input first:  [[[1.0, 0.0]]] [[[1.0, 0.0]]]
x,y [[1.0, 0.0]] [[1.0, 0.0]]
[[1.0, 0.0]] wtf [[1.0, 0.0]]
x failed
0 0 3
input first:  [] []
0 1 3
input first:  [] [[]]
0 2 3
input first:  [] [[[[0.0, 0.0]]]]
0 3 3
input first:  [] [[], [[[0.0, 0.0]]]]
1 0 3
input first:  [[]] []
1 1 3
input first:  [[]] [[]]
x,y [] []
[] wtf []
y failed
x failed
1 2 3
input first:  [[]] [[[[0.0, 0.0]]]]
x,y [] [[[0.0, 0.0]]]
[] wtf [[[0.0, 0.0]]]
x failed
1 3 3
input first:  [[]] [[], [[[0.0, 0.0]]]]
x,y [] []
[] wtf []
y failed
x failed
x,y [] [[[0.0, 0.0]]]
[] wtf [[[0.0, 0.0]]]
x failed
2 0 3
input first:  [[[[0.0, 0.0]]]] []
2 1 3
input first:  [[[[0.0, 0.0]]]] [[]]
x,y [[[0.0, 0.0]]] []
[[[0.0, 0.0]]] wtf []
y failed
x failed
2 2 3
input first:  [[[[0.0, 0.0]]]] [[[[0.0, 0.0]]]]
x,y [[[0.0, 0.0]]] [[[0.0, 0.0]]]
[[[0.0, 0.0]]] wtf [[[0.0, 0.0]]]
x failed
2 3 3
input first:  [[[[0.0, 0.0]]]] [[], [[[0.0, 0.0]]]]
x,y [[[0.0, 0.0]]] []
[[[0.0, 0.0]]] wtf []
y failed
x failed
x,y [[[0.0, 0.0]]] [[[0.0, 0.0]]]
[[[0.0, 0.0]]] wtf [[[0.0, 0.0]]]
x failed
3 0 3
input first:  [[], [[[0.0, 0.0]]]] []
3 1 3
input first:  [[], [[[0.0, 0.0]]]] [[]]
x,y [] []
[] wtf []
y failed
x failed
x,y [[[0.0, 0.0]]] []
[[[0.0, 0.0]]] wtf []
y failed
x failed
3 2 3
input first:  [[], [[[0.0, 0.0]]]] [[[[0.0, 0.0]]]]
x,y [] [[[0.0, 0.0]]]
[] wtf [[[0.0, 0.0]]]
x failed
x,y [[[0.0, 0.0]]] [[[0.0, 0.0]]]
[[[0.0, 0.0]]] wtf [[[0.0, 0.0]]]
x failed
3 3 3
input first:  [[], [[[0.0, 0.0]]]] [[], [[[0.0, 0.0]]]]
x,y [] []
[] wtf []
y failed
x failed
x,y [] [[[0.0, 0.0]]]
[] wtf [[[0.0, 0.0]]]
x failed
x,y [[[0.0, 0.0]]] []
[[[0.0, 0.0]]] wtf []
y failed
x failed
x,y [[[0.0, 0.0]]] [[[0.0, 0.0]]]
[[[0.0, 0.0]]] wtf [[[0.0, 0.0]]]
x failed
0 0 4
input first:  [] []
0 1 4
input first:  [] [[]]
0 2 4
input first:  [] [[[]]]
0 3 4
input first:  [] [[], [[]]]
0 4 4
input first:  [] [[[[[0.0, 0.0]]]]]
1 0 4
input first:  [[]] []
1 1 4
input first:  [[]] [[]]
x,y [] []
[] wtf []
y failed
x failed
1 2 4
input first:  [[]] [[[]]]
x,y [] [[]]
[] wtf [[]]
x failed
1 3 4
input first:  [[]] [[], [[]]]
x,y [] []
[] wtf []
y failed
x failed
x,y [] [[]]
[] wtf [[]]
x failed
1 4 4
input first:  [[]] [[[[[0.0, 0.0]]]]]
x,y [] [[[[0.0, 0.0]]]]
[] wtf [[[[0.0, 0.0]]]]
x failed
2 0 4
input first:  [[[]]] []
2 1 4
input first:  [[[]]] [[]]
x,y [[]] []
[[]] wtf []
y failed
x failed
2 2 4
input first:  [[[]]] [[[]]]
x,y [[]] [[]]
[[]] wtf [[]]
x failed
2 3 4
input first:  [[[]]] [[], [[]]]
x,y [[]] []
[[]] wtf []
y failed
x failed
x,y [[]] [[]]
[[]] wtf [[]]
x failed
2 4 4
input first:  [[[]]] [[[[[0.0, 0.0]]]]]
x,y [[]] [[[[0.0, 0.0]]]]
[[]] wtf [[[[0.0, 0.0]]]]
x failed
3 0 4
input first:  [[], [[]]] []
3 1 4
input first:  [[], [[]]] [[]]
x,y [] []
[] wtf []
y failed
x failed
x,y [[]] []
[[]] wtf []
y failed
x failed
3 2 4
input first:  [[], [[]]] [[[]]]
x,y [] [[]]
[] wtf [[]]
x failed
x,y [[]] [[]]
[[]] wtf [[]]
x failed
3 3 4
input first:  [[], [[]]] [[], [[]]]
x,y [] []
[] wtf []
y failed
x failed
x,y [] [[]]
[] wtf [[]]
x failed
x,y [[]] []
[[]] wtf []
y failed
x failed
x,y [[]] [[]]
[[]] wtf [[]]
x failed
3 4 4
input first:  [[], [[]]] [[[[[0.0, 0.0]]]]]
x,y [] [[[[0.0, 0.0]]]]
[] wtf [[[[0.0, 0.0]]]]
x failed
x,y [[]] [[[[0.0, 0.0]]]]
[[]] wtf [[[[0.0, 0.0]]]]
x failed
4 0 4
input first:  [[[[[0.0, 0.0]]]]] []
4 1 4
input first:  [[[[[0.0, 0.0]]]]] [[]]
x,y [[[[0.0, 0.0]]]] []
[[[[0.0, 0.0]]]] wtf []
y failed
x failed
4 2 4
input first:  [[[[[0.0, 0.0]]]]] [[[]]]
x,y [[[[0.0, 0.0]]]] [[]]
[[[[0.0, 0.0]]]] wtf [[]]
x failed
4 3 4
input first:  [[[[[0.0, 0.0]]]]] [[], [[]]]
x,y [[[[0.0, 0.0]]]] []
[[[[0.0, 0.0]]]] wtf []
y failed
x failed
x,y [[[[0.0, 0.0]]]] [[]]
[[[[0.0, 0.0]]]] wtf [[]]
x failed
4 4 4
input first:  [[[[[0.0, 0.0]]]]] [[[[[0.0, 0.0]]]]]
x,y [[[[0.0, 0.0]]]] [[[[0.0, 0.0]]]]
[[[[0.0, 0.0]]]] wtf [[[[0.0, 0.0]]]]
x failed
>>> ================================ RESTART ================================
>>> 
0 0 0
input first:  [] []
0 0 1
input first:  [[0.0, 0.0]] [[0.0, 0.0]]
x,y [0.0, 0.0] [0.0, 0.0]
[0.0, 0.0] wtf [0.0, 0.0]
0 1 1
input first:  [[0.0, 0.0]] [[1.0, 0.0]]
x,y [0.0, 0.0] [1.0, 0.0]
[0.0, 0.0] wtf [1.0, 0.0]
1 0 1
input first:  [[1.0, 0.0]] [[0.0, 0.0]]
x,y [1.0, 0.0] [0.0, 0.0]
[1.0, 0.0] wtf [0.0, 0.0]
1 1 1
input first:  [[1.0, 0.0]] [[1.0, 0.0]]
x,y [1.0, 0.0] [1.0, 0.0]
[1.0, 0.0] wtf [1.0, 0.0]
0 0 2
input first:  [] []
0 1 2
input first:  [] [[[0.0, 0.0]]]
0 2 2
input first:  [] [[[1.0, 0.0]]]
1 0 2
input first:  [[[0.0, 0.0]]] []
1 1 2
input first:  [[[0.0, 0.0]]] [[[0.0, 0.0]]]
x,y [[0.0, 0.0]] [[0.0, 0.0]]
[[0.0, 0.0]] wtf [[0.0, 0.0]]
x failed
Traceback (most recent call last):
  File "C:/An/Delta Func/autocomposer.py", line 166, in <module>
    file.write(str([[AutoVision(x,top),AutoVision(y,top)],gcomposition(AutoVision(x,top),AutoVision(y,top))]))
  File "C:/An/Delta Func/autocomposer.py", line 152, in gcomposition
    if y[0] == x[1]:
IndexError: list index out of range
>>> ================================ RESTART ================================
>>> 
0 0 0
input first:  [] []
0 0 1
input first:  [[0.0, 0.0]] [[0.0, 0.0]]
x,y [0.0, 0.0] [0.0, 0.0]
[0.0, 0.0] wtf [0.0, 0.0]
0 1 1
input first:  [[0.0, 0.0]] [[1.0, 0.0]]
x,y [0.0, 0.0] [1.0, 0.0]
[0.0, 0.0] wtf [1.0, 0.0]
1 0 1
input first:  [[1.0, 0.0]] [[0.0, 0.0]]
x,y [1.0, 0.0] [0.0, 0.0]
[1.0, 0.0] wtf [0.0, 0.0]
1 1 1
input first:  [[1.0, 0.0]] [[1.0, 0.0]]
x,y [1.0, 0.0] [1.0, 0.0]
[1.0, 0.0] wtf [1.0, 0.0]
0 0 2
input first:  [] []
0 1 2
input first:  [] [[[0.0, 0.0]]]
0 2 2
input first:  [] [[[1.0, 0.0]]]
1 0 2
input first:  [[[0.0, 0.0]]] []
1 1 2
input first:  [[[0.0, 0.0]]] [[[0.0, 0.0]]]
x,y [[0.0, 0.0]] [[0.0, 0.0]]
[[0.0, 0.0]] wtf [[0.0, 0.0]]
x failed
1 2 2
input first:  [[[0.0, 0.0]]] [[[1.0, 0.0]]]
x,y [[0.0, 0.0]] [[1.0, 0.0]]
[[0.0, 0.0]] wtf [[1.0, 0.0]]
x failed
2 0 2
input first:  [[[1.0, 0.0]]] []
2 1 2
input first:  [[[1.0, 0.0]]] [[[0.0, 0.0]]]
x,y [[1.0, 0.0]] [[0.0, 0.0]]
[[1.0, 0.0]] wtf [[0.0, 0.0]]
x failed
2 2 2
input first:  [[[1.0, 0.0]]] [[[1.0, 0.0]]]
x,y [[1.0, 0.0]] [[1.0, 0.0]]
[[1.0, 0.0]] wtf [[1.0, 0.0]]
x failed
0 0 3
input first:  [] []
0 1 3
input first:  [] [[]]
0 2 3
input first:  [] [[[[0.0, 0.0]]]]
0 3 3
input first:  [] [[], [[[0.0, 0.0]]]]
1 0 3
input first:  [[]] []
1 1 3
input first:  [[]] [[]]
x,y [] []
[] wtf []
y failed
x failed
1 2 3
input first:  [[]] [[[[0.0, 0.0]]]]
x,y [] [[[0.0, 0.0]]]
[] wtf [[[0.0, 0.0]]]
x failed
1 3 3
input first:  [[]] [[], [[[0.0, 0.0]]]]
x,y [] []
[] wtf []
y failed
x failed
x,y [] [[[0.0, 0.0]]]
[] wtf [[[0.0, 0.0]]]
x failed
2 0 3
input first:  [[[[0.0, 0.0]]]] []
2 1 3
input first:  [[[[0.0, 0.0]]]] [[]]
x,y [[[0.0, 0.0]]] []
[[[0.0, 0.0]]] wtf []
y failed
x failed
2 2 3
input first:  [[[[0.0, 0.0]]]] [[[[0.0, 0.0]]]]
x,y [[[0.0, 0.0]]] [[[0.0, 0.0]]]
[[[0.0, 0.0]]] wtf [[[0.0, 0.0]]]
x failed
2 3 3
input first:  [[[[0.0, 0.0]]]] [[], [[[0.0, 0.0]]]]
x,y [[[0.0, 0.0]]] []
[[[0.0, 0.0]]] wtf []
y failed
x failed
x,y [[[0.0, 0.0]]] [[[0.0, 0.0]]]
[[[0.0, 0.0]]] wtf [[[0.0, 0.0]]]
x failed
3 0 3
input first:  [[], [[[0.0, 0.0]]]] []
3 1 3
input first:  [[], [[[0.0, 0.0]]]] [[]]
x,y [] []
[] wtf []
y failed
x failed
x,y [[[0.0, 0.0]]] []
[[[0.0, 0.0]]] wtf []
y failed
x failed
3 2 3
input first:  [[], [[[0.0, 0.0]]]] [[[[0.0, 0.0]]]]
x,y [] [[[0.0, 0.0]]]
[] wtf [[[0.0, 0.0]]]
x failed
x,y [[[0.0, 0.0]]] [[[0.0, 0.0]]]
[[[0.0, 0.0]]] wtf [[[0.0, 0.0]]]
x failed
3 3 3
input first:  [[], [[[0.0, 0.0]]]] [[], [[[0.0, 0.0]]]]
x,y [] []
[] wtf []
y failed
x failed
x,y [] [[[0.0, 0.0]]]
[] wtf [[[0.0, 0.0]]]
x failed
x,y [[[0.0, 0.0]]] []
[[[0.0, 0.0]]] wtf []
y failed
x failed
x,y [[[0.0, 0.0]]] [[[0.0, 0.0]]]
[[[0.0, 0.0]]] wtf [[[0.0, 0.0]]]
x failed
0 0 4
input first:  [] []
0 1 4
input first:  [] [[]]
0 2 4
input first:  [] [[[]]]
0 3 4
input first:  [] [[], [[]]]
0 4 4
input first:  [] [[[[[0.0, 0.0]]]]]
1 0 4
input first:  [[]] []
1 1 4
input first:  [[]] [[]]
x,y [] []
[] wtf []
y failed
x failed
1 2 4
input first:  [[]] [[[]]]
x,y [] [[]]
[] wtf [[]]
x failed
1 3 4
input first:  [[]] [[], [[]]]
x,y [] []
[] wtf []
y failed
x failed
x,y [] [[]]
[] wtf [[]]
x failed
1 4 4
input first:  [[]] [[[[[0.0, 0.0]]]]]
x,y [] [[[[0.0, 0.0]]]]
[] wtf [[[[0.0, 0.0]]]]
x failed
2 0 4
input first:  [[[]]] []
2 1 4
input first:  [[[]]] [[]]
x,y [[]] []
[[]] wtf []
y failed
x failed
2 2 4
input first:  [[[]]] [[[]]]
x,y [[]] [[]]
[[]] wtf [[]]
x failed
2 3 4
input first:  [[[]]] [[], [[]]]
x,y [[]] []
[[]] wtf []
y failed
x failed
x,y [[]] [[]]
[[]] wtf [[]]
x failed
2 4 4
input first:  [[[]]] [[[[[0.0, 0.0]]]]]
x,y [[]] [[[[0.0, 0.0]]]]
[[]] wtf [[[[0.0, 0.0]]]]
x failed
3 0 4
input first:  [[], [[]]] []
3 1 4
input first:  [[], [[]]] [[]]
x,y [] []
[] wtf []
y failed
x failed
x,y [[]] []
[[]] wtf []
y failed
x failed
3 2 4
input first:  [[], [[]]] [[[]]]
x,y [] [[]]
[] wtf [[]]
x failed
x,y [[]] [[]]
[[]] wtf [[]]
x failed
3 3 4
input first:  [[], [[]]] [[], [[]]]
x,y [] []
[] wtf []
y failed
x failed
x,y [] [[]]
[] wtf [[]]
x failed
x,y [[]] []
[[]] wtf []
y failed
x failed
x,y [[]] [[]]
[[]] wtf [[]]
x failed
3 4 4
input first:  [[], [[]]] [[[[[0.0, 0.0]]]]]
x,y [] [[[[0.0, 0.0]]]]
[] wtf [[[[0.0, 0.0]]]]
x failed
x,y [[]] [[[[0.0, 0.0]]]]
[[]] wtf [[[[0.0, 0.0]]]]
x failed
4 0 4
input first:  [[[[[0.0, 0.0]]]]] []
4 1 4
input first:  [[[[[0.0, 0.0]]]]] [[]]
x,y [[[[0.0, 0.0]]]] []
[[[[0.0, 0.0]]]] wtf []
y failed
x failed
4 2 4
input first:  [[[[[0.0, 0.0]]]]] [[[]]]
x,y [[[[0.0, 0.0]]]] [[]]
[[[[0.0, 0.0]]]] wtf [[]]
x failed
4 3 4
input first:  [[[[[0.0, 0.0]]]]] [[], [[]]]
x,y [[[[0.0, 0.0]]]] []
[[[[0.0, 0.0]]]] wtf []
y failed
x failed
x,y [[[[0.0, 0.0]]]] [[]]
[[[[0.0, 0.0]]]] wtf [[]]
x failed
4 4 4
input first:  [[[[[0.0, 0.0]]]]] [[[[[0.0, 0.0]]]]]
x,y [[[[0.0, 0.0]]]] [[[[0.0, 0.0]]]]
[[[[0.0, 0.0]]]] wtf [[[[0.0, 0.0]]]]
x failed
>>> ================================ RESTART ================================
>>> 
0 0 0
input first: [] []
0 0 1
input first: [[0.0, 0.0]] [[0.0, 0.0]]
x,y [0.0, 0.0] [0.0, 0.0]
[0.0, 0.0] wtf [0.0, 0.0]
0 1 1
input first: [[0.0, 0.0]] [[1.0, 0.0]]
x,y [0.0, 0.0] [1.0, 0.0]
[0.0, 0.0] wtf [1.0, 0.0]
1 0 1
input first: [[1.0, 0.0]] [[0.0, 0.0]]
x,y [1.0, 0.0] [0.0, 0.0]
[1.0, 0.0] wtf [0.0, 0.0]
1 1 1
input first: [[1.0, 0.0]] [[1.0, 0.0]]
x,y [1.0, 0.0] [1.0, 0.0]
[1.0, 0.0] wtf [1.0, 0.0]
0 0 2
input first: [] []
0 1 2
input first: [] [[[0.0, 0.0]]]
0 2 2
input first: [] [[[1.0, 0.0]]]
1 0 2
input first: [[[0.0, 0.0]]] []
1 1 2
input first: [[[0.0, 0.0]]] [[[0.0, 0.0]]]
x,y [[0.0, 0.0]] [[0.0, 0.0]]
[[0.0, 0.0]] wtf [[0.0, 0.0]]
1 2 2
input first: [[[0.0, 0.0]]] [[[1.0, 0.0]]]
x,y [[0.0, 0.0]] [[1.0, 0.0]]
[[0.0, 0.0]] wtf [[1.0, 0.0]]
2 0 2
input first: [[[1.0, 0.0]]] []
2 1 2
input first: [[[1.0, 0.0]]] [[[0.0, 0.0]]]
x,y [[1.0, 0.0]] [[0.0, 0.0]]
[[1.0, 0.0]] wtf [[0.0, 0.0]]
2 2 2
input first: [[[1.0, 0.0]]] [[[1.0, 0.0]]]
x,y [[1.0, 0.0]] [[1.0, 0.0]]
[[1.0, 0.0]] wtf [[1.0, 0.0]]
0 0 3
input first: [] []
0 1 3
input first: [] [[]]
0 2 3
input first: [] [[[[0.0, 0.0]]]]
0 3 3
input first: [] [[], [[[0.0, 0.0]]]]
1 0 3
input first: [[]] []
1 1 3
input first: [[]] [[]]
x,y [] []
[] wtf []
1 2 3
input first: [[]] [[[[0.0, 0.0]]]]
x,y [] [[[0.0, 0.0]]]
[] wtf [[[0.0, 0.0]]]
1 3 3
input first: [[]] [[], [[[0.0, 0.0]]]]
x,y [] []
[] wtf []
x,y [] [[[0.0, 0.0]]]
[] wtf [[[0.0, 0.0]]]
2 0 3
input first: [[[[0.0, 0.0]]]] []
2 1 3
input first: [[[[0.0, 0.0]]]] [[]]
x,y [[[0.0, 0.0]]] []
[[[0.0, 0.0]]] wtf []
2 2 3
input first: [[[[0.0, 0.0]]]] [[[[0.0, 0.0]]]]
x,y [[[0.0, 0.0]]] [[[0.0, 0.0]]]
[[[0.0, 0.0]]] wtf [[[0.0, 0.0]]]
2 3 3
input first: [[[[0.0, 0.0]]]] [[], [[[0.0, 0.0]]]]
x,y [[[0.0, 0.0]]] []
[[[0.0, 0.0]]] wtf []
x,y [[[0.0, 0.0]]] [[[0.0, 0.0]]]
[[[0.0, 0.0]]] wtf [[[0.0, 0.0]]]
3 0 3
input first: [[], [[[0.0, 0.0]]]] []
3 1 3
input first: [[], [[[0.0, 0.0]]]] [[]]
x,y [] []
[] wtf []
x,y [[[0.0, 0.0]]] []
[[[0.0, 0.0]]] wtf []
3 2 3
input first: [[], [[[0.0, 0.0]]]] [[[[0.0, 0.0]]]]
x,y [] [[[0.0, 0.0]]]
[] wtf [[[0.0, 0.0]]]
x,y [[[0.0, 0.0]]] [[[0.0, 0.0]]]
[[[0.0, 0.0]]] wtf [[[0.0, 0.0]]]
3 3 3
input first: [[], [[[0.0, 0.0]]]] [[], [[[0.0, 0.0]]]]
x,y [] []
[] wtf []
x,y [] [[[0.0, 0.0]]]
[] wtf [[[0.0, 0.0]]]
x,y [[[0.0, 0.0]]] []
[[[0.0, 0.0]]] wtf []
x,y [[[0.0, 0.0]]] [[[0.0, 0.0]]]
[[[0.0, 0.0]]] wtf [[[0.0, 0.0]]]
0 0 4
input first: [] []
0 1 4
input first: [] [[]]
0 2 4
input first: [] [[[]]]
0 3 4
input first: [] [[], [[]]]
0 4 4
input first: [] [[[[[0.0, 0.0]]]]]
1 0 4
input first: [[]] []
1 1 4
input first: [[]] [[]]
x,y [] []
[] wtf []
1 2 4
input first: [[]] [[[]]]
x,y [] [[]]
[] wtf [[]]
1 3 4
input first: [[]] [[], [[]]]
x,y [] []
[] wtf []
x,y [] [[]]
[] wtf [[]]
1 4 4
input first: [[]] [[[[[0.0, 0.0]]]]]
x,y [] [[[[0.0, 0.0]]]]
[] wtf [[[[0.0, 0.0]]]]
2 0 4
input first: [[[]]] []
2 1 4
input first: [[[]]] [[]]
x,y [[]] []
[[]] wtf []
2 2 4
input first: [[[]]] [[[]]]
x,y [[]] [[]]
[[]] wtf [[]]
2 3 4
input first: [[[]]] [[], [[]]]
x,y [[]] []
[[]] wtf []
x,y [[]] [[]]
[[]] wtf [[]]
2 4 4
input first: [[[]]] [[[[[0.0, 0.0]]]]]
x,y [[]] [[[[0.0, 0.0]]]]
[[]] wtf [[[[0.0, 0.0]]]]
3 0 4
input first: [[], [[]]] []
3 1 4
input first: [[], [[]]] [[]]
x,y [] []
[] wtf []
x,y [[]] []
[[]] wtf []
3 2 4
input first: [[], [[]]] [[[]]]
x,y [] [[]]
[] wtf [[]]
x,y [[]] [[]]
[[]] wtf [[]]
3 3 4
input first: [[], [[]]] [[], [[]]]
x,y [] []
[] wtf []
x,y [] [[]]
[] wtf [[]]
x,y [[]] []
[[]] wtf []
x,y [[]] [[]]
[[]] wtf [[]]
3 4 4
input first: [[], [[]]] [[[[[0.0, 0.0]]]]]
x,y [] [[[[0.0, 0.0]]]]
[] wtf [[[[0.0, 0.0]]]]
x,y [[]] [[[[0.0, 0.0]]]]
[[]] wtf [[[[0.0, 0.0]]]]
4 0 4
input first: [[[[[0.0, 0.0]]]]] []
4 1 4
input first: [[[[[0.0, 0.0]]]]] [[]]
x,y [[[[0.0, 0.0]]]] []
[[[[0.0, 0.0]]]] wtf []
4 2 4
input first: [[[[[0.0, 0.0]]]]] [[[]]]
x,y [[[[0.0, 0.0]]]] [[]]
[[[[0.0, 0.0]]]] wtf [[]]
4 3 4
input first: [[[[[0.0, 0.0]]]]] [[], [[]]]
x,y [[[[0.0, 0.0]]]] []
[[[[0.0, 0.0]]]] wtf []
x,y [[[[0.0, 0.0]]]] [[]]
[[[[0.0, 0.0]]]] wtf [[]]
4 4 4
input first: [[[[[0.0, 0.0]]]]] [[[[[0.0, 0.0]]]]]
x,y [[[[0.0, 0.0]]]] [[[[0.0, 0.0]]]]
[[[[0.0, 0.0]]]] wtf [[[[0.0, 0.0]]]]
>>> ================================ RESTART ================================
>>> 
>>> ================================ RESTART ================================
>>> 
4
>>> ================================ RESTART ================================
>>> 
0
>>> ================================ RESTART ================================
>>> 
0 0 0
input first: [] []
0 0 1
input first: [[0.0, 0.0]] [[0.0, 0.0]]
x,y [0.0, 0.0] [0.0, 0.0]
[0.0, 0.0] wtf [0.0, 0.0]
0 1 1
input first: [[0.0, 0.0]] [[1.0, 0.0]]
x,y [0.0, 0.0] [1.0, 0.0]
[0.0, 0.0] wtf [1.0, 0.0]
1 0 1
input first: [[1.0, 0.0]] [[0.0, 0.0]]
x,y [1.0, 0.0] [0.0, 0.0]
[1.0, 0.0] wtf [0.0, 0.0]
1 1 1
input first: [[1.0, 0.0]] [[1.0, 0.0]]
x,y [1.0, 0.0] [1.0, 0.0]
[1.0, 0.0] wtf [1.0, 0.0]
0 0 2
input first: [] []
0 1 2
input first: [] [[[0.0, 0.0]]]
0 2 2
input first: [] [[[1.0, 0.0]]]
1 0 2
input first: [[[0.0, 0.0]]] []
1 1 2
input first: [[[0.0, 0.0]]] [[[0.0, 0.0]]]
x,y [[0.0, 0.0]] [[0.0, 0.0]]
[[0.0, 0.0]] wtf [[0.0, 0.0]]
1 2 2
input first: [[[0.0, 0.0]]] [[[1.0, 0.0]]]
x,y [[0.0, 0.0]] [[1.0, 0.0]]
[[0.0, 0.0]] wtf [[1.0, 0.0]]
2 0 2
input first: [[[1.0, 0.0]]] []
2 1 2
input first: [[[1.0, 0.0]]] [[[0.0, 0.0]]]
x,y [[1.0, 0.0]] [[0.0, 0.0]]
[[1.0, 0.0]] wtf [[0.0, 0.0]]
2 2 2
input first: [[[1.0, 0.0]]] [[[1.0, 0.0]]]
x,y [[1.0, 0.0]] [[1.0, 0.0]]
[[1.0, 0.0]] wtf [[1.0, 0.0]]
0 0 3
input first: [] []
0 1 3
input first: [] [[]]
0 2 3
input first: [] [[[[0.0, 0.0]]]]
0 3 3
input first: [] [[], [[[0.0, 0.0]]]]
1 0 3
input first: [[]] []
1 1 3
input first: [[]] [[]]
x,y [] []
[] wtf []
1 2 3
input first: [[]] [[[[0.0, 0.0]]]]
x,y [] [[[0.0, 0.0]]]
[] wtf [[[0.0, 0.0]]]
1 3 3
input first: [[]] [[], [[[0.0, 0.0]]]]
x,y [] []
[] wtf []
x,y [] [[[0.0, 0.0]]]
[] wtf [[[0.0, 0.0]]]
2 0 3
input first: [[[[0.0, 0.0]]]] []
2 1 3
input first: [[[[0.0, 0.0]]]] [[]]
x,y [[[0.0, 0.0]]] []
[[[0.0, 0.0]]] wtf []
2 2 3
input first: [[[[0.0, 0.0]]]] [[[[0.0, 0.0]]]]
x,y [[[0.0, 0.0]]] [[[0.0, 0.0]]]
[[[0.0, 0.0]]] wtf [[[0.0, 0.0]]]
2 3 3
input first: [[[[0.0, 0.0]]]] [[], [[[0.0, 0.0]]]]
x,y [[[0.0, 0.0]]] []
[[[0.0, 0.0]]] wtf []
x,y [[[0.0, 0.0]]] [[[0.0, 0.0]]]
[[[0.0, 0.0]]] wtf [[[0.0, 0.0]]]
3 0 3
input first: [[], [[[0.0, 0.0]]]] []
3 1 3
input first: [[], [[[0.0, 0.0]]]] [[]]
x,y [] []
[] wtf []
x,y [[[0.0, 0.0]]] []
[[[0.0, 0.0]]] wtf []
3 2 3
input first: [[], [[[0.0, 0.0]]]] [[[[0.0, 0.0]]]]
x,y [] [[[0.0, 0.0]]]
[] wtf [[[0.0, 0.0]]]
x,y [[[0.0, 0.0]]] [[[0.0, 0.0]]]
[[[0.0, 0.0]]] wtf [[[0.0, 0.0]]]
3 3 3
input first: [[], [[[0.0, 0.0]]]] [[], [[[0.0, 0.0]]]]
x,y [] []
[] wtf []
x,y [] [[[0.0, 0.0]]]
[] wtf [[[0.0, 0.0]]]
x,y [[[0.0, 0.0]]] []
[[[0.0, 0.0]]] wtf []
x,y [[[0.0, 0.0]]] [[[0.0, 0.0]]]
[[[0.0, 0.0]]] wtf [[[0.0, 0.0]]]
0 0 4
input first: [] []
0 1 4
input first: [] [[]]
0 2 4
input first: [] [[[]]]
0 3 4
input first: [] [[], [[]]]
0 4 4
input first: [] [[[[[0.0, 0.0]]]]]
1 0 4
input first: [[]] []
1 1 4
input first: [[]] [[]]
x,y [] []
[] wtf []
1 2 4
input first: [[]] [[[]]]
x,y [] [[]]
[] wtf [[]]
1 3 4
input first: [[]] [[], [[]]]
x,y [] []
[] wtf []
x,y [] [[]]
[] wtf [[]]
1 4 4
input first: [[]] [[[[[0.0, 0.0]]]]]
x,y [] [[[[0.0, 0.0]]]]
[] wtf [[[[0.0, 0.0]]]]
2 0 4
input first: [[[]]] []
2 1 4
input first: [[[]]] [[]]
x,y [[]] []
[[]] wtf []
2 2 4
input first: [[[]]] [[[]]]
x,y [[]] [[]]
[[]] wtf [[]]
2 3 4
input first: [[[]]] [[], [[]]]
x,y [[]] []
[[]] wtf []
x,y [[]] [[]]
[[]] wtf [[]]
2 4 4
input first: [[[]]] [[[[[0.0, 0.0]]]]]
x,y [[]] [[[[0.0, 0.0]]]]
[[]] wtf [[[[0.0, 0.0]]]]
3 0 4
input first: [[], [[]]] []
3 1 4
input first: [[], [[]]] [[]]
x,y [] []
[] wtf []
x,y [[]] []
[[]] wtf []
3 2 4
input first: [[], [[]]] [[[]]]
x,y [] [[]]
[] wtf [[]]
x,y [[]] [[]]
[[]] wtf [[]]
3 3 4
input first: [[], [[]]] [[], [[]]]
x,y [] []
[] wtf []
x,y [] [[]]
[] wtf [[]]
x,y [[]] []
[[]] wtf []
x,y [[]] [[]]
[[]] wtf [[]]
3 4 4
input first: [[], [[]]] [[[[[0.0, 0.0]]]]]
x,y [] [[[[0.0, 0.0]]]]
[] wtf [[[[0.0, 0.0]]]]
x,y [[]] [[[[0.0, 0.0]]]]
[[]] wtf [[[[0.0, 0.0]]]]
4 0 4
input first: [[[[[0.0, 0.0]]]]] []
4 1 4
input first: [[[[[0.0, 0.0]]]]] [[]]
x,y [[[[0.0, 0.0]]]] []
[[[[0.0, 0.0]]]] wtf []
4 2 4
input first: [[[[[0.0, 0.0]]]]] [[[]]]
x,y [[[[0.0, 0.0]]]] [[]]
[[[[0.0, 0.0]]]] wtf [[]]
4 3 4
input first: [[[[[0.0, 0.0]]]]] [[], [[]]]
x,y [[[[0.0, 0.0]]]] []
[[[[0.0, 0.0]]]] wtf []
x,y [[[[0.0, 0.0]]]] [[]]
[[[[0.0, 0.0]]]] wtf [[]]
4 4 4
input first: [[[[[0.0, 0.0]]]]] [[[[[0.0, 0.0]]]]]
x,y [[[[0.0, 0.0]]]] [[[[0.0, 0.0]]]]
[[[[0.0, 0.0]]]] wtf [[[[0.0, 0.0]]]]
>>> ================================ RESTART ================================
>>> 
x,y [0.0, 0.0] [0.0, 0.0]
[0.0, 0.0] wtf [0.0, 0.0]
x,y [0.0, 0.0] [1.0, 0.0]
[0.0, 0.0] wtf [1.0, 0.0]
x,y [1.0, 0.0] [0.0, 0.0]
[1.0, 0.0] wtf [0.0, 0.0]
x,y [1.0, 0.0] [1.0, 0.0]
[1.0, 0.0] wtf [1.0, 0.0]
x,y [[0.0, 0.0]] [[0.0, 0.0]]
[[0.0, 0.0]] wtf [[0.0, 0.0]]
x,y [[0.0, 0.0]] [[1.0, 0.0]]
[[0.0, 0.0]] wtf [[1.0, 0.0]]
x,y [[1.0, 0.0]] [[0.0, 0.0]]
[[1.0, 0.0]] wtf [[0.0, 0.0]]
x,y [[1.0, 0.0]] [[1.0, 0.0]]
[[1.0, 0.0]] wtf [[1.0, 0.0]]
x,y [] []
[] wtf []
x,y [] [[[0.0, 0.0]]]
[] wtf [[[0.0, 0.0]]]
x,y [] []
[] wtf []
x,y [] [[[0.0, 0.0]]]
[] wtf [[[0.0, 0.0]]]
x,y [[[0.0, 0.0]]] []
[[[0.0, 0.0]]] wtf []
x,y [[[0.0, 0.0]]] [[[0.0, 0.0]]]
[[[0.0, 0.0]]] wtf [[[0.0, 0.0]]]
x,y [[[0.0, 0.0]]] []
[[[0.0, 0.0]]] wtf []
x,y [[[0.0, 0.0]]] [[[0.0, 0.0]]]
[[[0.0, 0.0]]] wtf [[[0.0, 0.0]]]
x,y [] []
[] wtf []
x,y [[[0.0, 0.0]]] []
[[[0.0, 0.0]]] wtf []
x,y [] [[[0.0, 0.0]]]
[] wtf [[[0.0, 0.0]]]
x,y [[[0.0, 0.0]]] [[[0.0, 0.0]]]
[[[0.0, 0.0]]] wtf [[[0.0, 0.0]]]
x,y [] []
[] wtf []
x,y [] [[[0.0, 0.0]]]
[] wtf [[[0.0, 0.0]]]
x,y [[[0.0, 0.0]]] []
[[[0.0, 0.0]]] wtf []
x,y [[[0.0, 0.0]]] [[[0.0, 0.0]]]
[[[0.0, 0.0]]] wtf [[[0.0, 0.0]]]
x,y [] []
[] wtf []
x,y [] [[]]
[] wtf [[]]
x,y [] []
[] wtf []
x,y [] [[]]
[] wtf [[]]
x,y [] [[[[0.0, 0.0]]]]
[] wtf [[[[0.0, 0.0]]]]
x,y [[]] []
[[]] wtf []
x,y [[]] [[]]
[[]] wtf [[]]
x,y [[]] []
[[]] wtf []
x,y [[]] [[]]
[[]] wtf [[]]
x,y [[]] [[[[0.0, 0.0]]]]
[[]] wtf [[[[0.0, 0.0]]]]
x,y [] []
[] wtf []
x,y [[]] []
[[]] wtf []
x,y [] [[]]
[] wtf [[]]
x,y [[]] [[]]
[[]] wtf [[]]
x,y [] []
[] wtf []
x,y [] [[]]
[] wtf [[]]
x,y [[]] []
[[]] wtf []
x,y [[]] [[]]
[[]] wtf [[]]
x,y [] [[[[0.0, 0.0]]]]
[] wtf [[[[0.0, 0.0]]]]
x,y [[]] [[[[0.0, 0.0]]]]
[[]] wtf [[[[0.0, 0.0]]]]
x,y [[[[0.0, 0.0]]]] []
[[[[0.0, 0.0]]]] wtf []
x,y [[[[0.0, 0.0]]]] [[]]
[[[[0.0, 0.0]]]] wtf [[]]
x,y [[[[0.0, 0.0]]]] []
[[[[0.0, 0.0]]]] wtf []
x,y [[[[0.0, 0.0]]]] [[]]
[[[[0.0, 0.0]]]] wtf [[]]
x,y [[[[0.0, 0.0]]]] [[[[0.0, 0.0]]]]
[[[[0.0, 0.0]]]] wtf [[[[0.0, 0.0]]]]
>>> ================================ RESTART ================================
>>> 
>>> ================================ RESTART ================================
>>> 
checking addresspls
Traceback (most recent call last):
  File "C:/An/Delta Func/autocomposer.py", line 313, in <module>
    print(Addresspls(["cat",["c","a","t"],[],pairfinder("cat",[])]))
NameError: name 'pairfinder' is not defined
>>> ================================ RESTART ================================
>>> 
checking addresspls
Traceback (most recent call last):
  File "C:/An/Delta Func/autocomposer.py", line 332, in <module>
    print(Addresspls(["cat",["c","a","t"],[],pairfinder("cat",[])]))
  File "C:/An/Delta Func/autocomposer.py", line 280, in pairfinder
    if x == charpair[0]:
IndexError: list index out of range
>>> ================================ RESTART ================================
>>> 
checking addresspls
Traceback (most recent call last):
  File "C:/An/Delta Func/autocomposer.py", line 332, in <module>
    print(Addresspls(["cat",["c","a","t"],[],pairfinder("cat",["[","]"])]))
  File "C:/An/Delta Func/autocomposer.py", line 321, in Addresspls
    for x in interim:
NameError: name 'interim' is not defined
>>> ================================ RESTART ================================
>>> 
checking addresspls
Traceback (most recent call last):
  File "C:/An/Delta Func/autocomposer.py", line 332, in <module>
    print(Addresspls(["cat",["c","a","t"],[],pairfinder("cat",["[","]"])]))
  File "C:/An/Delta Func/autocomposer.py", line 327, in Addresspls
    Interim = str(InsertAt(list(Interim),1,x))
  File "C:/An/Delta Func/autocomposer.py", line 266, in InsertAt
    VALUE = List[:Index]
TypeError: slice indices must be integers or None or have an __index__ method
>>> ================================ RESTART ================================
>>> 
checking addresspls
wtf is interim 1
Traceback (most recent call last):
  File "C:/An/Delta Func/autocomposer.py", line 333, in <module>
    print(Addresspls(["cat",["c","a","t"],[],pairfinder("cat",["[","]"])]))
  File "C:/An/Delta Func/autocomposer.py", line 328, in Addresspls
    Interim = str(InsertAt(list(Interim),1,x))
  File "C:/An/Delta Func/autocomposer.py", line 266, in InsertAt
    VALUE = List[:Index]
TypeError: slice indices must be integers or None or have an __index__ method
>>> ================================ RESTART ================================
>>> 
checking addresspls
wtf is interim 1
x should be 1 1
Traceback (most recent call last):
  File "C:/An/Delta Func/autocomposer.py", line 334, in <module>
    print(Addresspls(["cat",["c","a","t"],[],pairfinder("cat",["[","]"])]))
  File "C:/An/Delta Func/autocomposer.py", line 329, in Addresspls
    Interim = str(InsertAt(list(Interim),1,x))
  File "C:/An/Delta Func/autocomposer.py", line 266, in InsertAt
    VALUE = List[:Index]
TypeError: slice indices must be integers or None or have an __index__ method
>>> ================================ RESTART ================================
>>> 
checking addresspls
wtf is interim 1
x should be 1 1
Traceback (most recent call last):
  File "C:/An/Delta Func/autocomposer.py", line 334, in <module>
    print(Addresspls(["cat",["c","a","t"],[],pairfinder("cat",["[","]"])]))
  File "C:/An/Delta Func/autocomposer.py", line 329, in Addresspls
    Interim = str(InsertAt(list(Interim),"1",x))
  File "C:/An/Delta Func/autocomposer.py", line 266, in InsertAt
    VALUE = List[:Index]
TypeError: slice indices must be integers or None or have an __index__ method
>>> ================================ RESTART ================================
>>> 
checking addresspls
wtf is interim 1
tools
['1']
1
>>> ================================ RESTART ================================
>>> 
checking addresspls
wtf is interim 1
tools
['1']
endtools
1
>>> ================================ RESTART ================================
>>> 
checking addresspls
wtf is interim 1
tools
Traceback (most recent call last):
  File "C:/An/Delta Func/autocomposer.py", line 336, in <module>
    print(Addresspls(["cat",["c","a","t"],[],pairfinder("cat",["[","]"])]))
  File "C:/An/Delta Func/autocomposer.py", line 329, in Addresspls
    Interim = InsertAt(list(Interim),"1",x)
  File "C:/An/Delta Func/autocomposer.py", line 266, in InsertAt
    VALUE = List[:Index]
TypeError: slice indices must be integers or None or have an __index__ method
>>> ================================ RESTART ================================
>>> 
checking addresspls
wtf is interim 1
tools
Traceback (most recent call last):
  File "C:/An/Delta Func/autocomposer.py", line 336, in <module>
    print(Addresspls(["cat",["c","a","t"],[],pairfinder("cat",["[","]"])]))
  File "C:/An/Delta Func/autocomposer.py", line 330, in Addresspls
    print(InsertAt(Interim,"1",x))
  File "C:/An/Delta Func/autocomposer.py", line 266, in InsertAt
    VALUE = List[:Index]
TypeError: slice indices must be integers or None or have an __index__ method
>>> ================================ RESTART ================================
>>> 
checking addresspls
wtf is interim 1
tools
Traceback (most recent call last):
  File "C:/An/Delta Func/autocomposer.py", line 336, in <module>
    print(Addresspls(["cat",["c","a","t"],[],pairfinder("cat",["[","]"])]))
  File "C:/An/Delta Func/autocomposer.py", line 330, in Addresspls
    print(InsertAt(Interim,"1",int(x)))
  File "C:/An/Delta Func/autocomposer.py", line 267, in InsertAt
    VALUE.append(obj)
AttributeError: 'str' object has no attribute 'append'
>>> ================================ RESTART ================================
>>> 
checking addresspls
wtf is interim 1
tools
['1', '1']
endtools
1
>>> ================================ RESTART ================================
>>> 
checking addresspls
wtf is interim 1
tools
endtools
Traceback (most recent call last):
  File "C:/An/Delta Func/autocomposer.py", line 335, in <module>
    print(Addresspls(["cat",["c","a","t"],[],pairfinder("cat",["[","]"])]))
  File "C:/An/Delta Func/autocomposer.py", line 331, in Addresspls
    ANS = int(Interim, 2)
TypeError: int() can't convert non-string with explicit base
>>> ================================ RESTART ================================
>>> 
checking addresspls
wtf is interim 1
tools
endtools
wtf is interim now ['1', '1']
Traceback (most recent call last):
  File "C:/An/Delta Func/autocomposer.py", line 336, in <module>
    print(Addresspls(["cat",["c","a","t"],[],pairfinder("cat",["[","]"])]))
  File "C:/An/Delta Func/autocomposer.py", line 332, in Addresspls
    ANS = int(Interim, 2)
TypeError: int() can't convert non-string with explicit base
>>> ================================ RESTART ================================
>>> 
checking addresspls
OG Interim [0, 1, 2]
afterzfill 1
wtf is interim 1
tools
endtools
wtf is interim now ['1', '1']
Traceback (most recent call last):
  File "C:/An/Delta Func/autocomposer.py", line 340, in <module>
    print(Addresspls(["cat",["c","a","t"],[],pairfinder("cat",["[","]"])]))
  File "C:/An/Delta Func/autocomposer.py", line 336, in Addresspls
    ANS = int(Interim, 2)
TypeError: int() can't convert non-string with explicit base
>>> ================================ RESTART ================================
>>> 
checking addresspls
OG Interim [0, 1, 2]
afterzfill [0, 1, 2]
wtf is interim [0, 1, 2]
tools
endtools
tools
endtools
tools
endtools
wtf is interim now [0, 1, 2]
Traceback (most recent call last):
  File "C:/An/Delta Func/autocomposer.py", line 340, in <module>
    print(Addresspls(["cat",["c","a","t"],[],pairfinder("cat",["[","]"])]))
  File "C:/An/Delta Func/autocomposer.py", line 336, in Addresspls
    ANS = int(ANS, 2)
TypeError: int() can't convert non-string with explicit base
>>> ================================ RESTART ================================
>>> 
checking addresspls
OG Interim [0, 1, 2]
afterzfill [0, 1, 2]
wtf is interim [0, 1, 2]
tools 1
endtools ['1', 0, 1, 2]
tools ['1', 0, 1, 2]
endtools [0, '1', 1, 2]
tools [0, '1', 1, 2]
endtools [0, 1, '1', 2]
wtf is ANS now [0, 1, '1', 2]
Traceback (most recent call last):
  File "C:/An/Delta Func/autocomposer.py", line 340, in <module>
    print(Addresspls(["cat",["c","a","t"],[],pairfinder("cat",["[","]"])]))
  File "C:/An/Delta Func/autocomposer.py", line 336, in Addresspls
    ANS = int(ANS, 2)
TypeError: int() can't convert non-string with explicit base
>>> ================================ RESTART ================================
>>> 
checking addresspls
OG Interim [0, 1, 2]
afterzfill 1
wtf is interim [0, 1, 2]
tools 1
endtools ['1', 0, 1, 2]
tools ['1', 0, 1, 2]
endtools [0, '1', 1, 2]
tools [0, '1', 1, 2]
endtools [0, 1, '1', 2]
wtf is ANS now [0, 1, '1', 2]
Traceback (most recent call last):
  File "C:/An/Delta Func/autocomposer.py", line 340, in <module>
    print(Addresspls(["cat",["c","a","t"],[],pairfinder("cat",["[","]"])]))
  File "C:/An/Delta Func/autocomposer.py", line 336, in Addresspls
    ANS = int(ANS, 2)
TypeError: int() can't convert non-string with explicit base
>>> ================================ RESTART ================================
>>> 
checking addresspls
OG Interim [0, 1, 2]
what is longest 2
afterzfill 1
wtf is interim [0, 1, 2]
tools 1
endtools ['1', 0, 1, 2]
tools ['1', 0, 1, 2]
endtools [0, '1', 1, 2]
tools [0, '1', 1, 2]
endtools [0, 1, '1', 2]
wtf is ANS now [0, 1, '1', 2]
Traceback (most recent call last):
  File "C:/An/Delta Func/autocomposer.py", line 340, in <module>
    print(Addresspls(["cat",["c","a","t"],[],pairfinder("cat",["[","]"])]))
  File "C:/An/Delta Func/autocomposer.py", line 336, in Addresspls
    ANS = int(ANS, 2)
TypeError: int() can't convert non-string with explicit base
>>> ================================ RESTART ================================
>>> 
checking addresspls
OG Interim [0, 1, 2]
afterzfill 1
wtf is interim [0, 1, 2]
tools 1
endtools ['1', 0, 1, 2]
tools ['1', 0, 1, 2]
endtools [0, '1', 1, 2]
tools [0, '1', 1, 2]
endtools [0, 1, '1', 2]
wtf is ANS now [0, 1, '1', 2]
Traceback (most recent call last):
  File "C:/An/Delta Func/autocomposer.py", line 340, in <module>
    print(Addresspls(["cat",["c","a","t"],[],pairfinder("cat",["[","]"])]))
  File "C:/An/Delta Func/autocomposer.py", line 336, in Addresspls
    ANS = int(ANS, 2)
TypeError: int() can't convert non-string with explicit base
>>> ================================ RESTART ================================
>>> 
checking addresspls
OG Interim [0, 1, 2]
afterzfill 0000000004
wtf is interim [0, 1, 2]
tools 0000000004
endtools ['1', 0, 1, 2]
tools ['1', 0, 1, 2]
endtools [0, '1', 1, 2]
tools [0, '1', 1, 2]
endtools [0, 1, '1', 2]
wtf is ANS now [0, 1, '1', 2]
Traceback (most recent call last):
  File "C:/An/Delta Func/autocomposer.py", line 341, in <module>
    print(Addresspls(["cat",["c","a","t"],[],pairfinder("cat",["[","]"])]))
  File "C:/An/Delta Func/autocomposer.py", line 337, in Addresspls
    ANS = int(ANS, 2)
TypeError: int() can't convert non-string with explicit base
>>> ================================ RESTART ================================
>>> 
checking addresspls
OG Interim [0, 1, 2]
afterzfill 1
wtf is interim [0, 1, 2]
tools 1
endtools ['1', 0, 1, 2]
tools ['1', 0, 1, 2]
endtools [0, '1', 1, 2]
tools [0, '1', 1, 2]
endtools [0, 1, '1', 2]
wtf is ANS now [0, 1, '1', 2]
Traceback (most recent call last):
  File "C:/An/Delta Func/autocomposer.py", line 341, in <module>
    print(Addresspls(["cat",["c","a","t"],[],pairfinder("cat",["[","]"])]))
  File "C:/An/Delta Func/autocomposer.py", line 337, in Addresspls
    ANS = int(ANS, 2)
TypeError: int() can't convert non-string with explicit base
>>> ================================ RESTART ================================
>>> 
checking addresspls
OG Interim [0, 1, 2]
afterzfill 01
wtf is interim [0, 1, 2]
tools 01
endtools ['1', 0, 1, 2]
tools ['1', 0, 1, 2]
endtools [0, '1', 1, 2]
tools [0, '1', 1, 2]
endtools [0, 1, '1', 2]
wtf is ANS now [0, 1, '1', 2]
Traceback (most recent call last):
  File "C:/An/Delta Func/autocomposer.py", line 341, in <module>
    print(Addresspls(["cat",["c","a","t"],[],pairfinder("cat",["[","]"])]))
  File "C:/An/Delta Func/autocomposer.py", line 337, in Addresspls
    ANS = int(ANS, 2)
TypeError: int() can't convert non-string with explicit base
>>> ================================ RESTART ================================
>>> 
checking addresspls
OG Interim [0, 1, 2]
afterzfill 1
wtf is interim [0, 1, 2]
tools 1
endtools ['1', 0, 1, 2]
tools ['1', 0, 1, 2]
endtools [0, '1', 1, 2]
tools [0, '1', 1, 2]
endtools [0, 1, '1', 2]
wtf is ANS now [0, 1, '1', 2]
Traceback (most recent call last):
  File "C:/An/Delta Func/autocomposer.py", line 341, in <module>
    print(Addresspls(["cat",["c","a","t"],[],pairfinder("cat",["[","]"])]))
  File "C:/An/Delta Func/autocomposer.py", line 337, in Addresspls
    ANS = int(ANS, 2)
TypeError: int() can't convert non-string with explicit base
>>> ================================ RESTART ================================
>>> 
checking addresspls
OG Interim [0, 1, 2]
afterzfill 1
wtf is interim [0, 1, 2]
tools 1
endtools ['1', 0, 1, 2]
tools ['1', 0, 1, 2]
endtools [0, '1', 1, 2]
tools [0, '1', 1, 2]
endtools [0, 1, '1', 2]
wtf is ANS now [0, 1, '1', 2]
Traceback (most recent call last):
  File "C:/An/Delta Func/autocomposer.py", line 340, in <module>
    print(Addresspls(["cat",["c","a","t"],[],pairfinder("cat",["[","]"])]))
  File "C:/An/Delta Func/autocomposer.py", line 336, in Addresspls
    ANS = int(ANS, 2)
ValueError: invalid literal for int() with base 2: "[0, 1, '1', 2]"
>>> ================================ RESTART ================================
>>> 
checking addresspls
OG Interim [0, 1, 2]
afterzfill 1
wtf is interim [0, 1, 2]
tools 1
endtools ['1', '1']
tools ['1', '1']
endtools ['[', '1', "'", '1', "'", ',', ' ', "'", '1', "'", ']']
tools ['[', '1', "'", '1', "'", ',', ' ', "'", '1', "'", ']']
endtools ['[', "'", '1', '[', "'", ',', ' ', "'", '1', "'", ',', ' ', '"', "'", '"', ',', ' ', "'", '1', "'", ',', ' ', '"', "'", '"', ',', ' ', "'", ',', "'", ',', ' ', "'", ' ', "'", ',', ' ', '"', "'", '"', ',', ' ', "'", '1', "'", ',', ' ', '"', "'", '"', ',', ' ', "'", ']', "'", ']']
wtf is ANS now ['[', "'", '1', '[', "'", ',', ' ', "'", '1', "'", ',', ' ', '"', "'", '"', ',', ' ', "'", '1', "'", ',', ' ', '"', "'", '"', ',', ' ', "'", ',', "'", ',', ' ', "'", ' ', "'", ',', ' ', '"', "'", '"', ',', ' ', "'", '1', "'", ',', ' ', '"', "'", '"', ',', ' ', "'", ']', "'", ']']
Traceback (most recent call last):
  File "C:/An/Delta Func/autocomposer.py", line 340, in <module>
    print(Addresspls(["cat",["c","a","t"],[],pairfinder("cat",["[","]"])]))
  File "C:/An/Delta Func/autocomposer.py", line 336, in Addresspls
    ANS = int(ANS, 2)
ValueError: invalid literal for int() with base 2: '[\'[\', "\'", \'1\', \'[\', "\'", \',\', \' \', "\'", \'1\', "\'", \',\', \' \', \'"\', "\'", \'"\', \',\', \' \', "\'", \'1\', "\'", \',\', \' \', \'"\', "\'", \'"\', \',\', \' \', "\'", \',\', "\'"
>>> ================================ RESTART ================================
>>> 
checking addresspls
OG Interim [0, 1, 2]
afterzfill 1
wtf is interim [0, 1, 2]
tools 1
Traceback (most recent call last):
  File "C:/An/Delta Func/autocomposer.py", line 340, in <module>
    print(Addresspls(["cat",["c","a","t"],[],pairfinder("cat",["[","]"])]))
  File "C:/An/Delta Func/autocomposer.py", line 333, in Addresspls
    ANS = str(InsertAt(ANS,"1",int(x)))
  File "C:/An/Delta Func/autocomposer.py", line 267, in InsertAt
    VALUE.append(obj)
AttributeError: 'str' object has no attribute 'append'
>>> ================================ RESTART ================================
>>> 
checking addresspls
OG Interim [0, 1, 2]
afterzfill 1
wtf is interim [0, 1, 2]
tools 1
endtools ['1', '1']
tools ['1', '1']
endtools ['[', '1', "'", '1', "'", ',', ' ', "'", '1', "'", ']']
tools ['[', '1', "'", '1', "'", ',', ' ', "'", '1', "'", ']']
endtools ['[', "'", '1', '[', "'", ',', ' ', "'", '1', "'", ',', ' ', '"', "'", '"', ',', ' ', "'", '1', "'", ',', ' ', '"', "'", '"', ',', ' ', "'", ',', "'", ',', ' ', "'", ' ', "'", ',', ' ', '"', "'", '"', ',', ' ', "'", '1', "'", ',', ' ', '"', "'", '"', ',', ' ', "'", ']', "'", ']']
wtf is ANS now ['[', "'", '1', '[', "'", ',', ' ', "'", '1', "'", ',', ' ', '"', "'", '"', ',', ' ', "'", '1', "'", ',', ' ', '"', "'", '"', ',', ' ', "'", ',', "'", ',', ' ', "'", ' ', "'", ',', ' ', '"', "'", '"', ',', ' ', "'", '1', "'", ',', ' ', '"', "'", '"', ',', ' ', "'", ']', "'", ']']
Traceback (most recent call last):
  File "C:/An/Delta Func/autocomposer.py", line 340, in <module>
    print(Addresspls(["cat",["c","a","t"],[],pairfinder("cat",["[","]"])]))
  File "C:/An/Delta Func/autocomposer.py", line 336, in Addresspls
    ANS = int(ANS, 2)
ValueError: invalid literal for int() with base 2: '[\'[\', "\'", \'1\', \'[\', "\'", \',\', \' \', "\'", \'1\', "\'", \',\', \' \', \'"\', "\'", \'"\', \',\', \' \', "\'", \'1\', "\'", \',\', \' \', \'"\', "\'", \'"\', \',\', \' \', "\'", \',\', "\'"
>>> ================================ RESTART ================================
>>> 
checking addresspls
OG Interim [0, 1, 2]
afterzfill 1
wtf is interim [0, 1, 2]
tools 1
fml this is list not string ['1', '1']
endtools 1
tools 1
fml this is list not string ['1', '1']
endtools 1
tools 1
fml this is list not string ['1', '1']
endtools 1
wtf is ANS now 1
1
>>> ================================ RESTART ================================
>>> 
checking addresspls
OG Interim [0, 1, 2]
afterzfill 1
wtf is interim [0, 1, 2]
tools 1
fml this is list not string ['1', '1']
%s ['1', '1']
endtools 1
tools 1
fml this is list not string ['1', '1']
%s ['1', '1']
endtools 1
tools 1
fml this is list not string ['1', '1']
%s ['1', '1']
endtools 1
wtf is ANS now 1
1
>>> ================================ RESTART ================================
>>> 
hello world
hello world
hello world
hello world
>>> ================================ RESTART ================================
>>> 
checking addresspls
OG Interim [0, 1, 2]
afterzfill 1
wtf is interim [0, 1, 2]
tools 1
fml this is list not string ['1', '1']
['1', '1']
endtools 1
tools 1
fml this is list not string ['1', '1']
['1', '1']
endtools 1
tools 1
fml this is list not string ['1', '1']
['1', '1']
endtools 1
wtf is ANS now 1
1
>>> ================================ RESTART ================================
>>> 
checking addresspls
OG Interim [0, 1, 2]
afterzfill 1
new interim <filter object at 0x032CB790>
tools 1
fml this is list not string ['1', '1']
['1', '1']
endtools 1
tools 1
fml this is list not string ['1', '1']
['1', '1']
endtools 1
wtf is ANS now 1
1
>>> ================================ RESTART ================================
>>> 
checking addresspls
OG Interim [0, 1, 2]
fml C base <filter object at 0x035C8590>
afterzfill 1
new interim <filter object at 0x035C8590>
tools 1
fml this is list not string ['1', '1']
['1', '1']
endtools 1
tools 1
fml this is list not string ['1', '1']
['1', '1']
endtools 1
wtf is ANS now 1
1
>>> ================================ RESTART ================================
>>> 
checking addresspls
OG Interim [0, 1, 2]
fml C base [0, 1]
afterzfill 1
new interim <filter object at 0x033C85B0>
tools 1
fml this is list not string ['1', '1']
['1', '1']
endtools 1
tools 1
fml this is list not string ['1', '1']
['1', '1']
endtools 1
wtf is ANS now 1
1
>>> ================================ RESTART ================================
>>> 
checking addresspls
OG Interim [0, 1, 2]
afterzfill 1
new interim [0, 1]
tools 1
fml this is list not string ['1', '1']
['1', '1']
endtools 1
tools 1
fml this is list not string ['1', '1']
['1', '1']
endtools 1
wtf is ANS now 1
1
>>> ================================ RESTART ================================
>>> 
checking addresspls
OG Interim [0, 1, 2]
afterzfill 001
new interim [0, 1]
tools 001
fml this is list not string ['1', '0', '0', '1']
['1', '0', '0', '1']
endtools 001
tools 001
fml this is list not string ['0', '1', '0', '1']
['0', '1', '0', '1']
endtools 001
wtf is ANS now 001
1
>>> ================================ RESTART ================================
>>> 
t for beforehand test for b
>>> ================================ RESTART ================================
>>> 
t for beforehand
test for b
>>> ================================ RESTART ================================
>>> 
t for beforehand
tes
>>> ================================ RESTART ================================
>>> 
tes
t for beforehand
>>> ================================ RESTART ================================
>>> 
checking addresspls
OG Interim [0, 1, 2]
afterzfill 001
new interim [0, 1]
Traceback (most recent call last):
  File "C:/An/Delta Func/autocomposer.py", line 338, in <module>
    print(Addresspls(["cat",["c","a","t"],[],pairfinder("cat",["[","]"])]))
  File "C:/An/Delta Func/autocomposer.py", line 332, in Addresspls
    ANS = ANS[:x-1] + 1 + ANS[x+1:]
TypeError: Can't convert 'int' object to str implicitly
>>> ================================ RESTART ================================
>>> 
checking addresspls
OG Interim [0, 1, 2]
afterzfill 001
new interim [0, 1]
wtf is ANS now 1101
13
>>> ================================ RESTART ================================
>>> 
checking addresspls
OG Interim [0, 1, 2]
afterzfill 001
new interim [0, 1]
wtf is ANS now 101001
41
>>> ================================ RESTART ================================
>>> 
tes
t for beforehand
>>> ================================ RESTART ================================
>>> 
checking addresspls
OG Interim [0, 1, 2]
afterzfill 001
new interim [0, 1]
wtf is ANS now 101001
41
>>> ================================ RESTART ================================
>>> 
checking addresspls
OG Interim [0, 1, 2]
afterzfill 001
new interim [0, 1]
stats 0 001 00 001
stats 1 001001  01001
wtf is ANS now 101001
41
>>> ================================ RESTART ================================
>>> 

test for beforehand
>>> 
