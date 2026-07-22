from typing import List

def read_integers() -> List[int]:
    user_input = input()

    my_list = []

    for element in user_input.split(","):
        my_list.append(int(element))

    return my_list


# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
