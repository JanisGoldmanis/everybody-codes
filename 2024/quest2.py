with open('input/quest_2_part1.txt', 'r') as file:
    lines = file.readlines()

runic_words = lines[0].strip().split(':')[1].split(',')
inscription = lines[2].strip()

count = sum(inscription.count(word) for word in runic_words)

print(f"Part 1: {count}")


with open('input/quest_2_part_2.txt', 'r') as file:
    lines = file.readlines()

runic_words = lines[0].strip().split(':')[1].split(',')
runic_words = set(runic_words)
runic_words |= {word[::-1] for word in runic_words}
inscriptions = [line.strip() for line in lines[2:]]

runic_symbols = 0

for inscription in inscriptions:

    valid_indices = set()

    for i in range(len(inscription)):
        for word in runic_words:
            if inscription.startswith(word, i):
                valid_indices.update(range(i, i + len(word)))

    runic_symbols += len(valid_indices)

print(f"Part 2: {runic_symbols}")


from collections import defaultdict

with open('input/quest_2_part_3.txt', 'r') as file:
    lines = file.readlines()

runic_words = set(lines[0].strip().split(':')[1].split(','))
inscriptions = [line.strip() for line in lines[2:]]

ROW_COUNT = len(inscriptions)
COL_COUNT = len(inscriptions[0])

valid_arr = [['.'] * len(inscriptions[0]) for _ in range(len(inscriptions))]

DIRECTIONS = [(1,0), (-1, 0), (0, 1), (0, -1)]

words_by_start = defaultdict(list)

for word in runic_words:
    words_by_start[word[0]].append(word)


def matches(word, row, col, dr, dc):
    for i in range(len(word)):
        r = row + dr * i
        c = col + dc * i

        if r < 0 or r >= ROW_COUNT:
            return False

        if c >= COL_COUNT:
            c %= COL_COUNT  # wrap

        if inscriptions[r][c] != word[i]:
            return False

    return True


for row in range(ROW_COUNT):
    for col in range(COL_COUNT):
        start_char = inscriptions[row][col]

        if start_char not in words_by_start:
            continue

        for word in words_by_start[start_char]:
            for dr, dc in DIRECTIONS:
                if matches(word, row, col, dr, dc):
                    for i in range(len(word)):
                        r = row + dr * i
                        c = (col + dc * i) % COL_COUNT
                        valid_arr[r][c] = 'X'

result = sum(row.count('X') for row in valid_arr)
print(f"Part 3: {result}")