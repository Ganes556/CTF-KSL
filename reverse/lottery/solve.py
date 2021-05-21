# uncompyle6 version 3.7.4
# Python bytecode 3.6 (3379)
# Decompiled from: Python 2.7.18 (default, Apr 20 2020, 20:30:41) 
# [GCC 9.3.0]
# Warning: this version of Python has problems handling the Python 3 "byte" type in constants properly.

# Embedded file name: uler.py
# Compiled at: 2020-03-03 01:44:07
# Size of source mod 2**32: 3338 bytes
from random import randint
FLAG = 'R E D A C T E D'

def banner():
    print('\n+=======================================================+\n|                                                       |\n|    .____           __    __                           |\n|    |    |    _____/  |__/  |_  ___________ ___.__.    |\n|    |    |   /  _ \\   __\\   __\\/ __ \\_  __ <   |  |    |\n|    |    |__(  <_> )  |  |  | \\  ___/|  | \\/\\___  |    |\n|    |_______ \\____/|__|  |__|  \\___  >__|   / ____|    |\n|            \\/                     \\/       \\/         |\n|                                                       |\n+=======================================================+\n')


def prime():
    prime = []
    for Number in range(1, 51):
        count = 0
        for i in range(2, Number // 2 + 1):
            if Number % i == 0:
                count = count + 1
                break

        if count == 0 and Number != 1:
            prime.append(Number)

    return prime


def check(ticket,ticket2 = [i for i in range(50)]):
    ticket = list(ticket)

    # for i in range(50):
    #     if(type("a") == type(ticket2[i])):
    #         ticket[i] = ticket2[i]

    if len(ticket) != 50:
        return 'Invalid ticket...'
    prob = 0
    for i in range(50):
        if i in prime():
            if 48 <= ord(ticket[i]) ^ i % 10 <= 57:
                prob += 1
                ticket2[i] = ticket[i]
        elif i % 6 == 0 and i not in prime():
            if 65 <= ord(ticket[i]) - 20 <= 90:
                prob += 1
                ticket2[i] = ticket[i]
        elif i % 5 == 0 and i not in prime():
            if 97 <= ord(ticket[i]) <= 122 and ord(ticket[i]) % 10 == 3:
                prob += 1
                ticket2[i] = ticket[i]
        elif i % 9 == 0 and i not in prime():
            if 48 <= ord(ticket[i]) <= 57:
                prob += 1
                ticket2[i] = ticket[i]
        elif i % 13 == 0 and i not in prime():
            if 65 <= ord(ticket[i]) <= 90:
                prob += 1
                ticket2[i] = ticket[i]
        elif i % 4 == 0 and i not in prime():
            if 97 <= ord(ticket[i]) <= 122 and ord(ticket[i]) % 10 == 7:
                prob += 1
                ticket2[i] = ticket[i]
        elif i % 3 == 0 and i not in prime():
            if 48 <= ord(ticket[i]) ^ i % 3 <= 57:
                prob += 1
                ticket2[i] = ticket[i]
        elif 48 <= ord(ticket[i]) ^ i % 3 <= 57 or 65 <= ord(ticket[i]) ^ i % 10 <= 90 or 97 <= ord(ticket[i]) <= 122 and ord(ticket[i]) % 10 == 7:
            prob += 1
            ticket2[i] = ticket[i]

    return ticket2
    # if prob < 10:
    #     return 'Try Again...'
    # if 10 <= prob <= 25:
    #     return 'You get $5'
    # if 25 < prob <= 40:
    #     return 'You get $10'
    # if 40 < prob <= 49:
    #     return 'You get $50'
    # if prob == 50:
    #     return 'You got FLAG: {}'.format(FLAG)


def buy():
    # print(prime())
    ticket = ''
    for i in range(50):
        if randint(0, 2) == 0:
            ticket += chr(randint(48, 57))
        else:
            if randint(0, 2) == 1:
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
        else:
            if inp == '2':
                ticket = input('Ticket: ')
                print(check(ticket))
                if FLAG in check(ticket):
                    exit()
            else:
                if inp == '3':
                    print('Goodbye...')
                    exit()
                else:
                    print('Unknown input\n')

def solve():
    c = 0

    while True:
        a = buy()
        chk = check(a) 
        for i in chk:
            if(type("a") == type(i)):
                c +=1
        if c == 50:
            print("".join(chk))
            exit() 
        c = 0

if __name__ == '__main__':
    # main()
    solve()
# okay decompiling lottery.pyc
