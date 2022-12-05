def parse(L):
    empty = L.index('')
    count = int(L[empty-1].split()[-1]) - 1
    stacks = [[L[y][x]
               for y in range(empty-2, -1, -1)
               if L[y][x].isalpha()]
              for x in range(1, 1 + count * 4 + 1, 4)]
    script = [(int(x), int(a)-1, int(b)-1)
              for (_, x, _, a, _, b) in (s.split() for s in L[empty+1:])]
    return (stacks, script)

# After the rearrangement procedure completes, what crate ends up on top of
# each stack?
def day05a(raw):
    stacks, script = parse(raw[:-1].split('\n'))
    for (c, a, b) in script:
        stacks[b] += stacks[a][-1:-c-1:-1]
        stacks[a]  = stacks[a][:-c]
    return ''.join(s[-1] for s in stacks)

# After the rearrangement procedure completes, what crate ends up on top of
# each stack?
def day05b(raw):
    stacks, script = parse(raw[:-1].split('\n'))
    for (c, a, b) in script:
        stacks[b] += stacks[a][-c:]
        stacks[a]  = stacks[a][:-c]
    return ''.join(s[-1] for s in stacks)

def test_05_ex1(day05_ex_raw): assert day05a(day05_ex_raw(0)) == 'CMZ'
def test_05_ex2(day05_ex_raw): assert day05b(day05_ex_raw(0)) == 'MCD'

def test_05a(day05_raw): assert day05a(day05_raw) == 'FZCMJCRHZ'
def test_05b(day05_raw): assert day05b(day05_raw) == 'JSDHQMZGF'
