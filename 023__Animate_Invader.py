import os
import sys
import time

def animate_invader():
  initial_dist_top_invader = 0
  final_dist_top_invader = 20
  initial_dist_left_invader = 10
  left_dist_invader = initial_dist_left_invader
  final_dist_left_invader = 80
  step = 1
  
  initial_dist_top_ship = 21
  initial_dist_top_ship_2 = 21
  initial_dist_left_ship = 15
  final_dist_left_ship = 70
  left_dist_ship = initial_dist_left_ship
  step2 = 1

  while True:
    sys.stdout.write("\n"* initial_dist_top_invader+ '\n'+(" "*(initial_dist_left_invader-1)) + "_-^-_"+
        '\n'+(" "*initial_dist_left_invader) + "/|\\"+ '\n'+(" "*(initial_dist_left_invader-1)) + "/ | \\")
    sys.stdout.flush()
    # time.sleep(0.07)
    initial_dist_left_invader += step

    if initial_dist_left_invader > final_dist_left_invader or initial_dist_left_invader <= left_dist_invader:
      step = -step
      initial_dist_top_invader += 3
      initial_dist_top_ship_2 = initial_dist_top_ship - initial_dist_top_invader

      if initial_dist_top_invader > final_dist_top_invader:
        initial_dist_top_invader = 0
        initial_dist_left_invader = left_dist_invader
        step = 1

    sys.stdout.write("\n"* initial_dist_top_ship_2 + '\n'+(" "*(initial_dist_left_ship))+ "_^_"+
                     '\n'+(" "*initial_dist_left_ship) + "\\_/")
    sys.stdout.flush()
    # time.sleep(0.01)
    initial_dist_left_ship += step2

    if initial_dist_left_ship > final_dist_left_ship or initial_dist_left_ship <= left_dist_ship:
        step2 = -step2

    time.sleep(0.005)
    os.system('cls')  



animate_invader()

