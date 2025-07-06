while True:
    line = input().strip()
    if not line:
        continue
    c, n = map(int, line.split())
    if c == 0 and n == 0:
        break

    cipher_from = input()
    cipher_to = input()

    mapping = {}

    for f, t in zip(cipher_from, cipher_to):
        mapping[f] = t
        mapping[t] = f
        mapping[f.lower()] = t.lower()
        mapping[t.lower()] = f.lower()

    for _ in range(n):
        encrypted = input()
        decrypted = []
        for ch in encrypted:
            if ch in mapping:
                decrypted.append(mapping[ch])
            elif ch.lower() in mapping:
              
                if ch.isupper():
                    decrypted.append(mapping[ch.lower()].upper())
                else:
                    decrypted.append(mapping[ch.lower()])
            else:
                decrypted.append(ch)
        print("".join(decrypted))
    print()
