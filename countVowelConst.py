def countVowelConst(s):
    ct = 0
    cnct = 0
    vowel = ['a','e','i','o','u','A','E','I','O','U']
    for i in s:
        if i in vowel:
            ct += 1
        else:
            cnct += 1
    return ct,cnct

a,b = countVowelConst('Azimabad Colony')
print(f"Vowel {a} and Consonant {b}" )  
