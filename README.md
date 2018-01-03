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

## Basic Operations on the linkled list

- Add value to Head/Tail
- Add value at specific index
- Remove value
- Find value
- Create list from Linked List
- Reverse the Linked List

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
- Depth-First Search graph algorithms can be implemented with stack (or rercursion).
- Finding Euler-Cycles in a graph.
- Balancing symbols.

## Queue

A Queue is a data structure used for storing data similar to Stack.

The first element to be inserted is the first one Lo be deleted. First in First
out (FIFO).

Linked List implementation of a Queue.

### Basic Operations on the Queue

- EnQueue operation is implemented by inserting an element at the end of the list.

- DeQueue operation is implemented by deleting an element from the beginning of the list.

### Applications

- IO Buffers.
- CPU scheduling.
