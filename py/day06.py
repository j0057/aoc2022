def find_marker(s, n):
    return next(i for i in range(n, len(s)) if len({*s[i-n:i]}) == n)

# How many characters need to be processed before the first start-of-packet
# marker is detected?
def day06a(s):
    return find_marker(s, 4)

def test_06_ex1(): assert day06a('mjqjpqmgbljsphdztnvjfqwrcgsmlb') == 7
def test_06_ex2(): assert day06a('bvwbjplbgvbhsrlpgdmjqwftvncz') == 5
def test_06_ex3(): assert day06a('nppdvjthqldpwncqszvftbrmjlhg') == 6
def test_06_ex4(): assert day06a('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg') == 10
def test_06_ex5(): assert day06a('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw') == 11

def test_06a(day06_text): assert day06a(day06_text) == 1909
