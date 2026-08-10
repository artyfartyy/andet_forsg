import time

def rindfleisch():
    ы = ""
    counter = int(0)

    æ = input("""
    RINDFLEISCH NIGHT FUNKIN 1.0
    PRESS 'ENTER' TO PLAY
    """)
    if æ == "":
        whopper = True
        start = time.time()
        print("Hurry! Write 'Rindfleisch' 10 times!")

        while whopper == True:
                
                bruh = input()
                if bruh == "Rindfleisch":
                    
                    counter += 1
                    print(ы, counter)
        
                    if counter == 6:
                        print("Keep going!")
                    else: 
                        pass
        
                    if counter == 7:
                        print ("6-7 haha")
                    else:
                        pass
        
                    if counter == 10:
                        end = time.time()
                        length = end - start
                        print(f"""
                        Game over. {length} seconds.""")
        
                        quit()
                else:
                    whopper = False
                    print("GG. Start over. Get good.")
    else:
        print("Fuck you.")                
    
    



rindfleisch()