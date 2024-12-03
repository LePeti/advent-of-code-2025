import re

from input.input_3 import memory

if __name__ == "__main__":
    full_memory = "".join(memory)

    pattern = re.compile(f"mul\\((\\d\\d?\\d?),(\\d\\d?\\d?)\\)")

    dont_splits = full_memory.split("don't()")

    # valid operations before the first "don't" appear
    valid_operations = pattern.findall(dont_splits[0])

    # valid operations after the first "don't" appear
    for dont_split in dont_splits[1:]:
        # split the string by "do()" and then rejoin the rest of the string after the first one
        do_splits = dont_split.split("do()")
        enabled_part = "".join(do_splits[1:])
        valid_operations += pattern.findall(enabled_part)

    result = sum([int(x) * int(y) for x, y in valid_operations])

    print(result)
