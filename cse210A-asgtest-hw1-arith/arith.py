
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
    def next_char(self):
        self.index+=1
        # if end of input, current character is none
        if(self.index > len(self.text)-1):
            self.current = None
        # otherwise set the character
        else:
            self.current = self.text[self.index]
     
    def skip(self):
         while self.current is not None and self.current.isspace():
             self.next_char()

    #deal with integer being multiple digits
    def big_num(self):
        result = ''
        while self.current is not None and self.current.isdigit():
            result = result + self.current
            self.next_char()
        casted = int(result)
        return casted

    def next_token(self):
        while self.current is not None:

            if(self.current.isspace()):
                print("skipping")
                self.next_char()

            if self.current.isdigit():
                value = self.big_num()
                print("get_next_token() returning int token {}".format(value))
                return Token(INT,value)

            elif self.current == '*':
                self.next_char()
                print("get_next_token() returning mul token")
                return Token(MUL,'*')

            elif self.current == '+':
                self.next_char()
                print("get_next_token() returning add token")
                return Token(ADD,'+')

            elif self.current == "-":
                self.next_char()
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

# initialize the parser to start with the first token from the input
class Parser(object):
    def __init__(self,lexer):
        self.lexer = lexer
        self.curr_token = self.lexer.next_token()
    
    # get the next token from the input if the current token and next token have matching types
    def get_token(self,token_type):
        if self.curr_token.type == token_type:
            self.curr_token = self.lexer.next_token()
        else:
            self.error()
    
    def factor(self):
        token = self.curr_token
        if(token.type == INT):
            self.get_token(INT)
            return Num(token)
        elif token.type == SUB:
            self.curr_token = self.lexer.next_token()
            token = self.curr_token
            token.value = -1 * self.curr_token.value
            self.curr_token  = self.lexer.next_token()
            return Num(token)
    
    def term(self):
        node = self.factor()

        while self.curr_token.type == MUL:
            token = self.curr_token
            if token.type == MUL:
                self.get_token(MUL)
            
            node = MathOp(node,self.factor(), token)
        
        return node

    
    def expr(self):
        node = self.term()

        while self.curr_token.type in (ADD,SUB):
            token = self.curr_token
            if token.type == ADD:
                self.get_token(ADD)
            elif token.type == SUB:
                self.get_token(SUB)
            
            node = MathOp(node,self.term(),token)

        return node

    
    def parse(self):
        return self.expr()


class VisitTree(object):
    def visit(self, node):
        method_name = 'visit_' + type(node).__name__
        visitor = getattr(self, method_name, self.generic_visit)
        return visitor(node)

    def generic_visit(self, node):
        raise Exception('No visit_{} method'.format(type(node).__name__))
    
class Interpreter(VisitTree):
    def __init__(self,parser):
        self.parser = parser

    # interpret the nodes and perform functions
    def visit_MathOp(self,node):
        print("in solve")
        
        if(node.op.type==MUL):
            return (self.visit(node.left) * self.visit(node.right))
        elif(node.op.type==ADD):
            print("in add")
            return (self.visit(node.left) + self.visit(node.right))
        elif(node.op.type==SUB):
            return (self.visit(node.left) - self.visit(node.right))

    def visit_Num(self,node):
        return (node.value)
    
    # pase tree then sove tree 
    def driver(self):
        tree = self.parser.parse()
        return self.visit(tree)

def main():
    checker = Num(Token(INT,6))
    print(type(checker))
    # token_t0 = Token(INT, 5)
    # token_t1 = Token(MUL,"*")
    # token_t0.token_print()
    # token_t1.token_print()
    
    while True:
        try:
            raw_data = ("-2 + 3 * 5 + -6")
            #raw_data = input("")
            
        except EOFError:
            break
        
        lexer = Lexer(raw_data)
        parser = Parser(lexer)
        print("breaker point")
        interpreter = Interpreter(parser)
        result = interpreter.driver()
        print(result)
        break

if __name__ == "__main__":
    main()