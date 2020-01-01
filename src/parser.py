from Objects.varObject import VariableObject

class Parser(object):

    def __init__(self, tokens):
        # This will hold the tokens that have been created by the lexer
        self.tokens = tokens
        # This will hold the token index we are parsing at
        self.token_index = 0
        self.transpiled_code = ""


    # The parse method to loop through tokens
    def parse(self):
        while self.token_index < len(self.tokens):
            
            # Holds the type of token e.g-IDENTIFIER
            token_type  = self.tokens[self.token_index][0]
            token_value = self.tokens[self.token_index][1]

            # This will trigger in case of variable declaration
            if token_type == "VAR_DECLARATION" and token_value == "var":
                self.parse_variable_declaration(self.tokens[self.token_index:len(self.tokens)])

            # Increment token index 
            self.token_index +=1 
        
        print(self.transpiled_code)

    
    def parse_variable_declaration(self, token_stream):

        tokens_checked = 0

        name     = ""
        operator = ""
        value    = ""

        for token in range (0, len(token_stream)):

            token_type  = token_stream[tokens_checked][0]
            token_value = token_stream[tokens_checked][1]

            # Breaks out of loop in case of statement end
            if token == 4 and token_type == "STATEMENT_END": break

            
            # This will get the variable name and also perform error validiation
            elif token == 1 and token_type == "IDENTIFIER":
                name = token_value
            elif token == 1 and token_type != "IDENTIFIER":
                print("ERROR: Invalid variable name ' " + token_value +" ' ")
                quit()

            # This will check variable assignment operator    
            elif token == 2 and token_type =="OPERATOR":
                operator = token_value
            elif token == 2 and token_type !="OPERATOR":
                print("ERROR: Assignment operator is missing or invalid")
                quit()

            # This will get variable values assigned 
            elif token == 3 and token_type in['STRING', 'INTEGER', 'IDENTIFIER']:
                value = token_value
            elif token == 3 and token_type not in['STRING', 'INTEGER', 'IDENTIFIER']:
                print("Invalid Variable assignment value '"+token_value+"'")
                quit()

            tokens_checked += 1

        # Increment token index by number of tokens checked
        self.token_index = tokens_checked
    
        varObj = VariableObject()
        self.transpiled_code += varObj.transpile(name, operator, value)