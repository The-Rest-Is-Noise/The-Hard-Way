# this one is like yoiur scripts with argv
def print_two(*args):
    arg1, arg2 = args
    print(f"Let's play: {arg1}{arg2}")


def print_two_again(arg1, arg2):
    # arg1, arg2 = args
    print(f"arg1: {arg1}, arg2 = {arg2}")

def print_one(arg1):
    print(f"arg1: {arg1}")

def print_none():
    print("I ain't got nuffin' bud!")

print_two("Mambo ", "#9")
print_two_again("Zed's", "Dead")
print_one("I want a pot belly.")
print_none()
