def parse(text):
    return [[int(c) for c in elf.split('\n')] for elf in text.split('\n\n')]

# Find the Elf carrying the most Calories. How many total Calories is that Elf
# carrying?
def day01a(text):
    return max(sum(e) for e in parse(text))

# Find the top three Elves carrying the most Calories. How many Calories are
# those Elves carrying in total?
def day01b(text):
    return sum(sorted(sum(e) for e in parse(text))[-3:])

def test_01_ex1(day01_ex_text): assert day01a(day01_ex_text(0)) == 24000
def test_01_ex2(day01_ex_text): assert day01b(day01_ex_text(0)) == 45000

def test_01a(day01_text): assert day01a(day01_text) == 68467
def test_01b(day01_text): assert day01b(day01_text) == 203420
