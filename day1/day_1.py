# time complexity O(n)
def two_sum(target_value, numbers, start_idx = 0):
    seen = set()
    for value in numbers[start_idx:]:
        complement = target_value - value
        if complement in seen:
            return value, complement
        seen.add(value)

    return None, None

# time complexity O(n^2)
# reduces to two sum problem
def three_sum(target_value, numbers):
    for i, value in enumerate(numbers):
        complement = target_value - value
        value_1, value_2 = two_sum(complement, numbers, i)
        if value_1 is not None:
            return value, value_1, value_2

    return None, None, None
        
# no negative values, not sorted, assume valid input with a valid result    
expense_file = open('input_1.txt', 'r')
expense_report = [int(value) for value in expense_file]

# problem 1
target_value = 2020
value_1, value_2 = two_sum(target_value, expense_report) 

result_1 = value_1 * value_2
print(result_1)


# problem 2
value_1, value_2, value_3 = three_sum(target_value, expense_report) 

result_2 = value_1 * value_2 * value_3
print(result_2)
