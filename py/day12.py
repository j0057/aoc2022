from queue import PriorityQueue
from math import inf as INFINITY

def parse(L):
    find = lambda c: next(C for C in ((y, s.find(c)) for (y, s) in enumerate(L)) if C[1] > -1)
    return {(y, x): {'S': 1, 'E': 26}.get(c) or (ord(c)-ord('a')+1)
            for (y, s) in enumerate(L)
            for (x, c) in enumerate(s)}, find('S'), find('E')

def neighbours(G, y1, x1):
    return [(y2, x2) for (y2, x2) in [(y1, x1+1), (y1+1, x1), (y1, x1-1), (y1-1, x1)]
                     if (y2, x2) in G and G[y2, x2] - G[y1, x1] <= 1]

def uniform_cost_search(G, source, target):
    reached = {source: 0}
    frontier = PriorityQueue()
    frontier.put((0, source))
    while not frontier.empty():
        cost, node = frontier.get()
        if node == target:
            return cost
        for child in neighbours(G, *node):
            if child not in reached or cost+1 < reached[child]:
                reached[child] = cost+1
                frontier.put((cost+1, child))
    return INFINITY

# What is the fewest steps required to move from your current position to the
# location that should get the best signal?
def day12a(L):
    return uniform_cost_search(*parse(L))

# What is the fewest steps required to move starting from any square with
# elevation a to the location that should get the best signal?
def day12b(L):
    G, _, target = parse(L)
    return min(uniform_cost_search(G, source, target)
               for source in G
               if G[source] == 1)

def test_12_ex1(day12_ex_lines): assert day12a(day12_ex_lines(0)) == 31
def test_12_ex2(day12_ex_lines): assert day12b(day12_ex_lines(0)) == 29

def test_12a(day12_lines): assert day12a(day12_lines) == 468
def test_12b(day12_lines): assert day12b(day12_lines) == 459
