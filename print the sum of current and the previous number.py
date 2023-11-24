previous_number = 0

for i in range(10):
    current_number = i
    result = current_number + previous_number
    print(f"Sum of {current_number} and {previous_number} is: {result}")
    previous_number = current_number
