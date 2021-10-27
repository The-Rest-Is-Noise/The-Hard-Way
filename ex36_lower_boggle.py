def lower_boggle(came_from):

    print("LOG: lower boggle()")
    from ex36_library import library
    from ex36_dead import dead
    from ex36_train import train

    prompt = ":> "

    came_from = came_from
    if came_from == "library_station":
        other_stop = "main_train_station"
    else:
        other_stop = "library_station"

    intro_text_line1 = "\nYou arrive at Lower Boggle. There's not much here, only the train station."
    #intro_text_line2 = "."
    #intro_text_line3 = "."
    decision_text = """Do you choose to:
    1 - stay on the train until the next stop?
    2 - get off and get the train back from whence you came?
    Select a number from above."""
    #intro_text_line3 = "After a quarter of an hour the bus pulls into the side of the road and stops."
    #intro_text_line4 = "The driver opens the doors of the bus but says nothing."
    intro_text_optionMain = "\nYou arrive at the main train station and alight.\n"
    intro_text_optionLibrary = "\nYou arrive at the train statio next to the library.\n"
    last_chance_text = "So many choices. Isn't life hard!"
    dead_reason_text = "You are lost on the outskirts of somewhere, on the ring-road to nowhere, on the verge of indecision."

    print(intro_text_line1)
    #print(intro_text_line2)
    #print(intro_text_line3)
    print(decision_text)
    user_choice = input(prompt)
    print("came_from: ", came_from)
    print("user choice: ", user_choice)
    if user_choice == "1" and came_from == "library_station":
        print(intro_text_optionMain)
        train()
    if user_choice == "1" and came_from == "main_train_station":
        print(intro_text_optionLibrary)
        library()
    if user_choice == "2" and came_from == "library_station":
        print(intro_text_optionLibrary)
        library()
    if user_choice == "1" and came_from == "main_train_station":
        print(intro_text_optionMain)
        train()
    else:
        print(last_chance_text)
        #print(intro_text_line3)
        print(decision_text)
        user_choice = input(prompt)
        if user_choice == "1" and came_from == "library_station":
            train()
        if user_choice == "1" and came_from == "main_station()":
            library()
        if user_choice == "2" and came_from == "library_station":
            library()
        if user_choice == "1" and came_from == "main_station()":
            train()
        else:
            dead(dead_reason_text)
