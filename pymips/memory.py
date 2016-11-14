"Emulates memory cells"
from collections import defaultdict

class Memory:
    def __init__(self):
        self.mem = defaultdict(hex)

    def memWrite(self, address: hex, value: any)->None:
        self.mem[address] = value

    def memRead(self, address: hex)->any:
        return self.mem[address]
