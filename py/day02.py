def parse(grid):
    return [('ABC'.index(a), ('XYZ'.index(b))) for (a, b) in grid]

# 0=Rock 1=Paper 2=Scissor
def outcome(a, b):
    return 6 if (a + 1) % 3 == b \
        else 3 if a == b \
        else 0

def day02a(grid):
    return sum(outcome(a, b) + b + 1 for (a, b) in parse(grid))

EX = [['A', 'Y'], ['B', 'X'], ['C', 'Z']]

def test_02_ex1(): assert day02a(EX) == 15

def test_02a(day02_grid): assert day02a(day02_grid) == 15523
