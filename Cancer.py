cars = ["1", "2", "3"]

with open('message.txt', 'r') as document:
    answer = {}
    for line in document:
        line = line.split()
        if not line:  # empty line?
            continue
        answer[line] = line[1:]
print(answer)



