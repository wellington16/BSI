class Node():
    
    def __init__(self, key):
        self.key = key
        self.parent = None
        self.left = None
        self.right = None

    def __str__(self):
        return str("No: " + str(self.key) )#+ "\t" + "dado: " + str(self.()))
class AVL():
    
    def __init__(self):
        self.root = None
        
    def inorder(self,  x):
        if x != None:
            self.inorder( x.left)
            #l.append(str(x.key))
            print(x.key)
            self.inorder( x.right)
            
    def preorder(self, x):
        if x != None:
            #l.append(str(x.key))
            print(x.key)
            self.preorder(x.left)
            self.preorder(x.right)
            
    def postorder(self, x):
        if x != None:
            self.preorder(x.left)
            self.preorder(x.right)
            print(x.key)
            #l.append(str(x.key))
    
    def search(self, k):
        x = self.root
        while x != None and k != x.key:
            if k < x.key:
                x = x.left
            else:
                x = x.right
        return x
            
    def minimum(self, x):
        while x.left != None:
            x = x.left
        return x
    
    def maximum(self, x):
        while x.right != None:
            x = x.right
        return x
        
    def successor(self, x):
        if x == None:
            return None
        else:
            if x.right != None:
                return self.minimum(x.right)
            y = x.parent
            while y != None and x == y.right:
                x = y
                y = y.parent
            return y
        
    def predecessor(self, x):
        if x == None:
            return None
        else:
            if x.left != None:
                return self.maximum(x.left)
            y = x.parent
            while y != None and x == y.left:
                x = y
                y = y.parent
            return y

    def insert(self, z):
        z = Node(z)
        y = None
        x = self.root
        while x != None:
            y = x
            if z.key <= x.key:
                x = x.left
            else:
                x = x.right
        z.parent = y
        if y == None:
            self.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z
        '''
        parent = y
        while parent is not None:
            if self.balancing(parent) == True:
                break
            else:
                parent = parent.parent
        '''
            
    def transplant(self, u, v):
        if u.parent == None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        if v != None:
            v.parent = u.parent
            
    def delete(self, z):
        z = self.search(z)
        if z.left == None:
            self.transplant(z, z.right)
        elif z.right == None:
            self.transplant(z, z.left)
        else:
            y = self.minimum(z.right)
            if y.parent != z:
                self.transplant(y, y.right)
                y.right = z.right
                y.right.parent = y
            self.transplant(z, y)
            y.left = z.left
            y.left.parent = y
            
    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left is not None:
            y.left.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x is x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y
        
    def right_rotate(self, y):
        x = y.left
        y.left = x.right
        if x.right is not None:
            x.right.parent = y
        x.parent = y.parent
        if y.parent is None:
            self.root = x
        elif y is y.parent.right:
            y.parent.right = x
        else:
            y.parent.left = x
        x.right = y
        y.parent = x

    def doubleRotateRight(self, x):  # x eh no
        filhoesq = x.right()
        self.left_rotate(filhoesq)
        self.right_rotate(x)

    def doubleRotateleft(self, x):
        filhodir = x.left
        self.right_rotate(filhodir)
        self.left_rotate(x)

    def height(self, x):
        if x is None:
            return -1
        h1 = self.height(x.left)
        h2 = self.height(x.right)
        return (1 + max(h1, h2))
        
    def balance_factor(self, x):
        return (self.height(x.right) - self.height(x.left))
    
    def balancing(self, x):
        factor = self.balance_factor(x)
        if factor > 1:
            if self.balance_factor(x.right) < 0:
                self.doubleRotateleft(x)
            else:
                self.left_rotate(x)
            return True
        elif factor < -1:
            if self.balance_factor(x.left) > 0:
                self.doubleRotateRight(x)
            else:
                self.right_rotate(x)
            return True
        else:
            return False

minhaArvore = AVL()
minhaArvore.insert(10)
minhaArvore.insert(20)
minhaArvore.insert(20)
minhaArvore.insert(30)


print("Em Ordem:")
minhaArvore.inorder(minhaArvore.root)
minhaArvore.left_rotate(minhaArvore.root)
print("Em Pré-ordem")
minhaArvore.delete(10)
minhaArvore.inorder(minhaArvore.root)
print("Em Pós-ordem")
minhaArvore.postorder(minhaArvore.root)