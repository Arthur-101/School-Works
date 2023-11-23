##########################    Counsol Animation    #######################

import time
import sys
import random

#######   >>>>>>   Animation 1   <<<<<<   #######

# animation = "|/-\\"
# start_time = time.time()
# while True:
#     for i in range(4):
#         time.sleep(0.2) here
#         sys.stdout.write("\r" + animation[i % len(animation)])
#         sys.stdout.flush()
#     if time.time() - start_time > 10:  # The animation will last for 10 seconds
#         break
# sys.stdout.write("\rDone!")


#######   >>>>>>   Animation 2   <<<<<<   #######

# emote = ["(-_-)", "(*_*)", "(*_-)", "(-_*)", "(0_0)", "(^_^)", "(^_-)", "(-_^)", "(>_<)", "('_')"]
emote = ["(-_-)", "(*_*)", "(*_-)", "(-_*)", "(^_^)", "(>_<)", "('_')"]
# emote = ["(-_-)", "(^_^)", "(>_<)",]
start_time2 = time.time()
while True:
    # for i in range(4):
    time.sleep(0.4)
    sys.stdout.write("\r"+random.choice(emote))
    sys.stdout.flush()
    time.sleep(0.4)
    sys.stdout.write("\r"+random.choice(emote))
    sys.stdout.flush()
    if time.time() - start_time2 > 15:  # The animation will last for 15 seconds
        break
sys.stdout.write("\rDone!")
