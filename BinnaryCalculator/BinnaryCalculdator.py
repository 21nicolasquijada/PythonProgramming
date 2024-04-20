#COMENTAR CODIGO
#COMENTAR CODIGO
import random
import time

execute = 0

while True:
    start = time.time()
    range_ = int(input("Type a range to give you a number: \n"))
    value = random.randint(0,range_)
    print("You must transform ", value, " to binnary.")
    
    while True:
    
        binnary_response = int(input("Give me your response:\n"),2)
    
        if bin(value) == bin(binnary_response):
            print("WELL DONE!\n")
            print("  XXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
            print(" XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
            print("XXXXXXXXXXXXXXXXXX         XXXXXXXX")
            print("XXXXXXXXXXXXXXXX              XXXXXXX")
            print("XXXXXXXXXXXXX                   XXXXX")
            print(" XXX     _________ _________     XXX")
            print("  XX    I  _xxxxx I xxxxx_  I    XX")
            print(" ( X----I         I         I----X )")
            print("( +I    I      00 I 00      I    I+ )")
            print(" ( I    I    __0  I  0__    I    I )")
            print("  (I    I______ /   \_______I    I)")
            print("   I           ( ___ )           I")
            print("   I    _  :::::::::::::::  _    i")
            print("    \    \___ ::::::::: ___/    /")
            print("     \_      \_________/      _/")
            print("       \        \___,        /")
            print("         \                 /")
            print("          |\             /|")
            print("          |  \_________/  |")

    
            response = input("Do yo want try with another number? (y/n):\n")
    
            response.lower()
    
            if response == 'n':
                print("Thank you for use the programm.")
                exit()
            else:
                print("I will give you antother number. Good Luck.")
                time.sleep(3)
                break
        else:
            print("Ooops, that's not correct. Try again: \n")
            print("You must transform ", value, " to binnary.")
            end = time.time()
            
            if end-start > 120.0:
                y_n = input("Surrender? (y/n):\n")
                if y_n.lower() == "n":
                    start = time.time()
                    continue
                    
                else:
                    print("The correct binnary value of " , value, "is ", bin(value)) #Cambiar para que no aparezca "0b" 
                    exit()
    


