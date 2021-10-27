my_raw = b'\xe1\x8a\xa0\xe1\x88\x9b\xe1\x88\xad\xe1\x8a\x9b'
#my_file = open("ex23-i-o-test-file.txt", "rb")
#my_raw = my_file.read()

# my_file.close()

#print(my_raw)
my_string = my_raw.decode()
my_raw_back = my_string.encode()

#print("DBES: 'dee-bees'")
print(f"Input bytes: {my_raw}")
#print("Decode-Bytes: ")
print(f"Intermediate (string): {my_string}")
#print("Encode-String: ")
print(f"Output: {my_raw_back}")
print(" ")
