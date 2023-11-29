"""
Given a list of words followed by two words, the task is to find the minimum distance between the given two words in the list of words.

Examples:

Input: S = { “the”, “quick”, “brown”, “fox”, “quick”}, word1 = “the”, word2 = “fox”
Output: 3
Explanation: Minimum distance between the words “the” and “fox” is 3

Input: S = {“geeks”, “for”, “geeks”, “contribute”,  “practice”}, word1 = “geeks”, word2 = “practice”
Output: 2
Explanation: Minimum distance between the words “geeks” and “practice” is 2

"""

def min_distance(words,word1,word2):
    index1=None
    index2=None
    for i in range(len(words)):
       

        if words[i]==word1:
            index1=i
        if words[i]==word2:
            index2=i

    distance=None
    if index1>index2:
        distance=index1-index2
    else:
        distance=index2-index1

    return distance

    
   
       

inp_words=["The","Quick","Brown","Fox","Jumps"]
word1="Brown"
word2="Fox"
res=min_distance(inp_words,word1,word2)
print(res)