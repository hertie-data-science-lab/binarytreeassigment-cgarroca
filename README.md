[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-8d59dc4de5201274e310e4c54b9627a8934c3b88527886e3b421487c677d23eb.svg)](https://classroom.github.com/a/f4MOD0El)
# BinaryTree

Clone the Github template and add the four traversal methods to the LinkedBinaryTree.
All 4 traversal methods should be public and accessible through the Main file.

```preorder()```: A method to preorder traverse the binary tree

```
Algorithm preorder(T, p):
  perform the "visit" action for position p
  for each child c in T.children(p) do
    preorder(T, c)
```


```postorder()```: A method to postorder traverse the binary tree
```
Algorithm postorder(T, p):
  for each child c in T.children(p) do
    postorder(T, c)
perform the "visit" action for position p
```

```inorder()```: A method to inorder traverse the tree

```
Algorithm inorder(p):
  if p has a left child lc then
    inorder(lc)
perform the "visit" action for position p
if p has a right child rc then
  inorder(rc)
```

Finally, edit the Main.py file to test all these methods on the existing tree.
