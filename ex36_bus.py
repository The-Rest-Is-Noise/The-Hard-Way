def bus():
    print("LOG: bus()")
    from ex36_bus_stop1 import bus_stop1
    from ex36_bus_stop2 import bus_stop2
    from ex36_dead import dead

    prompt = ":> "

    intro_text_line1 = "\nYou're sitting at the back of the top-deck of a double-decker."
    intro_text_line2 = "After a while the bus pulls into the side of the road. The driver opens the doors."
    decision_text = """Do you choose to:
1 - get of the bus and explore?
2 - stay on the bus and see where it goes?
Select a number from above."""
    #intro_text_line3 = "After a quarter of an hour the bus pulls into the side of the road and stops."
    #intro_text_line4 = "The driver opens the doors of the bus but says nothing."
    last_chance_text = "You better make a choice. Life and bus drivers don't wait for ever."
    dead_reason_text = "You fall asleep at the back of the bus."

    print(intro_text_line1)
    print(intro_text_line2)
    print(decision_text)
    user_choice = input(prompt)
    if user_choice == "1":
        bus_stop1()
    if user_choice == "2":
        bus_stop2()
    else:
        print(last_chance_text)
        print(decision_text)
        user_choice = input(prompt)
        if user_choice == "1":
            bus()
        if user_choice == "2":
            train()
        else:
            print("You stay, slouching where you are, never mustering the courage to make a decision - you drift now as you have always drifted, mere flotsem on the sea of life.")
            dead(dead_reason_text)
