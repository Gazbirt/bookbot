def num_of_words(inputString):
    output = len(inputString.split())
    return output

def char_count(inputString):
    charDictionary = {}
    workingString = inputString.lower()
    for i in range(len(workingString) - 1):
        if workingString[i] in charDictionary:
            charDictionary[workingString[i]] += 1
        else:
            charDictionary[workingString[i]] = 1
    return charDictionary

