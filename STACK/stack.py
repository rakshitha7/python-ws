class Stack():
    def __init__(self):
        self.st = []

    def push(self,ele):
    
        self.st.append(ele)
    
    def pop(self):
        if self.is_empty():
            print("stack is empty")
        else:
            ele=self.st.pop()
            print(f"elemenr {ele} removed from stack")

    def search(self,searchele):
        if self.is_empty():
            print("stack is empty")
        else:
            for index,ele in enumerate(self.st):
                if ele == searchele:
                    return index
            return -1
    def show(self):
        if self.is_empty():
            print("stack is empty")
        else:
            print(self.st)
       

    def is_empty(self):
        return len(self.st)==0



if __name__ == "__main__":
    st=Stack()

    while True:
        print("1.push 2.pop 3.search 4.display 5.exit")
        try:
            ch =int(input("enter your choice:"))
            if ch==1:
                ele=input("enter the element to push")
                st.push(ele)
            elif ch==2:
                st.pop()
            elif ch==3:
                ele=input("enter the element to searched")
                res=st.search(ele)
                if res != -1:
                    print(f"element {ele} is found in the position {res}")
                else:
                    print(f"element {ele} is not found ")
            elif ch==4:
                st.show()
            elif  ch==5:
                exit()
            else:
                raise ValueError

        except ValueError:
            print("enter only number 1 to 5")