class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        # Your code goes here
        new=Node(new_val)
        if(self.root==None):
            self.root=new
        else:
            crnt=self.root
            nxt=self.root
            while(crnt!=None):
                prnt=crnt
                if(new_val<crnt.value):
                    crnt=crnt.left
                else:
                    crnt=crnt.right
            if(new_val<prnt.value):
                prnt.left=new
            else:
                prnt.right=new


    def printSelf(self):
        # Your code goes here
        print(self.root)
        
    def search(self, find_val):
        # Your code goes here
        while(self.root!=None):
            if(self.root.value==find_val):
                return True
            if(self.root.value<find_val):
                self.root=self.root.right
            else:
                self.root=self.root.left
        return False

