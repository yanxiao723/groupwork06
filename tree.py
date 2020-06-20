_l# -*- coding: utf-8 -*-
"""
Created on Sun Jun 14 19:31:44 2020

@author: yan
"""
class Node(object):
    def __init__(self, item):
        self.item = item  # 表示对应的元素
        self.left = None  # 表示左子节点
        self.right = None  # 表示右子节点

    def __str__(self):
        # print 一个 Node 类时会打印 __str__ 的返回值
        return str(self.item)


class Tree(object):
    def __init__(self):
        # 根节点定义为 root 永不删除，作为哨兵使用。
        self.root = Node('root')

    def add(self, item):
        node = Node(item)
        # 如果二叉树为空，那么添加的点将插入 root 节点处
        if self.root is None:
            self.root = node
        else:
            # 在 q 列表中，添加二叉树的根节点
            q = [self.root]
            while True:
                pop_node = q.pop(0)
                # 左子树为空则将点添加到左子树
                if pop_node.left is None:
                    pop_node.left = node
                    return
                # 右子树为空则将点添加到右子树
                elif pop_node.right is None:
                    pop_node.right = node
                    return
                else:
                    q.append(pop_node.left)
                    q.append(pop_node.right)

    def get_parent(self, item):
        if self.root.item == item:
            # 根节点没有父节点
            return None
        # 在 tmp 列表中，添加二叉树的根节点
        tmp = [self.root]
        while tmp:
            pop_node = tmp.pop(0)
            # 如果点的左子树为要寻找的点
            if pop_node.left and pop_node.left.item == item:
                # 返回这个点，即为寻找点的父节点
                return pop_node
            # 如果点的右子树为要寻找的点
            if pop_node.right and pop_node.right.item == item:
                # 返回这个点，即为寻找点的父节点
                return pop_node
            # 添加 tmp 列表里的元素
            if pop_node.left is not None:
                tmp.append(pop_node.left)
            if pop_node.right is not None:
                tmp.append(pop_node.right)
        return None

    def delete(self, item):
        # 如果根为空，就什么也不做
        if self.root is None:
            return False

        parent = self.get_parent(item)
        if parent:
            # 确定待删除节点
            del_node = parent.left if parent.left.item == item else parent.right
            # 待删除节点的左子树为空时
            if del_node.left is None:
                # 如果待删除节点是父节点的左孩子
                if parent.left.item == item:
                    parent.left = del_node.right
                # 如果待删除节点是父节点的右孩子
                else:
                    parent.right = del_node.right
                # 删除变量 del_node
                del del_node
                return True
            # 待删除节点的右子树为空时
            elif del_node.right is None:
                # 如果待删除节点是父节点的左孩子
                if parent.left.item == item:
                    parent.left = del_node.left
                # 如果待删除节点是父节点的右孩子
                else:
                    parent.right = del_node.left
                # 删除变量 del_node
                del del_node
                return True
            else:  # 左右子树都不为空
                tmp_pre = del_node
                # 待删除节点的右子树
                tmp_next = del_node.right

                # 寻找待删除节点右子树中的最左叶子节点并完成替代
                if tmp_next.left is None:
                    # 替代
                    tmp_pre.right = tmp_next.right
                    tmp_next.left = del_node.left
                    tmp_next.right = del_node.right
                else:
                    # 让 tmp_next 指向右子树的最左叶子节点
                    while tmp_next.left:
                        tmp_pre = tmp_next
                        tmp_next = tmp_next.left
                    # 替代
                    tmp_pre.left = tmp_next.right
                    tmp_next.left = del_node.left
                    tmp_next.right = del_node.right
                # 如果待删除节点是父节点的左孩子
                if parent.left.item == item:
                    parent.left = tmp_next
                # 如果待删除节点是父节点的右孩子
                else:
                    parent.right = tmp_next
                del del_node
                return True
        else:
            return False
    def inorder(self,node):#递归中序
        if node is None:
            return []
        #print(node.item)
        result =[node.item]
        left = self.inorder(node.left)
        right = self.inorder(node.right)
        return left+result+right
    def ahead(self,node):#递归先序
        if node is None:
            return []
        result =[node.item]
        left = self.ahead(node.left)
        right = self.ahead(node.right)
        return result+left+right
    def after(self,node):#递归后序
        if node is None:
            return []
        result =[node.item]
        left = self.after(node.left)
        right = self.after(node.right)
        return left+right+result
#    def inorder_1(self,node):
#        if node is None:
#            return []
#        re =[]
#        
#        cur =node
#        if cur.left is None and cur.right is None:
#            return cur.item
#        while cur.left  is not None and cur.right is not None:
#            print('begin')
#            print(cur.item)
#            print('----------------------')
#            while cur.left is not None and cur.left  not in re:
#                cur = cur.left
#            if  cur.item not in re:
#                re.append(cur.item)
#            if self.get_parent(cur.item).item not in re:
#                re.append(self.get_parent(cur.item).item)
#            cur = self.get_parent(cur.item)
#            while cur.right is not None:
#                cur = cur.right
#                break 
#            #print(cur.item)
#            if cur.left is None and cur.right is None:
#                re.append(cur.item)
#                cur = self.get_parent(cur.item)
#                #print(cur.item)
#                while cur.item in re:
#                    
#                    cur = self.get_parent(cur.item)
#                    #print('---------')
#                    #print(cur.item)
#                #print(cur.item)
#                re.append(cur.left.item)
#        return re
    def ahead_1(self,node): # 先序
        stack = []
        result =[]
        while stack or node:
            while node:
                result.append(node.item)
                stack.append(node)
                node = node.left
            node= stack.pop()
            node= node.right
            #print('---------')
        return  result
    def inorder_1(self,node): # 中序
        stack = []
        result =[]
        while stack or node:
            while node:
                
                stack.append(node)
                node = node.left
            node= stack.pop()
            result.append(node.item)
            node= node.right
            #print('---------')
        return  result
    def after_1(self,node):
        stack=[]
        result =[]
        while stack or node:
            while node:
                stack.append(node)
                node= node.left if node.left else node.right
            node = stack.pop()
            result.append(node.item)
            if stack and stack[-1].left == node :
                node = stack[-1].right
            else:
                node = None
        return result
                

                
            
            
            
            
            
            
            
            
#        elif cur.right is None :
#            cur = node
#            
#            while cur.left is not None:
#                cur = cur.left
#            result.append(cur.item)
#            result.append(self.get_parent(cur.item))
#            cur = self.get_parent(cur.item).right
#            while cur 
#                
#            
#        elif cur.left is None:
#        
#            
#            
#        else:
#            
#            
#        
#        
#        
#        while cur_next is not None:
#            cur_next =cur_next.left
#        result.append(cur.item)
#        cur = self.get_parent(cur.item)
#        result.append(cur)
#        while 
#            
#    
        
        
        
        
        
        
        
        
        
a = Tree()       
for i in range(1,11):
    a.add(i)
#m= a.preorder(a.root)
#m
    
print('先序')
print(a.ahead(a.root),a.ahead_1(a.root))
print('中序')
print(a.inorder(a.root),a.inorder_1(a.root))
print('后序')
print(a.after(a.root),a.after_1(a.root))

    
            
        
        
        
        
        
