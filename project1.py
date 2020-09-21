"""
CS 3620
Choose Your Own Adventure
Author: Suresh Shrestha
Date: 9/20/2020
"""

options_ab = ["A", "a", "B", "b"]
options_abc = ["A", "a", "B", "b", "C", "c"]


def begin():
    print("Welcome to 'Choose Your Own Adventure' Game! ")
    name = input("Please enter your name: ")
    print("Hello " + name + "!" + " Now that we are ready, lets play...")


def narrative():
    print("You're sitting at home and your stomach growls, you realize you haven't eaten and need to decide on food.")
    decision_point1()


def decision_point1():
    decision = ''
    while decision not in options_ab:
        decision = input("Do you: \n [A] Cook your own food or \n [B] Go get food: ")
        if decision == 'A' or decision == 'a':
            narrative_cook()
        elif decision == 'B' or decision == 'b':
            narrative_get_food()
        else:
            print("Invalid input.")


def narrative_get_food():
    print("You type into your phone 'Food near me' and a list of places to eat pops up. It’s late and most of "
          "the places are closed. ")
    decision_point12()


def decision_point12():
    decision = ''
    while decision not in options_ab:
        decision = input("Do you: \n [A] Get Fried Chicken or \n [B] Get Pizza: ")
        if decision == 'A' or decision == 'a':
            narrative_chicken()
        elif decision == 'B' or decision == 'b':
            narrative_pizza()
        else:
            print("Invalid input.")


def narrative_pizza():
    print("You Decide to go buy a cheap pizza but realize that it’s too much food for just you so you invite a friend. "
          "\nAs your friend arrives you notice a crowd of people behind them. You were not prepared for a party.")
    decision_point13()


def decision_point13():
    decision = ''
    while decision not in options_ab:
        decision = input("Do you: \n [A] Tell them all to go home or \n [B] Have a party anyway: ")
        if decision == 'A' or decision == 'a':
            narrative_go_home()
        elif decision == 'B' or decision == 'b':
            narrative_party()
        else:
            print("Invalid input.")


def narrative_party():
    print("You decide to order more Pizza and invite everyone inside. You meet a bunch of people and eventually "
          "lose yourself in the night. \nThe next morning you wake up in a parking lot with no additional "
          "recollection of the night before and several strange texts and new contacts in your phone. \nYou spend "
          "the next week trying to figure out what happened the night of the party but no one seems to remember. "
          "\nYou begin to think you’re going insane but eventually carry on with your life as though nothing happened.")


def narrative_go_home():
    print("You let your friend know that you were just wanting to get one pizza for dinner and that you are not "
          "wanting a bunch of people over tonight. \nAfter some time, you eventually gather the crowd that had "
          "somehow already entered your house and kick them all out. \nEveryone goes home disappointed and you "
          "decide you are now too exhausted to eat. \nYou decide to sleep instead and end up having a dream about "
          "a pizza eating a crowd of people rather than a crowd of people eating pizza.")


def narrative_chicken():
    print("You go get fried chicken and eat alone in your car. \nAs you look around you realize this chicken place "
          "is in a sketchy area, you’re pretty sure you see a drug deal go down but are not entirely sure. \nYou lock "
          "your doors, eat quickly and drive away. \nAs you go to sleep, you make a mental note to buy pepper "
          "spray the next time you can.")


def narrative_cook():
    print("You look in your pantry and notice it is bare. You need to gather ingredients.")
    decision_point2()


def decision_point2():
    decision = ''
    while decision not in options_ab:
        decision = input("Do you: \n [A] Go to the store or \n [B] Go to the garden: ")
        if decision == 'A' or decision == 'a':
            narrative_store()
        elif decision == 'B' or decision == 'b':
            pass
        else:
            print("Invalid input.")


def narrative_store():
    print("You drive to the store and get the ingredients that you need, as you're checking out a masked man walks in "
          "holding up a gun and proclaiming that they are robbing the place.")
    decision_point3()


def decision_point3():
    decision = ''
    while decision not in options_ab:
        decision = input("Do you: \n [A] Give them your money and belongings or \n [B] Fight: ")
        if decision == 'A' or decision == 'a':
            narrative_give_money()
        elif decision == 'B' or decision == 'b':
            narrative_fight()
        else:
            print("Invalid input.")


