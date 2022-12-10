from itertools import islice

def parse(code):
    for ins in code:
        match ins.split():
            case ['noop']:      yield (1, 'noop',)
            case ['addx', n]:   yield (2, 'addx', int(n))

def run(code, IP=0, X=1):
    state = lambda: (IP, X)
    while IP < len(code):
        for _ in range(code[IP][0]):
            yield state()
        match code[IP]:
            case (_, 'noop',):
                pass
            case (_, 'addx', n):
                X += n
        IP += 1
    yield state()

# Find the signal strength during the 20th, 60th, 100th, 140th, 180th, and
# 220th cycles. What is the sum of these six signal strengths?
def day10a(code):
    exe = run([*parse(code)])
    prb = islice(enumerate(exe), 20-1, None, 40)
    return sum((n+1) * X for (n, (_, X)) in prb)

def test_10_ex1(day10_ex_lines): assert [*run([*parse(day10_ex_lines(0))])] == [(0, 1), (1, 1), (1, 1), (2, 4), (2, 4), (3, -1)]
def test_10_ex2(day10_ex_lines): assert day10a(day10_ex_lines(1)) == 13140

def test_10a(day10_lines): assert day10a(day10_lines) == 14540
