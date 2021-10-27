def dead(why):
    print(why, "Good Job, you are now dead!")
    exit(0)

prompt_with_break = "\n:> "
prompt = ":> "

#-------------------------------------------------------------------
#
#   COPY FROM BELOW HERE
#
#-------------------------------------------------------------------

def section_x():
    prompt_with_break = "\n:> "
    prompt = ":> "

    option_1_text = "ABC1"
    option_2_text = "ABC2"
    #option_3_text = "ABC3"
    dead_reason_text = "An explanation of your untimely demise."
    #some_option_1_intro_text = "This is the option 1 introductory text." #optional
    #some_option_2_intro_text = "This is the option 2 introductory text." #optional
    #some_option_3_intro_text = "This is the option 3 introductory text." #optional
    intro_text_line1 = "\n123"
    intro_text_line2 = "456"
    intro_text_line3 = "789"

    def decision_prompt_text():
        print("Please choose from the following options: ")
        print(f"1 for {option_1_text}")
        print(f"2 for {option_2_text}")
        #print(f"3 for {option_3_text}")

    print(intro_text_line1)
    print(intro_text_line2)
    print(intro_text_line3)
    decision_prompt_text()
    section_x_choice = input(prompt_with_break)
    if section_x_choice == "1":
        #print(some_option_1_intro_text) #only needed if specified above
        from ex36_XXX import specify_function_here()
        next_func_1()
    elif section_x_choice == "2":
        #print(some_option_2_intro_text) #only needed if specified above
        from ex36_XXX import specify_function_here()
        next_func_2()
    #elif section_x_choice == "3":
        #print(some_option_3_intro_text) #only needed if specified above
        #from ex36_XXX import specify_function_here()
        #next_func_3()
    else:
        print("Last chance?")
        decision_prompt_text()
        section_x_choice = input(prompt)
        if section_x_choice == "1":
            #print(some_option_1_intro_text) #only needed if specified above
            next_func_1()
        elif section_x_choice == "2":
            #print(some_option_2_intro_text) #only needed if specified above
            next_func_2()
        #elif section_x_choice == "3":
            #print(some_option_3_intro_text) #only needed if specified above
            #next_func_3()
        else:
            dead(dead_reason_text)


#-------------------------------------------------------------------
#
#   COPY TO ABOVE HERE
#
#-------------------------------------------------------------------
def next_func_1():
    print("Exit at func 1")
    exit(0)

def next_func_2():
    print("Exit at func 2")
    exit(0)


section_x()
