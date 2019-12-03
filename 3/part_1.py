from itertools import combinations
import weakref


class _PositionProxy(object):
    def __init__(self):
        super(_PositionProxy, self).__init__()
        self._previous = None
        self._next = None
        self._x = 0
        self._y = 0

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    def set_next(self, obj):
        self._next = weakref.ref(obj)

    @property
    def next(self):
       return self._next()

    @property
    def previous(self):
        return self._previous

    def _up(self, count):
        self._y += count

    def _down(self, count):
        self._y -= count

    def _left(self, count):
        self._x -= count

    def _right(self, count):
        self._x += count



class Position(_PositionProxy):
    UP_CHAR = "U"
    DOWN_CHAR = "D"
    LEFT_CHAR = "L"
    RIGHT_CHAR = "R"

    def __init__(self, position=_PositionProxy()):
        super(Position, self).__init__()
        self._previous = position
        self._next = position.set_next(self)

    def __repr__(self):
        return "<Position {}x{}>".format(
            self._x, self._y
        )

    def up(self, count):
        p = Position(self)
        p._up(count)
        return p

    def down(self, count):
        p = Position(self)
        p._down(count)
        return p

    def left(self, count):
        p = Position(self)
        p._left(count)
        return p

    def right(self, count):
        p = Position(self)
        p._right(count)
        return p

    def parse_instruction(self, instruction):
        char = instruction[0]
        instruction = int(instruction[1:])
        if char == self.UP_CHAR:
            return self.up(instruction)
        elif char == self.DOWN_CHAR:
            return self.down(instruction)
        elif char == self.LEFT_CHAR:
            return self.left(instruction)
        elif char == self.RIGHT_CHAR:
            return self.right(instruction)
        else:
            raise ValueError("Unknown character \"{}\"".format(char))

    def position_paths(self):
        obj = self
        path = []
        while obj is not None:
            path.append((obj.x, obj.y))
            obj = obj.previous
        return path

    def intersections(self, other):
        positions = self.position_paths()
        other_positions = other.position_paths()

        return [value for value in positions if value in other_positions and value != (0, 0)]


def manhattan_distance(source, dest):
    return sum(abs(source - dest) for source, dest in zip(source, dest))




with open("input.txt", "rb") as fh:
    data = fh.read().split("\n")


wires = []
for path in data:
    if not path:
        continue
    _wire = Position()
    instructions = path.split(",")
    for instruction in instructions:
        if not instruction:
            continue
        _wire = _wire.parse_instruction(instruction)
    wires.append(_wire)

print(wires)
intersections = set({})
combos = list(combinations(wires, 2))
for first, second in combos:
    points = first.intersections(second)
    intersections = intersections.union(set(points))

print(intersections)
for intersection in intersections:
    print(manhattan_distance(intersection, (0, 0)))
