for i in range(16):
    if 32 <= ord(p1[i]) <= 126:
        if p1[i] not in 'LMAO':
            if p1[i] not in ' ~`!@#$%^&*()_+=-}{][|"\'<,>.?/:;\\':
                if p1[i] not in collected_string:
                    collected_string.append(p1[i])
                    if p1[i] not in 'abcdefghijklmnopqrstuvwxyz':
                        skor += 1