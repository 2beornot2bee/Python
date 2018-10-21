class Parent(object):
##  Any function has to have same name in child class Like: override function on parent and child classes.
    def override(self):
        print("PARENT override() ")


class Child(Parent):

    def override(self):
        print("CHILD override()")



dad=Parent()
son=Child()

dad.override()
son.override()
