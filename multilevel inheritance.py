class GrandParent:
    def granparent_method(self):
        print('This is a method from the GrandParent class. ')

class Parent(GrandParent):
    def parent_method(self):
        print('This is a method from the Parent class. ')

class Child(Parent,GrandParent): # IS# multiple inherited
    def child_method(self):
        print('This is a method from the child class. ')

#Example 
child = Child()  #object create
child.granparent_method()
child.parent_method()  #Inherited from parent
child.child_method()  #own method

