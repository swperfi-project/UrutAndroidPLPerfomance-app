# pidigits Python 3 #5 program
# https://benchmarksgame-team.pages.debian.net/benchmarksgame/program/pidigits-python3-5.html

# The Computer Language Benchmarks Game
# https://salsa.debian.org/benchmarksgame-team/benchmarksgame/
#
# Translated from Mr Ledrug's C program by Jeremy Zerfas.
# Transliterated from GMP to gmpy2 by Isaac Gouy


from sys import argv
from gmpy2 import xmpz

def extract_Digit(nth):
    global tmp1, tmp2, acc, den, num
    tmp1 = num * nth
    tmp2 = tmp1 + acc
    tmp1 = tmp2 // den

    return tmp1


def eliminate_Digit(d):
    global acc, den, num
    acc = acc - den * d
    acc = acc * 10
    num = num * 10


def next_Term(k):
    global acc, den, num
    k2=k*2+1
    acc = acc + num * 2
    acc = acc * k2
    den = den * k2
    num = num * k


def run(num):
    global tmp1, tmp2, acc, den, num
    n=num

    tmp1 = xmpz(0)
    tmp2 = xmpz(0)

    acc = xmpz(0)
    den = xmpz(1)
    num = xmpz(1)


    i=0
    k=0
    while i<n:
        k+=1
        next_Term(k)

        if num > acc:
            continue


        d=extract_Digit(3)
        if d!=extract_Digit(4):
            continue


        print(chr(48+d), end="")
        i+=1
        if i%10==0:
            print("\t:%d" % (i))
        eliminate_Digit(d)