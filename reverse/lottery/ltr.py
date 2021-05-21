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

        if count == 0:
            if Number != 1:
                prime.append(Number)

    return prime


def check(ticket):
    ticket = list(ticket)
    if len(ticket) != 50:
        return 'Invalid ticket...'
    prob = 0
    for i in range(50):
        if i in prime():
            if 48 <= ord(ticket[i]) ^ i % 10 <= 57:
                prob += 1
        else:
            if i % 6 == 0:
                pass
            if i not in prime():
                if 65 <= ord(ticket[i]) - 20 <= 90:
                    prob += 1
            elif i % 5 == 0 and i not in prime():
                if 97 <= ord(ticket[i]) <= 122 and ord(ticket[i]) % 10 == 3:
                    prob += 1
            elif i % 9 == 0 and i not in prime():
                if 48 <= ord(ticket[i]) <= 57:
                    prob += 1
            elif i % 13 == 0 and i not in prime():
                if 65 <= ord(ticket[i]) <= 90:
                    prob += 1
            elif i % 4 == 0 and i not in prime():
                if 97 <= ord(ticket[i]) <= 122:
                    if ord(ticket[i]) % 10 == 7:
                        prob += 1
            elif i % 3 == 0 and i not in prime():
                if 48 <= ord(ticket[i]) ^ i % 3 <= 57:
                    prob += 1
            elif 48 <= ord(ticket[i]) ^ i % 3 <= 57 or 65 <= ord(ticket[i]) ^ i % 10 <= 90 or 97 <= ord(ticket[i]) <= 122 and ord(ticket[i]) % 10 == 7:
                prob += 1

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
    print(prime())
    ticket = ''
    for i in range(50):
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
        # chk2 = check(a,chk[0])
        
        
        for i in chk2[0]:
            if(type("a") == type(i)):
                c +=1

        print(c)
        if c == 15:
            print(chk2)
            exit() 

        c = 0
            # if(chk[1] == 50):
            #     print("dapat",chk[0])
            #     exit()
        
        

if __name__ == '__main__':
    dbug()
    # main()