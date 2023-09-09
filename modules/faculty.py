import pandas as pd
import subject

class Faculty:
    def __init__(self, name, abb, assigned_subjects=None, theory_load=0, practical_load=0):
        self.name = name
        self.abb = abb
        self.assigned_subjects = assigned_subjects if assigned_subjects is not None else {}
        self.theory_load = theory_load
        self.practical_load = practical_load
        self.total_load = self.calculate_total_load()

    def calculate_total_load(self):
        return self.theory_load + self.practical_load

    def add_subject(self, subject):
        self.assigned_subjects.append(subject)

    def to_dict(self):
        return {
            "Name": self.name,
            "Abbreviation": self.abb,
            "Assigned Subjects": self.assigned_subjects,
            "Theory Load": self.theory_load,
            "Practical Load": self.practical_load,
            "Total Load": self.total_load
        }
    
    def __str__(self):
        return f"Name: {self.name}\nAbbreviation: {self.abb}\nassigned_Subjects: {', '.join(self.assigned_subjects)}\nTheory Load: {self.theory_load}\nPractical Load: {self.practical_load}\nTotal Load: {self.total_load}"

# Create objects for faculties based on the provided information
faculties = [
    Faculty("Dr. P.G. Musrif", "PGM", assigned_subjects=["Engineering Physics", "Universal Human Values-I"]),
    Faculty("Mr. S.V. Arlikar", "SVA", assigned_subjects=["Engineering Physics", "Universal Human Values-I"]),
    Faculty("Dr. Manisha Raghuvanshi", "MR", assigned_subjects=["Engineering Physics", "Universal Human Values-I"]),
    Faculty("Dr. Y.P.Patil", "YPP", assigned_subjects=["Industrial Chemistry"]),
    Faculty("Dr. Nidhi Sharma", "NS", assigned_subjects=["Industrial Chemistry"]),
    Faculty("Mr. P.G.Mahajan", "PGM", assigned_subjects=["Industrial Chemistry"]),
    Faculty("Mrs. G.N.Mawale", "GNM", assigned_subjects=["Engineering Mechanics"]),
    Faculty("Mrs. A.A. Athawale", "AAA", assigned_subjects=["Engineering Mechanics"]),
    Faculty("Mr. A.H.Raheja", "AHR", assigned_subjects=["Engineering Mechanics"]),
    Faculty("Mr. V. D. Deshmukh", "VDD", assigned_subjects=["Engineering Mechanics"]),
    Faculty("Mr. R. B. Tope", "RBT", assigned_subjects=["Engineering Mathematics I", "Applied Mathematics (ENTC)"]),
    Faculty("Mr. N. A. Shaikh", "NAS", assigned_subjects=["Engineering Mathematics I", "Discrete Mathematics and Statistics (AIDS)"]),
    Faculty("Mr. P.S. Gaur", "PSG", assigned_subjects=["Engineering Mathematics I"]),
    Faculty("Mr. P. B. Shinde", "PBS", assigned_subjects=["Engineering Mathematics I"]),
    Faculty("Mr. D.S.Shelar", "DSS", assigned_subjects=["Engineering Mathematics I"]),
    Faculty("Ms. S. S. Raskar", "SSR", assigned_subjects=["Engineering Mathematics I"]),
    Faculty("Mr. M.B.Nigade", "MBN", assigned_subjects=["Engineering Graphics and introduction to CAD", "Project Based Learning Management I", "EG- Activity"]),
    Faculty("Mr. A. J. More", "AJM", assigned_subjects=["Engineering Graphics and introduction to CAD", "Project Based Learning Management I", "EG- Activity"]),
    Faculty("Mr. S.S. Gadadhe", "SSG", assigned_subjects=["Engineering Graphics and introduction to CAD", "Project Based Learning Management I", "EG- Activity", "Universal Human Values-I"]),
    Faculty("Mr. N.P.Bhone", "NPB", assigned_subjects=["Engineering Graphics and introduction to CAD", "Project Based Learning Management I", "EG- Activity"]),
    Faculty("Dr.Naseem Khayyum", "NK", assigned_subjects=["Engineering Graphics and introduction to CAD", "Project Based Learning Management I", "EG- Activity"]),
    Faculty("Mr. A.S. Apate", "ASA", assigned_subjects=["Engineering Graphics and introduction to CAD", "Project Based Learning Management I", "EG- Activity", "Universal Human Values-I"]),
    Faculty("Mr. N.D.Gaikwad", "NDG", assigned_subjects=["Engineering Graphics and introduction to CAD", "Project Based Learning Management I", "EG- Activity"]),
    Faculty("Dr. Pritam Saha", "PS", assigned_subjects=["Engineering Graphics and introduction to CAD", "Project Based Learning Management I", "EG- Activity"]),
    Faculty("Mr. P.A. Patil", "PAP", assigned_subjects=["Basic Electronics Engineering"]),
    Faculty("Mr. C. K,Bhange", "CKB", assigned_subjects=["Basic Electronics Engineering"]),
    Faculty("Mrs. Supriya Lohar", "SL", assigned_subjects=["Basic Electronics Engineering"]),
    Faculty("Mr. P.P.Mahajan", "PPM", assigned_subjects=["Basic Electrical Engineering"]),
    Faculty("Mrs.S.M.Shaikh", "SMS", assigned_subjects=["Basic Electrical Engineering"]),
    Faculty("Mrs.P.P.Mane", "PPM", assigned_subjects=["Basic Electrical Engineering"]),
    Faculty("Mr. P.B.Wakhare", "PBW", assigned_subjects=["Problem Solving and Programming-I"]),
    Faculty("Mrs. P.M. Patil", "PMP", assigned_subjects=["Problem Solving and Programming-I"]),
    Faculty("Ms. S. K. More", "SKM", assigned_subjects=["Problem Solving and Programming-I"]),
    Faculty("Ms. R. R. Owhal", "RRO", assigned_subjects=["Problem Solving and Programming-I"]),
    Faculty("Mrs. D. S. Moarey", "DSM", assigned_subjects=["Sports 1"]),
]

faculty_dicts = [faculty.to_dict() for faculty in faculties]

# Create a DataFrame from the list of dictionaries
df = pd.DataFrame(faculty_dicts)

print(df)