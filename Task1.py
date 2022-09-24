"""
Task 1: (Python)
Given a list of names, create a running Python project that sorts it alphabetically,
Python has this functionality built-in, but see if you can do it without using sort()!
Examples:   
Input : [“d”,“b”,“a”,“c”,“f”,“h”,“g”,“e”]
Output : [“a”,“b”,“c”,“d”,“e”,“f”,“g”,“h”] 
"""
input =['d','b','a','c','f','h','g','e']

for i in range(0,len(input)):
	for j in range(0,len(input)):
		if input[i]<input[j]:
			input[i],input[j]=input[j],input[i]
print(input)
