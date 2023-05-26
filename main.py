#!/usr/bin/env python
#aqilhafiz
import random

def main():
   """Start a music guessing game. """
   print("Guess the song!")

   song =  [
     "Nafisa",
      "Raja Kertas",
      "Hentian Ini",
      "Titian Perjalanan",
      "Aku Tetap Aku",
      "Apa Nak Di Kata",
      "Semangat Yang Hilang"
     ]
  
   x = random.choice (song)
   print(x)
   guess = None 

   while x != guess:

      guess = str(input("What song of Xpdc is this?"))

      if x == guess:
          print("YOu guessed {} . CONGRATULATIONS you got it ringht !".format(guess))
          break
      else:
          print("You guessed {}. Unfortunately you got the wrong answer. Please try again!". format(guess))

main()
       

  
      



    
  
   