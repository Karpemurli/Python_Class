# take one base class

class A:
    def method_A(self):
        return 'Method A'
    
# class B inheritance from A:

class B(A):
    
    def method_B(self):
        return 'Method B'
    
#class c inherits from class B

class C(A):
    
    def method_C(self):
        return 'Method C'
    
# class d inherits from class b and c

class D(B,C):
    
    def method_D(self):
        return 'Method D'
    
#create the object 

obj_d = D()

print(obj_d.method_A())
print(obj_d.method_B())
print(obj_d.method_C())
print(obj_d.method_D())