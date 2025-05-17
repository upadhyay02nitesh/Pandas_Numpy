class A:
    def __init__(self,a,b,c):
        self.a=a 
        self.b=b 
        self.c=c 

class B(A):
    def __init__(self,a,b,c,d):
        super().__init__(a,b,c)
        self.d=d 
    def disp(self):
        print(self.a,self.b,self.c,self.d)

b=B(1,2,3,4)
b.disp()