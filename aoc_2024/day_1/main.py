from collections import Counter

def parse_input(fpath):
    with open(fpath, "r") as f:
        lines = f.readlines()

    map_f = lambda x: map(lambda x: int(x), x.replace("\n", "").split("   "))
    list_1, list_2 =zip(*map(map_f, lines))
    return list_1, list_2


def problem_1(list_1, list_2):
    iterator = zip(sorted(list_1), sorted(list_2))
    return sum((abs(x - y) for x, y in iterator))


def problem_2(list_1, list_2):
    counted = Counter(list_2)
    return sum((counted[x]*x for x in list_1))


list_1, list_2 = parse_input("./input.txt")

print(problem_1(list_1, list_2))
print(problem_2(list_1, list_2))