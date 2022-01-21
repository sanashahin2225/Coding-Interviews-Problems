def are_anagrams(s1,s2):
    if len(s1) != len(s2):
        return False
    freqS1 = {}
    freqS2 = {}
    
    for i in s1:
        if i in freqS1.keys():
            freqS1[i] += 1
        else:
            freqS1[i] = 1
    for i in s2:
        if i in freqS2.keys():
            freqS2[i] += 1
        else:
            freqS2[i] = 1
    if freqS1 == freqS2:
        return True
    
    else:
        return False
  
print(are_anagrams("nameless","salesmen"))  #True
print(are_anagrams("danger","ganred"))    #True
print(are_anagrams("coffee","ceofefe"))     #False
