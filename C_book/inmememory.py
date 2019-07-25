from contact import Contact
from beautifultable import BeautifulTable
class InMemoryImpl:
    contact_list = []


    @classmethod
    def addContact(cls):
        name = input("enter the name:")
        email =  input("enter the email:")
        mobile =  input("enter the mobile no:")
        address =  input("enter the address:")
        cls.contact_list.append(Contact(name,email,mobile,address))
        print(f"contact is added successfully with name: {name}")


    @classmethod
    def deleteContact(cls):
        name=input("enter the name to be deleted")
        contact = cls.get_contact_by_name(name)
        if contact:
            cls.contact_list.remove(contact)
            print(f"contact {name} deleted successfully....")
            InMemoryImpl._paint(cls.contact_list)
        else:
            print(f"contact with name:{name} not found....")
        

    @classmethod
    def updateContact(cls):
        name=input("enter the name to update")
        contact=cls.get_contact_by_name(name)
        if contact:
            print("1.name 2.email 3.mobile 4.addrress")
            ch=int(input("enter your xhoice"))
            if ch==1:
                print(f"old name:{contact.get__name()}")
                name=input("enter the new name")
                if name:
                    contact.set__name(name)
            elif ch==2:
                print(f"old email:{contact.get__email()}")
                email=input("enter the new email")
                if email:
                    contact.set__email(email)
            elif ch==3:
                print(f"old mobile:{contact.get__mobile()}")
                mobile=input("enter the new mobile")
                if mobile:
                    contact.set__mobile(mobile)
            elif ch==4:
                print(f"old addrres:{contact.get__address()}")
                address=input("enter the new address")
                if address:
                    contact.set__address(address)

            else:
                print("the contact with the {name} not present")



        



    @classmethod
    def viewContact(cls):
        InMemoryImpl._paint(cls.contact_list)

    @classmethod
    def searchContact(cls):
        if(len(cls.contact_list)) > 0:
            name=input("enter the name to be searched:")
            s_list=list(filter(lambda x:name.lower() in x.get__name().lower(),cls.contact_list))

            if len(s_list) > 0:
                InMemoryImpl._paint(s_list)
            else:
                print(f"there is no data is not found in the given search..")
        else:
            print("contact book is empty.....!   you cant do search")


    @staticmethod
    def _paint(lst):
        if len(lst) != 0:
            table=BeautifulTable()
            table.column_headers = ["Name", "Email", "Mobile","Address"]
            for c in lst:
                table.append_row([c.get__name(),c.get__email(),c.get__mobile(),c.get__address()])
            print(table)
        else:
            print(f"contact book is empty!......")


    @classmethod
    def get_contact_by_name(cls,name):
        if len(cls.contact_list) > 0:
            contact=list(filter(lambda x:x.get__name().lower() == name.lower(),cls.contact_list))
            return contact[0] if contact else None