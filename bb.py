#implement python program to demonstrate binary search tree it's operation

class Node:
    def __init__ (self,key):
        self.left=None
        self.rigth=None
        self.val=key

    def insert (root,key):
        if root is None:
            return Node(key)
        else:
            if root.val==key:
                return root
            elif root.val<key:
                root.right=insert(root.right,key)
            else:
                root.left=insert(root.left,key)
        return root

    def Inorder(root):
        if root:
            Inorder(root.left)
            print(root.val,end=" ")
            Inorder(root.right)

    def Preorder(root):
        if root:
            print(root.val,end=" ")
            preorder(root.left)
            preorder(root.right)

    def Postorder(root):
        if root:
            postorder(root.left)
            postorder(root.rigth)
            print(root.val,end=" ")


    #Driver code
    if __name__=="__main__":
        r=Node(25)
        r=insert(r,20)
        r=insert(r,36)
        r=insert(r,10)
        r=insert(r,22)
        r=insert(r,30)
        r=insert(r,40)
        r=insert(r,5)
        r=insert(r,12)
        r=insert(r,28)
        r=insert(r,38)
        r=insert(r,48)

    #Function call
    print("Inorder traversal of binary search tree is:")
    Inorder(r)
    print("\n")
    print("\Preorder traversal of binary search tree is:")
    Preorder(r)
    print("\n")
    print("\Postorder traversal of binary search tree is:")
    postorder(r)
    print("\n")
        
            
