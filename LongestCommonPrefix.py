
"""
Problem Statement: Given a set of strings, find the longest common prefix.
Examples:

Input: {“geeksforgeeks”, “geeks”, “geek”, “geezer”}
Output: “gee”

Input: {“apple”, “ape”, “april”}
Output: “ap”
"""





words=["april", "ape", "apple"]


def LCP(inp):
    smaller_length=len(words[0])
    for item in words:
        cur_length=len(item)
        if cur_length<smaller_length:
            smaller_length=cur_length

    i=0
    req_word=""
    while i<smaller_length:
        current_letter=words[0][i]
        for item in words:
            if item[i]!=current_letter:
                return req_word
        
        req_word+=current_letter
        i+=1

    return req_word

res=LCP(words)
print(res)
            
        


