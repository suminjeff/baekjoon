while True:
    line = input().strip()
    if line == "#":
        break
    
    char, sentence = line[0], line[2:]
    
    count = sentence.lower().count(char.lower())
    
    print(f"{char} {count}")
