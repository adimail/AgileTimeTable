import pandas as pd

class Subject:
    def __init__(self, name, abb, theory_hours=1, practical_hours=2, division_dependent=0, even_term=0, odd_term=0, flag=9, has_practical=True, has_theory=True):
        self.name = name
        self.abb = abb
        self.theory_hours = theory_hours
        self.practical_hours = practical_hours
        self.division_dependent = division_dependent
        self.even_term = even_term
        self.odd_term = odd_term
        self.flag = flag
        self.has_practical = has_practical
        self.has_theory = has_theory

    def to_dict(self):
        return {
            "Name": self.name,
            "Abbreviation": self.abb,
            "Theory hours":self.theory_hours,
            "Practical hours (per batch)": self.practical_hours,
            "Division Dependent": self.division_dependent,
            "Even Term": self.even_term,
            "Odd Term": self.odd_term,
            "Flag": self.flag
        }


def split_classes(dataframe, is_odd_term=False, is_core=0, pr_suffix=False):
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
    if(pr_suffix):
        df.loc[:, 'Abbreviation'] = df['Abbreviation'].apply(lambda x: x + "(pr)")
    return df

subjects = [
    Subject("Engineering Mathematics - I", "EM-I",3,2, False, False, True),
    Subject("Engineering Mathematics - II", "EM-II",3,2, False, True, False),
    Subject("Industrial Chemistry", "CHEM",3,2, True, True, True, flag=1),
    Subject("Engineering Physics", "PHY",3,2, True, True, True, flag=0),
    Subject("Engineering Graphics and Introduction to Cad", "EG",2,2, False, False, True),
    Subject("Environmental Informatics", "EI",1,2, False, True, False),
    Subject("Basic Electronics Engineering", "BXE",3,2, True, True, True, flag=1),
    Subject("Basic Electrical Engineering", "BEE",3,2, True, True, True, flag=0),
    Subject("Engineering Mechanics", "EM",2,2, False, False, True),
    Subject("Basics In Mechanical Engineering", "BME",2,2, False, True, False),
    Subject("Project Based Learning and Management - I", "PBLM-I",0,2, False, False, True, has_theory=False),  
    Subject("Project Based Learning and Management - II", "PBLM-II",0,2, False, True, False, has_theory=False),  
    Subject("Problem Solving and Programming - I", "PSP-I",2,2, False, False, True),
    Subject("Problem Solving and Programming - II", "PSP-II",2,2, False, True, False),
    Subject("Universal Human Values - I", "UHV-I",1,0, False, False, True, has_practical=False),  
    Subject("Universal Human Values - II", "UHV-II",1,0, False, True, False, has_practical=False),
    Subject("Physical Education", "PE",1,0, False, True, True, has_practical=False)
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

sem1_computer_practical = split_classes(fy_btech_practicals,1,0,1)
sem1_non_computer_practical = split_classes(fy_btech_practicals,1,1,1)
sem2_computer_practical = split_classes(fy_btech_practicals,0,0,1)
sem2_non_computer_practical = split_classes(fy_btech_practicals,0,1,1)

# print(sem2_computer_practical)