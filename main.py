# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 15:18:23 2023

@author: Jorge Roa & Carmen Garro
"""

from mlbt import MutableLinkedBinaryTree

lbt = MutableLinkedBinaryTree()

print(len(lbt))
print(lbt.root())

lbt.add_root(1)
lbt.add_left(lbt.root(), 2)
lbt.add_right(lbt.root(), 3)

l = lbt.left(lbt.root())
r = lbt.right(lbt.root())

lbt.add_left(l, 4)
lbt.add_right(l, 5)

lbt.add_left(r, 6)
lbt.add_right(r, 7)

print(len(lbt))
print(lbt.height(lbt.root()))

#evaluate all the functions:

print("##Preorder##")
#Should be: 1,2,4,5,3,6,7
for p in lbt.preorder(0):
    print(p.element())

print("##Postorder##")
#Should be: 4,5,2,6,7,3,1
for p in lbt.postorder():
    print(p.element())

print("##Inorder##")
#Should be: 4,2,5,1,6,3,7
for p in lbt.inorder():
    print(p.element())