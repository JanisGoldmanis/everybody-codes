with open('input/quest_2_part1.txt', 'r') as file:
    lines = file.readlines()

words = lines[0].strip().split(':')[1].split(',')
inscription = lines[2].strip()

result = 0

for word in words:
    result += inscription.count(word)

print(f"Part 1: {result}")


with open('input/quest_2_part_2.txt', 'r') as file:
    lines = file.readlines()

words = lines[0].strip().split(':')[1].split(',')
words += [word[::-1] for word in words]
inscriptions = [line.strip() for line in lines[2:]]

runic_symbols = 0

for inscription in inscriptions:

    valid_id = set()

    for i in range(len(inscription)):
        for word in words:
            if len(word) > len(inscription) - i:
                continue

            if word == inscription[i:i+len(word)]:
                ids = [n for n in range(i, i+len(word))]
                for id in ids:
                    valid_id.add(id)

    runic_symbols += len(valid_id)

print(f"Part 2: {runic_symbols}")


with open('input/quest_2_part_3.txt', 'r') as file:
    lines = file.readlines()

words = lines[0].strip().split(':')[1].split(',')
# words += [word[::-1] for word in words]
inscriptions = [line.strip() for line in lines[2:]]

valid_arr = [['.'] * len(inscriptions[0]) for _ in range(len(inscriptions))]

DIRECTIONS = [(1,0), (-1, 0), (0, 1), (0, -1)]

ROW_COUNT = len(inscriptions)
COL_COUNT = len(inscriptions[0])

def verify_word(inscriptions, row, column, word, dir=None):
    if inscriptions[row][column] != word[0]:
        return False

    if len(word) == 1:
        return True

    valid_directions = []

    if dir is None:
        for direction in DIRECTIONS:
            next_row = row + direction[0]

            if next_row < 0 or next_row >= ROW_COUNT:
                continue

            next_column = column + direction[1]
            if next_column >= COL_COUNT:
                next_column -= COL_COUNT

            if verify_word(inscriptions, next_row, next_column, word[1:], direction):
                valid_directions.append(direction)
        return valid_directions

    next_row = row + dir[0]
    if next_row < 0 or next_row >= ROW_COUNT:
        return False

    next_column = column + dir[1]
    if next_column >= COL_COUNT:
        next_column -= COL_COUNT

    return verify_word(inscriptions, next_row, next_column, word[1:], dir)


for row in range(len(inscriptions)):
    for column in range(len(inscriptions[row])):
        for word in words:
            directions = verify_word(inscriptions, row, column, word)

            if type(directions) is bool and directions:
                valid_arr[row][column] = 'X'
            elif directions:
                for direction in directions:
                    for i in range(len(word)):
                        next_row = row + direction[0] * i

                        next_column = column + direction[1] * i
                        if next_column >= COL_COUNT:
                            next_column -= COL_COUNT

                        valid_arr[next_row][next_column] = 'X'


result = sum([line.count('X') for line in valid_arr])

print(f"Part 3: {result}")