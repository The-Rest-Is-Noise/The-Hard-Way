def add(a, b):
    print(f"Adding {a} + {b}")
    return a + b

def subtract(a, b):
    print(f"Subtracting {a} - {b}")
    return a - b

def multiply(a, b):
    print(f"Multiplying {a} * {b}")
    return (a * b)

def divide(a, b):
    print(f"Divinding {a} / {b}")
    return(a / b)

print("Let us do some math with just functions.")
print("Please enter two values to add for AGE: ")
age_val1 = float(input("value 1:> "))
age_val2 = float(input("value 2:> "))
age = add(age_val1, age_val2)
print(f"THE VALUE FOR AGE IS: {age}")

height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print(f"Age: {age}, Height {height}, Weight: {weight}, IQ: {iq}.")

print("Here is a puzzle.")

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print("That becomes: ", int(what), " Can you do that by hand?")
