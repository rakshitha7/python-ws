'''4. Write a program to accept an input string from the user and determine the vowels in the string
and calculate the number of vowels. (Hint: Use filter method.)
Example:
Input: quintessential
Output: [&#39;u&#39;, &#39;i&#39;, &#39;e&#39;, &#39;e&#39;, &#39;i&#39;, &#39;a&#39;];'''

name=input("enter your name")
lst = ['a','e','i','o','u']
c=0
for i in name:
    if i in lst:
        c=c+1
print(c)


#using filter
'''print(len(list(filter(lambda x:x in lst,name))))'''