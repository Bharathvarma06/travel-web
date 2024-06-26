def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def apply_operation(operation, x, y):
    return operation(x, y)

result_addition = apply_operation(add, 5, 3)
print("Result of addition:", result_addition)  # Output: 8

result_subtraction = apply_operation(subtract, 10, 4)
print("Result of subtraction:", result_subtraction)  # Output: 6