class Myclass:
    __private_var=27

    def __privMeth(self):
        print ("I'm inside class Myclass")

    def hello(self):
        print ("Private Varible Value:", Myclass.__private_var)

object=Myclass()
object.hello()
object.__privMeth