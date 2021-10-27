def main():
    print("This is main.")
    print("Let us call: sub one")
    sub_one()
    print("and now for something completely different:")
    sub_two()

def sub_two():
    print("Sub Two.")
    print("Sub Two will now call:")
    sub_one()

def sub_one():
    print("Sub One.")

main()
