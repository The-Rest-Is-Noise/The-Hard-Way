blood_groups = ["A", "B", "O", "AB"]
print(blood_groups)
prompt = ":> "

print("\nPlease enter you blood group. Please select from: ", blood_groups)
user_blood_group = input(prompt)

print("Your blood group is: ", user_blood_group)

#print("That just leaves: ")

#for bg in blood_groups:
#    if bg != user_blood_group:
    #    print(bg)
        ##print(', '.join(blood_groups))

#other_bgs = blood_groups
#print("other before removal: ", other_bgs)
#print("only_not_yours: ", only_not_yours)
#print("Index of user_blood_group is: ", blood_groups.index(user_blood_group))
#only_not_yours = blood_groups.pop(blood_groups.index(user_blood_group))

#print("only_not_yours: ", only_not_yours)

not_your_bgs = blood_groups
removed_your_bg = not_your_bgs.pop(not_your_bgs.index(user_blood_group))
print(not_your_bgs)
