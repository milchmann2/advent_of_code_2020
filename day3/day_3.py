
map_file = open('input_3.txt', 'r')
map_part = [line.rstrip()  for line in map_file]
print(map_part)
goal = len(map_part)
part_length = len(map_part[0])

TREE = '#'


def check_slopes(right, down):
    row, col = 0, 0
    hit_tree_count = 0

    while row < goal:
        if map_part[row][col % part_length] == TREE:
            hit_tree_count += 1
        row += down
        col += right

    return hit_tree_count

slope_input = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

multiplied_tree_count = 1
for right, down in slope_input:
    multiplied_tree_count *= check_slopes(right, down)


print(multiplied_tree_count)
        
