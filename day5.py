import hashlib

door = "cxdnnyjw"

password = [None] * 8

print(password)

cnt = 0

while True:
    m = hashlib.md5()
    m.update((door + str(cnt)).encode())
    h = m.hexdigest()
    if h[:5] == "00000":
        pos = int(h[5], 16)
        if pos < len(password) and password[pos] is None:
            password[pos] = h[6]
        if not None in password:
            break
        print(h, cnt, password)

    cnt += 1

print(''.join(password))

