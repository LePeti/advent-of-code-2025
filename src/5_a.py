# from input.input_5_rules import RULES
from input.input_5_rules_small import RULES

# from input.input_5_updates import UPDATES
from input.input_5_updates_small import UPDATES


def is_rule_necessary(rule: tuple[int, int], update: list[int]) -> bool:
    return rule[0] in update and rule[1] in update


def get_necessary_rules(rules: list[tuple[int, int]], update: list[int]) -> list[tuple[int, int]]:
    return [rule for rule in rules if is_rule_necessary(rule, update)]


def rule_passes(rule: tuple[int, int], update: list[int]) -> bool:
    return update.index(rule[0]) < update.index(rule[1])


def is_valid_update(rules: list[tuple[int, int]], update: list[int]) -> bool:
    necessary_rules = get_necessary_rules(rules, update)
    # quit checking when the first rule fails
    for rule in necessary_rules:
        if not rule_passes(rule, update):
            return False
    return True


def fix_invalid_update(rules: list[tuple[int, int]], update: list[int]) -> list[int]:
    necessary_rules = get_necessary_rules(rules, update)
    for rule in necessary_rules:
        if not rule_passes(rule, update):
            update = fix_update_based_on_rule(rule, update)
    return update


def fix_update_based_on_rule(rule: tuple[int, int], update: list[int]) -> list[int]:
    index_to_pop = update.index(rule[0])
    number_to_move = update.pop(index_to_pop)
    # index_to_insert = update.index(rule[1])
    # return update[:index_to_insert] + [number_to_move] + update[index_to_insert:]
    return [number_to_move] + update


def get_middle_number(update: list[int]) -> int:
    return update[len(update) // 2]


if __name__ == "__main__":

    invalid_updates_middle_number = []

    # print(fix_invalid_update([(10, 1), (1, 3), (3, 4), (8, 10)], [3, 4, 1, 2, 10]))

    for update in UPDATES:
        if not is_valid_update(RULES, update):
            print("=====================================")
            print(f"invalid update: {update}")
            print(f"necessary rules: {get_necessary_rules(RULES, update)}")
            fixed_update = fix_invalid_update(RULES, update)
            print(f"fixed update: {fixed_update}")
            invalid_updates_middle_number.append(get_middle_number(fixed_update))
        else:
            print("=====================================")
            print(f"valid update: {update}")

    print(sum(invalid_updates_middle_number))
