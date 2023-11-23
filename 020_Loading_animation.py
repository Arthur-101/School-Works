import time

####   For animation 1   ####
animate = [
 '[=    ]', '[==   ]', '[===  ]', '[==== ]', '[=====]', '[ ====]', '[  ===]', '[   ==]', '[    =]', '[     ]'
]

####   For animation 2   ####
# animate = [
#  '[=    ]', '[ =   ]', '[  =  ]', '[   = ]', '[    =]', '[   = ]', '[  =  ]', '[ =   ]'
# ]

####   For animation 3   ####
# animate = [
#  '[=    ]', '[ =   ]', '[  =  ]', '[   = ]', '[    =]', '[     ]'
# ]

a=0

while True:
    time.sleep(0.2)
    print('\r'+animate[a], end='')
    a += 1
    if a ==  len(animate):
        a = 0
