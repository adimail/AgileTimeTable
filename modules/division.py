class Division:
    def __init__(self, name = "", gfm = "", is_core=True):
        self.name = name
        self.gfm = gfm
        self.is_core = is_core #Core divisions include instrumentation, electrical, entc

fy_btech_divisions = [
    Division("A", is_core=0),
    Division("B", is_core=0),
    Division("C", is_core=0),
    Division("D", is_core=1),
    Division("E", is_core=0),
    Division("F", is_core=0),
    Division("G", is_core=1),
    Division("H", is_core=1),
    Division("I", is_core=1),
]

        