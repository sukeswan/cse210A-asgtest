import sys

# macros for data types
MUL = "MUL"
ADD = "ADD"
SUB = "SUB"
INT = "INT"
EOF = "EOF"


# Data will tokenized into raw data and type tuple
# examples: Token(INT, 45) 
#           Token(MUL, "*")

class Token(object):
    def __init__(self,type,value):
        self.type = type
        self.value = value

    # string representation for debugging and testing tokens
    def token_print(self):
        print("Token({},{})".format(self.type, self.value))
        

#Lexer class will process the raw string data from standard in 
class Lexer(object):
    def __init__(self,text):
        # text, index to iterate through text, and current for current character
        self.text = text
        self.index = 0 
        self.current = text[self.index]
    
    # move the index up to the next char
    def advance(self):
        print("advance start: {}".format(self.index))
        self.index+=1
        print("advance up: {}".format(self.index))
        # if end of input, current character is none
        if(self.index > len(self.text)-1):
            print("advance() out of bounds case")
            self.current = None
        # otherwise set the character
        else:
            print("advancing")
            self.current = self.text[self.index]
     
    def skip(self):
         while self.current is not None and self.current.isspace():
             self.advance()

    #deal with integer being multiple digits
    def big_num(self):
        result = ''
        while self.current is not None and self.current.isdigit():
            result = result + self.current
            self.advance()
        casted = int(result)
        print("Big num returns {}".format(casted))
        return casted

    def get_next_token(self):
        while self.current is not None:

            if(self.current.isspace()):
                print("skipping")
                self.advance()

            if self.current.isdigit():
                value = self.big_num()
                print("get_next_token() returning int token {}".format(value))
                return Token(INT,value)

            elif self.current == '*':
                self.advance()
                print("get_next_token() returning mul token")
                return Token(MUL,'*')

            elif self.current == '+':
                self.advance()
                print("get_next_token() returning add token")
                return Token(ADD,'+')

            elif self.current == "-":
                self.advance()
                print("get_next_token() returning sub token")
                return Token(SUB,'-')
        
        return Token(EOF, None)
            

# wrapper AST class
class AST(object):
    pass

# for math operations with a left int and right int
class MathOp(AST):
    def __init__(self,left,right,op):
        self.left= left
        self.right = right
        self.op = op
        self.token = op 

# for integer values
class Num(AST):
    def __init__(self,token):
        #set value to be the value in the integer token object
        self.token = token
        self.value = token.value
        self.op = INT

class Parser(object):
    def __init__(self,lexer):
        self.lexer = lexer
        self.curr_token = lexer.get_next_token()

    # function to deal with integer types 
    def get_numbers(self):
        token = self.curr_token
        if token.type == INT:
            node = Num(token)
            self.curr_token  = self.lexer.get_next_token()
            return node
        # deal with negative numbers by geting next token and make negative
        elif token.type == SUB:
            self.curr_token = self.lexer.get_next_token()
            token = self.curr_token
            token.value = -1 * self.curr_token.value
            self.curr_token  = self.lexer.get_next_token()
            return Num(token)

    # for a multiply expression get the fist number, and make a math operation
    def multiply(self):
        node = self.get_numbers()
        if self.curr_token.type == MUL:
            self.current_token = self.lexer.get_next_token()
            node = MathOp(node,self.get_numbers(),MUL)
        return node
    
    # to made additiion and subtraction nodes 
    def expression(self):
        node = self.multiply()
        while self.curr_token.type in (ADD,SUB):
            token = self.curr_token
            if token.type == ADD:
                self.curr_token = self.lexer.get_next_token()
                node =  MathOp(node,self.multiply(), ADD)
            elif token.type == SUB:
                self.curr_token = self.lexer.get_next_token()
                node =  MathOp(node,self.multiply(), SUB)
        return node 
    
    def parse(self):
        return self.expression()

class Interpreter(object):
    def __init__(self,root):
        self.root = root

    # interpret the nodes and perform functions
    def solve(self,node):
        if(node.op==INT):
            print("returning value {}".format(node.value))
            return (node.value)
        elif(node.op==MUL):
            return (self.solve(node.left) * self.solve(node.right))
        elif(node.op==ADD):
            return (self.solve(node.left) + self.solve(node.right))
        elif(node.op==SUB):
            return (self.solve(node.left) - self.solve(node.right))
    
    # pase tree then sove tree 
    def driver(self):
        tree = self.root.parse()
        return self.solve(tree)

def main():

    token_t0 = Token(INT, 5)
    token_t1 = Token(MUL,"*")
    token_t0.token_print()
    token_t1.token_print()

    while True:
        try:
            raw_data = ("3 * 2")
            #raw_data = input("")
            
        except EOFError:
            break
        
        lexer = Lexer(raw_data)
        parser = Parser(lexer)
        interpreter = Interpreter(parser)
        result = interpreter.driver()
        print(result)
        break

if __name__ == "__main__":
    main()