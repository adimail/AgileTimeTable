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
        self.time_slots = ['A1', 'A2', 'B1', 'B2', 'C1', 'C2', 'C3']
        self.timetable = np.empty((len(self.days), (len(self.time_slots))), dtype=object)

    def assign_lecture(self, row, col, lecture):
        self.timetable[row, col] = lecture['Abbreviation']

    def assign_lecture_randomly(self, lecture):
        if lecture['Abbreviation'] == 'PE':
            empty_cells = [(i, 6) for i in range(5) if self.timetable[i, 6] is None]
        else:
            empty_cells = [(i, j) for i in range(len(self.days)) for j in range(len(self.time_slots)-1) if self.timetable[i, j] is None]

        if empty_cells:
            random_cell = random.choice(empty_cells)
            self.timetable[random_cell[0], random_cell[1]] = lecture['Abbreviation']
            # print(empty_cells)

    def print_timetable(self):
        # Iterate over rows and columns to print only the subject name
        for i, day in enumerate(self.days):
            for j, time_slot in enumerate(self.time_slots):
                lecture = self.timetable[i, j]
                if lecture is not None and 'subject' in lecture:
                    print(f"{day}-{time_slot}: {lecture['subject']}")

    def create_dataframe(self):
        data = self.timetable
        timetable_df = pd.DataFrame(data, index=self.days, columns=self.time_slots)
        return timetable_df

    def export_to_excel(self, filename_prefix="timetable"):
        current_datetime = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"{filename_prefix}_{current_datetime}.xlsx"
        timetable_df = self.create_dataframe()
        timetable_df.to_excel(filename)

def extract_columns(dataframe):
    result_list = []

    for _, row in dataframe.iterrows():
        name = row['Name']
        abbreviation = row['Abbreviation']
        hours = row['Theory hours']
        
        # Extend the result list with the lecture abbreviation repeated according to its assigned hours
        result_list.extend([{'Name': name, 'Abbreviation': abbreviation}] * hours)

    return result_list

divE_semI_theory = TimetableLoader_fe()

theory_lectures = extract_columns(subject.sem1_computer_theory)

random.shuffle(theory_lectures)

for lecture in theory_lectures:
    divE_semI_theory.assign_lecture_randomly(lecture)

timetable = divE_semI_theory.create_dataframe()
timetable = timetable.fillna("--")
print(timetable)

# for i, lecture in enumerate(theory_lectures):
#     row_index = i // len(divE_semI_theory.time_slots)
#     col_index = i % len(divE_semI_theory.time_slots)
#     divE_semI_theory.assign_lecture(row_index, col_index, lecture)

# timetable = divE_semI_theory.create_dataframe()
# print(timetable)


# for item in result_list:
#     print(item['Abbreviation'])

# odd_cells = [(0, 0), (0, 2), (0, 4)]
# random_cell = (0, 0)

# if random_cell in odd_cells:
#     print("Exists")

# print(subject.sem1_computer_practical)