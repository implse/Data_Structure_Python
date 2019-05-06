# Data Structure in Python

## Abstract Data Types (ADTs)

Abstract data types are a theoretical computer science concept. They simply describe what kind of data a data structure can hold and what operations are allowed on the data.

## Data Structures (DS)

Concrete implementation of Abstract Data Types ADTs that organize data stored in memory. For every operation that is allowed on an abstract data type we have one method or one function that is defined by the data structure's class.

- One Abstract data types operation  = One function in Data Structure.


## Linked List

<p align="center">
  <img width="480" height="180" src="images\LinkedList_480_180.png">
</p>

A Linked List is a data structure used for storing collections of data. Each element of a linked list is called an node.

Linked Lists typically contain unidirectional links (next node), but some implementations make use of bidirectional links (next and previous nodes).

- Not contiguous piece of memory.
- Differing size storage space at each index.
- Dynamic - New piece of memory allocated for each node.

Linked Lists are sequential-access data structure.

### Nodes

Nodes are the fundamental building block of many computer science data structures. They form the basis for linked lists, stacks, queues, trees, and more.

An individual node contains data and links to other nodes. Each data structure adds additional constraints or behavior to these features to create the desired structure.

- Contain data, which can be a variety of data types
- Contain links to other nodes. If a node has no links, or they are all null/None, or you have reached the end of the path you were following.
- Can be orphaned if there are no existing links to them.

### Time Complexity

|Operation                   |Big O    |
|----------------------------|---------|
|Indexing                    |O(n)     |
|Insert/Delete at beginning  |O(1)     |
|Insert/Delete at ending     |O(1)/O(n)|
|Insertion/Deletion in middle|O(n)     |
|Access Time                 |O(n)     |

* Insert/Delete at ending : depend on the implementation. Tail reference.

### Basic Operations on Linked List

- Add value to Head/Tail
- Add value at specific index
- Remove value
- Find value
- Create list from Linked List
- Reverse the Linked List

### Linked List vs Array

### Advantages

- You need Insertion / Deletion in the list to be extremely fast.
- You Insert / Delete items in the middle of the list.
- You can’t evaluate the size of the list, it needs to grow
or shrink throughout the execution.

### Disadvantages

- You frequently need random, unordered access to the data.
- You need extreme performance to access the items.
- The number of items doesn't change during execution, so you can easily allocate contiguous space of computer memory.

## Stack

<p align="center">
  <img width="480" height="360" src="images\Stack_180_360.png">
</p>

A stack is a simple data structure used for storing data.

The last element inserted is the first one to be deleted. Last in, First out (LIFO).


|Operation                   |Big O  |
|----------------------------|-------|
|Push value                  |O(1)   |
|Pop value                   |O(1)   |



### Basic Operations on Stack

- Push and Pop operations.

### Applications

- Stack Memory.
- Implementing function calls (memory stack, recursion)
- Depth-First Search algorithms can be implemented with stack (or recursion).
- Finding Euler-Cycles in a graph.
- Balancing symbols.

## Queue

<p align="center">
  <img width="480" height="180" src="images\Queue_480_180.png">
</p>

A Queue is a data structure used for storing data similar to Stack.

The first element to be inserted is the first one to be deleted. First in First
out (FIFO).

Linked List implementation of a Queue.

|Operation                   |Big O  |
|----------------------------|-------|
|Search                      |O(n)   |
|Insert                      |O(1)   |
|Delete                      |O(1)   |

### Basic Operations on Queue

- EnQueue operation is implemented by inserting an element at the end of the list.

- DeQueue operation is implemented by deleting an element from the beginning of the list.

### Applications

- IO Buffers.
- CPU scheduling.

## Tree

<p align="center">
  <img width="480" height="360" src="images\Tree_480_360.png">
</p>

A Tree structure is a way of representing the hierarchical nature of a structure in a graphical form.

Tree is an example of non-linear data structure.


### Glossary

