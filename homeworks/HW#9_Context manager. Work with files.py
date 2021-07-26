import re


def reader(filename):
    regexp = r'\d{1,2}\:\d{1,2}'

    with open(filename) as f:
        timer = f.read()
        time_list = re.findall(regex, time)
    if __name__ == '__main__':
        reader(files_contextmanagers_hw/files_contextmanagers/task1.txt)

# print(timer)


# time_list = re.findall(regexp, file)
# data = file.read()
# print(re.data)

# file.close()

#
# file = open(r'new_task1.txt', 'w')
# file.write(data)
# file.close()
