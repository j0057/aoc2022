ilen = lambda items: sum(1 for _ in items)

def stopwhen(pred, items):
    for x in items:
        yield x
        if pred(x):
            break

def parse(rows):
    return [[int(h) for h in row] for row in rows]

def is_visible(grid, sy, sx):
    return all(grid[y][sx] < grid[sy][sx] for y in range(sy-1, 0-1, -1)) \
        or all(grid[y][sx] < grid[sy][sx] for y in range(sy+1, len(grid))) \
        or all(grid[sy][x] < grid[sy][sx] for x in range(sx-1, 0-1, -1)) \
        or all(grid[sy][x] < grid[sy][sx] for x in range(sx+1, len(grid)))

def scenic_score(grid, sy, sx):
    return ilen(stopwhen(lambda y: grid[y][sx] >= grid[sy][sx], range(sy-1, 0-1, -1))) \
         * ilen(stopwhen(lambda y: grid[y][sx] >= grid[sy][sx], range(sy+1, len(grid)))) \
         * ilen(stopwhen(lambda x: grid[sy][x] >= grid[sy][sx], range(sx-1, 0-1, -1))) \
         * ilen(stopwhen(lambda x: grid[sy][x] >= grid[sy][sx], range(sx+1, len(grid))))

def day08a(grid):
    count = sum(is_visible(grid, y, x) for y in range(1, len(grid)-1)
                                       for x in range(1, len(grid)-1))
    return count + 4 * len(grid) - 4

def day08b(grid):
    return max(scenic_score(grid, y, x) for y in range(1,len(grid)-1)
                                        for x in range(1,len(grid)-1))

def test_08_ex1(day08_ex_lines): assert day08a(parse(day08_ex_lines(0))) == 21
def test_08_ex2(day08_ex_lines): assert day08b(parse(day08_ex_lines(0))) == 8

def test_08a(day08_lines): assert day08a(parse(day08_lines)) == 1805
def test_08b(day08_lines): assert day08b(parse(day08_lines)) == 444528
