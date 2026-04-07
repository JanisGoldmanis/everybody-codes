NECESSARY_POTIONS = {
    "A": 0,
    "B": 1,
    "C": 3,
    "D": 5,
}
GROUP_BONUS = {
    2: 2,
    3: 6,
}


def calculate_potions(group_size: int) -> None:
    """
    Split input into enemy groups based on group size.
    Replace 'x' with ''
    Look up necessary count of potions based on enemy type
    Look up necessary count of potions based on enemy group actual size
    """
    with open(f"input/quest_1_part_{group_size}.txt", "r") as file:
        enemies = file.read().strip()

    result = 0

    for i in range(0, len(enemies), group_size):
        enemy_group = enemies[i : i + group_size].replace("x", "")
        result += sum(NECESSARY_POTIONS[enemy] for enemy in enemy_group)
        result += GROUP_BONUS.get(len(enemy_group), 0)

    print(f"Necessary potions for Part {group_size}: {result}")


for i in range(1, 4):
    calculate_potions(i)
