user_data = input().lower().split(" ")


def is_checking_palindrome(sentence):
    """
    Function is checking - is sentence palindrome ?
    :param sentence:
    :return: bool
    """

    sentence = ''.join(sentence)
    b = sentence[::-1]

    if sentence == b:
        return True
    else:
        return False


print(is_checking_palindrome(user_data))
