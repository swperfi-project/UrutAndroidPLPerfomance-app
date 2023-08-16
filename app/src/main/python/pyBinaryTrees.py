# binary-trees Python 3 #4 program
# https://benchmarksgame-team.pages.debian.net/benchmarksgame/program/binarytrees-python3-4.html

# The Computer Language Benchmarks Game
# https://salsa.debian.org/benchmarksgame-team/benchmarksgame/
#
# contributed by Antoine Pitrou
# modified by Dominique Wahli and Daniel Nanz
# modified by Joerg Baumann
# modified by Jonathan Ultis
from multiprocessing.dummy import Pool

def make_tree(dd,cont=0):
    cont = cont + 1
    if dd > 0:
        return (make_tree(dd-1,cont+1), make_tree(dd-1,cont+1))
    return (None, None)

def check_tree(node,cont=0):
    l, r = node
    if l is None:
        return 1
    else:
        return 1 + check_tree(l,cont+1) + check_tree(r,cont+1)

def make_check(dd, make=make_tree, check=check_tree):
    return check(make(dd))

def pyBinaryTreesRun(n, min_depth=4):
    max_depth = max(min_depth + 2, n)
    stretch_depth = max_depth + 1

    print('stretch tree of depth {0}\t check: {1}'.format(
        stretch_depth, make_check(stretch_depth)))

    long_lived_tree = make_tree(max_depth)

    mmd = max_depth + min_depth
    pool = Pool()

    for dd in range(min_depth, stretch_depth, 2):
        ii = 2 ** (mmd - dd)
        cs = sum(pool.map(make_check, [dd]*ii))
        print('{0}\t trees of depth {1}\t check: {2}'.format(ii, dd, cs))
    print('long lived tree of depth {0}\t check: {1}'.format(
        max_depth, check_tree(long_lived_tree)))