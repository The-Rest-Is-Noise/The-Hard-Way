def train():

    print("LOG: train()")
    from ex36_lower_boggle import lower_boggle
    from ex36_upper_boggle import upper_boggle
    from ex36_bus import bus
    from ex36_dead import dead

    prompt = ":> "

    intro_text_line1 = "\nYou're standing in the train station and you look for the departures board."
    intro_text_line2 = "You notice that there is a train for Upper Boggle and also a train, from the other platform for Lower Boggle."
    intro_text_line3 = "They are both due in the next few minutes."
    decision_text = """Do you choose to:
1 - get the train to Upper Boggle?
2 - get the train to Lower Boggle?
Select a number from above."""
    decision_text2 = """Do you choose to:
1 - get the train to Upper Boggle?
2 - get the train to Lower Boggle?
3 - go get a bus instead?
Select a number from above."""
    #intro_text_line3 = "After a quarter of an hour the bus pulls into the side of the road and stops."
    #intro_text_line4 = "The driver opens the doors of the bus but says nothing."
    last_chance_text = "You better make a choice - both trains are due in soon."
    dead_reason_text = "You fall asleep on a bench on the platform. A pigeon steals your money and your passport. You slowly turn to dust."

    print(intro_text_line1)
    print(intro_text_line2)
    print(intro_text_line3)
    print(decision_text)
    user_choice = input(prompt)
    if user_choice == "1":
        upper_boggle()
    if user_choice == "2":
        lower_boggle("main_train_station")
    else:
        print(last_chance_text)
        print(decision_text2)
        user_choice = input(prompt)
        if user_choice == "1":
            upper_boggle()
        if user_choice == "2":
            lower_boggle("main_train_station")
        if user_choice == "3":
            bus()
        else:
            print("You stay, slouching where you are, never mustering the courage to make a decision - you drift now as you have always drifted, mere flotsem on the sea of life.")
            dead(dead_reason_text)
