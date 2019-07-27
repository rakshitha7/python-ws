'''4.	Write a program to read data from the file story.txt and determine the following:
•	Total number of words in the file
•	The word that occurs maximum number of times
•	The number of conjunctionsof various types (example: and, but, if)
'''

try:
    with open("story.txt")  as f:
        count=0
        lines=f.readlines()
    dic={}
    for line in lines:
        words=line.split("")
        for word in words:
            word=word.strip().strip("\n").upper().replace(',','').replace('.','')
            try:
                dic[word] +=1
            except KeyError:
                dic[word]=1
                if word in ['and','but','if']:
                    count +=1
    print(dic)
    max_val=max(dic.values())
    for k,v in dic.items():
        if v==max_val:
            print(f"{k}:{v}")

    print(f"the number of conjuction {count}")



except Exception as e:
    print(f"File not found please check path {e}") 