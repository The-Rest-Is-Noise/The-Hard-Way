def section_x():
    option_1 = "fill me in 1"
    option_2 = "fill me in 2"
    decision_prompt_text = "Decide: do you choose to do '{option 1}' or '{option 2}'?"
    some_option_1_intro_text = "This is the option 1 introductory text." #optional
    some_option_2_intro_text = "This is the option 2 introductory text." #optional
    option_1_text = "name of option 1"
    option_2_text = "name of option 2"
    dead_reason = "an explanation of your untimely demise"

    print("\n")
    print("Some intro. text.")
    print("Some more intro. text.")
    print(decision_prompt_text)

    section_x_choice = input(prompt_with_break)
    if section_x_choice == option_1_text:
        print(some_option_1_intro_text) #only needed if specified above
        next_func_1()
    elif section_x_choice == option_2_text:
        print(some_option_2_intro_text) #only needed if specified above
        next_func_2()
    else:
        print("Last chance?")
        print(decision_prompt_text)
        section_x_choice = input(prompt)
        if section_x_choice == option_1_text:
            print(some_option_1_intro_text) #only needed if specified above
            next_func_1()
        elif section_x_choice == option_2_text:
            print(some_option_2_intro_text) #only needed if specified above
            next_func_2()
        else:
            dead(dead_reason)
