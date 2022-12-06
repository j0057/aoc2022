def find_marker(s, n):
    return next(i for i in range(n, len(s)) if len({*s[i-n:i]}) == n)

# How many characters need to be processed before the first start-of-packet
# marker is detected?
def day06a(s):
    return find_marker(s, 4)

# How many characters need to be processed before the first start-of-message
# marker is detected?
def day06b(s):
    return find_marker(s, 14)

def test_06_ex1(): assert day06a('mjqjpqmgbljsphdztnvjfqwrcgsmlb') == 7
def test_06_ex2(): assert day06a('bvwbjplbgvbhsrlpgdmjqwftvncz') == 5
def test_06_ex3(): assert day06a('nppdvjthqldpwncqszvftbrmjlhg') == 6
def test_06_ex4(): assert day06a('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg') == 10
def test_06_ex5(): assert day06a('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw') == 11

def test_06_ex6(): assert day06b('mjqjpqmgbljsphdztnvjfqwrcgsmlb') == 19
def test_06_ex7(): assert day06b('bvwbjplbgvbhsrlpgdmjqwftvncz') == 23
def test_06_ex8(): assert day06b('nppdvjthqldpwncqszvftbrmjlhg') == 23
def test_06_ex9(): assert day06b('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg') == 29
def test_06_ex10(): assert day06b('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw') == 26

def test_06a(day06_text): assert day06a(day06_text) == 1909
def test_06b(day06_text): assert day06b(day06_text) == 3380
