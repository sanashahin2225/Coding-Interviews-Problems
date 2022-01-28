#Method-1
def reverse_string(s):
    str = ''
    for i in s:
        str = i+str
    return str
  
#Method-2
def reverse_string1(s):
    return s[::-1]

 #Method-3
def reverseString(s):
    if len(s) == 0:
        return s
    else:
        return reverseString(s[1:])+s[0]
    
#method-4
def reverseStr(s):
    str = "".join(reversed(s))
    return str
                  
print(reverseStr('sana'))
