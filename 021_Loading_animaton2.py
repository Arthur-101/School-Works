import time

timer = 0.03
start = ':|'
forward_sign = '='
backward_sign = '='
end = '|:'
space = ' '
m=0
n= int(input("Enter the length of loading bar (eg. 10, 15, 20, etc.) : "))


####   For Animation 1   ####
# while True:
#     animate = start + space*m + forward_sign + space*(n-m) + end
#     time.sleep(timer)
#     print('\r'+ animate, end='')
#     m += 1
#     if m>n:
#         m=0


####   For Animation 2   ####
# while True:
#     sign = forward_sign
#     if m==n:
#         for j in range(m):
#             animate = start + space*m + sign + space*(n-m) + end
#             time.sleep(timer)
#             print('\r'+ animate, end='')
#             m -= 1
#             sign = backward_sign
#     else:
#         animate = start + space*m + sign + space*(n-m) + end
#         time.sleep(timer)
#         print('\r'+ animate, end='')
#         m += 1
#         sign = forward_sign


####   For Animation 3   ####
# while True:
#     if m==n:
#         for j in range(m):
#             animate = start + space*(n-m) + forward_sign*m + end
#             time.sleep(timer)
#             print('\r'+ animate, end='')
#             m -= 1
#     else:
#         animate = start + forward_sign*m + space*(n-m) + end
#         time.sleep(timer)
#         print('\r'+ animate, end='')
#         m += 1

action = int(input('''Choose a number :\n1. Single arrow forward\n2. Single arrow forward and backward\n3. Multi Arrow
                   \nYour Pick? : '''))

if action == 1:

    ####   For Animation 1   ####
    while True:
        animate = start + space*m + forward_sign + space*(n-m) + end
        time.sleep(timer)
        print('\r'+ animate, end='')
        m += 1
        if m>n:
            m=0

elif action == 2:

    ####   For Animation 2   ####
    while True:
        sign = forward_sign
        if m==n:
            for j in range(m):
                animate = start + space*m + sign + space*(n-m) + end
                time.sleep(timer)
                print('\r'+ animate, end='')
                m -= 1
                sign = backward_sign
        else:
            animate = start + space*m + sign + space*(n-m) + end
            time.sleep(timer)
            print('\r'+ animate, end='')
            m += 1
            sign = forward_sign

elif action == 3:

    ####   For Animation 3   ####
    while True:
        if m==n:
            for j in range(m):
                animate = start + space*(n-m) + forward_sign*m + end
                time.sleep(timer)
                print('\r'+ animate, end='')
                m -= 1
        else:
            animate = start + forward_sign*m + space*(n-m) + end
            time.sleep(timer)
            print('\r'+ animate, end='')
            m += 1

