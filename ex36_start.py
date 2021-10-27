def start():
    print("LOG: start()")
    from ex36_bus import bus
    from ex36_train import train
    #from ex36_ice_cream_van import ice_cream_van

    prompt = ":> "
    dead_reason_text = "You fall asleep on a bench."
    intro_text_line1 = "\nYou stumble around, waiting for life to come calling."
    intro_text_line2 = """Do you choose to:
1 - get on the bus,
2 - catch a train
Select a number from above."""
    #intro_text_line3 = "After a quarter of an hour the bus pulls into the side of the road and stops."
    #intro_text_line4 = "The driver opens the doors of the bus but says nothing."
    last_chance_text = "You better grab these opportunities while you can!"

    print(intro_text_line1)
    print(intro_text_line2)
    user_choice = input(":>")
    if user_choice == "1":
        bus()
    if user_choice == "2":
        train()
    else:
        print(last_chance_text)
        print(intro_text_line2)
        user_choice = input(prompt)
        if user_choice == "1":
            bus()
        if user_choice == "2":
            train()
        else:
            print("Passersby are starting to notice you and you suspect there may soon be a scene.")
            dead(dead_reason_text)
