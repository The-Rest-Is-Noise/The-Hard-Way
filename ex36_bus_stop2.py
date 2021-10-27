def bus_stop2():

    print("LOG: bus_stop1()")
    from ex36_bridge import bridge
    from ex36_head_to_shops import head_to_shops
    from ex36_dead import dead

    prompt = ":> "

    intro_text_line1 = "\nYou are still the only passenger."
    intro_text_line2 = "The bus moves off and after a few minutes the driver turns into a side road. Several more minutes pass before the driver turns to you and says 'This is the last stop mate'."
    intro_text_line3 = "He then pulls the bus to the side of the road and again opens the doors. you have no choice but to alight."
    intro_text_line4 = "When you get off the bus you notice some shops away in the distance on the other side of some park land. There is also a bridge over the road but you can't see where it goes."
    decision_text = """Do you choose to:
    1 - try walking all the way back to the shops?
    2 - chance it and head over the bridge?
    Select a number from above."""
    intro_text_option1 = "You start on your long treck throught the park to the shops, hoping for better things."
    intro_text_option2 = "You start to walk up, over the bridge."
    last_chance_text = "It's a cold night and it's geting dark, from what's left of the light you see it's cloudy now too. Best not to hang around or you'll become bacalmed in these urban doldrums."
    dead_reason_text = """Years of frustration have taken their toll on you, you have lost all your fight.
    It starts to rain a little and you attempt to take shelter under the branches
     of a lonely looking and somewhat bare tree. It offers lower comfort."""

    print(intro_text_line1)
    print(intro_text_line2)
    print(intro_text_line3)
    print(intro_text_line4)
    print(decision_text)
    user_choice = input(prompt)
    if user_choice == "1":
        print(intro_text_option1)
        head_to_shops()
    if user_choice == "2":
        print(intro_text_option2)
        bridge()
    else:
        print(last_chance_text)
        #print(intro_text_line3)
        print(decision_text)
        user_choice = input(prompt)
        if user_choice == "1":
            print(bus_stop2_intro_text)
            head_to_shops()
        if user_choice == "2":
            bridge()
        else:
            dead(dead_reason_text)

#*************************************************************************
