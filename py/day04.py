def parse(L):
    return [tuple(int(x) for x in s.replace('-', ',').split(',')) for s in L]

# In how many assignment pairs does one range fully contain the other?
def day04a(L):
    return sum(a <= c <= d <= b or c <= a <= b <= d
               for (a, b, c, d) in parse(L))

# In how many assignment pairs do the ranges overlap?
def day04b(L):
    return sum(a <= c <= b or a <= d < b or c <= a <= d or c <= b <= d
               for (a, b, c, d) in parse(L))

def test_04_ex1(day04_ex_lines): assert day04a(day04_ex_lines(0)) == 2
def test_04_ex2(day04_ex_lines): assert day04b(day04_ex_lines(0)) == 4

def test_04a(day04_lines): assert day04a(day04_lines) == 459
def test_04b(day04_lines): assert day04b(day04_lines) == 779
