class VariableObject(object):

    def __init__(self):
        # This will hold the python executable string for variable declaration
        self.exec_string = ""
    
    def transpile(self,name,operator,value):
        # Appends the python executable string converted using parser
        self.exec_string += name + " "+operator+" "+value
        return self.exec_string
