class Tree:
    def __init__(self,val):
        self.left = None
        self.right = None
        self.data = val

ar = [6,3,7,4,9,8]
root = Tree(ar.pop(0))

while len(ar):
    ele = ar.pop(0)
    curr_node = root
    while True:
        if ele>curr_node.data:
            if curr_node.right is None:
                curr_node.right = Tree(ele)
                break
            curr_node = curr_node.right
        else:
            if curr_node.left is None:
                curr_node.left = Tree(ele)
                break
            curr_node = curr_node.left

#Do inorder traversal
def inorder(root):
    if root is None:
        return
    inorder(root.left)
    print(root.data)
    inorder(root.right)

# st = [[root,False]]
# while len(st):
#     n,status = st.pop(-1)
#     if status:
#         print(n)
#     elif(n):
#         st.append([n.data, True])
#         st.append([n.right, False])
#         st.append([n.left,False])

q = [[[root],0]]
while len(q):
    node_arr,l = q.pop(0)
    new_iter = []
    for i in range(len(node_arr)-1,-1,-1):
        print(node_arr[i].data)
        if l%2==0:
            if node_arr[i].left:
                new_iter.append(node_arr[i].left)
            if node_arr[i].right:
                new_iter.append(node_arr[i].right)
        else:
            if node_arr[i].right:
                new_iter.append(node_arr[i].right)
            if node_arr[i].left:
                new_iter.append(node_arr[i].left)
    q.append([new_iter,l+1])
# inorder(root)