try:
    num=100/0
except TypeError:
    print("except block...")
    print(f"{e}")
finally:
    print("finally block....")