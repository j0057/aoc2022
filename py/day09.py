from math import copysign

def parse(lines):
    DIR = {'R': +1, 'L': -1, 'U': +1j, 'D': -1j}
    return [(DIR[d], int(m)) for (d, m) in (line.split() for line in lines)]

def tail_step(M):
    return 0 if abs(M) < 2 \
      else copysign(1, M.real) + copysign(1, M.imag) * 1j if M.real and M.imag \
      else M * .5

def move_rope(R, d):
    yield (h := R[0] + d)
    yield from (h := t + tail_step(h-t) for t in R[1:])

def paths(steps, R):
    return (R := [*move_rope(R, d)]
            for (d, m) in steps
            for _ in range(m))

# How many positions does the tail of the rope visit at least once?
def day09a(lines): return len({R[-1] for R in paths(parse(lines), [0] * 2)})
def day09b(lines): return len({R[-1] for R in paths(parse(lines), [0] * 10)})

def test_09_ex1(day09_ex_lines): assert day09a(day09_ex_lines(3)) == 13
def test_09_ex2(day09_ex_lines): assert day09b(day09_ex_lines(3)) == 1
def test_09_ex3(day09_ex_lines): assert day09b(day09_ex_lines(7)) == 36

def test_09a(day09_lines): assert day09a(day09_lines) == 6391
def test_09b(day09_lines): assert day09b(day09_lines) == 2593
