import pandas as pd

class Subject:
    def __init__(self, name, abb, division_dependent, even_term, odd_term, flag = 0):
        self.name = name
        self.abb = abb
        self.division_dependent = division_dependent
        self.even_term = even_term
        self.odd_term = odd_term
        self.flag = flag

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

class theory(Subject):
    def __init__(self, name, abb, division_dependent, even_term, odd_term, length=1, flag=9, has_practical=True):
        self.name = name
        self.abb = abb
        self.division_dependent = division_dependent
        self.even_term = even_term
        self.odd_term = odd_term
        self.length = length
        self.flag = flag
        self.has_practical = has_practical


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


theory_subs = [
    theory("Engineering Mathematics - I", "EM-I", False, False, True),
    theory("Engineering Mathematics - II", "EM-II", False, True, False),
    theory("Industrial Chemistry", "CHEM", True, True, True, flag=1),
    theory("Engineering Physics", "PHY", True, True, True, flag=0),
    theory("Engineering Graphics and Introduction to Cad", "EG", False, False, True),
    theory("Environmental Informatics", "EI", False, True, False),
    theory("Basic Electronics Engineering", "BXE", True, True, True, flag=1),
    theory("Basic Electrical Engineering", "BEE", True, True, True, flag=0),
    theory("Engineering Mechanics", "EM", False, False, True),
    theory("Basics In Mechanical Engineering", "BME", False, True, False),
    theory("Project Based Learning and Management - I", "PBLM-I", False, False, True),  
    theory("Project Based Learning and Management - II", "PBLM-II", False, True, False),  
    theory("Problem Solving and Programming - I", "PSP-I", False, False, True),
    theory("Problem Solving and Programming - II", "PSP-II", False, True, False),
    theory("Universal Human Values - I", "UHV-I", False, False, True, has_practical=False),  
    theory("Universal Human Values - II", "UHV-II", False, True, False, has_practical=False),
    theory("Physical Education", "PE", False, True, True, has_practical=False)
]

practical_subs = [
    subject for subject in theory_subs if subject.has_practical
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