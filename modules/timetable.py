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
        practical_cells = [(i, j) for i in range(0, 5) for j in range(0, 6, 2) if self.timetable[i, j] is None]
        if lecture['Course type'] == 'Theory':
            if lecture['Abbreviation'] == 'PE':
                empty_cells = [(i, 6) for i in range(5) if self.timetable[i, 6] is None]
            else:
                empty_cells = [(i, j) for i in range(len(self.days)) for j in range(len(self.time_slots)-1) if self.timetable[i, j] is None]

            if empty_cells:
                random_cell = random.choice(empty_cells)
                self.timetable[random_cell[0], random_cell[1]] = lecture['Abbreviation']
            # print(empty_cells)

        if lecture['Course type'] == 'Practical':
            if practical_cells:
                random_cell = random.choice(practical_cells)
                self.timetable[random_cell[0], random_cell[1]] = lecture['Abbreviation']
                self.timetable[random_cell[0], random_cell[1]+1] = lecture['Abbreviation']

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
        practical_hours = row['Practical hours (per batch)']
        course_type = row['Course type']
        # Extend the result list with the lecture abbreviation repeated according to its assigned hours
        if(course_type=='Theory'):
            result_list.extend([{'Name': name, 'Abbreviation': abbreviation, 'Course type': course_type}] * hours)
        else:
            result_list.extend([{'Name': name, 'Abbreviation': abbreviation, 'Course type': course_type}])
    return result_list

def generate_tt(sem=1, is_theory=1, is_comp=1):
    df = TimetableLoader_fe()
    if(sem==1):
        if(is_comp):    
            if(is_theory):
                lectures = extract_columns(subject.sem1_computer_theory)
            else:
                lectures = extract_columns(subject.sem1_computer_practical)
        else:
            if(is_theory):
                lectures = extract_columns(subject.sem1_non_computer_theory)
            else:
                lectures = extract_columns(subject.sem1_non_computer_theory)
    else:
        if(is_comp):    
            if(is_theory):
                lectures = extract_columns(subject.sem2_computer_theory)
            else:
                lectures = extract_columns(subject.sem2_computer_practical)
        else:
            if(is_theory):
                lectures = extract_columns(subject.sem2_non_computer_theory)
            else:
                lectures = extract_columns(subject.sem2_non_computer_theory)

    random.shuffle(lectures)

    for period in lectures:
        df.assign_lecture_randomly(period)

    timetable = df.create_dataframe()
    timetable = timetable.fillna("--")

    return timetable


def genrate_timetable_for_division(sem=1, is_comp=1):
    df = TimetableLoader_fe()
    if(sem==1):
        if(is_comp):    
            lectures = extract_columns(subject.sem1_computer_theory)
        else:
            lectures = extract_columns(subject.sem1_non_computer_theory)
    else:
        if(is_comp):    
            lectures = extract_columns(subject.sem2_computer_theory)
        else:
            lectures = extract_columns(subject.sem2_non_computer_theory)
    random.shuffle(lectures)

    for period in lectures:
        df.assign_lecture_randomly(period)

    if(sem==1):
        if(is_comp):    
            lectures = extract_columns(subject.sem1_computer_practical)
        else:
            lectures = extract_columns(subject.sem1_non_computer_practical)
    else:
        if(is_comp):    
            lectures = extract_columns(subject.sem2_computer_practical)
        else:
            lectures = extract_columns(subject.sem2_non_computer_practical)
    random.shuffle(lectures)

    for period in lectures:
        df.assign_lecture_randomly(period)

    timetable = df.create_dataframe()
    timetable = timetable.fillna("--")

    return timetable


# divE_semII_practical = generate_tt(sem=2,is_theory=0,is_comp=1)
# print(divE_semII_practical)

# divE_semII_theory = generate_tt(sem=2,is_theory=1,is_comp=1)
# print(divE_semII_theory)

# divE_semII = genrate_timetable_for_division(2,1)
# print(divE_semII)