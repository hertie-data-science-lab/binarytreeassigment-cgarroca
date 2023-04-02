# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 15:13:42 2023

@author: Hannah
"""

from abc import ABC, abstractmethod

class Tree(ABC):
    """Abstract base class representing a tree structure."""
    
    class Position(ABC):
        """An abstraction representing the location of a single element."""
        
        @abstractmethod
        def element(self):
            """Return the element stored at this Position."""
            pass
        
        @abstractmethod
        def __eq__(self, other):
            """Return True if other Position represents the same location."""
            pass
        
        def __ne__(self, other):
            """Return True if other does not represent the same location."""
            return not (self == other)

    @abstractmethod
    def root(self):
        """Return Position representing the tree's root (or None if empty)."""
        pass
    
    @abstractmethod
    def parent(self, p):
        """Return Position representing p's parent (or None if p is root)."""
        pass
    
    @abstractmethod
    def num_children(self, p):
        """Return the number of children that Position p has."""
        pass
    
    @abstractmethod
    def children(self, p):
        """Generate an iteration of Positions representing p's children."""
        pass
    
    @abstractmethod
    def __len__(self):
        """Return the total number of elements in the tree."""
        pass
    
    def is_root(self, p):
        """Return True if Position p represents the root of the tree."""
        return self.root() == p
    
    def is_leaf(self, p):
        """Return True if Position p does not have any children."""
        return self.num_children(p) == 0
    
    def is_empty(self):
        """Return True if the tree is empty."""
        return len(self) == 0
    
    def depth(self, p):
        if self.is_root(p):
            return 0
        else:
            return 1 + self.depth(self.parent(p))
    
    def _height1(self):
        return max(self.depth(p) for p in self.positions if self.is_leaf(p))
        
    def _height2(self, p):
        if self.is_leaf(p):
            return 0
        else:
            return 1 + max(self._height2(c) for c in self.children(p))
    
    def height(self, p=None):
        if p is None:
            p = self.root()
        return self._height2(p)