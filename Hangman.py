import random

def hangman():
    guess_list=["england","india","pakistan","london","paris","newyork","turkey"]    
    word=random.choice(guess_list)
    chance=10
    correct_guess=""
    guess_words=set("abcdefghijklmnopqrstuvwxyz")
    
    while len(word)>0 :
        main_word=""
        
        
        for letter in word:
            
            if letter in correct_guess:
                main_word+=letter
            else:
                main_word+="_ "
                
                
        if main_word == word:
            print(f"    <<< {main_word.upper()} >>> ")
            print("    CONGRATULATIONS        ")
            print("  Your Guess is Correct")
            print("       You Won!!!       ")
            break
        
        
        print(f"Guess the Word {main_word}")
        guess=input()
        
        
        
        if guess in guess_words:
            correct_guess+=guess
        else:
            print("wrong charecter")
            print("please enter the valaid charecter")
            guess=input()

        
        if guess not in word:
            chance-=1
            
            if chance == 9:
                print()
                print("OOPS WRONG...")
                print("Now you have only 9 chance")
                print("---------------------")
                print("         o           ")
                
                
            if chance == 8:
                print()
                print("OOPS WRONG...")
                print("Now you have only 8 chance")
                print("---------------------")
                print("         o           ")
                print("         |           ")
                
                
            if chance == 7:
                print()
                print("OOPS WRONG...")
                print("Now you have only 7 chance")
                print("---------------------")
                print("         o           ")
                print("        \|/          ")
                
            
            if chance == 6:
                print()
                print("OOPS WRONG...")
                print("Now you have only 6 chance")
                print("---------------------")
                print("         o           ")
                print("        \|/          ")
                
                
            if chance == 5:
                print()
                print("OOPS WRONG...")
                print("Now you have only 5 chance")
                print("---------------------")
                print("         o           ")
                print("        \|/          ")
                print("         |           ")
                
            if chance == 4:
                print()
                print("OOPS WRONG...")
                print("Now you have only 4 chance")
                print("---------------------")
                print("         o           ")
                print("        \|/          ")
                print("         |           ")
                
            if chance == 3:
                print()
                print("OOPS WRONG...")
                print("Now you have only 3 chance")
                print("---------------------")
                print("         o           ")
                print("        \|/          ")
                print("         |           ")
                print("        /            ")
            
            if chance == 2:
                print()
                print("OOPS WRONG...")
                print("Now you have only 2 chance")
                print("---------------------")
                print("         o           ")
                print("        \|/          ")
                print("         |           ")
                print("        / \          ")
                
            if chance == 1:
                print()
                print("OOPS WRONG...")
                print("Now you have only 1 chance")
                print("----------------------")
                print(" _________            ")
                print("|                     ")
                print("|         o           ")
                print("|        \|/          ")
                print("|         |           ")
                print("|        / \          ")
                
                
            if chance == 0:
                print()
                print("    Oh NO... you missed all the chance     ")
                print("        Bad luck You lose the Game         ")
                print("         You let a Good Men Die :(         ")
                print(" <<< ---------------------------------- >>>")
                print(" _________            ")
                print("|         |           ")
                print("|         o           ")
                print("|        \|/          ")
                print("|         |           ")
                print("|        / \          ")
                break                




print("""  
      ---<<<<<<<<  HANGMAN GAME  >>>>>>>>--- 
      
      """)

name=input("ENTER YOUR NAME :-- ").upper()
print(f"""
            WELCOME {name}!   
        ---------------------  
    <<< Let's Start the Hangman Game >>> 
"You have 10 Chance to Guess the Correct Word 

""")

hangman()