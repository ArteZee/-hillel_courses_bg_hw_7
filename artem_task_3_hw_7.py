sentence = input().lower().split(" ")

def polindrome (sentence):

    sentence = ''.join(sentence)
    sentence = list(sentence)
    b = sentence[::-1]

    if sentence == b:
        return ("True")
    else:
        return ("False")

print(polindrome(sentence))
