# George Orwell Novels = GON
# lower case = lc
slots = ["Mon am", "Mon pm", "Tue am", "Tue pm", "Wed am", "Wed pm", "Thu am", "Thu pm", "Fri am", "Fri pm"]
lc_slots = [ x.lower() for x in slots]
slots_range = len(slots)-1
prompt = ":> "
selected_slot_1 = "<NULL>"
selected_slot_2 = "<NULL>"
input_matched = False




print("Please pick a time for your session: ")
for i in range (0,slots_range):
    print(f"{slots[i]}")
lc_user_input = input(prompt).lower()

day = lc_user_input.split(' ', 1)
day_2_char = day[2:]

print(lc_user_input)
print(day_2_char)

if day in lc_slots:
    app_day = day
else:
    for i in range(0,slots_range):
        if day_2_char in lc_slots[i]:
            #print("Did you mean:", GON[i], " Y/N?")
            user_answer = input(prompt)
            if user_answer == "Y" or "y":

                input_matched = True
