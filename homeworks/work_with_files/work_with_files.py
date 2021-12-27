import pickle
import statistics
import openpyxl

# Task 3
print('\ntask_1')

d_sub = {}
with open('task1.txt', 'r') as file:
    for line in file:
        key = line.strip()
        value = file.readline().strip()
        d_sub[key] = value
print(d_sub)

with open(r'new_task1.txt', 'w') as new_file:
    for value in d_sub.values():
        new_file.write(value)

# Task 3
print('\ntask_2')

with open("task2", "rb") as file:
    average = pickle.load(file)
print(statistics.mean(average))

# Task 3
print('\ntask_3')


class My_manager:
    def __init__(self, path):
        self.path = path
        self.file = openpyxl.load_workbook(path)

    def __enter__(self):
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            self.file.save(self.path)
            self.file.close()
        else:
            print("Something gone wrong!")
            self.file.close()
            return True


with My_manager("task_3_file.xlsx") as file:
    active_sheet = file.active
    text = active_sheet.cell(row=1, column=1)
    print(active_sheet["A1"].value)
    text.value = 'task_3'
    raise Exception