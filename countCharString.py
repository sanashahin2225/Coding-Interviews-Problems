def countChar(s,ch):
    ct = 0
    for i in s:
        if i == ch:
            ct += 1
    return ct

print(countChar('sana shahin is an enngineer','e'))
