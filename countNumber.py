import re

def countNumbers(s):
    ct = 0
    pattern = "[0-9]+"
    for i in s:
        if re.match(pattern,i):
            ct +=1
    return ct

print(countNumbers('sanajnsdlkn772409u3kjjnsdn92u301u'))
