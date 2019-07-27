'''
1.	Write a program to read the stock_price.csv file and perform the following operations:
•	ConvertPrice to a numeric value (example:1.02K = 1020)
•	Display the names of the two companies – one whose stock value is maximum and the other whose stock value is minimum.
•	Display the names of the companies whose stock value is within the price range that is input by the user.
'''

import csv
class Stock:
    def __init__(self,name,symbol,exchange,price):
        self.name=name
        self.symbol=symbol
        self.exchange=exchange
        self.price=price

    def __str__(slef):
        return f"{self.name},{self.symbol},{self.exchange},{self.price}"
def clean_init_get_stock():
    try:
        with open("stock_price.csv") as f:
            data=csv.reader(f,delimiter=",")
            stock_lst=[]
            line=0
            for d in data:
                if line==0:
                    line +=1
                    continue
                stock_lst.append(Stock(*d))
        for s in stock_lst:
            if "K" in s.price:
                s.price=float(s.price.strip().replace("K","")*1000)
            else:
                s.price=float(s.price.strip())
            print(s)
    except Exception as e:
        print('{},value{!r}'.format(e.args[0],e))
    return stock_lst
    



def show_stock_by_price(price):
    st_lst=clean_init_get_stock()
    f_list=list(filter(lambda x:x.price <= price,st_lst))
    if f:
        show_stock_info(list(f))
    else:
        print(f"no stock find for given price:{price}")



def max_min_stock_price():
    st_lst=clean_init_get_stock()
    #logic to find max and min price stock in th list

def show_stock_info():
    for l in lst:
        print(l)

except Exception as e:
    print(f"File not found please check path {e}") 