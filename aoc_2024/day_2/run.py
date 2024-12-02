import numpy as np

def parse_input(fpath):
    with open(fpath, "r") as f:
        lines = f.readlines()

    map_f = lambda x: list(map(lambda x: int(x), x.replace("\n", "").split(" ")))
    return list(map(map_f, lines))


def _one_report(report):
    diffs = np.diff(report)
    signs = np.sign(diffs)
    magnitudes = np.abs(diffs)
    unique, counts = np.unique(signs, return_counts=True)
    return (unique.shape[0] == 1) & (unique[0] != 0) & (magnitudes >= 1).all() & (magnitudes <= 3).all()


def _can_remove_level(report):
    return any([_one_report(report[:i] + report[i + 1:]) for i in range(len(report))])
    


def problem_1(reports):
    return sum([_one_report(report) for report in reports])


def problem_2(reports):
    return sum([_can_remove_level(report) for report in reports])

reports = parse_input("./input.txt")
print(problem_1(reports))
print(problem_2(reports))
