while True:
    try:
        lower = upper = number = space = 0
        S = input()
        for s in S:
            if s.islower():
                lower += 1
            elif s.isupper():
                upper += 1
            elif s.isnumeric():
                number += 1
            elif s == " ":
                space += 1
        print(lower, upper, number, space)
    except:
        break