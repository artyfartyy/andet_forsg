import time
import random
import threading as t


def rindfleisch(): # the game itself + encouraging messages

    counter = int(0)
    whopper = True
    start = time.time()
    #        t.Timer(5, loss).start()
    print("Hurry! Input 'Rindfleisch' 10 times!")
    
    while whopper == True:
    
                    cheese = False
                    bruh = input()
    
    
                    if bruh == "Rindfleisch":
                        
                        counter += 1
            
                        if counter in [4, 5, 6, 8] and cheese == False:
                            morty = random.randint(1, 4)
                            if morty == 4:
                                print(f"{counter}. Keep going!")
                                cheese = True
                            else:
                                print(f"{counter}!")
    
                        elif counter == 7: 
                            josh = random.randint(1, 4)
                            if josh == 4:
                                print("6-7 haha")
                            else:
                                print("7!")
    
                        elif counter == 10:
                            print("10! Game over.")
                            end = time.time()
                            leng = end - start
                            length = round(leng, 3)
                            print(f"""
                            It took you {length} seconds to write Rindfleisch 10 times.""")

                            time.time()
                            time.sleep(1.5)
                            time.time()

                            presence = False
                            hmm = input("Add score to leaderboard? (y/n) ")
                            hmm = hmm.lower()
                            if hmm in ["y", "yes", "yurr", "ye", "ы", "rindfleisch"]:
                                name = input("Name: ")
                                name = name.upper()

                                with open("leaderboard.txt", "r") as hamburg:
                                    hamburg.readlines()


                                #if name in hamburg: # 13/08/2026 21:15 UTC +1: i'm TRYING to create an overwrite mechanic
                                #    presence = True

                                #else:
                                #    pass
                                
                                addtoleaderboard(name, length)
                            else:
                                 pass
                            
                            quit()
    
                        
                            
                        
                        else:
                            print(f"{counter}!")
    
                    else:
                        whopper = False
                        print("""
                        GG. Start over. Get good.
                        """)
#    def loss():
#        global burger
#        burger = 69420   - here I tried to make the game stop itself after 60 seconds, will retry at another point
        
def viewleaderboard(): # prints out a numerated leaderboard
    with open("leaderboard.txt", "r") as hamburg:
        print("")
        lines = hamburg.readlines()
        for number, entry in enumerate(lines, start=1):
            if number <= 3:
                print(f"{number}! {entry}")
            else:
                print(f"{number}. {entry}")
    

def test(): # prints amount of entries in leaderboard
    with open("leaderboard.txt", "r") as hamburg:
        strc = hamburg.readlines()
        print(len(strc))


def cheataddtoleaderboard(): # manually add a name and a time record to the board
    naem = str(input("name: "))
    naem = naem.upper()
    time = float(input("time: "))

    with open("leaderboard.txt", "r") as fleisch:
            butter = fleisch.readlines()
            for i, entry in enumerate(butter):
                if naem in entry:
                    butter.pop(i)
                    break
                else:
                     pass
                
    with open("leaderboard.txt", "w") as booh:
          booh.writelines(butter)

    with open("leaderboard.txt", "a") as hamburg:
          hamburg.write(f"{naem}, {time} \n")

        
    with open("leaderboard.txt", "r") as bamhurg:
            lines = bamhurg.readlines()

            lines.sort(key = lambda line: float(line.split()[-1])) # according to chatgpt, the "-1" was the cause of my suffering all along

            maxentries = 10
            lines = lines[:maxentries]
            
    with open("leaderboard.txt", "w") as ron:
          ron.writelines(lines)
            
            
    
    #with open("leaderboard.txt", "w") as ron:
            #ron.writelines(lines)
             
    
    #with open("leaderboard.txt", "w") as hrskæg:
    #        for number, entry in enumerate(lines, start=1):
    #            if number <= 3:
    #                hrskæg.write(f"{number}! {entry}")             this is so horrible now that I look back at it
    #            else:
    #                hrskæg.write(f"{number}. {entry}")
    

