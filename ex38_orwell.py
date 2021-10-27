# George Orwell Novels = GON
# lower case = lc
GON = ["Animal Farm", "The Road to Wigan Pier", "Keep the Aspidistra Flying", "Coming Up For Air", "1984"]
lc_GON = [ x.lower() for x in GON]
GON_range = len(GON)
prompt = ":> "
fav_GON = "<NO ANSWER GIVEN!>"
input_matched = False

print(f"Eric Arthur Blair, more commonly know as George Orwell, wrote the following books:{GON}.")
print("What is your favourite George Orwell novel?")
lc_user_input = input(prompt).lower()

def check_for_match(lc_user_input):
    for i in range(0,GON_range):
        if lc_user_input == lc_GON[i]:
            print("Yes, that's a good one.")
            input_matched = True
            fav_GON = GON[i]
            return(fav_GON, input_matched)

fav_GON, input_matched = check_for_match(lc_user_input)

print(input_matched)
#def check_first_word()
if input_matched == False:
    print("I don't know that one.")
    #print("I'm not sure I know that one.")
    # this strips the first word off of the user first_word_of_user_input
    # split breaks of the first word to create a tuple with 'first' and 'rest of original string'
    # we use ((xxx)[0]) to specify that our variable is set equalt to the first entry in the tuple
    # in other words we stip off eveytihg except the first word
    first_word_of_user_input = (lc_user_input.split(' ', 1)[0])
    first_chars_of_user_input = first_word_of_user_input[:2]
    for i in range(0,GON_range):
        if first_word_of_user_input in lc_GON[i]:
            print("Did you mean:", GON[i], " Y/N?")
            user_answer = input(prompt)
            if user_answer == "Y" or "y":
                fav_GON = GON[i]
                input_matched = True
        else:
            #print("checking 1st 2 chars!")
            #print(f"Checking for: {first_chars_of_user_input} in {lower_case_orwell_novels[i]}")
            if input_matched == False:
                if first_chars_of_user_input in lc_GON[i]:
                    print("Did you mean:", GON[i], " Y/N?")
                    user_answer = input(prompt)
                    if user_answer == "Y" or "y":
                        fav_GON = GON[i]
                        input_matched = True

print("Your favourite George Orwell novel has been recorded as: ")
print(fav_GON)
print("Thank you!")
