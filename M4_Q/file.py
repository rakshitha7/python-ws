try:
    with open ("data.txt") as f:
        line_count=0
        word_count=0
        lst=[]
        lines=f.readlines()
        for line in lines:
            line_count +=1
            words=line.split()
            for word in words:
                lst.append(word)
                word_count+=1
    print(line_count)
    print(word_count)

    print(lst)

        



except Exception as e:
    print(f"File not found please check path {e}")