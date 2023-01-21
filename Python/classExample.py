# Naming convention of varaibles/attibutes
class Example(object):
    def __init__(self):
        self.var1 = 1  # public variable
        self._var2 = 3  # private variable but open for subclassing and external use
        self.__var3 = 8  # private variable and not open for subclassing and external use
        self.__var4__ = 10  # dunder variable


obj1 = Example()
print(obj1.var1)
print(obj1.__dict__)
print(obj1._Example__var3)  # correct syntax to access a private variable which is not open for subclassing and
# external use

# WITH statement : using user-defined class in the WITH statement
# the with statement uses the __enter__() and __exit__() methods of the file object.
# so inorder to use user-defined class in the WITH statement, we have to define this methods
class Man():
    def __enter__(self):
        print('Inside __enter__ method')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('Inside __exit__ method')
        print("{} | {} | {}".format(exc_type, exc_val, exc_tb))

    def growUp(self):
        print('Growing up...')


with Man() as obj:
    obj.growUp()

print('# ' * 20)
# @classmethod and @staticmethod decorators
class Toy(object):
    count = 0

    def __init__(self, name, color):
        self.name = name
        self.color = color
        self.count = self.incrementCount()
        self.checkforName(self.name)

    @classmethod   #The @classmethod decorator denotes a method that operates on the class attributes rather than
    # instance attributes.
    def incrementCount(cls):
        cls.count += 1
        return cls.count

    @classmethod
    def getCount(self):
        print('Number of toys manufactured so far : {}'.format(self.count))

    @staticmethod
    def checkforName(name):
        if name.startswith('w') or name.startswith('W'):
            print('Howdy! Its Woody this side')
        elif name.startswith('B') or name.startswith('B'):
            print('No fear, Buzz Lightyear is here')
        else:
            print('{} in the team'.format(name))


woody = Toy('Woody', 'Brown')
jessie = Toy('Jessie', 'Fair')
buzz = Toy('Buzz LightYear', 'White')
potatohead = Toy('Mr Potatohead', 'Brown')
forky = Toy('Forky', 'white')
Toy.getCount()


# Enforcing encapsulation: @property class
