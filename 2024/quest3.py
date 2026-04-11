def dig(input, directions):
    with open(input) as f:
        char_arr = [[0 if char == '.' else 1 for char in line.strip()] for line in f.readlines()]
    result = sum(sum(line) for line in char_arr)
    layer = 1
    coordinates_to_dig = []
    for row in range(len(char_arr)):
        for col in range(len(char_arr[row])):
            if char_arr[row][col] == 1:
                coordinates_to_dig.append((row, col))
    def parse_arr(char_arr, layer, coordinates_to_dig):
        result = 0
        next_layer = layer + 1
        next_coordinates_to_dig = []

        for coord in coordinates_to_dig:
            adjacent_good = True

            for direction in directions:
                next_row = coord[0] + direction[0]

                if not (0 <= next_row < len(char_arr)):
                    adjacent_good = False
                    break

                next_col = coord[1] + direction[1]
                if not (0 <= next_col < len(char_arr[next_row])):
                    adjacent_good = False
                    break

                adj_coord = (next_row, next_col)

                adj_layer = char_arr[adj_coord[0]][adj_coord[1]]

                fall = adj_layer - next_layer

                if fall < -1:
                    adjacent_good = False
                    break

            if adjacent_good:
                result += 1
                char_arr[coord[0]][coord[1]] = next_layer
                next_coordinates_to_dig.append(coord)

        return result, next_coordinates_to_dig

    digged = True
    while digged > 0:
        digged, coordinates_to_dig = parse_arr(char_arr, layer, coordinates_to_dig)
        result += digged
        layer += 1
    print(f"{input}: {result}")


ORTHO_DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
ALL_DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]


dig("input/quest_3_part_1.txt", ORTHO_DIRECTIONS)
dig("input/quest_3_part_2.txt", ORTHO_DIRECTIONS)
dig("input/quest_3_part_3.txt", ALL_DIRECTIONS)