import random
answer=random.randint(1,100)
name=input("enter your name: ")
guess = 0
while guess != answer:
  guess=int(input(F"hay {name} enter a number to guess :"))
  if (guess>answer):
    print(f"{name}your guess {name} was too high")
  elif (guess<answer):
    print(f"your guess {name} was too low")
  else:
    print(f"your guess {name} was correct ")
