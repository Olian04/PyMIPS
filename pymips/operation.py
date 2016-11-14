from pymips.config import config as conf
from pymips.register import Registry, zero
from pymips.memory import Memory


def add(rd: Registry, rs: Registry, rt: Registry)->None:
    """ add
    rd.val = rs.val + rt.val"""
    if conf.DOLOG: print("add ${} ${} ${}".format(rd.name, rs.name, rt.name))
    rd.val = rs.val + rt.val

def addi(rd: Registry, rs: Registry, imm: int)->None:
    """ add imidiate
    rd.val = rs.val + imm"""
    if conf.DOLOG: print("addi ${} ${} {}".format(rd.name, rs.name, imm))
    rd.val = rs.val + imm

def beq(rd: Registry, rs: Registry, lable: str)->str:
    """ branch equal
    rs.val == rt.val"""
    res = (rd.val == rs.val)
    if conf.DOLOG:
        print("beq ${} ${} {}".format(rd.name, rs.name, lable))
        if res:
            print("j", lable)
    return res

def sw(rt: Registry, rt: Registry, rt: int):
    """ store word
    todo
    """
    pass
