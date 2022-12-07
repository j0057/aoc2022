def parse_output(I):
    cur = []
    for line in I:
        match line.split():
            case ['$', 'cd', '/']:
                pass
            case ['$', 'cd', '..']:
                break
            case ['$', 'cd', name]:
                cur.append(('d', name, *parse_output(I)))
            case ['$', 'ls']:
                pass
            case ['dir', name]:
                pass
            case [size, name]:
                cur.append(('f', name, int(size)))
            case x:
                raise Exception(f"WTF: {x!r}")
    return sum(size for (_, _, size, *_) in cur), sorted(cur)

def find_dirs(tree):
    match tree:
        case ('f', _, _):
            return
        case ('d', _, size, subdirs):
            yield size
            for subdir in subdirs:
                for d in find_dirs(subdir):
                    yield d

# Find all of the directories with a total size of at most 100000. What is the
# sum of the total sizes of those directories?
def day07a(lines):
    tree = ('d', '', *parse_output(iter(lines)))
    return sum(size for size in find_dirs(tree) if size < 100_000)

# Find the smallest directory that, if deleted, would free up enough space on
# the filesystem to run the update. What is the total size of that directory?
def day07b(lines):
    tree = ('d', '', *parse_output(iter(lines)))
    used = next(find_dirs(tree))
    free = 70_000_000 - used
    return min(size for size in find_dirs(tree) if size + free >= 30_000_000)

def test_07_ex1(day07_ex_lines): assert day07a(day07_ex_lines(1)) == 95437
def test_07_ex2(day07_ex_lines): assert day07b(day07_ex_lines(1)) == 24933642

def test_07a(day07_lines): assert day07a(day07_lines) == 1513699
def test_07b(day07_lines): assert day07b(day07_lines) == 7991939