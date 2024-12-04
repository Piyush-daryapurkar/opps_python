class person:
    def __init__(self,name,age):#__init__ conctructor hai ise call nhi krna pdta 
        self.name=name
        self.age=age
p=person("amit",10) #p is object
print(p.name,p.age)