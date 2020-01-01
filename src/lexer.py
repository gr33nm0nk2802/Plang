
import re 

class Lexer(object):

    def __init__(self, source_code):
        self.source_code = source_code

    def tokenize(self):
        
        # Variable to store all tokens created by the lexer
        tokens = []

        # Create a word list of the source code
        source_code = self.source_code.split()

        # Index of the word we are at
        source_index = 0

        # Looping throug each word in the source code to generate tokens
        while source_index < len(source_code):

            word= (source_code[source_index])
            
            # This will recognising variable and creating token
            if word == "var": tokens.append(["VAR_DECLARATION", word])
            
            # This will recognise a word and create an identifier token
            elif re.match('[a-z]',word) or re.match('[A-Z]',word):
                if word[len(word)-1]==";":
                    tokens.append(["IDENTIFIER", word[0:len(word)-1]])
                else:
                    tokens.append(["IDENTIFIER", word])
            
            # This will recognise an integer and create an integer token
            elif re.match('[0-9]',word):
                if word[len(word)-1]==";":
                    tokens.append(["INTEGER", word[0:len(word)-1]])
                else:
                    tokens.append(["INTEGER", word])
            
            # This will recognise an operator and create an OPERATOR token
            elif word in "+-*/%=":
                tokens.append(["OPERATOR", word])   

            # If STATEMENT_END (;) is found at the last character in a word add a STATEMENT_END token 
            if word[len(word)-1]==';':
                tokens.append(["STATEMENT_END", ';'])       
            
            #incrementing index
            source_index += 1   
        
        print(tokens)

        # Return created tokens
        return tokens










