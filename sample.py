# -*- coding: utf-8 -*-

# check odd or even
def odd_or_even(max = 5):
    for i in range(1, max+1):
        if i % 2 != 0:
            print("{0} is odd（奇数）".format(i))
        else:
            print("{0} is even（偶数）".format(i))

# main function
if __name__ == "__main__":
    odd_or_even(3)
