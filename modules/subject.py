import pandas as pd

# Define the Subject class
class Subject:
    def __init__(self, name, abb, division_dependent, even_term, odd_term, theory_hours, practical_hours):
        self.name = name
        self.abb = abb
        self.division_dependent = division_dependent
        self.even_term = even_term
        self.odd_term = odd_term
        self.theory_hours = theory_hours
        self.practical_hours = practical_hours
        self.total_load = self.theory_hours + self.practical_hours

    def to_dict(self):
        return {
            "Name": self.name,
            "Abbreviation": self.abb,
            "Division Dependent": self.division_dependent,
            "Even Term": self.even_term,
            "Odd Term": self.odd_term,
            "Theory Hours": self.theory_hours,
            "Practical Hours": self.practical_hours,
            "Total Load": self.total_load
        }

# Create different objects for each subject
subjects = [
    Subject("Engineering Mathematics - I", "EM-I", False, False, True, 3, 6),
    Subject("Engineering Mathematics - II", "EM-II", False, True, False, 3, 6),
    Subject("Industrial Chemistry", "CHEM", True, True, True, 3, 6),
    Subject("Engineering Physics", "PHY", True, True, True, 3, 6),
    Subject("Engineering Graphics and Introduction to Cad", "EG", False, False, True, 1, 6),
    Subject("Environmental Informatics", "EI", False, True, False, 1, 6),
    Subject("Basic Electronics Engineering", "BXE", True, True, True, 3, 6),
    Subject("Basic Electrical Engineering", "BEE", True, True, True, 3, 6),
    Subject("Engineering Mechanics", "EM", False, False, True, 2, 6),
    Subject("Basics In Mechanical Engineering", "BME", False, True, False, 2, 6),
    Subject("Project Based Learning and Management - I", "PBLM-I", False, False, True, 0, 6),  # Assuming empty values
    Subject("Project Based Learning and Management - II", "PBLM-II", False, True, False, 0, 6),  # Assuming empty values
    Subject("Problem Solving and Programming - I", "PSP-I", False, False, True, 2, 6),
    Subject("Problem Solving and Programming - II", "PSP-II", False, True, False, 2, 6),
    Subject("Universal Human Values - I", "UHV-I", False, False, True, 1, 0),  # Assuming empty values for practical
    Subject("Universal Human Values - II", "UHV-II", False, True, False, 1, 0),  # Assuming empty values for practical
    Subject("Physical Education", "PE", False, True, True, 1, 0),  # Assuming empty values for practical
]

# Convert the list of Subject objects to a list of dictionaries
subject_dicts = [subject.to_dict() for subject in subjects]

# Create a DataFrame from the list of dictionaries
df = pd.DataFrame(subject_dicts)

print(df)
