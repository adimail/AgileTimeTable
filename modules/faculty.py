import subject
import pandas as pd

class FacultyProfile:
    def __init__(self, name, abbreviation, subjects_assigned=None, divisions_assigned=None, ):
        self.name = name
        self.abbreviation = abbreviation
        self.subjects_assigned = subjects_assigned if subjects_assigned is not None else []
        self.divisions_assigned = divisions_assigned if divisions_assigned is not None else []
        self.theory_load = 0
        self.practical_load = 0

    def add_subject(self, subject):
        """Add a subject to the list of subjects taught by the faculty."""
        self.subjects_assigned.append(subject)

    def add_division(self, division):
        """Add a division to the list of divisions assigned to the faculty."""
        self.divisions_assigned.append(division)

    def set_load_distribution(self, theory_load, practical_load):
        """Set the load distribution for theory and practical sessions."""
        self.theory_load = theory_load
        self.practical_load = practical_load

    def __str__(self):
        """String representation of the faculty profile."""
        return f"Name: {self.name}\nAbbreviation: {self.abbreviation}\nSubjects Taught: {', '.join(self.subjects_assigned)}\nDivisions Assigned: {', '.join(self.divisions_assigned)}\nTheory Load: {self.theory_load} hours\nPractical Load: {self.practical_load} hours"

# Example usage:
pbw = FacultyProfile("Mr. P.B. Wakhare", "PBW")
pbw.add_subject("PSP-I")
pbw.add_subject("PSP-II")
pbw.add_division("A")
pbw.add_division("E")
pbw.set_load_distribution(4, 14)
print(pbw)
