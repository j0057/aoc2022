def parse(L):
    return [eval(s) for s in L if s]

def ordered(X, Y):
    match (X, Y):
        case (list(X), int(Y)): Y = [Y]
        case (int(X), list(Y)): X = [X]
    match (X, Y):
        case (int(a), int(b)) if a < b: return True
        case (int(a), int(b)) if a > b: return False
        case (int(a), int(b)) if a == b: return None
        case (list(A), list(B)):
            check = (o for (a, b) in zip(A, B) if (o := ordered(a, b)) is not None)
            if (result := next(check, None)) is not None:
                return result
            elif len(A) == len(B):
                return None
            else:
                return len(A) < len(B)
        case _: 1/0 # BANGK!
    return False

# Determine which pairs of packets are already in the right order. What is the
# sum of the indices of those pairs?
def day13a(L):
    chunks = lambda I, n: zip(*[iter(I)] * n)
    return sum(i+1 for (i, (a, b)) in enumerate(chunks(parse(L), 2)) if ordered(a, b))

def test_13_ex1(day13_ex_lines): assert day13a(day13_ex_lines(0)) == 13

def test_13a(day13_lines): assert day13a(day13_lines) == 5675
