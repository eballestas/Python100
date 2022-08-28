rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random


driver = int(input("What do you choose? Type 0 for Rock, 1 for paper, 2 for scissors: "))

print("You Choose: ")
if driver == 0:
	print(rock)
elif driver == 1:
	print(paper)
elif driver == 2:
	print(scissors)

print("Computer Choose: ")
compdriver = random.randint(0,2)

if compdriver == 0:
	print(rock)
elif compdriver == 1:
	print(paper)
elif compdriver == 2:
	print(scissors)

if compdriver > driver:
	print("Computer Win!")
elif compdriver < driver:
	print("You Win!")
elif driver == compdriver:
	print("it´s a draw!")