def narrative_fight():
    print("As the robber points the gun at you, you start raging in fear. In seconds the rage builds up courage and you"
          "decide you can take on the robber in a fight")
    decision_point4()


def decision_point4():
    decision = ''
    while decision not in options_abc:
        decision = input("Do you: \n [A] Kick the gun out of his hands or \n [B] Run at him with your fists or "
                         "\n [C] Quickly search for something to use as a weapon : ")
        if decision == 'A' or decision == 'a':
            narrative_kick_gun()
        elif decision == 'B' or decision == 'b':
            narrative_fists()
        elif decision == 'C' or decision == 'c':
            narrative_search_weapon()
        else:
            print("Invalid input.")


def narrative_search_weapon():
    print("As you stare death in the eyes, you look around and notice a fire extinguisher and a snicker bar.")
    decision_point5()


def decision_point5():
    decision = ''
    while decision not in options_ab:
        decision = input("Do you: \n [A] Use the fire extinguisher or \n [B] Use the Snickers bar: ")
        if decision == 'A' or decision == 'a':
            narrative_extinguisher()
        elif decision == 'B' or decision == 'b':
            narrative_snickers()
        else:
            print("Invalid input.")


def narrative_snickers():
    print("You lift the snickers bar up to the robber and hand it over to him as you exclaim 'You're not you "
          "when you're hungry'. \nThe robber glares and accepts the Snickers bar, as they take the first bite, you "
          "give them a big hug. \n'Glad to have you back Grandma'")


def narrative_extinguisher():
    print("You pick up the fire extinguisher and shoot it at his eyes. \nAs the robber is blinded a shot is fired from "
          "his gun. \nYou run to hit him in the head and he passes out from the blow. \nYou look to see where his shot "
          "landed and yo notice that it hit a ceiling light. \nEveryone cheers, the authorities arrive and the robber"
          "is caught")


def narrative_fists():
    print("Clenching your fingers into your palms you charge towards the robber. \nThe robber stares directly at you "
          "and without a second of hesitation, heartlessly shoots you in the head. \nYou die immediately, the robber "
          "loots your body and your lifeless carcass is left on the grocery store floor until the cops arrive.")


def narrative_kick_gun():
    print("You attempt to kick the gun out of his hand and discover that you’re not as flexible as you remembered "
          "being. \nYou instead kick the air and the robber looks at you in confusion.")
    decision_point6()


def decision_point6():
    decision = ''
    while decision not in options_ab:
        decision = input("Do you: \n [A] Kick again or \n [B] Claim that you were killing a spider: ")
        if decision == 'A' or decision == 'a':
            narrative_kick_again()
        elif decision == 'B' or decision == 'b':
            narrative_spider()
        else:
            print("Invalid input.")


def narrative_spider():
    print("You look the robber dead in the eyes and say that there was a massive spider and you had to kill it. \n"
          "Luckily, the robber is terrified of spiders and thanks you for serving your community by removing "
          "it’s spiders.")
    decision_point7()


def decision_point7():
    decision = ''
    while decision not in options_ab:
        decision = input("Do you: \n [A] Pull your pet tarantula out of your pocket  or \n [B] Talk with the robber "
                         "about how great community service is: ")
        if decision == 'A' or decision == 'a':
            narrative_tarantula()
        elif decision == 'B' or decision == 'b':
            narrative_community_service()
        else:
            print("Invalid input.")


def narrative_community_service():
    print("You thank the robber for his compliment and then proceed to tell him about how great serving the community "
          "is. \nThe robber politely nods and starts looking around you notice he’s anxious as though he’s running "
          "out of time.")
    decision_point8()


def decision_point8():
    decision = ''
    while decision not in options_ab:
        decision = input("Do you: \n [A] Continue talking with the robber or \n [B] Invite the robber for dinner : ")
        if decision == 'A' or decision == 'a':
            narrative_keep_talking()
        elif decision == 'B' or decision == 'b':
            narrative_dinner()
        else:
            print("Invalid input.")