__Root:__ Top most node.

__Edge__ : Refer to the link from parent to child.

__Siblings:__ Children of the same parent.

__Leaf:__ A node with no children.

__Height (Tree):__ The height of a tree is the length of the path from the root to the deepest node in the tree.

__Height (Node):__ The height of a node is the length of the path from that node to the deepest node. Or is the number of layers it contains.

__Level:__ Number of edges between the node and the root + 1.

__Depth:__ Number of edges between the node and the root.

__Size:__ Number of nodes in the tree.


## Binary Tree

Binary Tree is a specialized form of tree with two child (left child and right child). It is simply a representation of data in Tree structure.

Strict Binary Tree : each node has exactly two children or no children.

Full Binary Tree : each node has exactly two children and are all leaf nodes.

The number of nodes n in a full binary tree is (2^h + 1) - 1.

Since, there are h levels we need to add all nodes at each level [ 2^0 + 2^1 + 2^2 + ... + 2^h = (2^h + 1) - 1].

## Binary Search Tree

Always sorted by implementation.

Binary Search Tree (BST or Ordered Binary Tree) is a special type of Binary Tree that follows these conditions:

- Left child node is smaller than its Parent node.
- Right child node is greater than its Parent Node.


No duplicate Keys.

### Advantages

- Fast search, insertion, deletion especially when balanced.

- Sort as you go instead of all at once.

- Simple implementation for good performance.

### Basic Operations on Binary Tree

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



If the Tree become unbalanced then the operations running times can be reduced to O(n).(worst case)


### Binary Search Tree Traversals


### Depth First Search Traversal

- 2 methods for DFS recursive or iterative.
- Iterative method use a stack (LIFO).
- Recursive method use stack memory.


- __InOrder:__ visit the Left SubTree then the Root then the Right SubTree recursively.
- __PreOrder:__ visit the Root then Left SubTree then the Right SubTree recursively.
- __PostOrder:__ visit the Left SubTree then the right Sub Tree and the Root recursively.


### Breadth First Search Traversal

- BFS use priority queue.
- Level Order Traversal.


### Delete a Node in a Binary Search Tree

Complexity : We have to find the Node then we delete it or set it to None.
O(log n) find operation + O(1) deletion = O(log n)

#### 3 Cases:
- No children.
- One Child.
- Two children.

#### Method for Two Children case:

Two possible options: We look for the largest Node in the left subtree (Predecessor) or the smallest Node int the right subtree (Successor).

- Start at the Root, find the node to delete.
- Find Predecessor or Successor
- Replace Node to delete value with Predecessor value.
- Delete predecessor.


## Binary Heap

A Binary Heap is a specialized Binary Search Tree data structure that satisfies the heap property.

A Binary Heap is define as a Binary Tree with two additional properties.

### Heap property

- A Binary Heap is a complete Binary Tree. Every level except possibly the last is completely filled.

### Heap ordering property

- Min heap : Each node is greater than or equal to its parent. min value is root.
- Max heap : Each node is less than or equal to its parent. max value is root.

Heaps are not sorted, considered "partially ordered".

### Priority Queues

- Almost always implement with a heap.
- Element with smaller numbers are higher priority.
- Element are inserted in O(log n) time.
- Ordering happens with each insertion, so the cost of ordering is distributed across insertion instead of in one big chunk.

#### Applications

Prioritizing data packets in routers.
Tracking unexplored routes in path-finding algorithms.
Bayesian spam filtering.
Data compression.
OS load Balancing, interrupt handling.

Height = log(n + 1) - 1
ex : if a Tree has 15 node : log(15 + 1) - 1 = 4 - 1 = 3

#### Array representation

Place values into array following level-order traversal.

- Left child index : 2n + 1
- Right child index : 2n + 2
- Parent index : (n - 1) / 2

Array implementation use less memory.(no node class require)
Can sort an array in-place.(Heapsort)

