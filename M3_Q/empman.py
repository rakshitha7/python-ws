
from emp import Employee

'''emp_1 = Employee(1,"sunny","M.Tech",56000,"CS")
emp_2 = Employee(1,"Bunny","M.Tech",46000,"IS")               #program to print employee salary after increment
emp_1.showInfo()
emp_1.increment_salary(2000)
emp_1.showInfo()
emp_2.showInfo()'''

lst_emp = []
def load_emp():   #number of employee 
    with open("empdata.txt") as f:
        fdata = f.readlines()
        for data in fdata:
            edata = data.strip("\n").split(",")
            empno=int(edata[0])
            ename=edata[1]
            qual=edata[2]
            salary=int(edata[3])
            dept_name=edata[4]
            emp=Employee(empno,ename,qual,salary,dept_name)
            lst_emp.append(emp)
    print(f"total employee count:{len(lst_emp)}")



def showDeptName():             #print the unique dept names
    dnames=set(map(lambda emp:emp.dept_name,lst_emp))
    for name in dnames:
        print(name)  



def showAllQualifications():
    qualification = set(map(lambda emp: emp.qual,lst_emp))
    for qual in qualification:
        print(qual)


def maxSalaryEmp():
    max_sal=max(list(map(lambda emp:emp.salary,lst_emp)))
    lst=list(filter(lambda x:x.salary==max_sal,lst_emp))
    for emp in lst:
        emp.show_info()


def showEmpCountByDeptName:
    pass

def showTotalSalaryByDeptName():
    pass

def showEmpCountByQual:
    pass


load_emp()
showDeptName()
showAllQualifications()
print("the peron with maximaunm salary")
maxSalaryEmp()