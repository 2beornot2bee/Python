class Parent(object):

    def implicity(self):
        print("PARENT implicity()")

class Child(Parent):
    pass

dad=Parent()
son=Child()

dad.implicity()
son.implicity()
