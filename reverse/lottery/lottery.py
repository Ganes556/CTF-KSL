# uncompyle6 version 3.5.0
# Python bytecode 3.6 (3379)
# Decompiled from: Python 2.7.5 (default, Aug  7 2019, 00:51:29) 
# [GCC 4.8.5 20150623 (Red Hat 4.8.5-39)]
# Embedded file name: uler.py
# Compiled at: 2020-03-03 01:44:07
# Size of source mod 2**32: 3338 bytes
from random import randint
FLAG = 'R E D A C T E D'

def banner():
    print('\n+=======================================================+\n|                                                       |\n|    .____           __    __                           |\n|    |    |    _____/  |__/  |_  ___________ ___.__.    |\n|    |    |   /  _ \\   __\\   __\\/ __ \\_  __ <   |  |    |\n|    |    |__(  <_> )  |  |  | \\  ___/|  | \\/\\___  |    |\n|    |_______ \\____/|__|  |__|  \\___  >__|   / ____|    |\n|            \\/                     \\/       \\/         |\n|                                                       |\n+=======================================================+\n')

# [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
def prime():
    prime = []
    for Number in range(1, 51):
        count = 0
        for i in range(2, Number // 2 + 1):
            if Number % i == 0:
                count = count + 1
                break

        if count == 0:
            if Number != 1:
                prime.append(Number)

    return prime

#,ticket2 = [i for i in range(50)]
def check(ticket):
    ticket = list(ticket)
    for i in range(50):
        if(type("a") == type(ticket2[i])):
            ticket[i] = ticket2[i]
            
    if len(ticket) != 50:
        return 'Invalid ticket...'
    prob = 0
    for i in range(50):
        if i in prime():
            if 48 <= ord(ticket[i]) ^ i % 10 <= 57:
                prob += 1
                # ticket2[i] = ticket[i]
            
        else:
            if i % 6 == 0:
                pass
            if i not in prime():
                if 65 <= ord(ticket[i]) - 20 <= 90:
                    prob += 1
                    # ticket2[i] = ticket[i]
            elif i % 5 == 0 and i not in prime():
                if 97 <= ord(ticket[i]) <= 122 and ord(ticket[i]) % 10 == 3:
                    prob += 1
                    # ticket2[i] = ticket[i]
            elif i % 9 == 0 and i not in prime():
                if 48 <= ord(ticket[i]) <= 57:
                    prob += 1
                    # ticket2[i] = ticket[i]
            elif i % 13 == 0 and i not in prime():
                if 65 <= ord(ticket[i]) <= 90:
                    prob += 1
                    # ticket2[i] = ticket[i]
            elif i % 4 == 0 and i not in prime():
                if 97 <= ord(ticket[i]) <= 122:
                    if ord(ticket[i]) % 10 == 7:
                        prob += 1
                        # ticket2[i] = ticket[i]
            elif i % 3 == 0 and i not in prime():
                if 48 <= ord(ticket[i]) ^ i % 3 <= 57:
                    prob += 1
                    # ticket2[i] = ticket[i]
            elif 48 <= ord(ticket[i]) ^ i % 3 <= 57 or 65 <= ord(ticket[i]) ^ i % 10 <= 90 or 97 <= ord(ticket[i]) <= 122 and ord(ticket[i]) % 10 == 7:
                prob += 1
                # ticket2[i] = ticket[i]
    # gabungan = [ticket2,prob]
    # return gabungan

    if prob < 10:
        return 'Try Again...'
    if 10 <= prob <= 25:
        return 'You get $5'
    if 25 < prob <= 40:
        return 'You get $10'
    if 40 < prob <= 49:
        return 'You get $50'
    if prob == 50:
        return 'You got FLAG: {}'.format(FLAG)


def buy():
    
    ticket = ''
    # for i in range(50):
    #     if randint(0, 2) == 0:
    #         ticket += chr(randint(48, 57))
    #     elif randint(0, 2) == 1:
    #         ticket += chr(randint(65, 90))
    #     else:
    #         ticket += chr(randint(97, 122))

    for i in range(50):
        # ticket +=chr(randint(48,122))
        if randint(0, 2) == 0:
            ticket += chr(randint(48, 57))
        elif randint(0, 2) == 1:
            ticket += chr(randint(65, 90))
        else:
            ticket += chr(randint(97, 122))

    return ticket


def menu():
    print('\nMenu:\n\n1. Buy Ticket\n2. Exchange Ticket\n3. Exit\n\n')


def main():
    banner()
    while 1:
        menu()
        inp = input('Input: ')
        if inp == '1':
            print("Here's your ticket: {}\n".format(buy()))
        elif inp == '2':
            ticket = input('Ticket: ')
            print(check(ticket))
            if FLAG in check(ticket):
                exit()
            elif inp == '3':
                print('Goodbye...')
                exit()
            else:
                print('Unknown input\n')
def dbug():
    c = 0
    while(True):

        a = buy()
        # prime -->[0, 1, '3', '3', 4, '1', 6, '4', 8, 9, 10, '7', 12, '3', 14, 15, 16, '2', 18, '0', 20, 21, 22, '7', 24, 25, 26, 27, 28, '0', 30, '1', 32, 33, 34, 35, 36, '6', 38, 39, 40, '9', 42, '0', 44, 45, 46, '5', 48, 49]
        chk = check(a) 
        chk2 = check(a,chk[0])
        
        
        for i in chk2[0]:
            if(type("a") == type(i)):
                c +=1

        print(c)
        if c == 35:
            print(chk2)
            exit() 

        c = 0
            # if(chk[1] == 50):
            #     print("dapat",chk[0])
            #     exit()
        
        
dbug()
# main()
# print(check("ml33a1c4iZj7f3fWg2Z0neg7emnZk0j1nWgmh6fbh9n0bcm5Vd"))
