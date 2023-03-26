# -*- coding: utf-8 -*-
def odd_or_even():
    max = 5 # loop count
    for i in range(1, max+1):
        if i % 2 != 0:
            print("{0} is odd".format(i))
        else:
            print("{0} is even".format(i))

# main function
if __name__ == "__main__":
    odd_or_even()
    print(u'あいうえお')
