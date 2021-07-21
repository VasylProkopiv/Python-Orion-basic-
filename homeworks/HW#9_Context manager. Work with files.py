file = open(r'files_contextmanagers_hw/files_contextmanagers/task1.txt', 'r')
data = file.read()
print(file.read())
file.close()

file = open(r'new_task1.txt', 'w')
file.write(data)
file.close()