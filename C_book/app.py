from inmememory import InMemoryImpl
while True:
    print("*"*75)
    print("1.add 2.view all 3.update 4.delete 5.search 6.exit")
    print("*"*75)
    ch=int(input("enter your choice"))
    if ch == 1:
        InMemoryImpl.addContact()

    elif ch == 2:
        InMemoryImpl.viewContact()

    elif ch == 3:
        InMemoryImpl.updateContact()

    elif ch == 4:
        InMemoryImpl.deleteContact()
        

    elif ch == 5:
        InMemoryImpl.searchContact()

    else:
        break

