def read_data(filename):
    arr = []

    with open(filename+'.txt') as file:
        for line in file:
            name = line.split(sep=' ')[0]
            surename = line.split(sep=' ')[1]
            year = int(line.split(sep=' ')[2])
            accuracy = float(line.split(sep=' ')[3])
            arr.append((name, surename, year, accuracy))
    return arr       


def write_data(filename, arr):
    with open(filename+'.max', 'w') as file:
        for data in arr:
            file.write(f'{anonymization(data[0])} {anonymization(data[1])} {data[2]}\n')


def anonymization(text):
    new_text = text[0] + '*'*(len(text)-4) + text[-3:]
    return new_text


def check(candidate):
    if(len(candidate[0])>3 and len(candidate[1])>=3 and candidate[1][-3:] == 'ski'):
        return 1
    return 0


filename = input()
table = read_data(filename)

output__table = []
curr_leader = ('', '', '', -1)

for candidate in table:
    if (check(candidate) and candidate[3] > curr_leader[3]):
        curr_leader = candidate
        output__table = []
        output__table.append(curr_leader)
    elif (check(candidate) and candidate[3] == curr_leader[3]):
        curr_leader = candidate
        output__table.append(curr_leader)



write_data(filename, output__table)