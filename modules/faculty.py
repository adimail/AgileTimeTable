import pandas as pd

class Faculty:
    def __init__(self, name, abb, assigned_subjects = None, theory_load=0, practical_load=0):
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
            "Total subjects": len(self.assigned_subjects),
            "Theory Load": self.theory_load,
            "Practical Load": self.practical_load,
            "Total Load": self.total_load
        }
    
    def __str__(self):
        return f"Name: {self.name}\nAbbreviation: {self.abb}\nassigned_Subjects: {', '.join(self.assigned_subjects)}\nTheory Load: {self.theory_load}\nPractical Load: {self.practical_load}\nTotal Load: {self.total_load}"

# Create objects for faculties based on the provided information
faculties = [
    Faculty("Dr. P.G. Musrif", "PGM", ["PHY", "USV-I"]),
    Faculty("Mr. S.V. Arlikar", "SVA", ["PHY", "USV-I"]),
    Faculty("Dr. Manisha Raghuvanshi", "MR", ["PHY", "USV-I"]),
    Faculty("Dr. Y.P.Patil", "YPP", ["CHEM"]),
    Faculty("Dr. Nidhi Sharma", "NS", ["CHEM"]),
    Faculty("Mr. P.G.Mahajan", "PGM", ["CHEM"]),
    Faculty("Mrs. G.N.Mawale", "GNM", ["EM"]),
    Faculty("Mrs. A.A. Athawale", "AAA", ["EM"]),
    Faculty("Mr. A.H.Raheja", "AHR", ["EM"]),
    Faculty("Mr. V. D. Deshmukh", "VDD", ["EM"]),
    Faculty("Mr. R. B. Tope", "RBT", ["EM-I", "Applied Mathematics (ENTC)"]),
    Faculty("Mr. N. A. Shaikh", "NAS", ["EM-I", "Discrete Mathematics and Statistics (AIDS)"]),
    Faculty("Mr. P.S. Gaur", "PSG", ["EM-I"]),
    Faculty("Mr. P. B. Shinde", "PBS", ["EM-I"]),
    Faculty("Mr. D.S.Shelar", "DSS", ["EM-I"]),
    Faculty("Ms. S. S. Raskar", "SSR", ["EM-I"]),
    Faculty("Mr. M.B.Nigade", "MBN", ["EG", "PBLM-I", "EG- Activity"]),
    Faculty("Mr. A. J. More", "AJM", ["EG", "PBLM-I", "EG- Activity"]),
    Faculty("Mr. S.S. Gadadhe", "SSG", ["EG", "PBLM-I", "EG- Activity", "USV-I"]),
    Faculty("Mr. N.P.Bhone", "NPB", ["EG", "PBLM-I", "EG- Activity"]),
    Faculty("Dr.Naseem Khayyum", "NK", ["EG", "PBLM-I", "EG- Activity"]),
    Faculty("Mr. A.S. Apate", "ASA", ["EG", "PBLM-I", "EG- Activity", "USV-I"]),
    Faculty("Mr. N.D.Gaikwad", "NDG", ["EG", "PBLM-I", "EG- Activity"]),
    Faculty("Dr. Pritam Saha", "PS", ["EG", "PBLM-I", "EG- Activity"]),
    Faculty("Mr. P.A. Patil", "PAP", ["BXE"]),
    Faculty("Mr. C. K,Bhange", "CKB", ["BXE"]),
    Faculty("Mrs. Supriya Lohar", "SL", ["BXE"]),
    Faculty("Mr. P.P.Mahajan", "PPM", ["BEE"]),
    Faculty("Mrs.S.M.Shaikh", "SMS", ["BEE"]),
    Faculty("Mrs.P.P.Mane", "PPM", ["BEE"]),
    Faculty("Mr. P.B.Wakhare", "PBW", ["PSP-I"]),
    Faculty("Mrs. P.M. Patil", "PMP", ["PSP-I"]),
    Faculty("Ms. S. K. More", "SKM", ["PSP-I"]),
    Faculty("Ms. R. R. Owhal", "RRO", ["PSP-I"]),
    Faculty("Mrs. D. S. Moarey", "DSM", ["PE"]),
]

faculty_dicts = [faculty.to_dict() for faculty in faculties]

# Create a DataFrame from the list of dictionaries
fy_btech_faculty = pd.DataFrame(faculty_dicts)

# print(fy_btech_faculty)