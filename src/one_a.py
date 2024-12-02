from input.input_one_a import list_a, list_b

if __name__ == "__main__":
    list_a_sorted = sorted(list_a)
    list_b_sorted = sorted(list_b)

    diffs = [abs(a - b) for a, b in zip(list_a_sorted, list_b_sorted)]

    solution = sum([abs(a - b) for a, b in zip(list_a_sorted, list_b_sorted)])

    print(solution)
