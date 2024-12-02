from input.input_2 import reports


def is_list_sorted(_list: list) -> bool:
    return _list == sorted(_list) or _list == sorted(_list, reverse=True)


def are_adjacent_levels_withins_bounds(_list: list) -> bool:
    return all([1 <= abs(a - b) <= 3 for a, b in zip(_list, _list[1:])])


if __name__ == "__main__":

    results = sum(
        [
            int(is_list_sorted(report) and are_adjacent_levels_withins_bounds(report))
            for report in reports
        ]
    )

    print(results)
