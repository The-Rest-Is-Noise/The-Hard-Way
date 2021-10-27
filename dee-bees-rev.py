#my_string = "Тоҷикӣ"
my_raw = b'\xd0\xa2\xd0\xbe\xd2\xb7\xd0\xb8\xd0\xba\xd3\xa3'
my_string = my_raw.decode(encoding="utf-8")
my_raw_back = my_string.encode(encoding="utf-8")

print("DBES: 'dee-bees'")
print(f"Input bytes: {my_raw}")
print("Decode-Bytes: ")
print(f"Intermediate (string): {my_string}")
print("Encode-String: ")
print(f"Output: {my_raw_back}")
