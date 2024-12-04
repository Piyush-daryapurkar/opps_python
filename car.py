class ABC:
    def __init__(self,v1,v2):
        self.__v1=v1
        self.__v2=v2
    def display(self):
        print(self.__v1)
        print(self.__v2) 
object=ABC(4,8)
object.display()
print(object.__v1) 
print(object.__v2)             
#its all about privet data , privet data only acses in class and function can call them