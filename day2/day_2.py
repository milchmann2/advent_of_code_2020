import re

password_file = open('input_2.txt', 'r')
passwords = [line for line in password_file]

# problem 1
valid_password_count = 0

for line in passwords:
    lower, upper, char, pw = re.findall('\d+|\w+', line)
    lower, upper = int(lower), int(upper)
    char_count = pw.count(char)
    if lower <= char_count <= upper:
        valid_password_count += 1

print(valid_password_count)


# problem 2
valid_password_count = 0
for line in passwords:
    pos_1, pos_2, char, pw = re.findall('\d+|\w+', line)
    pos_1, pos_2 = int(pos_1) - 1, int(pos_2) - 1
    if pw[pos_1] == char and pw[pos_2] != char or pw[pos_1] != char and pw[pos_2] == char:
        valid_password_count += 1

print(valid_password_count)
