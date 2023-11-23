#########################   THIS CODE WRITES TEXTS IN A FANCY WAY   #############################

import time
import sys

text = input('Write a text : ')
text = list(text)
pr_text = ""

print()

for i in text:
    if not i.isalpha() :
        pr_text += i
        sys.stdout.write("\r" + pr_text)
        time.sleep(0.1)
        sys.stdout.flush()
    else:
        if i.isupper():
            for j in range(ord('A'), ord(i)+1):
                sys.stdout.write("\r" + pr_text + chr(j))
                time.sleep(0.1)
                sys.stdout.flush()
            pr_text += i
        elif i.islower():
            for j in range(ord('a'), ord(i)+1):
                sys.stdout.write("\r" + pr_text + chr(j))
                time.sleep(0.1)
                sys.stdout.flush()
            pr_text += i
print('\n')




