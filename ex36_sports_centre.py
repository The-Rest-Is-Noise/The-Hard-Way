def sports_centre():

    print("LOG: sports_centre()")
    from ex36_upper_boggle import upper_boggle
    from ex36_library import library
    from ex36_dead import dead

    prompt = ":> "

    intro_text_line1 = "\nYou stand outside the hulk that is the municipal sports centre."
    intro_text_line2 = "You wonder briefly what you're doing here, how your life turned out like this."
    intro_text_line3 = """In the distance you see the library. You know there's a pub over that way somewhere."""
    decision_text = """Do you choose to:
    1 - go in and ask about that limited offer on membership that, in you heart-of-hearts, you know you'll never use?
    2 - get the Hell out of here and go back to Upper Boggle on the train?
    3 - wander over to the library, you heard they DVDs too now?
    4 - sit on one of the benches and have a long hard think about your life."""
    #intro_text_line3 = "After a quarter of an hour the bus pulls into the side of the road and stops."
    #intro_text_line4 = "The driver opens the doors of the bus but says nothing."
    option_3_intro_text = "\nUnbound joy! You see there's a pub not far from the library."
    option_4_intro_text = "\nYou start the walk to the library, with unjustified confidence in your ability to sharpen up."
    last_chance_text = "It's getting late in the day, the sky is beginning to bruise and night must fall."
    dead_reason_text1 = """You spend nearly an hour filling out forms and giving over a load of additional personal data.
    You sign up for the family membership even though you live alone. This on it's own makes you want to cry.
    You go home and turn on the gas and just sit there in silence. It's the calmest you're felt in years."""
    dead_reason_text2 = """It's the fact that you held life's tiller with so slight a grip that brought you here,
    and in this moment you can't find the courage to change. You sit on the grass and weep inwardly wishing it was all over.
    Your wish is granted sooner than you could imagine as you soon fall asleep on the garss and a fox eats your throat out leaving your bleed out, slowly, and silently."""

    print(intro_text_line1)
    print(intro_text_line2)
    print(intro_text_line3)
    print(decision_text)
    user_choice = input(prompt)
    if user_choice == "1":
        #print(bus_stop2_intro_text)
        dead(dead_reason_text1)
    if user_choice == "2":
        upper_boggle()
    if user_choice == "3":
        print(option_3_intro_text)
        library()
    else:
        print(last_chance_text)
        #print(intro_text_line3)
        print(decision_text)
        if user_choice == "1":
            #print(bus_stop2_intro_text)
            dead(dead_reason_text1)
        if user_choice == "2":
            upper_boggle()
        if user_choice == "3":
            print(option_3_intro_text)
            library()
        else:
            dead(dead_reason_text2)
