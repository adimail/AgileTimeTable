import pandas as pd

class Subject:
    def __init__(self, name, abb, division_dependent, even_term, odd_term):
        self.name = name
        self.abb = abb
        self.division_dependent = division_dependent
        self.even_term = even_term
        self.odd_term = odd_term

    def to_dict(self):
        return {
            "Name": self.name,
            "Abbreviation": self.abb,
            "Division Dependent": self.division_dependent,
            "Even Term": self.even_term,
            "Odd Term": self.odd_term,
        }

# Create different objects for each subject
subjects = [
    Subject("Engineering Mathematics - I", "EM-I", False, False, True),
    Subject("Engineering Mathematics - II", "EM-II", False, True, False),
    Subject("Industrial Chemistry", "CHEM", True, True, True),
    Subject("Engineering Physics", "PHY", True, True, True),
    Subject("Engineering Graphics and Introduction to Cad", "EG", False, False, True),
    Subject("Environmental Informatics", "EI", False, True, False),
    Subject("Basic Electronics Engineering", "BXE", True, True, True),
    Subject("Basic Electrical Engineering", "BEE", True, True, True),
    Subject("Engineering Mechanics", "EM", False, False, True),
    Subject("Basics In Mechanical Engineering", "BME", False, True, False),
    Subject("Project Based Learning and Management - I", "PBLM-I", False, False, True),  # Assuming empty values
    Subject("Project Based Learning and Management - II", "PBLM-II", False, True, False),  # Assuming empty values
    Subject("Problem Solving and Programming - I", "PSP-I", False, False, True),
    Subject("Problem Solving and Programming - II", "PSP-II", False, True, False),
    Subject("Universal Human Values - I", "UHV-I", False, False, True),  # Assuming empty values for practical
    Subject("Universal Human Values - II", "UHV-II", False, True, False),  # Assuming empty values for practical
    Subject("Physical Education", "PE", False, True, True),  # Assuming empty values for practical
]

# Convert the list of Subject objects to a list of dictionaries
subject_dicts = [subject.to_dict() for subject in subjects]

# Create a DataFrame from the list of dictionaries
fy_btech_subjects = pd.DataFrame(subject_dicts)
# print(fy_btech_subjects)

odd_term_subjects = fy_btech_subjects[fy_btech_subjects['Odd Term'] == True]
# print(odd_term_subjects)

odd_and_division_independent_subjects = fy_btech_subjects[(fy_btech_subjects['Odd Term'] == True) & (fy_btech_subjects['Division Dependent'] == False)]
# print(odd_and_division_independent_subjects)