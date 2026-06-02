def find_odd(func):
    def wrapper():
        numbers = func()
        print("Odd numbers:")
        for i in numbers:
            if i % 2 != 0:
                print(i)
        return numbers
    return wrapper

def find_even(func):
    def wrapper():
        numbers = func()
        print("Even numbers:")
        for i in numbers:
            if i % 2 == 0:
                print(i)
        return numbers
    return wrapper

@find_odd
@find_even
def get_numbers():
    return [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Run the function
get_numbers()

def count_sum_decorator(func):
    def wrapper(*args, **kwargs):
        numbers, target = func(*args, **kwargs)
        # Count occurrences
        count = numbers.count(target)
        # Sum of all occurrences
        total_sum = target * count
        print(f"Number {target} occurs {count} times")
        print(f"Sum of all occurrences of {target}: {total_sum}")
        return numbers, target
    return wrapper

@count_sum_decorator
def get_data():
    numbers = [1, 2, 3, 2, 4, 2, 5, 6, 2, 7]
    target = 2
    return numbers, target

# Run the function
get_data()
