while True:
    try:
        sentence = input()
        part1, part2 = sentence.split(',', 1)
        print(part1)
        print(part2)
    except EOFError:
        break
