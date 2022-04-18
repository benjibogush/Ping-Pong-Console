import random

file1 = open("fruits.txt", "r") # Opens the "fruits" file
fruits1 = file1.read()
fruits1 = fruits1.split("\n") # Splits into a list
fruits1.remove(fruits1[116])
fruits = []
for i in fruits1:
  i = i.lower()
  fruits.append(i)

file2 = open("animals.txt", "r") 
animals1 = file2.read()
animals1 = animals1.split("\n") 
animals1.remove(animals1[314])
animals = []
for i in animals1:
  i = i.lower()
  animals.append(i)

categories = ["Fruits", "Animals"] # List of categories
category = random.choice(categories) # Gets a random category

rounds = 1  # Keeps track of number of rounds
used_words = [] # List of used words

# Lists of animals and fruits for computer
less_animals1 = ['Ant', 'Baboon', 'Badger', 'Bat', 'Bear', 'Beaver', 'Camel', 'Cat', 'Clam', 'Cobra', 'Cougar', 'Coyote', 'Crow', 'Deer', 
'Dog', 'Donkey', 'Duck', 'Eagle', 'Ferret', 'Fox', 'Frog', 'Goat', 'Goose', 'Hawk', 'Lion', 'Lizard', 'Llama', 'Mole', 'Monkey', 
'Moose', 'Mouse', 'Mule', 'Newt', 'Otter', 'Owl', 'Panda', 'Parrot', 'Pigeon', 'Python', 'Rabbit', 'Ram', 'Rat', 'Raven', 'Rhino', 
'Salmon', 'Seal', 'Shark', 'Sheep', 'Skunk', 'Sloth', 'Snake', 'Spider', 'Stork', 'Swan', 'Tiger', 'Toad', 'Trout', 'Turkey', 'Turtle', 
'Weasel', 'Whale', 'Wolf', 'Wombat', 'Zebra']

less_fruits1 = ['Apple', 'Apricot', 'Avocado', 'Banana', 'Blueberry', 'Blackberry', 'Cantaloupe', 'Cherry', 'Coconut', 'Cranberry', 'Date', 'Dragonfruit', 
'Durian', 'Fig', 'Grape', 'Grapefruit', 'Guava', 'Honeydew', 'Jackfruit', 'Kiwi', 'Kumquat', 'Lemon', 'Lime', 'Loquat', 'Lychee', 'Mandarin', 'Mango', 
'Melon', 'Mulberry', 'Orange', 'Papaya', 'Peach', 'Pear', 'Persimmon', 'Plum', 'Pineapple', 'Pomegranate', 'Raspberry', 'Strawberry', 'Tomato', 'Watermelon']

less_animals = []
less_fruits = []
for i in less_animals1:
  less_animals.append(i.lower())
for i in less_fruits1:
  less_fruits.append(i.lower())