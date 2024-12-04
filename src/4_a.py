import numpy as np

# from input.input_4_small import word_search
from input.input_4 import word_search


def convert_input_to_matrix(input: list[list[str]]) -> list[list[list[str]]]:
    return np.array([list(row[0]) for row in input])


def find_x_in_matrix(matrix: np.array) -> tuple[int, int]:
    X, Y = np.where(matrix == "X")
    return [(x, y) for x, y in zip(X, Y)]


def get_surrounding_coordinates(array: np.array, x: int, y: int) -> list[tuple[int, int]]:
    rows, cols = array.shape
    surrounding_coords = []

    for i in range(x - 1, x + 2):
        for j in range(y - 1, y + 2):
            if (0 <= i < rows) and (0 <= j < cols) and (i != x or j != y):
                direction_from_x = get_direction(x, y, i, j)
                if is_enough_letters_in_direction((x, y), direction_from_x, array.shape):
                    surrounding_coords.append((i, j))

    return surrounding_coords


def get_direction(x_1: int, y_1: int, x_2: int, y_2: int) -> tuple[int, int]:
    return (x_2 - x_1, y_2 - y_1)


def is_enough_letters_in_direction(
    x_coords: tuple[int, int], direction: tuple[int, int], shape: tuple[int, int]
) -> bool:
    """Are there enough letters in the given direction to spell XMAS?"""

    if direction[0] < 0 and x_coords[0] < 3:
        return False
    if direction[0] > 0 and x_coords[0] + 3 >= shape[0]:
        return False
    if direction[1] < 0 and x_coords[1] < 3:
        return False
    if direction[1] > 0 and x_coords[1] + 3 >= shape[1]:
        return False
    return True

if __name__ == "__main__":
    word_search_matrix = convert_input_to_matrix(word_search)

    x_coordinates = find_x_in_matrix(word_search_matrix)

    xmas_count = 0
    for x_x, x_y in x_coordinates:
        print(f"X found at ({x_x},{x_y})")
        surrounding_coordinates = get_surrounding_coordinates(word_search_matrix, x_x, x_y)
        print(f"Surrounding coordinates: {surrounding_coordinates}")

        surrounding_m_coordinates = []
        x_to_m_directions = []
        for m_x, m_y in surrounding_coordinates:
            print(f"Checking ({m_x}, {m_y})")
            if word_search_matrix[m_x, m_y] == "M":
                print(f"Found M at ({m_x}, {m_y})")
                surrounding_m_coordinates.append((m_x, m_y))
                print(f"direction: {get_direction(x_x, x_y, m_x, m_y)}")
                x_to_m_directions.append(get_direction(x_x, x_y, m_x, m_y))

        # looking for As
        for (m_x, m_y), (dir_x, dir_y) in zip(surrounding_m_coordinates, x_to_m_directions):
            potential_next_letter_x = m_x + dir_x
            potential_next_letter_y = m_y + dir_y
            if word_search_matrix[potential_next_letter_x, potential_next_letter_y] == "A":
                print(f"Found A at ({potential_next_letter_x}, {potential_next_letter_y})")
                # now we need to check if the next letter is an S
                potential_next_letter_x += dir_x
                potential_next_letter_y += dir_y
                if word_search_matrix[potential_next_letter_x, potential_next_letter_y] == "S":
                    xmas_count += 1
                    print(f"Found S at ({potential_next_letter_x}, {potential_next_letter_y})")
                    print(
                        f"Found XMAS starting at {x_x, x_y} and ending at {potential_next_letter_x, potential_next_letter_y}"
                    )

    print(f"XMAS count: {xmas_count}")
