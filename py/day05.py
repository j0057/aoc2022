EX = '    [D]    \n' \
     '[N] [C]    \n' \
     '[Z] [M] [P]\n' \
     ' 1   2   3 \n' \
     '\n' \
     'move 1 from 2 to 1\n' \
     'move 3 from 1 to 3\n' \
     'move 2 from 2 to 1\n' \
     'move 1 from 1 to 2\n'

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

def day05a(raw):
    stacks, script = parse(raw[:-1].split('\n'))
    for (c, a, b) in script:
        stacks[b] += stacks[a][-1:-c-1:-1]
        stacks[a]  = stacks[a][:-c]
    return ''.join(s[-1] for s in stacks)

def test_05_ex1(): assert day05a(EX) == 'CMZ'

def test_05a(day05_raw): assert day05a(day05_raw) == 'FZCMJCRHZ'
