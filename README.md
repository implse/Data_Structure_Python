# Data Structure in Python

## Linked List
A linked List is a data structure used for storing collections of data.

- Not contiguous piece of memory.
- Differing size storage space at each index.
- Dynamic - New piece of memory allocated for each node.

|Operation                   |Big O  |
|----------------------------|-------|
|Indexing                    |O(n)   |
|Insert/Delete at beginning  |O(1)   |
|Insert/Delete at ending     |O(1)   |
|Insertion/Deletion in middle|O(n)   |
|Access Time                 |O(n)   |

## Basic Operations on the Linked List

- Add value to Head/Tail
- Add value at specific index
- Remove value
- Find value
- Create list from Linked List
- Reverse the Linked List

## Linked List vs Array

Linked List are preferable when :
- You need Insertion / Deletion in the list to be extremly fast.
- You Insert / Delete items in the middle of the list.
- You can’t evaluate the size of the list, it needs to grow
or shrink throughout the execution.

## Stack
A stack is a simple data structure used for storing data.

The last element inserted is the first one to be deleted. Last in, First out (LIFO).


Linked List implementation of a Stack.


|Operation                   |Big O  |
|----------------------------|-------|
|Push value                  |O(1)   |
|Pop value                   |O(1)   |
|Size                        |O(1)   |


### Basic Operations on the Stack

- Push and Pop operations.

### Applications

- Most important application of stack is : Stack Memory.
- Implementing function calls including recursion.
- Depth-First Search graph algorithms can be implemented with stack (or recursion).
- Finding Euler-Cycles in a graph.
- Balancing symbols.

## Queue

A Queue is a data structure used for storing data similar to Stack.

The first element to be inserted is the first one Lo be deleted. First in First
out (FIFO).

Linked List implementation of a Queue.

|Operation                   |Big O  |
|----------------------------|-------|
|Search                      |O(n)   |
|Insert                      |O(1)   |
|Delete                      |O(1)   |

### Basic Operations on the Queue

- EnQueue operation is implemented by inserting an element at the end of the list.

- DeQueue operation is implemented by deleting an element from the beginning of the list.

### Applications

- IO Buffers.
- CPU scheduling.

## Tree

A Tree structure is a way of representing the hierarchical nature of a structure in a graphical form.

Tree is an example of non-linear data structure.


### Glossary

__Root__ : top most node.

__Edge__ : refer to the link from parent to child.

__Siblings__ : Children of the same parent.

__Leaf__ : A node with no children.

__Height(Tree)__ : The height of a tree is the length of the path from the root to the deepest node in the tree.

__Height(Node)__ : The height of a node is the length of the path from that node to the deepest node. Or is the number of layers it contains.

__Level__ : Number of edges between the node and the root + 1.

__Depth__ : Number of edges between the node and the root.

__Size__ : Number of nodes in the tree.


### Binary Tree

__Binary Tree__ is a specialized form of tree with two child (left child and right Child). It is simply a representation of data in Tree structure


Strict Binary Tree : each node has exactly two children or no children.

Full Binary Tree : each node has exactly two children and all leaf nodes.

### Binary Search Tree

Always sorted by implementation.

__Binary Search Tree (BST or Ordered Binary Tree)__ is a special type of Binary Tree that follows following condition:

- left child node is smaller than its parent Node.
- right child node is greater than its parent Node.


No duplicate Keys.

__Advantages__ :

- Fast search, insertion, deletion especially when balanced.

- Sort as you go instead of all at once.

- Simple implementation for good performance.

### Basic Operations on the Binary Tree

- Inserting an element into a Tree.
- Deleting an element from a Tree.
- Searching for an element.
- Traversing the Tree.
- Find minimum and maximum value in the Tree.
- Finding the size of the Tree.
- Finding the height of the Tree.

|Operation                   |Big O    |
|----------------------------|---------|
|Search                      |O(log n) |
|Insert                      |O(log n) |
|Delete                      |O(log n) |

Worst case scenarios :

If the Tree become unbalanced then the operations running times can be reduced to O(n).


### Binary Tree Traversals:


3 main Tree Traversal Method :

- InOrder : visit the Left SubTree then the Root the the Right SubTree recursively.
- PreOrder : visit the Root then Left SubTree then the Right SubTree recursively.
- PostOrder : visit the Left SubTree then the right Sub Tree and the Root recursively.

Depth First Search Traversal :
- InOrder
- PreOrder
- PostOrder

Bread First Search Traversal :
- Level Order
