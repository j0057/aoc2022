from math import inf as INFINITY

def parse(L):
    find = lambda c: next(x+y*1j for (y, s) in enumerate(L)
                                 if (x := s.find(c)) > -1)
    return {x+y*1j: {'S': 1, 'E': 26}.get(c) or (ord(c)-ord('a')+1)
            for (y, s) in enumerate(L)
            for (x, c) in enumerate(s)}, find('S'), find('E')

def breadth_first_search(source, goal, expand):
    explored = {source}
    frontier = [(0, source)]
    while frontier:
        cost, node = frontier.pop(0)
        if goal(node):
            return cost
        for child in expand(node):
            if child in explored:
                continue
            explored.add(child)
            frontier.append((cost+1, child))
    return INFINITY

# What is the fewest steps required to move from your current position to the
# location that should get the best signal?
def day12a(grid, source, target):
    isgoal = lambda n: n == target
    expand = lambda n: [c for c in [n+1, n+1j, n-1, n-1j] if grid.get(c, INFINITY)-grid[n] <= 1]
    return breadth_first_search(source, isgoal, expand)

# What is the fewest steps required to move starting from any square with
# elevation a to the location that should get the best signal?
def day12b(G, source, target):
    isgoal = lambda n: G[n] == 1
    expand = lambda n: [c for c in [n+1, n+1j, n-1, n-1j] if G.get(c, -INFINITY)-G[n] >= -1]
    return breadth_first_search(target, isgoal, expand)

def test_12_ex1(day12_ex_lines): assert day12a(*parse(day12_ex_lines(0))) == 31
def test_12_ex2(day12_ex_lines): assert day12b(*parse(day12_ex_lines(0))) == 29

def test_12a(day12_lines): assert day12a(*parse(day12_lines)) == 468
def test_12b(day12_lines): assert day12b(*parse(day12_lines)) == 459
