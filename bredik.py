import os

# ____________________________________________________________
def add_litergue(func):
    def wrapper(*args, **kwargs):
        print("^You add litergue^")
        func(*args, **kwargs)
    return wrapper

def add_dress(func):
    def wrapper(*args, **kwargs):
        print("^You add dress^")
        func(*args, **kwargs)
    return wrapper

@add_litergue
@add_dress
def get_boobs(size):
    print(F"Here is your {size} size boobs")


# ____________________________________________________________


file_path = "test.txt"

def check(search_str):
    with open(file_path, 'r', encoding='utf-8') as f:
        for line_num, line in enumerate(f, 1):
            if search_str in line:
                print(F"{search_str} was found on {line_num} line")


if __name__ == "__main__":
    search_for = input("What do you search for?\n")

    check(search_for)