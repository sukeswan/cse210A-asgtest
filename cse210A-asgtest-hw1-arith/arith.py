# macros for data types
MUL = "MUL"
ADD = "ADD"
SUB = "SUB"
INT = "INT"


# Data will tokenized into raw data and type tuple
# examples: Token(INT, 45) 
#           Token(MUL, "*")

class Token(object):
    def __init__(self,type,value):
        self.type = type
        self.value = value

    # string representation for debugging and testing tokens
    def __repr__(self):
        return ("Token({},{})".format(self.type, repr(self.value)))

#Lexer class will process the raw string data from standard in 
class Lexer(object):
    def __init__(self,text):
        # text, index to iterate through text, and current for current character
        self.text = text
        self.index = 0 
        self.current = self.text[self.index]
    
    # move the index up to the next char
    def advance(self):
        self.pos+=1
        # if end of input, current character is none
        if(self.pos > len(self.text)-1):
            self.current = None
        # otherwise set the character
        else:
            self.current = self.text[self.pos]
        
        #skip whitespace
        if(self.current.isspace()):
            self.advance()
    
    def get_next_token(self):
        while self.current is not None:

            if self.current.isdigit():
                return Token(INT,self.integer())

            elif self.current == '*':
                self.advance()
                return Token(MUL,'*')

            elif self.current == '+':
                self.advance()
                return Token(ADD,'+')

            elif self.current == "-":
                self.advance()
                return Token(SUB,'-')
    


    


