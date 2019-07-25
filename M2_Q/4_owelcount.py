'''4. Write a program to accept an input string from the user and determine the vowels in the string
and calculate the number of vowels. (Hint: Use filter method.)
Example:
Input: quintessential
Output: [&#39;u&#39;, &#39;i&#39;, &#39;e&#39;, &#39;e&#39;, &#39;i&#39;, &#39;a&#39;];'''

name=input('Enter the name')

ls=['a','e','i','o','u']
vowel=list(filter(lambda x:x in ls,name))
count=len(vowel)
print(count)
print(vowel)