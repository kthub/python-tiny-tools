##
## python3系 基礎文法
## https://qiita.com/rohinomiya/items/aab6b16d1a470871713c
##
import sys

# execute only if run as a script
if __name__ == "__main__":

    # コマンドライン取得
    for arg in sys.argv[1:]: # argv[0]=スクリプト自身の名前
        print(arg)

    # nop
    pass

    # list
    nlst = [10, 20, 30]
    nlst[0] = 40
    print(len(nlst))
    for n in nlst:
        print(n)
    
    # tuple (= read only list)
    ntpl = (50, 60, 70)
    #ntpl[0] = 40  <== NG
    print(len(ntpl))
    for n in ntpl:
        print(n)
    
    # dictionary (= map)
    dict = { "key1":"東京都", "key2":"大阪府" }
    print(dict["key1"])

    # for loop
    for i in range(1, 10):
        print(i)
