import time
import random
import threading as t


def rindfleisch():

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
                            length = end - start
                            print(f"""
                            It took you {length} seconds to write Rindfleisch 10 times.""")

                            hmm = input("Add score to leaderboard? (y/n) ")

                            if hmm == "y":
                                 addtoleaderboard()
            
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
#        burger = 69420
        
def viewleaderboard():
    hamburg = open("leaderboard.txt", "r+")
    print(hamburg.read())

def addtoleaderboard(name, score):
   
    hamburg = open("leaderboard.txt", "a")
    






å = input("""
    RINDFLEISCH NIGHT FUNKIN 1.1
    PRESS 'ENTER' TO PLAY
    INPUT 'L' TO VIEW LEADERBOARD
    """)

æ = å.lower()

if æ == "":
    rindfleisch()

elif æ == "l":
    viewleaderboard()
        

                
else:
    print("Fuck you.")                
    