def massadd(): # adds 10 unnumerated artys to the leaderboard
     # to numerate artys, add another name with cheataddtoleaderboard()
     with open("leaderboard.txt", "a") as hamburg:
                for i in range(10):
                    time = random.randint(1, 69)
                    hamburg.write(f"arty, {time} \n")
     with open("leaderboard.txt", "r") as bamhurg:
                 lines = bamhurg.readlines()
                 lines.sort(key = lambda line: float(line.split()[-1]))
     
                 
         
     with open("leaderboard.txt", "w") as ron:
                 ron.writelines(lines)
                  
     #with open("leaderboard.txt", "r") as burh:
                    # strc = burh.readlines()
                    # if len(strc) > 10:
                    #     strc.pop(10)
                    # else:
                    #     pass
     #with open("leaderboard.txt", "w") as hrskæg:
     #           for number, entry in enumerate(lines, start=1):
     #               if number <= 3:
     #                   hrskæg.write(f"{number}! {entry}")
     #               else:
     #                   hrskæg.write(f"{number}. {entry}")
    
         
def addtoleaderboard(name, length): # adds name to leaderboard after a game

    
    fleisch = open("leaderboard.txt", "r")
    butter = fleisch.readlines()

    for i, entry in enumerate(butter):
            if name in entry:
                aynrand = float(entry.split()[-1])
                if aynrand > length:
                    butter.pop(i)
                    break
                else: 
                    print("Score not added. Do better next time.")
                    quit()
            else:
                 pass
    fleisch.close()

    with open("leaderboard.txt", "w") as booh:
             booh.writelines(butter)
    



    with open("leaderboard.txt", "a") as hamburg: # apparently, this saves me of a "hamburg.close()"
        hamburg.write(f"{name}, {length} \n")

    

    with open("leaderboard.txt", "r") as bamhurg:
        lines = bamhurg.readlines()
        lines.sort(key = lambda line: float(line.split()[-1]))

        maxentries = 10
        lines = lines[:maxentries]

    with open("leaderboard.txt", "w") as ron:
        ron.writelines(lines)
         
    
    
    #with open("leaderboard.txt", "w") as hrskæg:
        #for number, prst in enumerate(strc, start=1):
            #hrskæg.write(f"{number}. {prst}")

    print("Score added.")


def updateleaderboard():
    with open("leaderboard.txt", "r") as bamhurg:
             lines = bamhurg.readlines()
             lines.sort(key = lambda line: float(line.split()[-1]))
     
    with open("leaderboard.txt", "w") as ron:
             ron.writelines(lines)
              
    with open("leaderboard.txt", "r") as burh:
                 strc = burh.readlines()
                 if len(strc) > 10:
                     strc.pop(10)
                 else:
                     pass
         
    with open("leaderboard.txt", "w") as hrskæg:
             hrskæg.writelines(strc)


def resetleaderboard(): # for emergency/testing/ragequit purposes
    areyousure = input("Are you sure? ")
    areyousure = areyousure.lower()
    if areyousure == "yes":
        hamburg = open("leaderboard.txt", "w")
        hamburg.close()
        print("Ain't that a fact")
    else:
        quit()


choosing = input("""
    RINDFLEISCH NIGHT FUNKIN 1.2
    PRESS 'ENTER' TO PLAY
    INPUT 'L' TO VIEW LEADERBOARD
    INPUT 'E' TO EXIT
    """)

æ = choosing.lower()

match æ: # if/else is still more spiritually fulfilling imo, I just had to try this out
    case "":
        rindfleisch()

    case "l":
        viewleaderboard()

    case æ if æ in ["fuck this game and everyone playing it"]:
        resetleaderboard()

    case "e":
        quit()

    case "Lorem ipsum dolor sit amet vinum rubrum dies irae dies illa solvet saechlum in favilla teste David cum Sybilla":
        updateleaderboard()

    case "howmanyentries":
          test()

    case "thegreatleaderboardreplacement":
          massadd()

    case "add":
          cheataddtoleaderboard()

    case "massadd":
            massadd()

    case "print":
          ghamburg = open("leaderboard.txt", "r")
          glines = ghamburg.readlines()
          print(glines)
          print(len(glines))
          ghamburg.close()
            
    case _:
        print("Invalid input.")

    
    



