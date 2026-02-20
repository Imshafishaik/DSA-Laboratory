def first_unique_char(s):
    freq = {}

    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1

    for i in range(len(s)):
        if freq[s[i]] == 1:
            return i
    
    return -1

print(first_unique_char("leetcode"))  
print(first_unique_char("loveleetcode"))  
print(first_unique_char("aabb")) 


from collections import OrderedDict

def first_unique_char_ordered(s):
    freq = OrderedDict()
    
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1
    
    index = 0
    for ch in s:
        if freq[ch] == 1:
            return index
        index += 1
    
    return -1

print(first_unique_char_ordered("leetcode"))
