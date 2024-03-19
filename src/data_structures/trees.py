from collections import deque

class ListNode:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert(self, data):
        if not self.head:
            self.head = ListNode(data)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = ListNode(data)

    def print_list(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

class Tree:
    def __init__(self, root=None):
        self.root = root
    
    def dfs(self, node: TreeNode):
        if node is None:
            return []
        
        result = [node.data]
        result += self.dfs(node.left)
        result += self.dfs(node.right)
        return result
    
    def bfs(self, root: TreeNode):
        if root is None:
            return []
        
        queue = deque([root])
        result = []

        while queue:
            node = queue.popleft()
            result.append(node.data)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        return result
    
# exemplo de uso
node6 = TreeNode(4)
node7 = TreeNode(7)

node9 = TreeNode(1)
node5 = TreeNode(0)

node8 = TreeNode(3, left=node9)

node4 = TreeNode(6, left=node8)

node3 = TreeNode(2, left=node6, right=node7)
node2 = TreeNode(5, left=node4, right=node5)
node1 = TreeNode(8, left=node2, right=node3)

tree = Tree(node1)
print(f'Depth first search: {tree.dfs(node1)}')
print(f'Breadth first search: {tree.bfs(node1)}')