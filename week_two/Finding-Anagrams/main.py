"""
    Zuri Python Backend Tasks  
    >> Finding Anagram Task
    by Samuel Adebayo-Adesina
"""

# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True

import re

def find_anagram(word, anagram):
    # [assignment] Add your code here
    word = ''.join(re.split('\W',word))
    anagram = ''.join(re.split('\W',anagram))
    return sorted(word) == sorted(anagram)
    
print(find_anagram("below", "elbow"))
