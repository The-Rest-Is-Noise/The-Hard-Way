my_eval1 = True and True
my_eval2 = False and True
my_eval3 = (1 == 1) and 2 == 1
my_eval4 = "test" == "test"
my_eval5 = (1 == 1) and (2 != 1)
my_eval6 = True and (1 == 1)
my_eval7 = False and (0 != 0)
my_eval8 = True or (1 == 1)
my_eval9 = "test" == "testing"
my_eval10 = (1 != 0) and (2 == 1)
my_eval11 = "test" != "testing"
my_eval12 = "test" == 1
my_eval13 = not (True and False)
my_eval14 = not (1 == 1 or 0 != 1)
my_eval15 = not ((10 == 1) or (1000 == 1000))
my_eval16 = not ((1 != 10) or (3 == 4))
my_eval17 = not ("testing" == "testing" and "Zed" == "Douche Bag")
my_eval18 = 1 == 1 and (not ("testing" == 1 or 1 == 0))
my_eval19 = "chunky" == "bacon" and (not (3 == 4 or 3 == 3))
my_eval20 = 3 == 3 and (not ("testing" == "testing" or "Python" == "Fun"))

count = 1

print(f"Q{count}: {my_eval1}")
count += 1
print(f"Q{count}: {my_eval2}")
count += 1
print(f"Q{count}: {my_eval3}")
count += 1
print(f"Q{count}: {my_eval4}")
count += 1
print(f"Q{count}: {my_eval5}")
count += 1
print(f"Q{count}: {my_eval6}")
count += 1
print(f"Q{count}: {my_eval7}")
count += 1
print(f"Q{count}: {my_eval8}")
count += 1
print(f"Q{count}: {my_eval9}")
count += 1
print(f"Q{count}: {my_eval10}")
count += 1
print(f"Q{count}: {my_eval11}")
count += 1
print(f"Q{count}: {my_eval12}")
count += 1
print(f"Q{count}: {my_eval13}")
count += 1
print(f"Q{count}: {my_eval14}")
count += 1
print(f"Q{count}: {my_eval15}")
count += 1
print(f"Q{count}: {my_eval16}")
count += 1
print(f"Q{count}: {my_eval17}")
count += 1
print(f"Q{count}: {my_eval18}")
count += 1
print(f"Q{count}: {my_eval19}")
count += 1
print(f"Q{count}: {my_eval20}")
