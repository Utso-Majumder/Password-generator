import random
import string

def randomString(stringLength):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(stringLength))
print("Random String with the combination of lowercase and uppercase letters")
print("First Random String is ", randomString(8))
print("second Random String is ", randomString(8))