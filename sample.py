import pprint
import sys
from utils import shuffle

##
## Function Demo
##
# check odd or even
def odd_or_even(max = 5):
    for i in range(1, max+1):
        if i % 2 != 0:
            print("{0} is odd（奇数）".format(i))
        else:
            print("{0} is even（偶数）".format(i))

# odd or even
odd_or_even(3)

##
## Shuffle List
##
person = [
    'Keiichi',
    'Maki',
    'Yoko',
    'Hidekazu'
]
# print list
print("Before shuffle: {0}".format(person))
# shuffle
person = shuffle.shuffle(person)
# print list
print("After shuffle: {0}".format(person))

##
## Module search path
##
pprint.pprint(sys.path)