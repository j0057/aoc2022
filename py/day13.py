from functools import cmp_to_key

def parse(L):
    return [eval(s) for s in L if s]

def cmp(X, Y):
    match (X, Y):
        case (list(X), int(Y)): return cmp(X, [Y])
        case (int(X), list(Y)): return cmp([X], Y)
    match (X, Y):
        case (int(a), int(b)): return a - b
        case (list(A), list(B)):
            check = (o for (a, b) in zip(A, B) if (o := cmp(a, b)))
            return next(check, 0) or (len(A) - len(B))

# Determine which pairs of packets are already in the right order. What is the
# sum of the indices of those pairs?
def day13a(L):
    chunks = lambda I, n: zip(*[iter(I)] * n)
    return sum(i+1 for (i, (a, b)) in enumerate(chunks(parse(L), 2)) if cmp(a, b) < 0)

# Organize all of the packets into the correct order. What is the decoder key
# for the distress signal?
def day13b(L):
    S = sorted([p := [[2]], q := [[6]], *parse(L)], key=cmp_to_key(cmp))
    return (S.index(p)+1) * (S.index(q)+1)

def test_13_ex1(day13_ex_lines): assert day13a(day13_ex_lines(0)) == 13
def test_13_ex2(day13_ex_lines): assert day13b(day13_ex_lines(0)) == 140

def test_13a(day13_lines): assert day13a(day13_lines) == 5675
def test_13b(day13_lines): assert day13b(day13_lines) == 20383
