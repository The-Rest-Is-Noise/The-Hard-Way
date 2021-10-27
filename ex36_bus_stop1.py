def bus_stop1():

    print("LOG: bus_stop1()")
    from ex36_bus_stop2 import bus_stop2
    from ex36_head_to_shops import head_to_shops
    from ex36_dead import dead

    prompt = ":> "

    intro_text_line1 = "\nYou step down from the bus onto the pavement and notice there is a path leading away from the bus stop."
    intro_text_line2 = "The path leads leads toward some shops. There are several youths loitering near the shops. They seem to be throwing bottles at a small wall."
    intro_text_line3 = "You can always get back on the bus."
    decision_text = """Do you choose to:
    1 - get back on the bus?
    2 - head to the shops and see if you can call a taxi?
    Select a number from above."""
    #intro_text_line3 = "After a quarter of an hour the bus pulls into the side of the road and stops."
    #intro_text_line4 = "The driver opens the doors of the bus but says nothing."
    bus_stop2_intro_text = "\nYou get back on the bus. The driver gives you a quizzicle look but says nothing."
    last_chance_text = "It's a cold night and it's geting dark, you'd best make a move!"
    dead_reason_text = "You feel resigned to your fate and sit down. A pigeon, sensing your growing ennui, lands on you shoulder and pecks at your face. You grow listless and week."

    print(intro_text_line1)
    print(intro_text_line2)
    print(decision_text)
    user_choice = input(prompt)
    if user_choice == "1":
        print(bus_stop2_intro_text)
        bus_stop2()
    if user_choice == "2":
        head_to_shops()
    else:
        print(last_chance_text)
        print(intro_text_line3)
        print(decision_text)
        user_choice = input(prompt)
        if user_choice == "1":
            print(bus_stop2_intro_text)
            bus_stop2()
        if user_choice == "2":
            head_to_shops()
        else:
            dead(dead_reason_text)
