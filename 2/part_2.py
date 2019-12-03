import copy

with open("input.txt", "rb") as fh:
    data = [int(op) for op in fh.read().split(",")]

ADD = 1
MULTIPLIES = 2
EOF = 99


def do_op(data):
    for count, (op, first, second, dest) in enumerate(zip(data[::4], data[1::4], data[2::4], data[3::4])):
        if op == ADD:
            data[dest] = data[first] + data[second]
        elif op == MULTIPLIES:
            data[dest] = data[first] * data[second]
        elif op == EOF:
            break
        else:
            print("Unknown OP: {}".format(op))

    print("Ran {} instructions. [{}, {}, {}, {}]]".format(count+1, op, first, second, dest))
    print(data[0])
    return data

key_x = None
key_y = None
for x in range(100):
    data[1] = x
    for y in range(100):
        data[2] = y
        run_data = copy.copy(data)
        do_op(run_data)
        if run_data[0] == 19690720:
            print("data[1] = {}   data[2] = {}".format(x, y))
            key_x = x
            key_y = y
            break
    if key_x is not None and key_y is not None:
        break

if key_x and key_y:
    print(100 * key_x + key_y)
