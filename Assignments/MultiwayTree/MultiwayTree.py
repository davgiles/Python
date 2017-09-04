#  File: MultiwayTree.py
#  Description:
#  Student"s Name: David Giles
#  Student"s UT EID: dgg524
#  Course Name: CS 313E
#  Unique Number: 86940
#
#  Date Created: 08/04/17
#  Date Last Modified:

import ast


class MultiwayTree:

    # given pyTree (Python representation of tree), create node-pointer rep of tree
    def __init__(self, pyTree):
        self.children = []
        self.data = pyTree[0]
        for item in pyTree[1]:
            self.insertChild(item)

    def insertChild(self, newTree):
        t = MultiwayTree(newTree)
        self.children.append(t)

    def getChildren(self):
        return self.children

    def hasChildren(self):
        if self.children:
            return True
        else:
            return False

    def setRootVal(self, value):
        self.data = value

    def getRootVal(self):
        return self.data

    def preOrder(self):
        print(self.data, end=" ")
        if self.children:
            for item in self.children:
                item.preOrder()

    def isIsomorphicTo(self, other):
        if len(self.children) != len(other.children):
            return False

        for i in range(len(self.children)):
            self.children[i].isIsomorphicTo(other.children[i])

        return True


def main():

    in_file = open("./MultiwayTreeInput.txt", "r")

    trees = []

    for line in in_file:
        line = line.strip()
        line = ast.literal_eval(line)
        trees.append(line)

    for i in range(0, len(trees)-1, 2):
        a = MultiwayTree(trees[i])
        print("Tree " + str(i + 1) + ":  " + str(trees[i]))
        print("Tree " + str(i + 1) + " preorder:  ", end="")
        a.preOrder()
        print("\n")

        b = MultiwayTree(trees[i + 1])
        print("Tree " + str(i + 2) + ":  " + str(trees[i + 1]))
        print("Tree " + str(i + 2) + " preorder:  ", end="")
        b.preOrder()
        print("\n")

        if a.isIsomorphicTo(b):
            print("Tree " + str(i + 1) + " is isomorphic to Tree " + str(i + 2))
        else:
            print("Tree " + str(i + 1) + " is NOT isomorphic to Tree " + str(i + 2))

        print("\n")

main()
