def makeCapital(string):
    empty = ''
    string2 = string.split()
    for counter, word in enumerate(string2):
        word = word.capitalize()
        empty += word
        if counter != len(string2) - 1:
            empty += ' '
    return empty