def narrative_keep_talking():
    print("You continue your conversation with the robber and discover that the robber is your neighborhood "
          "librarian. \nYou begin to discuss various books you’ve read and exchange recommendations. \nBy the end of "
          "the conversation the robber is comfortable with you and expresses that he is in a financial crisis and "
          "would not be robbing the place if he was not so tight on cash. \nYou offer to create a go-fund-me for the "
          "librarian, they accept and eventually get back on their feet and continue to serve the community.")


def narrative_tarantula():
    print("As you pull you beloved Fuzzball out of your pocket, you strike fear in the robber eyes. \nYou then exclaim "
          "that this is your Favorite spider named Colby and that you were collecting the other spider as a snack for "
          "him. \nThe robber is terrifyingly interested in your spider and you proceed to tell him fun spider facts "
          "until he forgets about the robbery, you both exit the store with spider in hand.")


def decision_point9():
    decision = ''
    while decision not in options_ab:
        decision = input("Do you: \n [A] Go get dinner with robber while talking about your sweet Colby or "
                         "\n[B] Exchange Phone numbers with robber and refer them to a good pet store: ")
        if decision == 'A' or decision == 'a':
            narrative_dinner()
        elif decision == 'B' or decision == 'b':
            narrative_phone()
        else:
            print("Invalid input.")


def narrative_dinner():
    print("You and the robber go to dinner and hit it off. \nYou start dating and enjoy sharing with all your family "
          "and friends the story of how you two met the loves of your lives.")

    
def narrative_phone():
    print("The robber texts you a week later with a picture of his new BFF Henry who is also a tarantula. \nAfter "
          "several months of chatting you have become close friends with the robber and you all live a life of "
          "happiness and spiders.")
    

def narrative_kick_again():
    print("You attempt to kick again and fail. The robber has now realized that you are trying to fight him and "
          "takes you as hostage.")
    decision_point10()


def decision_point10():
    decision = ''
    while decision not in options_ab:
        decision = input("Do you: \n [A] Keep fighting or \n [B] Surrender: ")
        if decision == 'A' or decision == 'a':
            narrative_fighting()
        elif decision == 'B' or decision == 'b':
            narrative_surrender()
        else:
            print("Invalid input.")


def narrative_surrender():
    print("Because the robber now has a hostage, everyone complies with his demands. You loose all your "
          "belongings and walk home barefoot.")

    
def narrative_fighting():
    print("You notice the robber is fairly close to you now in order to hold the gun at your head, so you decide "
          "to do your cool fighting combo that you used to practice after playing video games as a kid. \nThis time, "
          "you successfully hit  your opponent and they are briefly stunned.")
    decision_point11()


def decision_point11():
    decision = ''
    while decision not in options_ab:
        decision = input("Do you: \n [A] Hit again or \n [B] Grab his gun and run: ")
        if decision == 'A' or decision == 'a':
            narrative_hit_again()
        elif decision == 'B' or decision == 'b':
            narrative_gun_run()
        else:
            print("Invalid input.")


def narrative_gun_run():
    print("you take off with his gun and run for a few blocks, as you run you notice several people on their "
          "phones staring at you and realize they have all called the authorities be cause they fear that you’re "
          "a danger. You realize the only option is to go to the authorities yourself and report the incident. After "
          "giving your description, the authorities were able to locate and capture the criminal. You stop back at "
          "the grocery store where the Manager gives you your groceries for free. You are then able to go home and "
          "enjoy your dinner.")


def narrative_hit_again():
    print("You hit him again and as you continue hitting him he decides to fight back, he notices the gun in his "
          "hand and fires. \nYou have been shot in a non vital organ and are knocked unconscious. \nYou wake up in "
          "a hospital bed with no ID or money, the cops arrive to interrogate you. \nYou tell them your story and "
          "spend the next 3 months recovering from the bullet wound.")
    

def narrative_give_money():
    print("You reach for your belongings and realize you have not paid for your groceries. \nYou ask the robber if "
          "you can keep enough money to pay for what you have. \nThe Robber kindly agrees to your request and then "
          "proceeds to take the same funds from the store clerk as you walk away free. \nHeart racing you go home and "
          "cook up the most exciting meal you’ve ever eaten. \nIt was not until after you ate your last bite that you "
          "remembered to report the robbery to the authorities.")


begin()
narrative()
