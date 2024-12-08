from typing import Tuple

import numpy as np

from input.input_6 import MAP as MAP_RAW

Position = Tuple[int, int]


def convert_input_to_matrix(input: list[list[str]]) -> np.ndarray:
    return np.array([list(row[0]) for row in input])


def find_starting_position(map: np.ndarray) -> Position:
    result: tuple[np.ndarray, np.ndarray] = np.where(map == "^")
    return (result[0][0], result[1][0])


def go_in_direction_until_object(
    map: np.ndarray, direction: str, position: Position
) -> Tuple[np.ndarray, Position, bool]:

    potential_paths_ahead = {
        "UP": map[: position[0], position[1]][::-1],
        "RIGHT": map[position[0], position[1] + 1 :],
        "DOWN": map[position[0] + 1 :, position[1]],
        "LEFT": map[position[0], : position[1]][::-1],
    }
    path_ahead: np.ndarray = potential_paths_ahead.get(direction)

    if "#" in path_ahead:
        object_in_sight = True
        object_distance = np.where(path_ahead == "#")[0][0] + 1
    else:
        object_in_sight = False
        object_distance = len(path_ahead) + 1

    if direction == "UP":
        new_position = (position[0] - (object_distance - 1), position[1])
        map[new_position[0] : position[0], position[1]] = "X"
    elif direction == "RIGHT":
        new_position = (position[0], position[1] + object_distance - 1)
        map[position[0], position[1] : new_position[1] + 1] = "X"
    elif direction == "DOWN":
        new_position = (position[0] + object_distance - 1, position[1])
        map[position[0] : new_position[0] + 1, position[1]] = "X"
    elif direction == "LEFT":
        new_position = (position[0], position[1] - (object_distance - 1))
        map[position[0], new_position[1] : position[1]] = "X"

    return map, new_position, object_in_sight


def turn_right(old_direction: str) -> str:
    new_directions = {
        "UP": "RIGHT",
        "RIGHT": "DOWN",
        "DOWN": "LEFT",
        "LEFT": "UP",
    }

    return new_directions[old_direction]


if __name__ == "__main__":

    MAP = convert_input_to_matrix(MAP_RAW)
    position = find_starting_position(MAP)
    direction = "UP"
    object_in_sight = True

    # Mark starting position as visited
    MAP[position[0]][position[1]] = "X"

    while object_in_sight:
        print("============")
        print(f"direction: {direction}")
        MAP, position, object_in_sight = go_in_direction_until_object(MAP, direction, position)
        direction = turn_right(direction)
        print(MAP)

    x_count = np.count_nonzero(MAP == "X")
    print(f"Total X count: {x_count}")
