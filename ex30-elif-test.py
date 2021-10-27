people = 30
cars = 40
trucks = 15


if people > (5 * trucks):
    print("More peeps than trucks")
elif trucks < cars:
    print("Less cars than trucks")
elif cars > people:
    print("Oh man, More cars than peeps")
else:
    print("You know, we could just walk")
