import re

def getNumbers(s):
    pattern = "[0-9]+"
    return re.findall(pattern,s)

print(getNumbers('sanajnsdlkn772409u3kjjnsdn92u301u'))
