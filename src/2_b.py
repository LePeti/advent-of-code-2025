from input.input_2 import reports


def is_list_sorted(_list: list) -> bool:
    try:
        return _list == sorted(_list) or _list == sorted(_list, reverse=True)
    except TypeError as e:
        print(e, _list)


def are_adjacent_levels_withins_bounds(_list: list) -> bool:
    return all([1 <= abs(a - b) <= 3 for a, b in zip(_list, _list[1:])])


if __name__ == "__main__":

    safe = 0
    for report in reports:
        print(report)
        if is_list_sorted(report) and are_adjacent_levels_withins_bounds(report):
            safe += 1
        else:
            for i in range(len(report)):
                if len(report) == 1:
                    safe += 1
                    continue
                else:
                    new_report = report.copy()
                    new_report.pop(i)
                    if is_list_sorted(new_report) and are_adjacent_levels_withins_bounds(new_report):
                        safe += 1
                        break

    print(safe)
