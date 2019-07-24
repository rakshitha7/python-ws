'''9. Write a program to find the word(s) that occur maximum and minimum number of times in the
given paragraph. Also, display those words next to their respective count.
Input:
&quot;Comprehensions are a feature of Python which I would really miss if I ever have to
leave it. Comprehensions are constructs that allow sequences to be built from other sequences. Several types of comprehensions are supported in both Python 2 and
Python 3.&quot;
Output:
Word appearing maximum times: abcdefg; x times
Word appearing minimum times: pqrstuv; y times
(Where abcdefg and pqrstuv are words from the given paragraph; x and y are the
number of instances these words appear in the paragraph.)
'''
data = "Comprehensions are a feature of Python which I would really miss if I ever \
have to leave it. Comprehensions are constructs that allow sequences to be built from other sequences.\
 Several types of comprehensions are supported in both Python 2 and Python 3"
d = dict()
count = 0
lst = []
words = data.split()
for word in words:
        if d.get(word) == None:
                d[word] = 1
        else :
                d[word] +=1

for i in d:
        if d[i] == 1:
                count += 1
                print(f"{i}:{d[i]} times")
print(f"unique count {count}")