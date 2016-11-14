"Emulates some of the functionality of mips"

class Registry:
    def __init__(self, name: str, value: int = 0):
        self._val = value
        self._name = name

    @property
    def name(self):
        return self._name

    @property
    def val(self):
        return self._val

    @val.setter
    def val(self, new):
        self._val = new

    def __str__(self)->str:
        return str(self._val)

zero = Registry("0")
":type zero: Registry"
