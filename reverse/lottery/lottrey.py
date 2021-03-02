from random import randint
FLAG = 'R E D A C T E D'

prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]

def check(ticket):
    global prime
    ticket = list(ticket)
    if len(ticket) != 50:
        return 'Invalid ticket...'
    prob = 0

    # H673uv0Z2o2wR5mimiaO64c0yZ0Or8r7mY3z16024faLazxT80
    for i in range(50):
        if i in prime:
            if 48 <= ord(ticket[i]) ^ i % 10 <= 57:
                prob += 1
        else:
            if i % 6 == 0:
                pass
            if i not in prime:
                if 65 <= ord(ticket[i]) - 20 <= 90:
                    prob += 1
            if i % 5 == 0 and i not in prime:
                if 97 <= ord(ticket[i]) <= 122 and ord(ticket[i]) % 10 == 3:
                    prob += 1
            if i % 9 == 0 and i not in prime:
                if 48 <= ord(ticket[i]) <= 57:
                    prob += 1
            if i % 13 == 0 and i not in prime:
                if 65 <= ord(ticket[i]) <= 90:
                    prob += 1
            if i % 4 == 0 and i not in prime:
                if 97 <= ord(ticket[i]) <= 122:
                    if ord(ticket[i]) % 10 == 7:
                        prob += 1
            if i % 3 == 0 and i not in prime:
                if 48 <= ord(ticket[i]) ^ i % 3 <= 57:
                    prob += 1
            if 48 <= ord(ticket[i]) ^ i % 3 <= 57 or 65 <= ord(ticket[i]) ^ i % 10 <= 90 or 97 <= ord(ticket[i]) <= 122 and ord(ticket[i]) % 10 == 7:
                prob += 1
    # return prob
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
def decode(ticket):
    ticket = list(ticket)
    prob = 0
    for i in range(50):
        if i in prime:
            if 48 <= ord(ticket[i]) ^ i % 10 <= 57:
                prob += 1
        else:
            if i % 6 == 0:
                pass
            if i not in prime:
                if 65 <= ord(ticket[i]) - 20 <= 90:
                    prob += 1
            if i % 5 == 0 and i not in prime:
                if 97 <= ord(ticket[i]) <= 122 and ord(ticket[i]) % 10 == 3:
                    prob += 1
            if i % 9 == 0 and i not in prime:
                if 48 <= ord(ticket[i]) <= 57:
                    prob += 1
            if i % 13 == 0 and i not in prime:
                if 65 <= ord(ticket[i]) <= 90:
                    prob += 1
            if i % 4 == 0 and i not in prime:
                if 97 <= ord(ticket[i]) <= 122:
                    if ord(ticket[i]) % 10 == 7:
                        prob += 1
            if i % 3 == 0 and i not in prime:
                if 48 <= ord(ticket[i]) ^ i % 3 <= 57:
                    prob += 1
            if 48 <= ord(ticket[i]) ^ i % 3 <= 57 or 65 <= ord(ticket[i]) ^ i % 10 <= 90 or 97 <= ord(ticket[i]) <= 122 and ord(ticket[i]) % 10 == 7:
                prob += 1

def buy():
    global prime
    # print(prime)
    ticket = ''
    for i in range(50):
        if randint(0, 2) == 0:
            ticket += chr(randint(48, 57))
        elif randint(0, 2) == 1:
            ticket += chr(randint(65, 90))
        else:
            ticket += chr(randint(97, 122))

    return ticket


def main():
    while 1:
        # H673uv0Z2o2wR5mimiaO64c0yZ0Or8r7mY3z16024faLazxT80
        ticket = buy()
        chk = check(ticket)
        if FLAG in str(chk):
            print(ticket)
        else:
            print(chk)
if __name__ == '__main__':
    main()
    # prime()