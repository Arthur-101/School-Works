#Rocket Animation - www.101computing.net/text-based-animations/
import os
import sys
import time

def animate_rocket():
  initial_dist_from_top = 16
  while True:
    print("\n" * initial_dist_from_top)
    print("          /\        ")
    print("          ||        ")
    print("          ||        ")
    print("         /||\        ")
    print("        / :: \       ")
    time.sleep(0.05)
    os.system('cls')  
    initial_dist_from_top -= 1
    if initial_dist_from_top < 0:
      initial_dist_from_top = 20


animate_rocket()

