from collections import defaultdict

def parse(L):
    return [[tuple(int(n) for n in c.split(',')) for c in s.split(' -> ')]
            for s in L]

def irange(i, j):
    if i <= j:
        return range(i, j+1)
    else:
        return range(i, j-1, -1)

def genpath(ax, ay, bx, by):
    if ay == by:
        return ((x, ay) for x in irange(ax, bx))
    else:
        return ((ax, y) for y in irange(ay, by))

def build(paths):
    return {x+y*1j: 1 for path in paths
                      for (a, b) in zip(path, path[1:])
                      for (x, y) in genpath(*a, *b)}

def drop_sand(grid, maxy):
    while (p := 500) and not grid[p]:
        while p.imag < maxy:
            match (grid[p-1+1j], grid[p+1j], grid[p+1+1j]):
                case (_,  0,  _): p +=  0+1j
                case (0, 1|2, _): p += -1+1j
                case (_, 1|2, 0): p += +1+1j
                case (_, 1|2, _):
                    grid[p] = 2
                    break
                case _: 1/0
        else:
            break

# Using your scan, simulate the falling sand. How many units of sand come to
# rest before sand starts flowing into the abyss below?
def day14a(L):
    grid = defaultdict(int, build(parse(L)))
    maxy = max(c.imag for c in grid)
    drop_sand(grid, maxy)
    return sum(v == 2 for v in grid.values())

# Using your scan, simulate the falling sand until the source of the sand
# becomes blocked. How many units of sand come to rest?
def day14b(L):
    grid = defaultdict(int, build(parse(L)))
    maxy = int(max(c.imag for c in grid))
    grid |= {x+(maxy+2)*1j: 1 for x in range(500-maxy-3, 500+maxy+3)}
    drop_sand(grid, maxy+3)
    return sum(v == 2 for v in grid.values())

def test_14_ex1(day14_ex_lines): assert day14a(day14_ex_lines(0)) == 24
def test_14_ex2(day14_ex_lines): assert day14b(day14_ex_lines(0)) == 93

def test_14a(day14_lines): assert day14a(day14_lines) == 757
def test_14b(day14_lines): assert day14b(day14_lines) == 24943
