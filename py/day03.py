PRIO = {**{chr(ord('a') + v): v+1  for v in range(26)},
        **{chr(ord('A') + v): v+27 for v in range(26)}}

def split(R):
    return [(s[:L], s[L:]) for (s, L) in ((s, len(s)//2) for s in R)]

def day03a(R):
    return sum(PRIO[({*a} & {*b}).pop()] for (a, b) in split(R))

EX = ['vJrwpWtwJgWrhcsFMMfFFhFp',
      'jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL',
      'PmmdzqPrVvPwwTWBwg',
      'wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn',
      'ttgJtRGJQctTZtZT',
      'CrZsJsPPZsGzwwsLwLmpwMDw']

def test_03_ex1(): assert day03a(EX) == 157

def test_03a(day03_lines): assert day03a(day03_lines) == 7863
