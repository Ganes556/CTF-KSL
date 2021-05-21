import time, sys, os

class bcolors:
    HEADER = '\x1b[95m'
    OKBLUE = '\x1b[94m'
    OKGREEN = '\x1b[92m'
    WARNING = '\x1b[93m'
    FAIL = '\x1b[91m'
    ENDC = '\x1b[0m'
    BOLD = '\x1b[1m'
    UNDERLINE = '\x1b[4m'


class status:
    status = 'Free'


def banner():
    os.system('clear')
    print bcolors.WARNING + "                                   _                \n ___ _ __   __ _ _ __ ___   __   _(_)_ __ _   _ ___ \n/ __| '_ \\ / _` | '_ ` _ \\  \\ \\ / / | '__| | | / __|\n\\__ \\ |_) | (_| | | | | | |  \\ V /| | |  | |_| \\__ \\ \n|___/ .__/ \\__,_|_| |_| |_|   \\_/ |_|_|   \\__,_|___/\n    |_|\n" + bcolors.ENDC


def menu():
    print bcolors.HEADER + ('\tSPAM VIRUS by AnehMan ({} Ver.)').format(status.status) + bcolors.ENDC
    print bcolors.OKBLUE + '\t\t[1] Spam Virus (Free Ver.)' + bcolors.ENDC
    print bcolors.OKBLUE + '\t\t[2] Spam Virus (Full Ver.)' + bcolors.ENDC
    print bcolors.OKBLUE + '\t\t[3] Validasi kode rahasia' + bcolors.ENDC
    print bcolors.OKBLUE + '\t\t[4] Exit' + bcolors.ENDC


def spam(noTelp):
    if noTelp != '089202069420':
        print bcolors.BOLD + bcolors.FAIL + '\tBro, hack hp mantanku, bukan hp orang lain.....\n' + bcolors.ENDC
        return
    i = 1
    while True:
        jml = bcolors.BOLD + bcolors.FAIL + str(i) + bcolors.ENDC
        noTelp = bcolors.BOLD + bcolors.OKGREEN + noTelp + bcolors.ENDC
        notif = bcolors.BOLD + bcolors.WARNING + ' virus telah dikirim ke nomer telpon ' + bcolors.ENDC
        print jml + notif + noTelp
        i += 1
        sys.stdout.flush()
        time.sleep(1)


def validate(kode):
    salah = bcolors.BOLD + bcolors.FAIL + '\tKode salah....\n' + bcolors.ENDC
    benar = bcolors.BOLD + bcolors.OKGREEN + '\tKode benar....\n' + bcolors.ENDC
    skor = 0
    if len(kode) != 65:
        print salah
        return
    p1 = kode[:16]
    p2 = kode[17:32]
    p3 = kode[33:48]
    p4 = kode[49:]
    collected_string = []
    for i in range(16):
        if 32 <= ord(p1[i]) <= 126:
            if p1[i] not in 'LMAO':
                if p1[i] not in ' ~`!@#$%^&*()_+=-}{][|"\'<,>.?/:;\\':
                    if p1[i] not in collected_string:
                        collected_string.append(p1[i])
                        if p1[i] not in 'abcdefghijklmnopqrstuvwxyz':
                            skor += 1

    if kode[16] == '-':
        skor += 1
    for i in range(15):
        if 32 <= ord(p2[i]) <= 126:
            if p2[i] not in collected_string:
                if p2[i] not in ' ~`!@#$%^&*()_+=-}{][|"\'<,>.?/:;\\':
                    if i % 2:
                        if p2[i] not in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
                            collected_string.append(p2[i])
                            skor += 1
                    elif p2[i] not in '1234567890':
                        if p2[i] not in 'bruh':
                            collected_string.append(p2[i])
                            skor += 1

    if kode[32] == '-':
        skor += 1
    for i in range(15):
        if 32 <= ord(p3[i]) <= 126:
            if p3[i] not in collected_string:
                if p3[i] not in ' ~`!@#$%^&*()_+=-}{][|"\'<,>.?/:;\\':
                    if p3[i] in '69420':
                        skor += 1
                        continue
                    if p3[i] in 'OMEGALUL':
                        skor += 1
                        continue
                    if p3[i] in 'pogchamp':
                        skor += 1

    if kode[48] == '-':
        skor += 1
    for i in range(16):
        if 32 <= ord(p4[i]) <= 126:
            if p4[i] not in collected_string:
                skor += 1

    if skor == 65:
        status.status = 'Full'
        print benar
    else:
        print salah


def option():
    inp = raw_input(bcolors.OKBLUE + '\t\tInput: ' + bcolors.ENDC)
    if inp == '1':
        noTelp = raw_input(bcolors.WARNING + '\n\tMasukkan no telp yang ingin di-spam virus: ' + bcolors.ENDC)
        spam(noTelp)
    elif inp == '2':
        if status.status == 'Free':
            print bcolors.BOLD + bcolors.FAIL + '\tStatus aplikasi masih free :(\n' + bcolors.ENDC
        else:
            print bcolors.BOLD + bcolors.FAIL + '\tJangan ngehek orang sembarangan gan. Daripada ngehek hape orang, mending ambil flag\n' + bcolors.ENDC
            print bcolors.BOLD + bcolors.OKGREEN + '\tR E D A C T E D' + bcolors.ENDC
            exit()
    elif inp == '3':
        if status.status == 'Full':
            print bcolors.BOLD + bcolors.WARNING + '\tSudah Full Ver.\n' + bcolors.ENDC
            return
        kode = raw_input(bcolors.OKGREEN + '\tMasukkan kode rahasia: ' + bcolors.ENDC)
        validate(kode)
    elif inp == '4':
        exit()
    else:
        print bcolors.BOLD + bcolors.FAIL + '\tInput tidak dikenal\n' + bcolors.ENDC


if __name__ == '__main__':
    banner()
    while True:
        menu()
        option()

