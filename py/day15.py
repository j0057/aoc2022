from functools import reduce

def parse(L):
    return {(int(f[2][2:-1]), int(f[3][2:-1])): (int(f[-2][2:-1]), int(f[-1][2:]))
            for f in (s.split() for s in L)} # must...not...use...re.findall...

def distances(S):
    return {(sx, sy): abs(bx-sx) + abs(by-sy) for ((sx, sy), (bx, by)) in S.items()}

def merge(I):
    return reduce(lambda R, i: (R[:-1] + [(R[-1][0], max(R[-1][1], i[1]))]) if i[0]-1 <= R[-1][1] else R + [i], I[1:], [I[0]])

def exclude_y(M, y):
    return merge(sorted(i for ((sx, sy), m) in M.items()
                          if m - abs(sy-y) > 0
                          for i in [(sx-m+abs(sy-y), sx), (sx, sx+m-abs(sy-y))]))

# Consult the report from the sensors you just deployed. In the row where
# y=2000000, how many positions cannot contain a beacon?
def day15a(S, y):
    I = exclude_y(distances(S), y)
    SB = {(ax, ay) for T in S.items()
                   for (ax, ay) in T
                   if ay == y and any(x1 <= ax <= x2 for (x1, x2) in I)}
    return sum(x2-x1+1 for (x1, x2) in I) - len(SB)

# Find the only possible position for the distress beacon. What is its tuning
# frequency?
def day15b(S, sq):
    M = distances(S)
    y, I = next((y, I) for y in range(sq) if len(I := exclude_y(M, y)) == 2)
    return (I[0][1]+1) * 4_000_000 + y

def test_15_ex1(day15_ex_lines): assert day15a(parse(day15_ex_lines(0)),  9) == 25
def test_15_ex2(day15_ex_lines): assert day15a(parse(day15_ex_lines(0)), 10) == 26
def test_15_ex3(day15_ex_lines): assert day15a(parse(day15_ex_lines(0)), 11) == 27

def test_15_ex4(day15_ex_lines): assert day15b(parse(day15_ex_lines(0)), 20) == 56000011

def test_15a(day15_lines): assert day15a(parse(day15_lines), 2_000_000) == 5716881
def test_15b(day15_lines): assert day15b(parse(day15_lines), 4_000_000) == 10852583132904
