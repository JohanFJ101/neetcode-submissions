def add_two_numbers() -> int:
    user_input = input()
    result = 0
    for number in user_input.split(","):
        result += int(number)
    return result



# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
