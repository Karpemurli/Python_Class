class test:
    #member function(methods)
    
    def show_message(self):
        print('Hello I am from class')
        
    def show(self):
        print('I am from show')
        
# if  I want to access the show_message() method I need to create the object of class.

obj_test = test() #here I am creating the odject
obj_test.show_message()
obj_test.show()


