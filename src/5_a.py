from input.input_5_rules import RULES
from input.input_5_updates import UPDATES


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


def get_middle_number(update: list[int]) -> int:
    return update[len(update) // 2]


if __name__ == "__main__":

    valid_updates_middle_number = []

    for update in UPDATES:
        if is_valid_update(RULES, update):
            valid_updates_middle_number.append(get_middle_number(update))

    print(sum(valid_updates_middle_number))
