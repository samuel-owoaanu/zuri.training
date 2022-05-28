"""
    Zuri Python Backend Tasks  
    >> Reading Text File Task
    by Samuel Adebayo-Adesina
"""
# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}
import re

def read_file_content(filename):
    # [assignment] Add your code here 
    file = open(f"./{str(filename)}",'r')
    return file.read()


def count_words():
    text = read_file_content("./story.txt")
    # [assignment] Add your code here
    text = text.lower()
    text_list=(text.split())
    text_set = set(text_list)
    text_search = list(text_set)
    word_count_dict = dict()
    
    for item in text_search:
        item_regex = re.compile(item)
        newlist = list(filter(item_regex.match, text_list))
        word_count_dict.update({item:len(newlist)})
        
    return word_count_dict

#print(count_words()) 
--> """{'instead,': 1, 'teaching': 1, 'once': 1, 'am': 1, 'walked': 1, 'or': 1, 'asked,': 1, 'this': 1, 'water': 2, 'glass': 4, 'be': 1, 
'empty': 1, 'would': 1, 'everyone': 1, 'principles': 1, 'while': 1, 'upon': 1, 'time': 1, 'half': 2, 'the': 3, 'holding?': 1, 'typical': 1, 
'auditorium': 1, 'raised': 1, 'smile': 1, 'how': 1, 'question.': 1, 'face,': 1, 'an': 1, 'professor': 2, 'she': 1, 'is': 1, 'students.': 1, 
'of': 2, 'stress': 1, 'heavy': 1, 'i': 3, 'her': 1, 'around': 1, 'management': 1, 'psychology': 1, 'stage': 1, 'water,': 1, 'a': 12, 'to': 1, 
'full': 1, 'as': 3, 'asked': 2, 'on': 3, 'expected': 1, 'filled': 1, 'they': 1, 'with': 2}
"""
