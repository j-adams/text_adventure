print("Welcome to Pet's day! Do you wan to be a dog or a cat? Write D for dog or C for cat")
person = input()

while (person != "c" and person != "C" and person != "D" and person != "d"):
    print("Please only enter D or C!")
    person=input()

if person == "C" or person == "c":
    print("Congrats! You're a cat! Press (a) to continue")
    person= input()
    
    while (person != "a" and person != "A"):
        print("Please only enter (a)")
        person=input()
        
    if (person == "a" or person == "A"):
        print("It's 5 AM, the sun is finally up, and you are wide awake. Your humans, however, do not yet know that the sun has risen (Silly humans!).")
        print()
        person=input("Do you want to tell them? Press (y) for yes or (n) for no.")

        while (person != "y" and person != "Y" and person != "N" and person != "n"):
            print("Please only enter (y) or (n)")
            person=input()

        if person == "Y" or person == "y":
            print("Success! After only half an hour (new record!) of meowing at the top of your little lungs, your humans are finally awake!")
            print()
            print("Despite knowing that the sun is up, they don't look very happy...")
            print()
            person=input("Press (a) to continue")

            while (person !="a" and person != "A"):
                print("Please only enter (a)")
                person=input()

            if person == "a" or person == "A":
                print("You have to make a split second decision!")
                print()
                person=input("Do you try to look as cute as possible to appease them?")

                while(person != "y" and person != "Y" and person != "N" and person != "n"):
                    print("Please only enter (y) or (n)!")
                    person=input()

                if person == "Y" or person == "y":
                    print("It worked! They pet you for a full 5 minutes before going back to work. Job well done! You end up spending the entire day watching birds and taking naps, a truly successful day.")
                    print()
                    print("Thanks for playing!")

                if person == "N" or person == "n":
                    print("Retreat! Retreat! Those humans could never catch you! You run too fast. What an adventure! Now you're starting to feel tired...")
                    print()
                    person=input("Do you go back to bed?")

                    while(person != "y" and person != "Y" and person != "N" and person != "n"):
                        print("Please only enter (y) or (n)!")
                        person=input()

                    if person == "Y" or person == "y":
                        print("Sleeping is nice. By the time you wake up, your owners are back and you are happy to see them. You get to eat chicken flavored wetfood, your favorite!")
                        print()
                        print("Thanks for playing!")

                    elif person == "N" or person == "n":
                        print("You have a super active day! Being lazy is for dogs. You on the other hand, watched baby robins fly all around! You could practically feel the wind in your fur. Too bad your house doesn't have a cat door...Still an amazing day!")
                        print()
                        print("Thanks for playing!")
                    
        elif person == "N" or person == "n":
            print("Meowing loudly for a long time just didn't seem worth it. Those humans are going to be silly no matter how much you try to help them.")
            print()
            print("You kept sleeping and now it is 8 AM! Your humans are at work and you have the whole house to yourself. What to do...")
            print()
            person=input("Press (a) to continue")

            while (person !="a" and person != "A"):
                print("Please only enter (a)")
                person=input()

            if person == "a" or person == "A":
                print("You look up. There's a shiny object somewhere up high and it looks vaguely like a fishbowl...")
                print()
                person=input("Do you want to investigate it?")

                while (person != "y" and person != "Y" and person != "N" and person != "n"):
                    print("Please only enter (y) or (n)!")
                    person=input()

                if person == "Y" or person == "y":
                    print("No mystery unsolved for you! It is in fact a fishbowl with a tasty lookin goldfish inside, mmm...")
                    print()
                    person=input("Press (a) to continue")

                    while (person !="a" and person != "A"):
                        print("Please only enter (a)")
                        person=input()

                    if person == "a" or person == "A":
                        print("It looks awfully tasty and you're really hungry...")
                        print()
                        person=input("Do you attempt to eat it?")

                        while (person != "y" and person != "Y" and person != "N" and person != "n"):
                            print("Please only enter (y) or (n)!")
                            person=input()

                        if person == "Y" or person == "y":
                            print("You caught it! And later when your owners got home, they caught you... and were not happy. They made you spend two weeks outside with only dryfood, no wetfood. But it was worth it, that goldfish was tasty!")
                            print()
                            print("Thanks for playing!")

                        if person == "N" or person == "n":
                            print("Good choice, when you got home your owners were so happy that you hadn't destroyed the house that they gave you an extra long pettin session. You also got to play with a brand new feather toy they brought home, what a day!")
                            print()
                            print("Thanks for playing!")

                elif person == "N" or person == "n":
                    print("You go back to sleep for the whole day. Besides a couple licking and stretching breaks. A nice relaxing day! Investigating is too much work anyway.")
                    print()
                    print("Thanks for playing!")

                



if person == "D" or person == "d":
    print("Boo! Dogs suck! They are too needy. Based on your choice, I can tell that you will be a failure at life and failures don't deserve to play this game :(")
    print()
    print("Hang your head in shame and reevaluate your life's choices!")

