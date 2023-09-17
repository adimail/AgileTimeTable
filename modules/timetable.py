from collections import Counter
from itertools import groupby
import numpy as np
import datetime
import pandas as pd
import random
import subject
from faculty import fy_btech_faculty
from division import fy_btech_divisions

class TimetableLoader_fe:
    def __init__(self, term="even", division="non-IT"):
        # Create an empty NumPy array to represent the timetable
        self.term = term
        self.division = division
        self.days = ['mon', 'tue', 'wed', 'thu', 'fri']
        self.time_slots = ['  8:15-9:15  ', '  9:15-10:15  ', '  10:30-11:30  ', '  11:30-12:30  ', '  1:15-2:15  ', '  2:15-3:15  ', '  3:15-4:15  ']
        self.timetable = np.empty((len(self.days), (len(self.time_slots))), dtype=object)

    def assign_lecture(self, row, col, lecture):
        self.timetable[row, col] = lecture['Abbreviation']

    def assign_lecture_randomly(self, lecture):
        practical_cells = [(i, j) for i in range(0, 5) for j in range(0, 6, 2) if self.timetable[i, j] is None]
        
        # practical_cells = [cell for key, group in groupby(sorted(practical_cells), key=lambda x: x[0]) for cell in random.sample(list(group), min(2, len(list(group))))][:7]


        if lecture['Course type'] == 'Theory':
            if lecture['Abbreviation'] == 'PE':
                empty_cells = [(i, 6) for i in range(5) if self.timetable[i, 6] is None]
            else:
                empty_cells = [(i, j) for i in range(len(self.days)) for j in range(len(self.time_slots) - 1) if self.timetable[i, j] is None]

            if empty_cells:
                # Filter out empty cells where a theory lecture with the same abbreviation is not already present in the row.
                empty_cells = [(i, j) for i, j in empty_cells if all(self.timetable[i, k] != lecture['Abbreviation'] for k in range(len(self.time_slots)))]

                if empty_cells:
                    random_cell = random.choice(empty_cells)
                    self.timetable[random_cell[0], random_cell[1]] = lecture['Abbreviation']
                    return True  # Successfully assigned a theory lecture

        elif lecture['Course type'] == 'Practical':
            if practical_cells:
                random_cell = random.choice(practical_cells)
                self.timetable[random_cell[0], random_cell[1]] = lecture['Abbreviation']
                self.timetable[random_cell[0], random_cell[1] + 1] = lecture['Abbreviation']
                return True  # Successfully assigned a practical lecture

        return False  # No assignment was made


    def create_dataframe(self):
        data = self.timetable
        timetable_df = pd.DataFrame(data, index=self.days, columns=self.time_slots)
        return timetable_df

    def export_to_excel(self, filename_prefix="timetable"):
        current_datetime = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"{filename_prefix}_{current_datetime}.xlsx"
        timetable_df = self.create_dataframe()
        timetable_df.to_excel(filename)

    def generate_complete_timetable(self, sem=1, is_theory=1, is_comp=1):
        if sem == 1:
            if is_comp:
                practical_lectures = extract_columns(subject.sem1_computer_practical)
                lectures = extract_columns(subject.sem1_computer_theory)
            else:
                practical_lectures = extract_columns(subject.sem1_non_computer_practical)
                lectures = extract_columns(subject.sem1_non_computer_theory)
        else:
            if is_comp:
                practical_lectures = extract_columns(subject.sem2_computer_practical)
                lectures = extract_columns(subject.sem2_computer_theory)
            else:
                practical_lectures = extract_columns(subject.sem2_non_computer_practical)
                lectures = extract_columns(subject.sem2_non_computer_theory)

        random.shuffle(practical_lectures)
        for period in practical_lectures:
            self.assign_lecture_randomly(period)
        
        for period in list(lectures):  # Create a copy of 'lectures' to avoid modifying it during iteration
            if self.assign_lecture_randomly(period):
                lectures.remove(period)

        print(type(lectures))
        timetable = self.create_dataframe()
        timetable = timetable.fillna("--")

        return timetable

def extract_columns(dataframe):
    list = []

    for _, row in dataframe.iterrows():
        name = row['Name']
        abbreviation = row['Abbreviation']
        hours = row['Theory hours']
        practical_hours = row['Practical hours (per batch)']
        course_type = row['Course type']
        
        if(course_type=='Theory'):
            list.extend([{'Name': name, 'Abbreviation': abbreviation, 'Course type': course_type}] * hours)
        else:
            list.extend([{'Name': name, 'Abbreviation': abbreviation, 'Course type': course_type}] * int(practical_hours/2))
    
    return list


#####################################################################################
#####################################################################################

div_e = TimetableLoader_fe()

complete_timetable = div_e.generate_complete_timetable(sem=1, is_theory=1, is_comp=1)
print(complete_timetable)








######
#This code snippet calculates the number of unique lectures and practicals in timetable
flat_values = complete_timetable.values.flatten()
pr_values_counts = {}
other_values_counts = {}

for value in flat_values:
    if "(pr)" in value and value != "--":
        if value in pr_values_counts:
            pr_values_counts[value] += 1
        else:
            pr_values_counts[value] = 1
    elif "(pr)" not in value and value != "--":
        if value in other_values_counts:
            other_values_counts[value] += 1
        else:
            other_values_counts[value] = 1

pr_values_counts = {key: value // 2 for key, value in pr_values_counts.items()}

print("\nPracticals")
for value, count in pr_values_counts.items():
    print(f"Value: {value}, Count: {count}")

print("\nTheory")
for value, count in other_values_counts.items():
    print(f"Value: {value}, Count: {count}")