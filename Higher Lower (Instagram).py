from art import logo, vs
from game_data import data
import random
import os
def clear(): os.system('cls') #on Windows System

def random_account():
  """Selects a random account from data selection"""
  return random.choice(data)


def format_data(account):
  """Format function breaks down data to present relevant information"""
  name = account["name"]
  description = account["description"]
  country = account["country"]
  return f"{name} is a, {description}, from {country}."

def check_followers(guess, a_followers, b_followers):
  """Checks followers against users guess, returns true if correct and false if wrong"""
  if a_followers > b_followers:
    return guess == "a"
  else:
    return guess == "b"
    
  

def game():
  print(logo)
  score = 0
  game_end = False
  account_a = random_account()
  account_b = random_account()
  while not game_end:
    account_a = account_b
    account_b = random_account()

    while account_a == account_b:
      account_b = random_account()
      
    print(f"Compare A: {format_data(account_a)}")
    print(vs)
    print(f"Against B: {format_data(account_b)}")
    guess = input("Which account has more followers? Select 'A' or 'B': ").lower()
    follower_count_a = account_a["follower_count"]
    follower_count_b = account_b["follower_count"]
    is_correct = check_followers(guess, follower_count_a, follower_count_b)

    clear()
    print(logo)
    if is_correct:
      score += 1
      print(f"That's correct! Your current score is {score}.")
    else:
      game_end = True
      print(f"Game over! Your score was {score}.")
      
    

game()