#########################   THIS CODE WRITES TEXTS IN A FANCY WAY   #############################

import time

text = input('Write a text : ')
print('\n'*32)
text = list(text)
pr_text = []

for i in text:
    if not i.isalpha() :
        pr_text.append(i)
        print(''.join(pr_text))
        print('\n' * 20)
        time.sleep(0.1)
    else:
        if i.isupper():
            for j in range(ord('A'), ord(i)+1):
                for k in pr_text:
                    time.sleep(0.001)
                    print(k, end='')
                # print(chr(j))
                print('\n'*20)
                # time.sleep(0.1)
            pr_text.append(chr(j))
            print()
        elif i.islower():
            for j in range(ord('a'), ord(i)+1):
                for k in pr_text:
                    time.sleep(0.001)
                    print(k, end='')
                # print(chr(j))
                print('\n'*20)
                # time.sleep(0.1)
            pr_text.append(chr(j))
            print()
