import lexer
import parser

def main():
    
    # Read the current flow source code in test.lang and store it in variable
    content = ""
    with open('test.lang','r') as file:
        content = file.read()
    
    ############################
    #         Lexer            #
    ############################

    # Calling the lexer file Lexer class and initializing it with the source code
    lex = lexer.Lexer(content)
    # Calling the tokenize method from inside the lexer instance
    tokens= lex.tokenize()

    ############################
    #         Parser           #
    ############################

    # Calling the parser file Parser class and initializing it with the source code
    parse = parser.Parser(tokens)
    # Calling the parse method from inside the parse instance
    parse.parse()

main()

