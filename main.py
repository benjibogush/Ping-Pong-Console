#/bin/python3
import random, time
from helper import *

print("Let's play word ping-pong!")
print("")
time.sleep(1)

# The Rules
print("How to play this game: ")
print("For example, the category is countries.")
print("The computer is your opponent.")
print("If you go first, you have to think of a country and type it in 5 seconds.")
print("If it takes more than 5 seconds to do that, you lose.")
print("What you think of cannot be something that you or the computer already said.")
print("Then it is the computer's turn, and it's the same rules for the computer.")
print("If you can't think of anything in the category, type 'idk.'")
print("")
time.sleep(2)

while True:
  rounds += 1
  print("Do you want to play easy mode or hard mode?")
  print("Type 'e' for easy and 'h' for hard mode.")
  time.sleep(1)
  mode = input(">")
  
  if mode != 'e' and mode != 'h': 
    while True: # repeats until player types "e" or "h"
      print("")
      print("Invalid input.")
      mode = input(">")
    
      if mode == 'e' or mode == 'h':
        break
  
  print("")
  
  print("The category is...") # tell the category
  time.sleep(1)
  print(category + "!")
  time.sleep(1)
  
  if category == 'Fruits':
    less_category = less_fruits
    category1 = fruits
    group = "fruit"
    
  else:
    less_category = less_animals
    category1 = animals
    group = "animal"
  
  # Codes for easy mode
  if mode == 'e': 
      print("The game is easy mode. You go first.")
      
      while True:
        t1 = time.perf_counter()
        player = input(">")
        player = player.lower()
        t2 = time.perf_counter() - t1
        
        if player == 'idk':
          time.sleep(1)
          print("")
          print("Computer wins!")
          break
        
        if player == '':
          time.sleep(1)
          print("")
          print("You typed nothing...")
          time.sleep(1)
          print("Computer wins!")
          break
        
        if player in used_words:
          print("That word was already used...")
          time.sleep(1)
          print("Computer wins!")
          break
        
        if player in category1:
          if player in less_category:
            less_category.remove(player)
            used_words.append(player)
            
          if t2 <= 5:
            print("")
            print("Computer's turn...")
            
            if less_category == []: # if computer ran out of words in category:
              print("The computer ran out of {}s...".format(group))
              time.sleep(1)
              print("You win!")
              break
            
            length = random.randint(1,6) # Sometimes takes 6 seconds for computer in easy mode
            word = random.choice(less_category).lower()
            time.sleep(length)
            print(word)
            print("")
            less_category.remove(word)
            used_words.append(word)
            
            if length == 6:
              time.sleep(1)
              print("Uh oh! It took the computer more than 5 seconds...")
              time.sleep(1)
              print("You win!")
              break
            
            print("Your turn.")
          
          else:
            print("")
            print("That took you more than 5 seconds...")
            time.sleep(1)
            print("Computer wins!")
            break
        
        elif player not in category1:
          print("")
          print("That is not a real {}...".format(group))
          time.sleep(1)
          print("Computer wins!")
          break
  
  # Codes for hard mode
  elif mode == 'h':
    print("The game is in hard mode. You go first.")
    less_category = list(category1)
    
    while True:
        t1 = time.perf_counter()
        player = input(">")
        player = player.lower()
        t2 = time.perf_counter() - t1
        
        if player == 'idk':
          time.sleep(1)
          print("Computer wins!")
          break
        
        if player == '':
          time.sleep(1)
          print("")
          print("You typed nothing...")
          time.sleep(1)
          print("Computer wins!")
          break
        
        if player in used_words:
          print("That word was already used...")
          time.sleep(1)
          print("Computer wins!")
          break
        
        if player in category1:
          if player in less_category:
            less_category.remove(player)
            used_words.append(player)
            
          if t2 <= 5:
            print("")
            print("Computer's turn...") 
            
            if less_category == []: 
              print("The computer ran out of {}s...".format(group))
              time.sleep(1)
              print("You win!")
              break
            
            word = random.choice(less_category).lower()
            time.sleep(1)
            print(word)
            print("")
            less_category.remove(word)
            used_words.append(word)
            
            print("Your turn.")
          
          else:
            print("")
            print("That took you more than 5 seconds...")
            time.sleep(1)
            print("Computer wins!")
            break
        
        elif player not in category1:
          print("")
          print("That is not a real {}...".format(group))
          time.sleep(1)
          print("Computer wins!")
          break
        
  time.sleep(1)
  print("__________________________________________")
  time.sleep(1)
  print("Round {}!".format(rounds))
  time.sleep(1)
  print("Want to play another round? y/n")
  time.sleep(1)
  new_round = input(">")
  
  while new_round != 'y' and new_round != 'yes' and new_round != 'n' and new_round != 'no':
    print("")
    print("Invalid input.")
    time.sleep(1)
    new_round = input(">")
  
  if new_round == 'y' or new_round == 'yes':
    print("")
    used_words = []
  
  elif new_round == 'n' or new_round == 'no':
    print("")
    print("Okay then.")
    break
      
      
      
      
      
    
    