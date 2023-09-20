import tkinter as tk
from tkinter import ttk
import pandas as pd

# Define the Subject class
class Subject:
    def __init__(self, name, abb, division_dependent, even_term, odd_term, theory_hours, practical_hours):
        self.name = name
        self.abb = abb
        self.division_dependent = division_dependent
        self.even_term = even_term
        self.odd_term = odd_term
        self.theory_hours = theory_hours
        self.practical_hours = practical_hours
        self.total_load = self.theory_hours + self.practical_hours

    def to_dict(self):
        return {
            "Name": self.name,
            "Abbreviation": self.abb,
            "Division Dependent": self.division_dependent,
            "Even Term": self.even_term,
            "Odd Term": self.odd_term,
            "Theory Hours": self.theory_hours,
            "Practical Hours": self.practical_hours,
            "Total Load": self.total_load
        }

# Create different objects for each subject
subjects = [
    Subject("Engineering Mathematics - I", "EM-I", False, False, True, 3, 6),
    Subject("Engineering Mathematics - II", "EM-II", False, True, False, 3, 6),
    Subject("Industrial Chemistry", "CHEM", True, True, True, 3, 6),
    Subject("Engineering Physics", "PHY", True, True, True, 3, 6),
    Subject("Engineering Graphics and Introduction to Cad", "EG", False, False, True, 1, 6),
    Subject("Environmental Informatics", "EI", False, True, False, 1, 6),
    Subject("Basic Electronics Engineering", "BXE", True, True, True, 3, 6),
    Subject("Basic Electrical Engineering", "BEE", True, True, True, 3, 6),
    Subject("Engineering Mechanics", "EM", False, False, True, 2, 6),
    Subject("Basics In Mechanical Engineering", "BME", False, True, False, 2, 6),
    Subject("Project Based Learning and Management - I", "PBLM-I", False, False, True, 0, 6),  # Assuming empty values
    Subject("Project Based Learning and Management - II", "PBLM-II", False, True, False, 0, 6),  # Assuming empty values
    Subject("Problem Solving and Programming - I", "PSP-I", False, False, True, 2, 6),
    Subject("Problem Solving and Programming - II", "PSP-II", False, True, False, 2, 6),
    Subject("Universal Human Values - I", "UHV-I", False, False, True, 1, 0),  # Assuming empty values for practical
    Subject("Universal Human Values - II", "UHV-II", False, True, False, 1, 0),  # Assuming empty values for practical
    Subject("Physical Education", "PE", False, True, True, 1, 0),  # Assuming empty values for practical
]

# Convert the list of Subject objects to a list of dictionaries
subject_dicts = [subject.to_dict() for subject in subjects]

# Create a DataFrame from the list of dictionaries
df = pd.DataFrame(subject_dicts)

# Function to update the selected subject by abbreviation
def update_subject_by_abbreviation():
    abbreviation = abb_entry.get()
    new_theory_hours = int(theory_hours_entry.get())
    new_practical_hours = int(practical_hours_entry.get())

    # Find the subject by abbreviation
    subject_index = df[df['Abbreviation'] == abbreviation].index
    if not subject_index.empty:
        subject_index = subject_index[0]
        # Update the DataFrame with the new theory and practical hours
        df.at[subject_index, "Theory Hours"] = new_theory_hours
        df.at[subject_index, "Practical Hours"] = new_practical_hours
        df.at[subject_index, "Total Load"] = new_theory_hours + new_practical_hours

        # Update the tree view with the new values
        tree.item(str(subject_index + 1), values=(
            df.at[subject_index, "Name"],
            df.at[subject_index, "Abbreviation"],
            df.at[subject_index, "Division Dependent"],
            df.at[subject_index, "Even Term"],
            df.at[subject_index, "Odd Term"],
            new_theory_hours,
            new_practical_hours,
        ))

# Create the main window
root = tk.Tk()
root.title("Subject Properties")

# Create a Treeview widget to display subjects
tree = ttk.Treeview(root, columns=("Name", "Abbreviation", "Division Dependent", "Even Term", "Odd Term", "Theory Hours", "Practical Hours"), show="headings")
tree.heading("Name", text="Name")
tree.heading("Abbreviation", text="Abbreviation")
tree.heading("Division Dependent", text="Division Dependent")
tree.heading("Even Term", text="Even Term")
tree.heading("Odd Term", text="Odd Term")
tree.heading("Theory Hours", text="Theory Hours")
tree.heading("Practical Hours", text="Practical Hours")
tree.pack()

# Insert subject data into the tree view
for index, row in df.iterrows():
    tree.insert("", "end", values=(row["Name"], row["Abbreviation"], row["Division Dependent"], row["Even Term"], row["Odd Term"], row["Theory Hours"], row["Practical Hours"]))

# Create labels and entry fields for editing subject properties by abbreviation
selected_subject_label = tk.Label(root, text="Update Subject by Abbreviation:")
selected_subject_label.pack()

abb_label = tk.Label(root, text="Abbreviation:")
abb_label.pack()
abb_entry = tk.Entry(root)
abb_entry.pack()

theory_hours_label = tk.Label(root, text="New Theory Hours:")
theory_hours_label.pack()
theory_hours_entry = tk.Entry(root)
theory_hours_entry.pack()

practical_hours_label = tk.Label(root, text="New Practical Hours:")
practical_hours_label.pack()
practical_hours_entry = tk.Entry(root)
practical_hours_entry.pack()

update_button = tk.Button(root, text="Update Subject", command=update_subject_by_abbreviation)
update_button.pack()

# Main loop
root.mainloop()
