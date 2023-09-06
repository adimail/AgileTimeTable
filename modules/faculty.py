class FacultyProfile:
    def __init__(self, name, abbreviation, subjects_taught=None, divisions_assigned=None):
        self.name = name
        self.abbreviation = abbreviation
        self.subjects_taught = subjects_taught if subjects_taught is not None else []
        self.divisions_assigned = divisions_assigned if divisions_assigned is not None else []

    def add_subject(self, subject):
        """Add a subject to the list of subjects taught by the faculty."""
        self.subjects_taught.append(subject)

    def add_division(self, division):
        """Add a division to the list of divisions assigned to the faculty."""
        self.divisions_assigned.append(division)

    def __str__(self):
        """String representation of the faculty profile."""
        return f"Name: {self.name}\nAbbreviation: {self.abbreviation}\nSubjects Taught: {', '.join(self.subjects_taught)}\nDivisions Assigned: {', '.join(self.divisions_assigned)}"

pbw = FacultyProfile("Mr.P.B.Wakhare", "PBW")
pbw.add_subject("PSP-I")
pbw.add_subject("PSP-II")
pbw.add_division("A")
pbw.add_division("E")
print(pbw)
