EX1 = '2-4,6-8 2-3,4-5 5-7,7-9 2-8,3-7 6-6,4-6 2-6,4-8'.split()

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

def test_04_ex1(): assert day04a(EX1) == 2
def test_04_ex2(): assert day04b(EX1) == 4

def test_04a(day04_lines): assert day04a(day04_lines) == 459
def test_04b(day04_lines): assert day04b(day04_lines) == 779
