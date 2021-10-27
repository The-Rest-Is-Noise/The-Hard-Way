def bridge():

    print("LOG: bridge()")
    from ex36_pub1 import pub1
    from ex36_library import library
    from ex36_dead import dead

    prompt = ":> "

    intro_text_line1 = "\nYou find yourself on a concrete bridge that spans the main road."
    intro_text_line2 = "When you reach the top of the bridge you can see that the path off the bridge splits in two."
    intro_text_line3 = "To the left you can see what appears to be a pub - you check it out on an app on your phone. It get's good reviews and you note it sells a variety of craft ales."
    intro_text_line4 = "To the right is what appears to be a municpal building of some desciption."
    decision_text = """Do you choose to:
    1 - go left to the pub and seek comfort there?
    2 - go right and see what's in the concrete block?
    Select a number from above."""
    #intro_text_option1 = "You start on your long treck throught the park to the shops, hoping for better things."
    #intro_text_option2 = "...o2"
    last_chance_text = "Come, come Mr Drift, I expect you to live."
    dead_reason_text = """Maybe it simply wasn't meant to be."""

    print(intro_text_line1)
    print(intro_text_line2)
    print(intro_text_line3)
    print(intro_text_line4)
    print(decision_text)
    user_choice = input(prompt)
    if user_choice == "1":
        #print(intro_text_option1)
        pub1()
    if user_choice == "2":
        #print(intro_text_option2)
        library()
    else:
        print(last_chance_text)
        #print(intro_text_line3)
        print(decision_text)
        user_choice = input(prompt)
        if user_choice == "1":
            print(bus_stop2_intro_text)
            pub1()
        if user_choice == "2":
            library()
        else:
            dead(dead_reason_text)

#*************************************************************************
