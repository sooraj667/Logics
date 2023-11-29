"""
Given a string, the task is to reverse the order of the words in the given string. 

Examples:

Input: s = “geeks quiz practice code” 
Output: s = “code practice quiz geeks”

Input: s = “i love programming very much” 
Output: s = “much very programming love i” 
"""

def rev(inp):
    inp_list=inp.split(" ")
    req_string=""
    for i in range((len(inp_list)-1),-1,-1):
        req_string+=f"{inp_list[i]} "

    return req_string

res=rev("i love programming very much")
print(res)

