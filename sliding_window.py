def length_of_longest_substring(s: str) -> int:
    char_set = set () # set of longest unique char set
    left = 0
    max_length = 0
    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left +=1
        char_set.add(s[right])
        max_length=max(max_length,right-left+1)
    return max_length

s="abcabcbb"
#print(length_of_longest_substring(s))

def length_of_longest_substring_two_distinct(s: str) -> int:
    char_count = {} #stores char count of the substring
    left = 0
    max_length = 0
    for right in range(len(s)):
        # Add the current character to the hash map
        char_count[s[right]] =char_count.get(s[right],0)+1
        # If more than two distinct characters, shrink the window
        while len(char_count) > 2:
            char_count[s[left]] -=1
            if char_count[s[left]] == 0:
                del char_count[s[left]]
            left +=1
        # update max_length
        max_length = max(max_length,right-left+1)
    return max_length
# s="eceba"
# print(length_of_longest_substring_two_distinct(s))

def length_of_longest_substring_k_distinct(s: str, k: int) ->int:
    if k==0 or not s:
        return 0
    char_count = {}
    left = 0
    max_length = 0 
    for right in range(len(s)):
         # Add the current character to the hash map
        char_count[s[right]] =char_count.get(s[right],0)+1
          # If more than k distinct characters, shrink the window
        while len(char_count) > k:
            char_count[s[left]] -=1
            if char_count[s[left]] == 0:
                del char_count[s[left]]
            left +=1
        # update max_length
        max_length = max(max_length,right-left+1)
    return max_length
        
s="eceba"
k=3
print(length_of_longest_substring_k_distinct(s,k))
    