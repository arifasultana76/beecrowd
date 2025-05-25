songs = [
    "PROXYCITY", "P.Y.N.G.", "DNSUEY!", "SERVERS", "HOST!",
    "CRIPTONIZE", "OFFLINE DAY", "SALT", "ANSWER!", "RAR?", "WIFI ANTENNAS"
]

for _ in range(int(input())):
    x, y = map(int, input().split())
    print(songs[x + y])
