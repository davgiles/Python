#  File: ExpressionTree.py
#  Description: This program creates expression trees,
#    displays in infix, prefix, and postfix notation,
#    and evaluates the expressions.
#  Student"s Name: David Giles
#  Student"s UT EID: dgg524
#  Course Name: CS 313E
#  Unique Number: 86940
#
#  Date Created: 08/02/17
#  Date Last Modified: 08/02/17

import operator


class BinaryTree(object):

    def __init__(self, initVal=None, parent=None):
        self.data = initVal
        self.left = None
        self.right = None
        self.parent = parent

    def insertLeft(self, newNode):
        if self.left == None:
            self.left = BinaryTree(newNode)
            self.left.parent = self
        else:
            t = BinaryTree(newNode)
            t.left = self.left
            self.left = t

    def insertRight(self, newNode):
        if self.right == None:
            self.right = BinaryTree(newNode)
            self.right.parent = self
        else:
            t = BinaryTree(newNode)
            t.right = self.right
            self.right = t

    def getLeftChild(self):
        return self.left

    def getRightChild(self):
        return self.right

    def setRootVal(self, value):
        self.data = value

    def getRootVal(self):
        return self.data

    def createTree(self, expr):
        current = self

        for token in expr:
            if token == "(":
                current.insertLeft(token)
                current = current.left
            elif token == ")":
                current = current.parent
            elif token in "+-*/":
                current.setRootVal(token)
                current.insertRight(token)
                current = current.right
            else:
                current.setRootVal(token)
                current = current.parent

    def evaluate(self):
        opers = {'+':operator.add, '-':operator.sub, '*':operator.mul, '/':operator.truediv}
        opand1 = None
        opand2 = None
        
        if self.left:
            opand1 = self.left.evaluate()
        if self.right:
            opand2 = self.right.evaluate()
            
        if opand1 and opand2:
            return opers[self.data](opand1, opand2)
        else:
            return eval(self.data)

    def preOrder(self):
        print(self.data, end=" ")
        if self.left:
            self.left.preOrder()
        if self.right:
            self.right.preOrder()

    def postOrder(self):
        if self.left:
            self.left.postOrder()
        if self.right:
            self.right.postOrder()
        print(self.data, end=" ")


def main():

    in_file = open("./treedata.txt", "r")

    for line in in_file:
        line = line.strip()
        expr = line.split()

        bt = BinaryTree()
        bt.createTree(expr)

        print("Infix expression:", line, end="\n\n")
        print("\tValue:\t", bt.evaluate())
        print("\tPrefix expression:", end="\t")
        bt.preOrder()
        print()
        print("\tPostfix expression:", end="\t")
        bt.postOrder()
        print("\n")

main()
