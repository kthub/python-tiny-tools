# -*- coding: utf-8 -*-
#
# answer for the question below
# http://www.neetaro.com/entry/atcoder-beginner-contest-abc-003
#
# B問題
import sys
if __name__ == '__main__':

    # 1st line
    f = sys.stdin.readline().rstrip('\r\n')
    # 2nd line
    s = sys.stdin.readline().rstrip('\r\n')

    winable = True
    for i in range(1, len(f)+1):
        c1 = f[i-1]
        c2 = s[i-1]
        if (c1 != c2):
            if ((c1 != '@') and (c2 != '@')):
                winable = False
            elif ((c1 == '@') and (c2 not in "atcoder")):
                    winable = False
            elif ((c2 == '@') and (c1 not in "atcoder")):
                    winable = False

    # 結果を出力
    if (winable):
        print("Possible to Win!!")
    else:
        print("You MUST lose!!")
