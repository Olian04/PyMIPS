from pymips import add, addi, beq, zero, Registry
from pymips import config
import sys

#!
def py_fac(n: int)->int:
    res = 1
    for i in range(1, n+1):
        res *= i
    return res
#?

def mips_fac(n: int)->int:
    a0 = Registry("a0", n) #
    v0 = Registry("v0") # res
    t0 = Registry("t0")#, a) # index
    t1 = Registry("t1")#, b) # mult value
    t2 = Registry("t2") # res

    addi(v0, zero, 1)
    while not beq(a0, zero, "fac_done"):

        add(t0, zero, v0)
        add(t1, zero, a0)
        addi(t2, zero, 0)
        while not beq(t0, zero, "mult_done"):
            add(t2, t2, t1)
            addi(t0, t0, -1)

        add(v0, zero, t2)

        addi(a0, a0, -1)

    return v0.val

if __name__ == '__main__':
    config.DOLOG = True
    count = 8
    print("Running... [WARNING: possibly long runtime if N > 10]\nN =", count)

    sysout = sys.stdout
    sys.stdout = open("%s.log" % __name__, "w")
    A, B = py_fac(count), mips_fac(count)
    sys.stdout = sysout

    print("""Python factorial: {}
Pretend mips factorial: {}, {}
Equal results: {}""".format(A, B, hex(B), A==B))
