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
        # find the first occurrence of "do()" and use the part after it
        do_index = dont_split.find("do()")
        if do_index != -1:
            enabled_part = dont_split[do_index:]
            valid_operations += pattern.findall(enabled_part)

    result = sum([int(x) * int(y) for x, y in valid_operations])

    print(result)
