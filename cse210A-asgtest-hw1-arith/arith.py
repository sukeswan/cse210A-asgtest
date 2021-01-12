import sys
print("\n..... arith.py starting .....\n")

# types for nodes 

INTEGER = 'INTEGER'
PLUS    = 'PLUS'
MINUS   = 'MINUS'
MUL     = 'MUL'
DIV     = 'DIV'

# nodes will type plus string character for operation 
# example: Node(MUL, "*")

class Node(object):
    def __init__(self, type, value):
        self.type = type
        self.value = value

    # String reprsentation for testing
    def __str__(self):
        return 'Node({type}, {value})'.format(
            type=self.type,
            value=repr(self.value)
        )

# an AST can either be a math operation or just an integer
class AST(object):
    pass

# Math operations are binary nodes with the root being the math operation 
class MathOp(AST):
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right

class Int(AST):
    def __init__(self, node):
        self.node = node
        self.value = node.value







#define the math operations 
mul_node = Node(MUL, '*')
plus_node = Node(PLUS, '+')
minus_node = Node(MINUS, '-')
div_node = Node(DIV, '/')




print("...... arith.py ending ......\n")
# inp = input(sys.stdin)
# print (inp)