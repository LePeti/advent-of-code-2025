import numpy as np

# from input.input_4_small import word_search
from input.input_4 import word_search


def convert_input_to_matrix(input: list[list[str]]) -> list[list[list[str]]]:
    return np.array([list(row[0]) for row in input])


def find_a_in_matrix(matrix: np.array) -> tuple[int, int]:
    X, Y = np.where(matrix == "A")
    return [(x, y) for x, y in zip(X, Y)]


def is_enough_space_for_mas(a_x: int, a_y: int, shape: tuple[int, int]) -> bool:
    if a_x < 1 or a_x + 1 >= shape[0]:
        return False
    if a_y < 1 or a_y + 1 >= shape[1]:
        return False
    return True


def is_xmas(a_x: int, a_y: int, matrix: np.array) -> bool:
    if matrix[a_x - 1, a_y - 1] == "M" and matrix[a_x + 1, a_y + 1] == "S":
        if matrix[a_x - 1, a_y + 1] == "M" and matrix[a_x + 1, a_y - 1] == "S":
            return True
        if matrix[a_x - 1, a_y + 1] == "S" and matrix[a_x + 1, a_y - 1] == "M":
            return True
    if matrix[a_x - 1, a_y - 1] == "S" and matrix[a_x + 1, a_y + 1] == "M":
        if matrix[a_x - 1, a_y + 1] == "S" and matrix[a_x + 1, a_y - 1] == "M":
            return True
        if matrix[a_x - 1, a_y + 1] == "M" and matrix[a_x + 1, a_y - 1] == "S":
            return True
    return False


if __name__ == "__main__":
    word_search_matrix = convert_input_to_matrix(word_search)

    a_coordinates = find_a_in_matrix(word_search_matrix)
    valid_a_coordinates = [
        coordinates
        for coordinates in a_coordinates
        if is_enough_space_for_mas(*coordinates, word_search_matrix.shape)
    ]

    xmas_count = 0

    for a_x, a_y in valid_a_coordinates:
        if is_xmas(a_x, a_y, word_search_matrix):
            xmas_count += 1

    print(xmas_count)
