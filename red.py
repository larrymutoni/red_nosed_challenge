def is_safe(levels):
    if len(levels) < 2:
        return True
    diffs = []
    for i in range(len(levels) - 1):
        diffs.append(levels[i + 1] - levels[i])
    inc = all(d > 0 for d in diffs)
    dec = all(d < 0 for d in diffs)
    if not (inc or dec):
        return False
    for d in diffs:
        if abs(d) < 1 or abs(d) > 3:
            return False
    return True

def is_safe_one_removed(levels):
    if is_safe(levels):
        return True
    for i in range(len(levels)):
        new_lv = levels[:i] + levels[i+1:]
        if is_safe(new_lv):
            return True
    return False

def count_reports(text):
    lines = text.strip().split("\n")
    p1 = 0
    p2 = 0
    for line in lines:
        if not line.strip():
            continue
        levels = [int(x) for x in line.split()]
        if is_safe(levels):
            p1 += 1
            p2 += 1
        elif is_safe_one_removed(levels):
            p2 += 1
    return p1, p2

ex = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9"""

a, b = count_reports(ex)
print("Part 1:", a)
print("Part 2:", b)
