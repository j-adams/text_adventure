print("Welcome to Pet's Day! Do you want to be a dog or a cat? Write D for dog or C for cat")
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
                    print("It worked! They pet you for a full 5 minutes before going back to get ready for work. Job well done!")
                    print("You take a well deserved nap but when you wake, the humans are gone!")
                    print()
                    person=input("Press (a) to contine")

                    while (person !="a" and person != "A"):
                        print("Please only enter (a)")
                        person=input()

                    if person == "a" or person == "A":
                        print("The house is empty and you listen to the muffled bird chirps and rustle of the leaves. You wish you were outside right now, to be able to enjoy the breeze and all of the exciting smells!")
                        print()
                        print("But wait, what's that? You hear a soft skuttering noise that sounds like it's coming from inside the house!")
                        print()
                        person=input("Do you want to invesigate it?")

                        while(person != "y" and person != "Y" and person != "N" and person != "n"):
                            print("Please only enter (y) or (n)!")
                            person=input()

                        if person == "y" or person == "Y":
                            print("You stalk the noise, following it until it is very, very, close. And guess what? It's coming from inside the walls! You turn a corner and notice a little hole in the wall that is just wide enough for you to squeeze through...")
                            print()
                            person=input("Do you choose to be a Fearless Adorable Little Kitty (part of the famous FALK association) and squeeze into the hole?")

                            while(person != "y" and person != "Y" and person != "N" and person != "n"):
                                print("Please only enter (y) or (n)!")
                                person=input()

                            if person == "Y" or person == "y":
                                print("You become as long as possible and squeeze through the hole and that's when you find a mouse! A real live mouse! It smells so much dirtier than all of your toys, but wow is it entertaining! You find its fear quite simply adorable.")
                                print()
                                print("You chase it and catch it! You take a big juicy bite, but yuck! It tastes awful. Not at all how you had imagined. How disapointing!")
                                print()
                                person=input("You are feeling tired now and escape from inside the walls. Do you want to take a nap?")

                                while(person != "y" and person != "Y" and person != "N" and person != "n"):
                                    print("Please only enter (y) or (n)!")
                                    person=input()

                                if person == "y" or person == "Y":
                                    print("Of course you want to take a nap! Today was tiring! You go to bed inside of a laundry basket that your owners left out. Mobile bed! As you sleep, you dream of that mouse again, but it tastes much better in your dreams.")
                                    print()
                                    print("It's dinner time by the time you wake up and you feel totally energized and ready to meow at your owners again tomorrow. When will those silly humans learn that they have to acknowledge the sun rising?!")
                                    print()
                                    print("Thanks for playing!")

                                elif person == "N" or person == "n":
                                    print("No time for napping! You see some birds and watch as they dance in the sky, salvating over how you wish to be outside to jump and catch them out of the air.")
                                    print()
                                    print("Before you know it, your humans are home! They look especially tired today, but you know one way to wake them up! With your singing!")
                                    print()
                                    person=input("Do you want to sing to them?")

                                    while(person != "y" and person != "Y" and person != "N" and person != "n"):
                                        print("Please only enter (y) or (n)!")
                                        person=input()

                                    if person == "y" or person == "Y":
                                        print("Of course you want to sing to them! You meow at the top of your lungs, 'Firework' by Katy Perry (only you think it's spelled 'Kitty Perry'). They don't seem to appreciate it fully, but at least they did that thing where they stagger their breath to show that they are happy (It's called laughing!). They also give you a little scratch behind the ears. You always knew how to make their strange looking faces change shape (aka smiling)!")
                                        print()
                                        print("What a great day!")
                                        print()
                                        print("Thanks for playing!")

                                    elif person == "N" or person == "n":
                                        print("They don't deserve to hear your beautiful voice. Plus too much work. You've gotta save the hard core vocals for 5 AM.")
                                        print()
                                        print("You end the evening by lying out on a human's lap receiving occasional back scratches. Later that night you dream of performing in one of those big open spaces, like the ones on the light screen (aka a theater seen on a TV).")
                                        print()
                                        print("Thanks for playing!")

                            if person == "N" or person == "n":
                                print("No way were you going to sacrifice your dignity trying to get through that tiny crack in the wall! Nuh uh! You are part of the Scared Adorable Little Kitties (from the famous SALK association) for life! Plus, watching birds is more entertaining anyway.")
                                print()
                                print("You spend the whole day watching them. Before you know it, the humans are home! They look like they're in a good mood too! How would you like to play a game of 'Lie Out, Look Cute, and Wait to be Pet'? It's trending on pinterest! Or that's what your humans say anyway.")
                                print()
                                person=input("So how about it, do you want to play LOLCWP?")

                                while(person != "y" and person != "Y" and person != "N" and person != "n"):
                                    print("Please only enter (y) or (n)!")
                                    person=input()

                                if person == "Y" or person == "y":
                                    print("Of course you want to try to be pet! Not only do you play LOLCWP, but you win too! You're so good at it, it's all of those years of practice.")
                                    print()
                                    print("For the rest of the evening you play intermittent games of LOLCWP. Such a great day!")
                                    print()
                                    print("Thanks for playing!")

                                elif person == "N" or person == "n":
                                    print("Nah, you decide against it. Looking cute is draining and you are already exhuasted from your day. You need your cute-y rest! So you choose to nap and decide that today was a pretty great day.")
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
