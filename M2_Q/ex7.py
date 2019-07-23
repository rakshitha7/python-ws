lst = []

def add(ele):
    lst.append(ele)

def delete():
    if len(lst) == 0:
        print("list is empty")
    else:    
        lst.pop()
  

def search(ele):
    if len(lst) == 0:
        print("list is empty")
    else:
        if ele in lst:
            print(ele)
        else:
            print("not found")

def display():
    if len(lst) == 0:
        print("list is empty")
    else:
        for i in lst:
            print(i)

while True:
    print("1.add 2. pop 3.search 4.display 5.exit")
    ch=int(input("enter the choice"))
    if ch == 1:
        ele=int(input("enter the element to be inserted"))
        add(ele)
    elif ch == 2:
        delete()
    elif ch == 3:
        ele=int(input("enter the element to be searched"))
        search(ele)
    elif ch == 4:
        display()
    else:
        break
        
