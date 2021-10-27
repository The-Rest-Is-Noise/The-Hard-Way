def library():

    print("LOG: library()")
    from ex36_lower_boggle import lower_boggle
    from ex36_dead import dead
    from ex36_pub1 import pub1

    prompt = ":> "

    def train_from_library():
        print("You get on the tube and get off at the next stop. You're not sure why.")
        print("These days it seems that you're not sure why you do a lot of things.")
        lower_boggle("library_station")

    intro_text_line1 = "\nYou stand outside a low concrete building built in what you think is called a Municipal Brutalist style."
    intro_text_line2 = "There is a sign above saying 'Library'."
    intro_text_line3 = """You also notice signs suggesting a tube station around the back.
    In the distance you see a building you recognise from a leaflet that came through your door as being the Sports Centre."""
    decision_text = """Do you choose to:
    1 - go in and ask about joining the library?
    2 - get on the tube and see where it takes you?
    3 - decide to sack this off and go find a pub?
    4 - Go and see if you can join the gym  because you heard there's a special on and it's only £99 a month now?
    Select a number from above."""
    #intro_text_line3 = "After a quarter of an hour the bus pulls into the side of the road and stops."
    #intro_text_line4 = "The driver opens the doors of the bus but says nothing."
    option_3_intro_text = "\nUnbound joy! You see there's a pub not far from the library."
    option_4_intro_text = "\nYou start the walk to the sports centre, with unjustified confidence in your ability to morph into the person you wish you were."
    last_chance_text = "It's getting late. Not much life left to live!"
    dead_reason_text = "Joining the library is a kind of living death. On the sight of your membership card you drift off into your own thoughts never to return."

    print(intro_text_line1)
    print(intro_text_line2)
    print(intro_text_line3)
    print(decision_text)
    user_choice = input(prompt)
    if user_choice == "1":
        #print(bus_stop2_intro_text)
        dead(dead_reason_text)
    if user_choice == "2":
        train_from_library()
    if user_choice == "3":
        print(option_3_intro_text)
        pub1()
    if user_choice == "4":
        print(option_4_intro_text)
        sports_centre()
    else:
        print(last_chance_text)
        #print(intro_text_line3)
        print(decision_text)
        user_choice = input(prompt)
        if user_choice == "1":
            #print(bus_stop2_intro_text)
            dead(dead_reason_text)
        if user_choice == "2":
            train_from_library()
        if user_choice == "3":
            print(option_3_intro_text)
            pub1()
        if user_choice == "4":
            print(option_4_intro_text)
            sports_centre()
        else:
            dead_reason_text = "You sit down outside the library. It gets colder and you try to wrap yourself in your arrogance but if fails to keep you warm."
            dead(dead_reason_text)
