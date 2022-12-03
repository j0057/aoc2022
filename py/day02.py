def parse(grid):
    return [('ABC'.index(a), ('XYZ'.index(b))) for (a, b) in grid]

# 0=Rock 1=Paper 2=Scissor
def outcome(a, b):
    return 6 if (a + 1) % 3 == b \
        else 3 if a == b \
        else 0

# 0=Lose 1=Draw 2==Win
def choice(a, o):
    return (a - 1) % 3 if o == 0 \
        else a if o == 1 \
        else (a + 1) % 3

# What would your total score be if everything goes exactly according to your
# strategy guide?
def day02a(grid):
    return sum(outcome(a, b) + b + 1 for (a, b) in parse(grid))

# Following the Elf's instructions for the second column, what would your total
# score be if everything goes exactly according to your strategy guide?
def day02b(grid):
    return sum(o * 3 + choice(a, o) + 1 for (a, o) in parse(grid))

EX = [['A', 'Y'], ['B', 'X'], ['C', 'Z']]

def test_02_ex1(): assert day02a(EX) == 15
def test_02_ex2(): assert day02b(EX) == 12

def test_02a(day02_grid): assert day02a(day02_grid) == 15523
def test_02b(day02_grid): assert day02b(day02_grid) == 15702
