def find_max(numbers):
    max_value = numbers  
    for number in numbers[1:]:   
        if number > max_value:
            max_value = number   
    return max_value

# Example usage
numbers = [10, 24, 76, 23, 12]
print(find_max(numbers))   