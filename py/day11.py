from math import prod

def parse(L):
    for i in range(0, len(L), 7):
        # "Starting items: 79, 98"
        X = [int(x.rstrip(',')) for x in L[i+1].split()[2:]]
        # "Operation: new = old * 19"
        match L[i+2].split()[4:]:
            case ["*", "old"]:  F = ("sqr",)
            case ["*", n]:      F = ("mul", int(n))
            case ["+", n]:      F = ("add", int(n))
        # "Test: divisible by 23"
        D = int(L[i+3].split()[-1])
        # "If true: throw to monkey 2"
        Y = int(L[i+4].split()[-1])
        # "If false: throw to monkey 3"
        N = int(L[i+5].split()[-1])
        yield (X, F, D, Y, N)

def run(M, R, *, relieve):
    S = [0 for _ in M]
    for _ in range(R):
        for (i, (X, F, D, Y, N)) in enumerate(M):
            S[i] += len(X)
            for x in X:
                match F:
                    case ("sqr",):   x *= x
                    case ("mul", n): x *= n
                    case ("add", n): x += n
                x = relieve(x)
                M[Y if x % D == 0 else N][0].append(x)
            X[:] = []
    return S

# Figure out which monkeys to chase by counting how many items they inspect
# over 20 rounds. What is the level of monkey business after 20 rounds of
# stuff-slinging simian shenanigans?
def day11a(lines):
    monkeys = [*parse(lines)]
    return prod(sorted(run(monkeys, 20, relieve=lambda x: x//3))[-2:])

def test_11_ex1(day11_ex_lines): assert day11a(day11_ex_lines(0)) == 10605

def test_11a(day11_lines): assert day11a(day11_lines) == 182293
