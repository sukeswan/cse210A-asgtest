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

    # skip will be used to skip white spaces in the raw data
    def skip(self):
         while self.current is not None and self.current.isspace():
             self.next_char()

    # deal with integer being multiple digits by parsing mutiple digits together
    def big_num(self):
        result = ''
        while self.current is not None and self.current.isdigit():
            result = result + self.current
            self.next_char()
        casted = int(result)
        return casted

    # used to get the next token from the lexer format type will be Token(type,value)
    def next_token(self):
        while self.current is not None:

            if(self.current.isspace()):
                #print("skipping")
                self.next_char()

            if self.current.isdigit():
                value = self.big_num()
                #print("get_next_token() returning int token {}".format(value))
                return Token(INT,value)

            elif self.current == '*':
                self.next_char()
                #print("get_next_token() returning mul token")
                return Token(MUL,'*')

            elif self.current == '+':
                self.next_char()
                #print("get_next_token() returning add token")
                return Token(ADD,'+')

            elif self.current == "-":
                self.next_char()
                #print("get_next_token() returning sub token")
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

    # recursive calls to factor will give highest precedence to to integers to be evaluate first
    def factor(self):
        token = self.curr_token
        if(token.type == INT):
            self.get_token(INT)
            return Num(token)
        elif token.type == SUB:
            self.curr_token = self.lexer.next_token()
            token = self.curr_token
            token.value = -1 * token.value
            self.curr_token  = self.lexer.next_token()
            return Num(token)
    
    # term will give the next level of precedence to multiplication 
    def term(self):
        node = self.factor()

        while self.curr_token.type == MUL:
            token = self.curr_token
            if token.type == MUL:
                self.get_token(MUL)
            
            node = MathOp(node,self.factor(), token)
        
        return node

    # the last level of priority is addition and subtraction, which have the same priority 
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


# solve a subtree based on the type of node
class VisitTree(object):
    def visit(self, node):
        method = 'solve_' + type(node).__name__
        visitor = getattr(self, method)
        return visitor(node)

# interpreter to evaluate AST Tree
class Interpreter(VisitTree):
    def __init__(self,parser):
        self.parser = parser

    # interpret the nodes and perform functions
    def solve_MathOp(self,node):
        
        if(node.op.type==MUL):
            return (self.visit(node.left) * self.visit(node.right))
        elif(node.op.type==ADD):
            return (self.visit(node.left) + self.visit(node.right))
        elif(node.op.type==SUB):
            return (self.visit(node.left) - self.visit(node.right))
        

    def solve_Num(self,node):
        return (node.value)
    
    # pase tree then sove tree 
    def driver(self):
        tree = self.parser.parse()
        return self.visit(tree)

def main():
    #checker = Num(Token(INT,6))
    #print(type(checker))
    # token_t0 = Token(INT, 5)
    # token_t1 = Token(MUL,"*")
    # token_t0.token_print()
    # token_t1.token_print()
    
    while True:
        try:
            #raw_data = ("-2 + 3 * 5 + -6")
            raw_data = input("")
            
        except EOFError:
            break
        
        lexer = Lexer(raw_data)
        parser = Parser(lexer)
        #print("breaker point")
        interpreter = Interpreter(parser)
        result = interpreter.driver()
        print(result)
        

if __name__ == "__main__":
    main()