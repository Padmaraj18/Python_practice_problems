#Practicing a python problems.
""" 3. A List Processor (Functions with Loops)
Functions are often used to process data, such as finding the average of a list of numbers. """

def calculate_average(numbers):
    if not numbers:
        return 0
    total = sum(numbers)
    return total / len(numbers)

# Usage
grades = [85, 90, 78, 92, 100]
avg = calculate_average(grades)

print(f"The class average is: {avg}")