Insert element :
- Insert at next available space.
- Shift up or bubble up.
- Swap with parent until fulfills the ordering property.(trickle up) Fix heap violation.

Remove element :

- Replace root with last element.
- Shift down (aka sink).
- Swap with smallest child(min) or largest child(max) until fulfills the ordering property.

Other methods

- peek : find-min or find-max.
- size : return the numbers of elements

## Building the Heap

- first we insert the data to the heap and we check wether the heap properties are met.
- if the heap properties are violated, we reconstruct the heap in order to make it a valid heap.(heapify process)

- it is O(n) process to construct a heap.
- if heap properties are violated it takes O(log n) to heapify.
- inserting an item to the heap is just adding the data to the array with incremented index.

### Add value to the Heap

  - Insert at next available space.
  - Trickle up or fixUp.

### Remove value from a Heap

  - Remove the root.
  - Replace with the last element.
  - Trickle down or fixDown.


## Heapify

Create a heap out of given array of elements.

Input: an array usually unsorted, unordered.
Output: an array that satisfies the heap property.

Balancing a heap is done by sift-up or sift-down operations (swapping elements which are out of order)

## Heapsort

Heap sort algorithm is a sorting technique that is based exclusively upon a binary heap data structure. It involves finding the largest (maximum) element, and sorting it at the end of an unsorted collection.

Python has a heapq module that implements a priority queue using a binary heap.

Time Complexity: O(n log n)
Space Complexity: O(n)

## AVL Tree

An AVL Tree is a self balancing Binary Search Tree. It is named after Adalson-Velskii and Landis.(1962)

This type of tree will adjust itself in order to maintain a low (logarithmic) height allowing for faster operations such as insertions and deletions.

AVL Tree Time Complexity:

|Operation                   |Average  |  Worst  |
|----------------------------|---------|---------
|Search                      |O(log n) |O(log n) |
|Insert                      |O(log n) |O(log n) |
|Delete                      |O(log n) |O(log n) |
|Remove                      |O(log n) |O(log n) |

For every node, height of the left and right children differ by at most +-1.

Balance Factor(Node) = Height(RightSubTree) - Height(LeftSubTree)

Each node store its height.

Height of a node: length of the longest path from it to a leaf.

The running time of BST operations depends on the height of the binary search tree. The tree should be balanced in order to get the best performance.

### Tree Rotations

The secret ingredient to most AVL Tree (Balanced Binary Search Tree) algorithms is the clever usage of a tree invariant and tree rotations.

A tree invariant is a property or rule you impose on your tree that it must meet after every operation. To ensure that the invariant is always satisfied a series of tree rotations are normally applied.

#### InOrder invariance

The tree rotation renders the inorder traversal of the binary tree invariant. This implies the order of the elements are not affected when a rotation is performed in any part of the tree.

## Graph

Graphs are mathematical structures that represent pairwise relationships between objects. A graph is an abstract data structure that represents the relationship between various objects.

A Graph is a pair V, E, where V is a set of Nodes called Vertices, and E is a collection of connections between vertices called Edges or Links.

Definition:

  - G = (V, E)

  V is a set of Vertices or Nodes.(number of Vertices)
  E is a set of Edges or Links.(number of connections)



There are tree types of graphs: Directed, Undirected and Weighted.

#### Vocabulary

__Edges:__ Represent the connection between two vertices.

__Vertices:__ Nodes in the graph.

__Path:__ A sequence of connected vertices.

__Cycles:__ A path that is cyclical.


### Applications

- Shortest Path Algorithm (GPS, High Frequency Trading).
- Graphs traversing: web crawlers.
- Spanning Trees: network protocol.
- Transportation network: Highway and Flight network.
- Graph theory is used for the study of algorithms :
    - Dijkstra's Algorithm
    - Prim's Algorithm
    - Kruskal's Algorithm

### Type of Graph

#### Undirected Graph
An undirected graph is a graph in which all the edges are bi-directional i.e. the edges do not point in any specific direction.

