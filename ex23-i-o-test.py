#my_string = "Тоҷикӣ"
my_file = open("ex23-i-o-test-file.txt", "rb")
my_raw = my_file.read()
my_file.close()

print(f"Input bytes: {my_raw}")

my_string = my_raw.decode()
my_raw_back = my_string.encode()


print(f"String: {my_string}")
print(f"Output bytes: {my_raw_back}")
