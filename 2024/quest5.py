with open('input/quest_5_part_1.txt', 'r') as f:
    char_arr = [[int(char) for char in line.strip().split()] for line in f.readlines()]

    print(char_arr)

    transposed = [list(row) for row in zip(*char_arr)]

print(transposed)