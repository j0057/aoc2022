from functools import reduce
from operator import and_ as intersect

chunks = lambda I, n: zip(*[iter(I)]*n)

PRIO = {**{chr(ord('a') + v): v+1  for v in range(26)},
        **{chr(ord('A') + v): v+27 for v in range(26)}}

def split(R):
    return [(s[:L], s[L:]) for (s, L) in ((s, len(s)//2) for s in R)]

# Find the item type that appears in both compartments of each rucksack. What
# is the sum of the priorities of those item types?
def day03a(R):
    return sum(PRIO[({*a} & {*b}).pop()] for (a, b) in split(R))

# Find the item type that corresponds to the badges of each three-Elf group.
# What is the sum of the priorities of those item types?
def day03b(R):
    return sum(PRIO[reduce(intersect, C).pop()] for C in chunks(map(set, R), 3))

def test_03_ex1(day03_ex_lines): assert day03a(day03_ex_lines(0)) == 157
def test_03_ex2(day03_ex_lines): assert day03b(day03_ex_lines(0)) == 70

def test_03a(day03_lines): assert day03a(day03_lines) == 7863
def test_03b(day03_lines): assert day03b(day03_lines) == 2488
