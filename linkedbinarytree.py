# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 15:15:46 2023

@author: Jorge Roa & Carmen Garro
"""

from binarytree import BinaryTree

class LinkedBinaryTree(BinaryTree):
    """Linked representation of a binary tree structure."""


    class _Node:
        __slots__ = '_element', '_parent', '_left', '_right'

        def __init__(self, element, parent=None, left=None, right=None):
            self._element = element
            self._parent = parent
            self._left = left
            self._right = right


    class Position(BinaryTree.Position):
        """An abstraction representing the location of a single element."""

        def __init__(self, container, node):
            """Constructor should not be invoked by user."""
            self._container = container
            self._node = node

        def element(self):
            return self._node._element


        def __eq__(self, other):
            return type(other) is type(self) and other._node is self._node

    def _validate(self, p):
        """Return associated node, if position is valid."""
        if not isinstance(p, self.Position):
            raise TypeError('p must be proper Position type')

        if p._container is not self:
            raise ValueError('p does not belong to this container')

        if p._node._parent is p._node:
            raise ValueError('p is no longer valid')
            return p._node
        return p._node

    def _make_position(self, node):
        """Return Position instance for given node (or None if no node)."""
        return self.Position(self, node) if node is not None else None


    def __init__(self):
        """Create an intially empty binary tree."""
        self._root = None
        self._size = 0
        self._positions = []


    def __len__(self):
        """Return the total number of elements in the tree."""
        return self._size

    def root(self):
        """Return the root Position of the tree (or None if tree is empty)."""
        return self._make_position(self._root)

    @property
    def positions(self):
        return self._positions

    def parent(self, p):
        """Return the Position of p's parent(or None if p is root)."""
        node = self._validate(p)
        return self._make_position(node._parent)


    def left(self, p):
        """Return the Position of p's left child(or None if no left child)."""
        node = self._validate(p)
        return self._make_position(node._left)

    def right(self, p):
        """Return the Position of p's left child(or NOne if no left child)."""
        node = self._validate(p)
        return self._make_position(node._right)

    def num_children(self, p):
        """Return the number of children of Position p."""
        node = self._validate(p)
        count = 0
        if node._left is not None:
            count += 1
        if node._right is not None:
            count += 1
        return count

    def _add_root(self, e):
        """Place element e at the root of an empty tree and return new Position.

        Raise ValueError if tree nonempty.
        """

        if self._root is not None: raise ValueError('Root exists')
        self._size = 1
        self._root = self._Node(e)
        pos = self._make_position(self._root)
        self._positions.append(pos)
        return pos

    def _add_left(self, p, e):
        """Create a new left child for Position p, storing element e.

        Return the Position of new node
        Raise ValueError if Position p is invalidor p already has a left child.
        """

        node = self._validate(p)
        if node._right is not None: raise ValueError('Left child exists')
        self._size += 1
        node._left = self._Node(e, node)
        pos = self._make_position(node._left)
        self._positions.append(pos)
        return pos

    def _add_right(self, p, e):
        """Create a new right child for Position p, storing element e.

        Return the Position of new node
        Raise ValueError if Position p is invalid or p already has a right child.
        """

        node = self._validate(p)
        if node._right is not None: raise ValueError('Right child exists')
        self._size += 1
        node._right = self._Node(e, node)
        pos = self._make_position(node._right)
        self._positions.append(pos)
        return pos


    def _replace(self, p, e):
        """Replace the element at position p with e, and return old element."""
        node = self._validate(p)
        old = node._element
        node._element = e
        return old

    def _delete(self, p):
        """Delete the node at Position p, and replace it with its child, if any..git/

        Return the element that had been stored at Position p
        Raise ValueError if Position p is invalid or p has two children.
        """

        node = self._validate(p)
        if self.num_children(p) == 2: raise ValueError('p has two children')
        child = node._left if node._left else node._right
        if child is not None:
            child._parent = node._parent
        if node is self._root:
            self._root = child
        else:
            parent = node._parent
            if node is parent._left:
                parent._left = child
            else:
                parent._right = child

        self._positions.remove(p)
        self._size -= 1
        node._parent = node
        return node._element

    def _attach(self, p, t1, t2):
        """Attach trees t1 and t2 as left and right subtrees of external p."""
        node = self._validate(p)
        if not self.is_leaf(p): raise ValueError('position must be leaf')
        if not type(self) is type(t1) is type(t2):
            raise TypeError('Tree types must match')
        self._size += len(t1) + len(t2)
        if not t1.is_empty():
            t1._root._parent = node
            node._left = t1._root
            t1._root = None
            t1._size = 0
        if not t2.is_empty():
            t2._root._parent = node
            node._right = t2.root
            t2._root = None
            t2._size = 0

    #### 1: function of preorder
    """Generate a preorder traversal of positions in the tree"""
    def preorder(self):
        if not self.is_empty():
            for p in self._subtree_preorder(self.root()):
                yield p

    """Generate a preorder traversal of positions in the subtree rooted at p"""
    def _subtree_preorder(self, p):
        yield p #visit the parent
        for c in self.children(p): #visit children
            for other in self._subtree_preorder(c):
                yield other

    #### 2: function of postorder
    """Generate a postorder traversal of positions in the tree"""
    def postorder(self):
        if not self.is_empty():
            for p in self._subtree_postorder(self.root()):
                yield p

    """Generate a postorder traversal of positions in the subtree rooted at p"""
    def _subtree_postorder(self, p):
        for c in self.children(p):
            for other in self._subtree_postorder(c):
                yield other
        yield p

    #### 3: function of inorder
    """Generate an inorder traversal of positions in the tree"""
    def inorder(self):
        if not self.is_empty():
            for p in self._subtree_inorder(self.root()):
                yield p

    """Generate an inorder traversal of positions in the subtree rooted at p"""
    def _subtree_inorder(self, p):
        if self.left(p) is not None: #visit subtree if it exists
            for other in self._subtree_inorder(self.left(p)):
                yield other
        yield p #print the parent
        if self.right(p) is not None: #visit right subtree, if it exists
            for other in self._subtree_inorder(self.right(p)):
                yield other



