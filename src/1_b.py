
from collections import Counter

from input.input_1_a import left_list, right_list

if __name__ == "__main__":
    right_counter = Counter(right_list)

    solution = sum([left_number * right_counter.get(left_number, 0) for left_number in left_list])

    print(solution)
