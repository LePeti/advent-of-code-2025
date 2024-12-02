
from input.input_1_a import left_list, right_list

if __name__ == "__main__":
    left_list_sorted = sorted(left_list)
    right_list_sorted = sorted(right_list)

    diffs = [abs(a - b) for a, b in zip(left_list_sorted, right_list_sorted)]

    solution = sum([abs(a - b) for a, b in zip(left_list_sorted, right_list_sorted)])

    print(solution)
