class MaxLimitError(Exception):

    def __init__(self,message):
        self.message=message

    def __str__(self):
        return f"{self.__class__.__name__}:{self.message}"

c=0
def login(username,password):
    global c
    if username=="abc" and password=="cba":
        print("login is successfull")
    else:
        print("invalid credential")
    c +=1
    if c>2:
        raise MaxLimitError("you have reached maximum numbe of attempts")

login("abc","abc")
login("a","c")
login("hd","gh")
login("abc","cba")