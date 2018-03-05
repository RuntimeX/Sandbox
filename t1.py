from collections import deque as dq
from random import randint as r


a = 1
list1 = ["3","d","6"]
list2 = ["d","4"]
list3 = ["1","d","20"]

while a != 1: #lst:
    numOfDice = dq([1])
    valOfDie = dq([])
    if lst(0) == 'd':
        lst.remove('d')
        lst.pop(valOfDie)
        xxx = [numOfDice,valOfDie]
    elif lst(0) == "1" and lst(1) == "d":   #in case 10 - 19dx
        a = 1
    

#ans = ''.join(int(c) for c in lst)

#def zzz():
#    c = 11
#    lst1 = []
#    while c > 0:
#        lst1.append(r(1,3))
#        c-=1
#    return lst1

