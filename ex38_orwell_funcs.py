# George Orwell Novels = GON
# lower case = lc
GON = ["Animal Farm", "The Road to Wigan Pier", "Keep the Aspidistra Flying", "Coming Up For Air", "1984"]
lc_GON = [ x.lower() for x in GON]
GON_range = len(GON)
prompt = ":> "
fav_GON = "<NO ANSWER GIVEN!>"
input_matched = False

def check_for_match(lc_user_input, fav_GON, input_matched):
    for i in range(0,GON_range):
        if lc_user_input == lc_GON[i]:
            print("Yes, that's a good one.")
            input_matched = True
            fav_GON = GON[i]
        else:
            input_matched = False
    return(fav_GON, input_matched)

def check_first_word(lc_user_input, fav_GON, input_matched):
    if input_matched == False:
        first_word_of_user_input = (lc_user_input.split(' ', 1)[0])
        for i in range(0,GON_range):
            if first_word_of_user_input in lc_GON[i]:
                print("Did you mean:", GON[i], " Y/N?")
                user_answer = input(prompt)
                if user_answer == "Y" or "y":
                    fav_GON = GON[i]
                    input_matched = True
        return(fav_GON, input_matched)

def check_1st_2_chars(lc_user_input, fav_GON, input_matched):
    if input_matched == False:
        first_word_of_user_input = (lc_user_input.split(' ', 1)[0])
        first_chars_of_user_input = first_word_of_user_input[:2]
        for i in range(0,GON_range):
            if first_chars_of_user_input in lc_GON[i]:
                print("Did you mean:", GON[i], " Y/N?")
                user_answer = input(prompt)
                if user_answer == "Y" or "y":
                    fav_GON = GON[i]
                    input_matched = True
        return(fav_GON, input_matched)


print(f"George Orwell, wrote the following books:{GON}.")
print("Which of these is your favourite George Orwell novel?")
lc_user_input = input(prompt).lower()
fav_GON, input_matched = check_for_match(lc_user_input, fav_GON, input_matched)
if input_matched == False:
    print("I don't know that one.")
    fav_GON, input_matched = check_first_word(lc_user_input, fav_GON, input_matched)
if input_matched == False:
    fav_GON, input_matched = check_1st_2_chars(lc_user_input, fav_GON, input_matched)

print("Your favourite George Orwell novel has been recorded as: ")
print(fav_GON)
