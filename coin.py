import random

def main():
  counterY = 0
  counterN = 0
  print("Welcome to the coin flipper, where the coin says yes or no.")
  print("It also stores the number of yes and no, if you prefer the most over the other")
  while True:
    print("Use any number for the number of flips. A 0 means you want to restart the counts. To exit, press -1.")
    inputs = input("")
    if int(inputs) == -1:
      if counterY > counterN:
        print("It's a yes!")
      elif counterY < counterN:
        print("It's a no!")
      else:
        print("It's equal...")
      return
    elif int(inputs) == 0:
      counterN = 0
      counterY = 0
      print("All numbers have been reset.")
    else:
      for i in range(int(inputs)):
        random_int = random.randint(1, 2)
        if random_int == 1:
          counterY += 1
        else:
          counterN += 1
      print(f"Up (Yes): {counterY}")
      print(f"Down (No): {counterN}")



if __name__ == "__main__":
  main()
