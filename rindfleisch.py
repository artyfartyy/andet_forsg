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

                            hmm = input("Add score to leaderboard? (y/n) ")
                            hmm = hmm.lower()
                            if hmm in ["y", "yes", "yurr", "ye", "ы", "rindfleisch"]:
                                name = input("Name: ")
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
        
def viewleaderboard():
    hamburg = open("leaderboard.txt", "r")
    print("")
    print(hamburg.read())
    hamburg.close()
    

def addtoleaderboard(name, length):
    with open("leaderboard.txt", "a") as hamburg: # apparently, this saves me of a "hamburg.close()"
        hamburg.write(f"{name}, {length} \n")
    

    with open("leaderboard.txt", "r") as bamhurg:
        lines = bamhurg.readlines()

    lines.sort(key = lambda line: float(line.split()[-1]))

    with open("leaderboard.txt", "w") as ron:
         ron.writelines(lines)
         


    print("Score added.")


def updateleaderboard():
     with open("leaderboard.txt", "r") as bamhurg:
             lines = bamhurg.readlines()
     
     lines.sort(key = lambda line: float(line.split()[-1]))
     
     with open("leaderboard.txt", "w") as ron:
              ron.writelines(lines)


def resetleaderboard():
    hamburg = open("leaderboard.txt", "w")
    hamburg.close()
    print("Ain't that a fact")
    



choosing = input("""
    RINDFLEISCH NIGHT FUNKIN 1.1
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

    case "fuck this game and everyone playing it":
        resetleaderboard()

    case "e":
        quit()

    case "update":
        updateleaderboard()
            
    case _:
        print("Fuck you.")
    



