class Man:
    #self.name: instance variable
    #variable stored per instance
    def __init__(self, name): #Same as constructor in CPP
        self.name = name
        print("init done")

    def hello(self): #Presenting 'self' as the first parameter of method is common.
        print("Hello "+self.name+ "!")

    def bye(self):
        print("Bye "+ self.name +"!")
m = Man("David") #Calling __init__ method
m.hello()
m.bye()
