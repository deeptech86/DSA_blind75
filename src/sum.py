def assignValues(str):
    # assign Values
    totalsum = 0
    alpha = {}
    alphabets = [chr(i) for i in range(ord('a'), ord('z') + 1)]
    printlst= [chr(i) for i in range(ord('a'), ord('z') + 1)]
    print(printlst)

    for i in range(0, len(alphabets)):
        alpha[alphabets[i]] = i+1

    for each_char in str:
        if each_char.isnumeric():
            totalsum += int(each_char)
        else:
            totalsum += alpha.get(each_char.lower())
    return totalsum


print(assignValues('Hello123'))