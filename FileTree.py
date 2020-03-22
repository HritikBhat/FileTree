class TreeNode:
    def __init__(self,data):
        #Stores the data
        self.data=data
        #Store children of the node
        self.children=[]

class Tree:
    def __init__(self,root):
        self.root=root

    def addNode(self,parent,node):
        #Adds node to parent's children list
        parent.children.append(node)

    def addNodes(self,parent,nodelist):
        #Add list of node to parent's children list
        parent.children.extend(nodelist)

    #It returns list which contains parent of the node(called by user to find) and node respectively.
    def findNode(self,root,data):
        if data is None:
            return -1
        if root is None:
            root = self.root
        if root.data is data:
            return 1
        else:
            for child in root.children:
                a=self.findNode(child,data)
                if a==1:
                    lt=[root,child]
                    return lt
                elif a is not None:
                    return a
        return -1

    def updateNode(self,data,newdata):
        val=self.findNode(None,data)
        if val==-1:
            print("The Node Is Not Present")
        else:
            val[1].data=newdata
            print("Update Successful!")

    def deleteNode(self,data):
        val=self.findNode(None,data)
        if val==-1:
            print("The Node Is Not Present")
        elif val==1:
            print("Root cannot be deleted!")
        else:
            val[0].children.remove(val[1])
            print("Delete Successful!")
        
    def printTree(self,root=None,i=0):
        if root is None:
            root = self.root
        space=i*' '
        print(space+root.data)
        i+=1
        for child in root.children:
            self.printTree(child,i)

"""
Demo Example To Run

A=TreeNode("A")
B=TreeNode("B")
C=TreeNode("C")
D=TreeNode("D")
Z=TreeNode("Z")
Y=TreeNode("Y")
tr=Tree(A)
tr.addNodes(A,[B,C])
tr.addNodes(B,[Z,Y])
tr.printTree()
lst=tr.findNode(None,'Z')
if lst != -1:
    print("Parent Of Finding Element:",lst[0].data)
    print("Finding Element:",lst[1].data)

#tr.deleteNode('Z')
#tr.printTree()

tr.updateNode('Z','J')
tr.printTree()
"""

