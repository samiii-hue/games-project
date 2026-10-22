import random
print("GAME COLLECTION")
player_name = input("Please enter your name:")
print("Welcome" , player_name , "!")
scores = {"Word Gussing": 0, 
"Rock,Paper,Scissors": 0, 
"Scrambled Words":0 ,
"Fun quiz":0 ,
"Number Gussing":0 ,
"Dooz":0, 
"Esm & Famil":0 ,
"Country_City Gussing":0}

def play_words_gussing():
     words = {"Library" : "A quiet place full of books" ,
"Sunflower" : "A big flower that turns to the sun" ,
"Umbrella": "You use it on rainy days" ,
"Sea": "Blue, full of waves and secrets" ,
"Music": " Sounds with rhythm and melody" ,
"Coffee": "A hot, bitter drink" ,
"Forest" : "A place full of trees and animals" ,
"Robot": "A machine you can program" ,
"Diamond" : "Very hard and very bright" ,
"Hourglass" :"It shows time with sand" ,
"Spaceship": "A vehicle for traveling to space" ,
"Rain": "Water drops from the sky" ,
"Window" : "It lets light and air into a room" ,
"Computer" : "A machine that processes information"}
     
     word = random.choice(list(words.keys()))
     hint = words[word]
     attemps = 3
     print("Word Gussing:)))))")
     print("Hint:" , hint)
     print("Word:", "_" * len(word))
     print("You have" , attemps ,"attemps.")
     
     while attemps > 0:
        guss = input("Guss the word:").strip().lower() 
        if guss == word.lower(): 
               print("Correct! Great job!")
               return True 
        else:
            attemps -= 1 
            if attemps > 0:
               print("Not quite!Try again.")
               print ("Attempts left:" , attemps)
               
     print("Game over! The word was:" , word)
     return False
def play_words_gussing_again():
    while True:
        result = play_words_gussing()
        if result:
            scores["Word Gussing"] += 1
            print("You earned 1 point!")
        answer = input("Play again? (yes/no):" ).strip().lower()
        if answer != "yes":
            print("Returning to Game Menu...")
            break



while True:
    print("******MAIN MENU******")
    print("Player:", player_name)
    print("1. Start Game")
    print("2. View Scores")
    print("3. Exit")
    
    choice = input("Choose an option:")
    
    if choice == "1":
        print("GAME MENU!!!!!!!")
        print("1.Word Gussing")
        print("2.Rock,paper,scissors")
        print("3.Scrambeld Words")
        print("4.Fun quiz")
        print("5.Number Gussing")
        print("6.Dooz")
        print("7.Esm & Famil")
        print("8.Country_City Gussing")
        print("9.Back to the Main Menu")
        
        game_choice = input("Choose a game:")
        
        if game_choice == "9":
             print("Returning to the Main Menu...!")
        elif game_choice == "1":
            result = play_words_gussing_again()
            if result:
                scores["Word Gussing"] += 1
                print("You earned points!")
        elif game_choice in ["3", "2", "4", "5", "6", "7", "8"]:
            print("Your selected game number is:", game_choice)
        else :
             print("Something went wrong! Please try again!")
             
    elif choice == "2":
        print("******SCORE BOARD******:")
        print("player:" , player_name)
        for game, score in scores.items():
            print(game , ":" , score)
            
    elif choice == "3":
        print("Bye Bye,", player_name,"!")
        break 
        
    else:
        print("Some thing went wrong! Please try again.")