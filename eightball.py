import random
name = input("Enter your name please and thank you: ")
question=""

answer = ""


def the_question():
  global question
  question = input(name + ", please enter your question : ")
  eightball_response()

def eightball_response():
  random_number = random.randint(1, 10)
  global answer
  if random_number == 1:
    answer = "Yeah"
    play_again()
  elif random_number == 2:
    answer = "very much yes!"
    play_again()
  elif random_number == 3:
    answer = "Without a doubt"
    play_again()
  elif random_number == 4:
    answer = "its nap time sorry"
    play_again()
  elif random_number == 5:
    answer = "not right now doing hot girl stuff"
    play_again()
  elif random_number == 6:
    answer = "wouldnt you like to know"
    play_again()
  elif random_number == 7:
    answer = "the law says no"
    play_again()
  elif random_number == 8:
    answer = "probs not homie"
    play_again()
  elif random_number == 9:
    answer = "heck nah"
    play_again()
  elif random_number == 10:
    answer = "never in a million years"
    play_again()
  else:
    answer = "Error"
    play_again()

def play_again():
  print(name + " asks: " + question)
  print("Magic 8 Ball's answer: " + answer)
  print("do you have another question," + name)
  
  proceed = input("Y or N: ").lower()
  if proceed == "y":
    print("Now running again: ")
    the_question()
  elif proceed == "n":
    print("have a nice day!")
  else:
    print("sorry please enter something else")

the_question()




