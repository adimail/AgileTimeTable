class Division:
    def __init__(self, name, subjects):
        self.name = name
        self.subjects = subjects
        self.timetable = {}  # Initialize an empty timetable for this division

    def change_subject(self, subject_index, new_subject):
        if 0 <= subject_index < len(self.subjects):
            self.subjects[subject_index] = new_subject
        else:
            print("Invalid subject index.")

    # def get_timetable(self):
    #     """
    #     Get the timetable for this division.
    #     """
    #     return self.timetable

    def __str__(self):
        return f"Division: {self.name}\nSubjects: {', '.join(self.subjects)}"