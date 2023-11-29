"""
Given a string that consists of only 0s, 1s and 2s, count the number of substrings that have an equal number of 0s, 1s, and 2s.

Examples: 

Input: str = “0102010”
Output:  2
Explanation: Substring str[2, 4] = “102” and substring str[4, 6] = “201” has equal number of 0, 1 and 2

Input: str = “102100211”
Output: 5
"""

def substrings(inp_string):
    maincount=0
    for i in range(len(inp_string)-3):
        sliced=inp_string[i:i+3]
        checkdict={}
        for num in sliced:
            if num not in checkdict:
                checkdict[num]=1
            else:
                checkdict[num]+=1

        if len(checkdict.values())==3:
            maincount+=1

    return maincount


        

          
res=substrings("102100211")
                
print(res)
