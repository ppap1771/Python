class stud:
    def __init__(self, x1):
        self.reg_no = x1
    
    def method1():
        pass

    def method2():
        pass

    def method3():
        pass

class cse(stud):
    def __init__(self, x1, x2):
        self.reg_no = x1
        self.year = x2
    
    def method1():
        pass
    
    def method2():
        pass

    def method3():
        pass

s1 = stud(661)
cs1 = cse(661, 2)

# cs1 = s1
s1 = cs1
print(s1)