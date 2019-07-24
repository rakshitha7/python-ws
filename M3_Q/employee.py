class Employee:
    def __init__(self,empno,ename,qual,salary,dept_name):
        self.empno=empno
        self.ename=ename
        self.qual=qual
        self.salary=salary
        self.dept_name = dept_name

    def show_info(self):
        print(f"{self.empno}-{self.ename},{self.qual}-{self.salary}-{self.dept_name}")

    def inc_salary(self,inc_amount):
        self.salary += inc_amount
        print(f"{self.ename} salary after increament:{self.salary}")