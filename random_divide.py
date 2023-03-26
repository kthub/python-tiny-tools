# -*- coding: utf-8 -*-

import random

# main function
if __name__ == "__main__":

    # print 1-5 for each person
    person = [
        'Keiichi',
        'Maki',
        'Yoko',
        'Hidekazu'
    ]

    # shuffle
    random.shuffle(person)

    for p in person:
        num = random.randint(1, 5)
        print(p + " : " + str(num))
