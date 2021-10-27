def upper_boggle():

    print("LOG: upper Boggle()")
    from ex36_sports_centre import sports_centre
    from ex36_dead import dead
    from ex36_train import train

    prompt = ":> "
    intro_text_line1 = "\nYou arrive at Upper Boggle. Nearby you see the sports centre."
    #intro_text_line2 = "."
    #intro_text_line3 = "."
    decision_text = """Do you choose to:
    1 - stay on the train until the you reach the main train station?
    2 - get off and go to the sports centre?
    Select a number from above."""
    #intro_text_line3 = "After a quarter of an hour the bus pulls into the side of the road and stops."
    #intro_text_line4 = "The driver opens the doors of the bus but says nothing."

    last_chance_text = "So many choices. Isn't life hard!"
    dead_reason_text = "Upper Boggle saps your will to live. Slowly your body's organs start to shut down."

    print(intro_text_line1)
    #print(intro_text_line2)
    #print(intro_text_line3)
    print(decision_text)
    user_choice = input(prompt)
    if user_choice == "1":
        train()
    if user_choice == "2":
        sports_centre()
    else:
        print(last_chance_text)
        #print(intro_text_line3)
        print(decision_text)
        user_choice = input(prompt)
        if user_choice == "1":
            train()
        if user_choice == "2":
            sports_centre()
        else:
            dead(dead_reason_text)
