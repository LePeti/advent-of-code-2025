import re

from input.input_3 import memory

if __name__ == "__main__":
    full_memory = "".join(memory)

    print(full_memory[:100])

    pattern = re.compile(f"mul\\((\\d\\d?\\d?),(\\d\\d?\\d?)\\)")
    valid_operations = pattern.findall(full_memory)

    result = sum([int(x) * int(y) for x, y in valid_operations])

    print(result)
