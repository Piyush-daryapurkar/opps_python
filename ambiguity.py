class A:
     def sum(self):
          print("A")
class B:
     def sum(self):
          print("B")    
class C(A,B):
     def add(self):
          print("c")                
d=C()
d.sum()         