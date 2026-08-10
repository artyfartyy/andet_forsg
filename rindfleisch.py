import time
import random
import threading as t


def rindfleisch():

#    def loss():
#        global burger
#        burger = 69420
        

    counter = int(0)

    æ = input("""
    RINDFLEISCH NIGHT FUNKIN 1.0
    PRESS 'ENTER' TO PLAY
    """)

    if æ == "":
            
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
        
                        quit()

                    
                        
                    
                    else:
                        print(f"{counter}!")

                else:
                    whopper = False
                    print("""
                    GG. Start over. Get good.
                    """)

                
    else:
        print("Fuck you.")                
    
    
rindfleisch()