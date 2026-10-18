print("GAME COLLECTION")
player_name = input("Please enter your name:")
print("Welcome" , player_name , "!")
scores = {"Word Gussing": 0, 
"Rock,Paper,Scissors": 0, 
"Scrambled Words":0 ,
"Fun quiz":0 ,
"number Gussing":0 ,
"Dooz":0, 
"Esm & Famil":0 ,
"Country_City Gussing":0}
print("player:" , player_name)
print("Your score are ready!")
print("SCORE BOARD:")
print("player:" , player_name)
for game, score in scores.items():
    print(game , ":" , score)
