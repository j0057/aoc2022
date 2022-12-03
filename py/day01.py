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

def test_01_ex1(): assert day01a('1000\n2000\n3000\n\n4000\n\n5000\n6000\n\n7000\n8000\n9000\n\n10000') == 24000
def test_01_ex2(): assert day01b('1000\n2000\n3000\n\n4000\n\n5000\n6000\n\n7000\n8000\n9000\n\n10000') == 45000

def test_01a(day01_text): assert day01a(day01_text) == 68467
def test_01b(day01_text): assert day01b(day01_text) == 203420
