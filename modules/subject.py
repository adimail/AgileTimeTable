import pandas as pd

class Subject:
    def __init__(self, name, abb, division_dependent, even_term, odd_term, length=1, flag=9, has_practical=True, has_theory=True):
        self.name = name
        self.abb = abb
        self.division_dependent = division_dependent
        self.even_term = even_term
        self.odd_term = odd_term
        self.length = length
        self.flag = flag
        self.has_practical = has_practical
        self.has_theory = has_theory

    def to_dict(self):
        return {
            "Name": self.name,
            "Abbreviation": self.abb,
            "Division Dependent": self.division_dependent,
            "Even Term": self.even_term,
            "Odd Term": self.odd_term,
            "Length": self.length,
            "Flag": self.flag
        }


def split_classes(dataframe, is_odd_term=False, is_core=0):
    if(is_core ):
        if(is_odd_term):
            flag = 0
        else:
            flag = 1
    else:
        if(is_odd_term):
            flag = 1
        else:
            flag = 0

    df = pd.DataFrame()
    df = dataframe[((dataframe['Odd Term'] == is_odd_term) & (dataframe['Division Dependent'] == 0)) | ((dataframe['Division Dependent'] == 1) & (dataframe['Flag'] == flag))]
    df.reset_index(drop=True, inplace=True)
    df.index += 1
    
    return df

subjects = [
    Subject("Engineering Mathematics - I", "EM-I", False, False, True),
    Subject("Engineering Mathematics - II", "EM-II", False, True, False),
    Subject("Industrial Chemistry", "CHEM", True, True, True, flag=1),
    Subject("Engineering Physics", "PHY", True, True, True, flag=0),
    Subject("Engineering Graphics and Introduction to Cad", "EG", False, False, True),
    Subject("Environmental Informatics", "EI", False, True, False),
    Subject("Basic Electronics Engineering", "BXE", True, True, True, flag=1),
    Subject("Basic Electrical Engineering", "BEE", True, True, True, flag=0),
    Subject("Engineering Mechanics", "EM", False, False, True),
    Subject("Basics In Mechanical Engineering", "BME", False, True, False),
    Subject("Project Based Learning and Management - I", "PBLM-I", False, False, True, has_theory=False),  
    Subject("Project Based Learning and Management - II", "PBLM-II", False, True, False, has_theory=False),  
    Subject("Problem Solving and Programming - I", "PSP-I", False, False, True),
    Subject("Problem Solving and Programming - II", "PSP-II", False, True, False),
    Subject("Universal Human Values - I", "UHV-I", False, False, True, has_practical=False),  
    Subject("Universal Human Values - II", "UHV-II", False, True, False, has_practical=False),
    Subject("Physical Education", "PE", False, True, True, has_practical=False)
]

theory_subs = [
    subject for subject in subjects if subject.has_theory
]

practical_subs = [
    subject for subject in subjects if subject.has_practical
]

theory_subject_dicts = [subject.to_dict() for subject in theory_subs]
fy_btech_theory = pd.DataFrame(theory_subject_dicts)
fy_btech_theory['Course type'] = "Theory"

practical_subject_dicts = [subject.to_dict() for subject in practical_subs]
fy_btech_practicals = pd.DataFrame(practical_subject_dicts)
fy_btech_practicals['Course type'] = "Practical"

sem1_computer_theory = split_classes(fy_btech_theory, 1,0)
sem1_non_computer_theory = split_classes(fy_btech_theory, 1,1)
sem2_computer_theory = split_classes(fy_btech_theory, 0,0)
sem2_non_computer_theory = split_classes(fy_btech_theory, 0, 1)

sem1_computer_practical = split_classes(fy_btech_practicals,1,0)    
sem1_non_computer_practical = split_classes(fy_btech_practicals,1,1)
sem2_computer_practical = split_classes(fy_btech_practicals,0,0)
sem2_non_computer_practical = split_classes(fy_btech_practicals,0,1)