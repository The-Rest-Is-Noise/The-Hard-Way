my_string = "Тоҷикӣ"
my_raw  = my_string.encode(encoding="utf-8")
my_string_back = my_raw.decode(encoding="utf-8")
print("DBES: 'dee-bees'")
print(f"Input string: {my_string}")
print("Encode-String: turn'string' into 'bytes':")
print(f"Intermediate (bytes): {my_raw}")
print("Decode-Bytes: turn raw 'bytes' into a 'string': ")
print(f"Output: {my_string_back}")
