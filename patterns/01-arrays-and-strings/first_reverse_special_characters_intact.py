def LetterReverse(s):
    # Step 1: create your letter checker
    lower = [
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
        "p",
        "q",
        "r",
        "s",
        "t",
        "u",
        "v",
        "w",
        "x",
        "y",
        "z",
    ]
    upper = [
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
        "G",
        "H",
        "I",
        "J",
        "K",
        "L",
        "M",
        "N",
        "O",
        "P",
        "Q",
        "R",
        "S",
        "T",
        "U",
        "V",
        "W",
        "X",
        "Y",
        "Z",
    ]
    all_letters = lower + upper  # combined list

    # Step 2: collect letters
    letters = []
    for char in s:
        if char in all_letters:  # this is your manual check
            letters.append(char)

    # Step 3: reverse the collected letters
    rev = letters[::-1]

    # Step 4: rebuild the string
    result = ""
    j = 0
    for char in s:
        if char in all_letters:
            result += rev[j]  # take next reversed letter
            j += 1  # move pointer forward
        else:
            result += char  # keep non-letter as is
    return result


print(LetterReverse("123abc123"))
