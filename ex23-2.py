import sys
script, encoding, error = sys.argv


def main(language_file, encoding, errors):
    line = language_file.readline()
# 'if line:' test to see if the next line of text is NOT empty, and if so executues the specified code
    if line:
        print_line(line, encoding, errors)
        return main(language_file, encoding, errors)


def print_line(line, encoding, errors):
    next_lang = line.strip()
    cooked_string = next_lang.encode(encoding, errors=errors)
    raw_bytes = cooked_string.decode(encoding, errors=errors)
    #raw_bytes = next_lang.encode(encoding, errors=errors)
    #cooked_string = raw_bytes.decode(encoding, errors=errors)

    print(cooked_string, "<===>", raw_bytes)
    #print(raw_bytes)


languages_file = open("ex23output.txt", encoding="utf-8")

main(languages_file, encoding, error)
