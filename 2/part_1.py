with open("input.txt", "rb") as fh:
    data = [int(op) for op in fh.read().split(",")]

ADD = 1
MULTIPLIES = 2
EOF = 99

data[1] = 12
data[2] = 2

for op, first, second, dest in zip(data[::4], data[1::4], data[2::4], data[3::4]):
    if op == ADD:
        data[dest] = data[first] + data[second]
    elif op == MULTIPLIES:
        data[dest] = data[first] * data[second]
    elif op == EOF:
        break
    else:
        print("Unknown OP: {}".format(op))

print(data[0])
