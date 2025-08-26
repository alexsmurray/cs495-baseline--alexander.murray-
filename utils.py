import re

def palindromeChecker(stringInput: str) -> bool:

    # make string all lower case
    normalizedString = stringInput.lower()

    # remove all punctuation
    normalizedString = re.sub(r'[^\w\s]','',normalizedString)

    # remove all spaces
    normalizedString = normalizedString.replace(" ", "")

    print(normalizedString)

    # reverse string (slicing) and check for palindrome
    return normalizedString == normalizedString[::-1]

