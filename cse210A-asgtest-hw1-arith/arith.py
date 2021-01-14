import sys
import random
print("\n..... arith.py starting .....\n")

# types for nodes 

INTEGER = 'INTEGER'
PLUS    = 'PLUS'
MINUS   = 'MINUS'
MUL     = 'MUL'


# an AST can either be a math operation or just an integer
class AST(object):
    pass

# Math operations are binary nodes with the root being the math operation 
class MathOp(AST):
    def __init__(self, left, right, op):
        self.left = left
        self.op = op
        self.right = right

class Int(AST):
    def __init__(self, value):
        self.value = value
        self.op = INTEGER

# interpret the nodes and perform functions
def interpreter(node):
    if(node.op==INTEGER):
        return (node.value)
    elif(node.op==MUL):
        return (interpreter(node.left) * interpreter(node.right))
    elif(node.op==PLUS):
        return (interpreter(node.left) + interpreter(node.right))
    elif(node.op==MINUS):
        return (interpreter(node.left) - interpreter(node.right))

# a function to run tests
def test(id,a,b,op):
    valA = Int(a)
    valB = Int(b)
    tester= MathOp(valA, valB, op)
    
    check2 = 0 

    check1 = interpreter(tester)
    if(op==MUL):
        check2 = a*b
    elif(op==PLUS):
        check2 = a+b
    elif(op==MINUS):
        check2 = a-b
    
    if(check1!=check2):
        print("TEST {} FAILED".format(id))
        print("A= {} B= {} w/ operation {}".format(a,b,op))
        return False
    
    return True

def run_basic_tests():

    all_passed = True
    
    while(all_passed):

        for i in range(10):
            a = random.randint(0,10)
            b = random.randint(1,11)

            all_passed = test(i+0.1, a,b,MUL)
            all_passed = test(i+0.2, a,b,PLUS)
            all_passed = test(i+0.3, a,b,MINUS)
        
        break
    
    if(all_passed):
        print("ALL BASIC TESTS PASSED\n")


def lexer(raw_data):
    # process the raw_data into list of tokens

    tokens = []
    opIndicies = []
    cur = 0 
    for chars in raw_data:
        #skip whitespaces
        if(chars == ' '):
            continue
        if(chars in "*+-"):
            opIndicies.append(cur)
        
        tokens.append(chars)
        cur+=1
    
    #keep track of indicies that need to be deleted
    delInd = []

    # bind - signs to negative values
    for i in opIndicies:
        if(i==0):
            tokens[1] = tokens[0] + tokens[1]
            delInd.append(0)
        if(tokens[i]=='-' and tokens[i-1] in "*+-"):
            tokens[i] = tokens[i] + tokens[i+1]
            delInd.append(i+1)
    
    final_tokens = []
    #copy over indicies 
    for i in range(len(tokens)):
        if(i in delInd):
            continue
        else:
            final_tokens.append(tokens[i])
    
    # keep track of new operational indicies 
    opIndicies = []
    cur = 0
    for chars in final_tokens:
        if(chars in "*+-"):
            opIndicies.append(cur)
        cur+=1


    print(final_tokens)
    print(opIndicies)

# buildAST(tokens, rootIndex):
#     root= tokens[rootIndex]
#     if(root not in "-+*"):
#         return Int(root)
#     elif(root == "-"):
#         return MathOp(left,right,MINUS)
#     elif(root == "-"):
#     elif(root == "-"):





lexer("6 + -3 * 8")


print("\n...... arith.py ending ......\n")
# inp = input(sys.stdin)
# print (inp)