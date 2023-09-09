import pandas as pd

class Division:
    def __init__(self, name = "",branch="", gfm = "guardian faculty member", is_core=True):
        self.name = name
        self.gfm = gfm
        self.branch = branch
        self.is_core = is_core #Core divisions include instrumentation, electrical, entc

    def to_dict(self):
        return {
            "Name": self.name,
            "GFM": self.gfm,
            "Branch": ["Computer" if not self.is_core else "non Computer"]
        }

divisions = [
    Division("A", "Computer Engineering", is_core=0),
    Division("B", "Computer Engineering", is_core=0),
    Division("C", "Information technology", is_core=0),
    Division("D", "Instrumentation", is_core=1),
    Division("E", "AI & DS", is_core=0),
    Division("F", "AI & DS", is_core=0),
    Division("G", "E&Tc", is_core=1),
    Division("H", "Instrumentation", is_core=1),
    Division("I", is_core=1),
]


# Convert the list of Subject objects to a list of dictionaries
division_dicts = [division.to_dict() for division in divisions]

# Create a DataFrame from the list of dictionaries
fy_btech_divisions = pd.DataFrame(division_dicts)
print(fy_btech_divisions)