from sys import api_version


def hammer_nails(input, avg=False):

    with open(input, 'r') as f:
        distances = [int(line.strip()) for line in f.readlines()]

    if not avg:
        target = min(distances)

    else:

        distances.sort()

        n = len(distances)

        target = distances[n // 2]

    result = sum(abs(distance - target) for distance in distances)


    print(result)


hammer_nails('input/quest_4_part_1.txt')
hammer_nails('input/quest_4_part_2.txt')
hammer_nails('input/quest_4_part_3.txt', avg=True)