#### Directed Graph
A directed graph is a graph in which all the edges are uni-directional i.e. the edges point in a single direction.

#### Weighted Graph
In a weighted graph, each edge is assigned a weight or cost. This value is used to represent a certain quantifiable relationship between the nodes they connect.

For example, weights could represent distance, time, the number of connections shared between two users in a social network.

These weights are used by Dijkstra’s Algorithm to optimize routes by finding the shortest or least expensive paths between nodes in a network.

### Graph representation

There are three common way to represent graph:
  - Adjacency Matrix.
  - Adjacency List.
  - Edge List.

### Adjacency Matrix

An adjacency matrix is a VxV binary matrix.

A binary matrix is a matrix in which the cells can have only one of two possible values. 0 or 1.(Undirected Graph)

For Directed Graph we use tree possible values. 0, 1 or -1.

Adjacency matrix provides constant time access O(1) to determine if there is an edge between two nodes.

Space complexity of the adjacency matrix is O(V**2).

__Pro:__ Faster for dense Graph. Simpler for Weighted Graph.

__Con:__ Uses more space.

### Adjacency List

An adjacency list is an array of separate lists. Each element of the array is a list, which contains all the vertices that are adjacent to vertex i.

The space complexity of adjacency list is O(V + E) because in an adjacency list information is stored only for those edges that actually exist in the graph. In a lot of cases, where a matrix is sparse using an adjacency matrix may not be very useful. This is because using an adjacency matrix will take up a lot of space where most of the elements will be 0, anyway. In such cases, using an adjacency list is better.

Pro : Faster and uses less space for Sparse graph.

Con : Slower for dense graph.

### Basic Operations on Graph

- Adding an edge.
- Deleting an edge.
- Detecting an edge.
- Finding neighbors of a vertex.
- Finding a path between two vertices.

### Graph Traversals

#### Breadth First Search

- Internally this Algorithm uses a Queue.

We visit every vertex exactly once.
We visit the neighbors the the neighbors of these new vertices and so on.

Time complexity : O(V + E)
Memory complexity is not good. We have to store a lot of references. O(N)

#### Depth First Search

- Internally this Algorithm uses a Stack.

It explores as far as possible along each branch before backtracking.

Time complexity : O(V + E)

Memory complexity is a bit better than BFS. O(log N)


##### Applications

- Kosaraju Algorithm.
- Detecting cycle. Checking whether a graph is a DAG (Directed Acyclic Graph)or not.
- Generating mazes or finding way out of the maze.

DAG : Directed Acyclic Graph is a finite directed graph with no directed cycles.


## Shortest Path Algorithm

- Finding a path between two vertices in a graph such that the sum of the weights of its edges is minimized.

- Dijkstra algorithm
- Floyd Warshall algorithm
- A* Search

## Dijkstra algorithm

- It was constructed by computer scientist Edsger Dijkstra in 1956.
- This is the fastest know single source shortest path algorithm for arbitrary directed graphs with unbounded non-negative weights.

- It uses greedy method: Always pick the next closest vertex to the source.
- It uses priority queue lo store unvisited vertices by distance from s.
- It does not work with negative weights.

#### Difference between Unweighted Shortest Path and Dijkstra's Algorithm

- To represent weights in the adjacency list, each vertex contains the weights of the edges (in addition to their identifier).

- Instead of ordinary queue we use priority queue (distances are the priorities) and the vertex with the smallest distance is selected for processing.

- The distance to a vertex is calculated by the sum of the weights of the edges on the path from the source to that vertex.

- We update the distances in case the newly computed distance is smaller than the old distance which we have already computed.

Time Complexity : O(V * Log(V) + E)

__Pseudo code__

1 - Find the cheapest unvisited node reachable.

2 - Mark it as visited and keep track on which nodes you can visit from it.

3 - Repeat.

Dijkstra algorithm find the fastest path.

Breadth-first search find the path with the fewest segments.
