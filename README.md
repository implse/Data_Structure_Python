# Data Structure in Python

A data structure is a specific way of organizing and storing data in a computer's memory to enable efficient access, modification, and manipulation of that data. Data structures can be thought of as containers for data elements, each with its own set of operations for performing tasks like insertion, deletion, retrieval, and traversal. Examples of data structures include arrays, linked lists, trees, and hash tables.

<p align="center">
  <img width="480" height="360" src="images\Data_Structure_480_360.png">
</p>

## Abstract Data Types (ADT)

An abstract data type (ADT) is a high-level description of a data structure that defines a set of operations that can be performed on the data and specifies their behavior. An ADT abstracts away the implementation details, focusing solely on what the data structure does, not how it does it. It provides a clear interface for interacting with the data, allowing programmers to use the data structure without needing to know its internal workings. Examples of ADTs include lists, stacks, queues, and dictionaries, which can have multiple concrete implementations.

- One Abstract data types operation  = One function in Data Structure.


## Linked List

<p align="center">
  <img width="480" height="360" src="images\Linked_List_480_360.png">
</p>

A `Linked list` is a data structure used for storing collections of `data`. Each element of a linked list is called an `node`.

`Linked List` typically contain an unidirectional links `next node`, but `doubly linked list` make use of bidirectional links (`next node` and `previous node`).

- New part of memory allocated for each node.
- Not contiguous piece of memory.
- Differing size storage space at each index.

Linked Lists are `sequential access` data structure.

### Nodes

`Nodes` are the fundamental building block of many computer science data structures. They form the basis for `linked lists`, `trees` and more.

An individual `node` contains `data` and links to the `next node`. Each data structure adds additional constraints or behavior to these features to create the desired structure.

- Contain data, which can be a variety of data types.
- Contain links to other `nodes`. If a `node` has no links then the `next node` is `None`.

The last `node` in a `linked list` points to `None`, and that tells you that it’s the end of the `linked list`.

### Time Complexity

|Operation                   |Big O    |
|----------------------------|---------|
|Indexing                    |`O(n)`   |
|Insert/Delete at beginning  |`O(1)`   |
|Insert/Delete at ending     |`O(1)/O(n)`|
|Insertion/Deletion in middle|`O(n)`   |
|Access Time                 |`O(n)`   |


### Basic Operations on Linked List

- Add value to Head/Tail
- Add or Update value at specific index
- Remove value
- Find value
- Create list from Linked List
- Reverse the Linked List

### Linked List vs Array

### Advantages

- Insertion / Deletion in the list is extremely fast.
- Insert / Delete items in the middle of the list.
- The size can grow or shrink throughout execution.

### Disadvantages

- Random, unordered access to the data.
- Access a specific index extremely fast.
- The number of items doesn't change during execution, so you can easily allocate contiguous space of computer memory.

## Stack

<p align="center">
  <img width="480" height="360" src="images\Stack_180_360.png">
</p>

A `stack` is a simple data structure used for storing `data`.

The `last` element inserted is the `first` one to be removed. `Last In, First Out` -  `LIFO`.

`Stacks` can be implemented using a `list` or `linked-list` as the underlying data structure.

### Stack Methods:

- `push` adds item to the top of the stack.
- `pop` return and removes item from the top of the stack.
- `peek` return item on the top of the stack without removing it.
- `is_empty` return `True` if the stack is empty.
- `get_length` return the number of items in the stack.


- Implemented using `list`, `Linked List` or `array`.
- Can have a limited size.
- `Stack` process item Last In, First Out.

### Time Complexity

|Operation                   |Big O  |
|----------------------------|-------|
|Push value                  |`O(1)` |
|Pop value                   |`O(1)` |
|Peek value                   |`O(1)` |


### Applications

- Stack Memory, implementing function calls (memory stack, recursion)
- Depth-First Search algorithms is implemented with stack or memory stack if using recursion.
- Finding Euler-Cycles in a graph.
- Balancing symbols and evaluating expressions.
- Backtracking algorithms.
- Browser back button stack.

## Queue

<p align="center">
  <img width="480" height="180" src="images\Queue_480_180.png">
</p>

A `queue` is a data structure used for storing `data` similar to `stack`.

The first element to be inserted is the first one to be removed. `First In, First
Out (FIFO)`.

`Queues` can be implemented using a `linked list` as the underlying data structure. The `front` of the `queue` is equivalent to the `head node` of a `linked list` and the `back` of the `queue` is equivalent to the `tail node`.

### Time Complexity

|Operation                   |Big O  |
|----------------------------|-------|
|Search                      |`O(n)` |
|Insert                      |`O(1)` |
|Delete                      |`O(1)` |

### Basic Operations on Queue

- `En-queue` - adds data to the `back` or end of the `queue`.

- `De-queue` - removes and return data from the `front` or beginning of the `queue`.

- `Peek` - return data from the `front` of the `queue` without removing it.

### Applications

- IO Buffers.
- CPU scheduling, order processing.
- Messaging


## Hash Table

<p align="center">
  <img width="480" height="360" src="images\Hash_Table_480_360.png">
</p>

`Hash Table` or `Hash Map` is a data structure that stores the `keys` and their associated `values` `(key, value pair)`.
`Hash Table` provide constant time, insertion, deletion, and lookup.

A `Hash Table` is basically made up of 2 different parts:
  - A `list` which is the actual container where the `data`.
  - A `Hash Function` or `Compression Function` uses to transform `input` data or `key` into `index`.

A good `Hash Function` should have the following characteristics:
  - Minimize Collisions.
  - Be easy and quick to compute.
  - Distribute `key` values evenly in the `hash table`.
  - Use all the information provided in the `key`.
  - Have a high load factor for a given set of `keys`.

Load Factor = Number of elements in the Hash Table / Hash Table size

`Hashing` is not a reversible process.



### Collisions

Collisions occur whenever a hash tables hashing function generates the same index for more than one key.

#### Separate Chaining

Separate Chaining is one of the most commonly used collision resolution technique. It is usually implemented using linked list.

A hash map that uses separate chaining with linked lists but experiences frequent collisions loses one of its most essential features.

With a good hash function chaining still averages out to have a search time of O(1), or constant lookup time.


#### Linear Probing (Open Addressing)

In open addressing we stick to the array as our underlying data structure, but we continue looking for a new index to save our data if the first result of our hash function has a different key’s data.

A common open method of open addressing is called probing. Probing means continuing to find new array indices in a fixed sequence until an empty index is found.

The issue with Linear Probing  is that the act of simply moving over the next available hash bucket and inserting an element at the next free space lead to something called clustering.

### Time Complexity

|Operation                   |Big O  |
|----------------------------|-------|
|Search                      |`O(1)` |
|Insert                      |`O(1)` |
|Delete                      |`O(1)` |


#### Applications

- Associative arrays
- Database indexing
- Caches
- Object representation
- Hash Functions are used in various algorithms to make their computing faster

## Tree

<p align="center">
  <img width="480" height="360" src="images\Tree_480_360.png">
</p>

A Tree structure is a way of representing the hierarchical nature of a structure in a graphical form.

Tree is an example of non-linear data structure.


### Glossary

`Root` : Top most node.

`Edge` : link between nodes. (parent to child).

`Siblings` : Children of the same parent.

`Leaf` : A node with no children.

`Height` (Tree) : The height of a tree is the length of the path from the root to the deepest node in the tree.

`Height` (Node) : The height of a node is the length of the path from that node to the deepest node. Or is the number of layers it contains.

`Level` : Number of edges between the node and the root + 1.

`Depth` : Number of edges between the node and the root.

`Size` : Number of nodes in the tree.


## Binary Tree

`Binary Tree` is a specialized form of `tree` with two child, `left child` and `right child`. It is simply a representation of data in `Tree structure`.

`Strict Binary Tree` : each `node` has exactly two children or no children.

`Full Binary Tree` : each `node` has exactly two children and are all leaf nodes.

The number of nodes `n` in a full binary tree is: `(2^h + 1) - 1`

Since, there are `h` levels we need to add all nodes at each level: `[ 2^0 + 2^1 + 2^2 + ... + 2^h = (2^h + 1) - 1]`

## Binary Search Tree


`Binary Search Tree` (BST or Ordered Binary Tree) is a special type of `Binary Tree` that follows these conditions:

- `Left child node` is smaller than its `Parent node`.
- `Right child node` is greater than its `Parent Node`.

Always sorted by implementation.

No duplicate Keys.

### Advantages

- Fast search, insertion, deletion especially when balanced.
- Sort as you go instead of all at once.
- Simple implementation for good performance.
- Only two traversals are enough to provide the elements in sorted order.

### Basic Operations on Binary Tree

- Inserting an element into a Tree.
- Deleting an element from a Tree.
- Searching for an element.
- Traversing the Tree.
- Find minimum and maximum value in the Tree.
- Finding the size of the Tree.
- Finding the height of the Tree.

|Operation                   |Big O     |
|----------------------------|----------|
|Search                      |`O(log n)`|
|Insert                      |`O(log n)`|
|Delete                      |`O(log n)`|



If the Tree become unbalanced then the operations running times can be reduced to `O(n)`.(worst case)

### Why is Binary Tree is so widely used?

Binary Tree is the most simplest and efficient data structure to be used in most Software Systems. It is the properties of Binary Tree that makes it so widely used.

There is a wide range of variants of Binary Tree which makes it very likely to find a suitable variant for a specific problem.

### Types of Binary Trees


There are various types of binary trees, and each of these binary tree types has unique characteristics.


#### Complete Binary Tree

A complete binary tree is a tree where all the tree levels are filled entirely with nodes, except the lowest level of the tree. Also, in the last or the lowest level of this binary tree, every node should possibly reside on the left side.


#### Perfect Binary Tree

A binary tree is said to be perfect if all the internal nodes have strictly two children, and every external or leaf node is at the same level or same depth within a tree.

A perfect binary tree having `height`  has `2n – 1` node.

#### Balanced Binary Tree

A binary tree is said to be ‘balanced’ if the tree height is `O(log n)`, where `n` is the number of nodes. In a balanced binary tree, the height of the left and the right subtrees of each node should vary by at most one.

An `AVL Tree` and a `Red-Black Tree` are some common examples of data structure that can generate a balanced binary search tree.

#### Height of Binary Tree

The height of the binary tree is the longest path from `root node` to any `leaf node` in the `tree`.

If there are `n` nodes in binary tree :

  - maximum height of the binary tree is `n-1`.
  - minimum height is `floor(log2(n))`

### Binary Search Tree Traversals


### Depth First Search Traversal

- 2 methods for `DFS` recursive or iterative.
- Iterative method use a stack (LIFO).
- Recursive method use stack-based memory.


- `In-order`

    - visit the `Left SubTree` then the `Root` then the `Right SubTree` recursively.
    - `In-order` traversal is used to retrieve data of binary search tree in sorted order.


- `Pre-Order`

    - visit the `Root` then `Left SubTree` then the `Right SubTree` recursively.
    - `Pre-Order` traversal is used to create a copy of the tree and is also used to get prefix expression of an expression tree.



- `Post-Order`

    - visit the `Left SubTree` then the `Right Sub Tree` and the `Root` recursively.
    - `Post-Order` traversal is used to delete the tree and is also used to get the postfix expression of an expression tree.


### Breadth First Search Traversal

- `BFS` use priority queue.
- Level Order Traversal.


### Delete a Node in a Binary Search Tree

Complexity : We have to find the `node` then we delete it or set it to `None`.
`O(log n)` find operation + `O(1)` deletion = `O(log n)`

#### 3 Cases:
- No children.
- One Child.
- Two children.

#### Method for Two Children case:

Two possible options: We look for the largest Node in the left subtree (Predecessor) or the smallest Node in the right subtree (Successor).

- Start at the Root, find the node to delete.
- Find Predecessor or Successor
- Replace Node to delete value with Predecessor value.
- Delete predecessor.


## Binary Heap

<p align="center">
  <img width="480" height="360" src="images\Heap_480_360.png">
</p>

A Binary Heap is a specialized Binary Search Tree data structure that satisfies the `heap property`.

A Binary Heap is define as a Binary Tree with two additional properties.

### Heap property

- A Binary Heap is a complete Binary Tree. Every level except possibly the last is completely filled.

### Heap ordering property

- `Min heap` : Each `node` is greater than or equal to its parent. `min` value is `root`.
- `Max heap` : Each `node` is less than or equal to its parent. `max` value is `root`.

Heaps are not sorted, considered "partially ordered".

### Priority Queues

- Almost always implement with a `heap`.
- Element with smaller numbers are higher priority.
- Element are inserted in `O(log n)` time.
- Ordering happens with each insertion, so the cost of ordering is distributed across insertion instead of in one big chunk.

#### Applications

Prioritizing data packets in routers.
Tracking unexplored routes in path-finding algorithms.
Bayesian spam filtering.
Data compression.
OS load Balancing, interrupt handling.

`Height = log(n + 1) - 1`
ex : if a Tree has 15 `node` : `log(15 + 1) - 1 = 4 - 1 = 3`

#### Array representation

Place values into array following level-order traversal.

- Left child index : `2n + 1`
- Right child index : `2n + 2`
- Parent index : `(n - 1) / 2`

Array implementation use less memory.(no node class require)
Can sort an array `in-place`.(Heapsort)

Insert element :
- Insert at next available space.
- `Shift up` or `bubble up`.
- Swap with parent until fulfills the ordering property.(trickle up) Fix heap violation.

Remove element :

- Replace `root` with `last element`.
- `Shift down` (aka sink).
- Swap with smallest child (`min`) or largest child (`max`) until fulfills the ordering property.

Other methods

- `peek` : find-min or find-max.
- `size` : return the numbers of elements

## Building the Heap

- first we insert the data to the heap and we check wether the heap properties are met.
- if the heap properties are violated, we reconstruct the heap in order to make it a valid heap.(heapify process)

- it is `O(n` process to construct a heap.
- if heap properties are violated it takes `O(log n)` to heapify.
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

`Input`: an array usually unsorted, unordered.
`Output`: an array that satisfies the heap property.

Balancing a heap is done by sift-up or sift-down operations (swapping elements which are out of order)

## Heapsort

Heap sort algorithm is a sorting technique that is based exclusively upon a binary heap data structure. It involves finding the largest (maximum) element, and sorting it at the end of an unsorted collection.

Python has a `heapq` module that implements a priority queue using a binary heap.

Time Complexity: `O(n log n)`
Space Complexity: `O(n)`

## AVL Tree

An `AVL Tree` is a self balancing Binary Search Tree. It is named after Adalson-Velskii and Landis.(1962)

This type of tree will adjust itself in order to maintain a low (logarithmic) height allowing for faster operations such as insertions and deletions.

AVL Tree Time Complexity:

|Operation                   |Average  |  Worst  |
|----------------------------|---------|---------
|Search                      |`O(log n)`|`O(log n)`|
|Insert                      |`O(log n)`|`O(log n)`|
|Delete                      |`O(log n)`|`O(log n)`|
|Remove                      |`O(log n)`|`O(log n)`|

For every node, height of the left and right children differ by at most +-1.

Balance Factor(Node) = Height(RightSubTree) - Height(LeftSubTree)

Each node store its height.

Height of a node: length of the longest path from it to a leaf.

The running time of BST operations depends on the height of the binary search tree. The tree should be balanced in order to get the best performance.

### Tree Rotations

The secret ingredient to most AVL Tree (Balanced Binary Search Tree) algorithms is the clever usage of a tree invariant and tree rotations.

A tree invariant is a property or rule you impose on your tree that it must meet after every operation. To ensure that the invariant is always satisfied a series of tree rotations are normally applied.

#### In-Order invariance

The tree rotation renders the in-order traversal of the binary tree invariant. This implies the order of the elements are not affected when a rotation is performed in any part of the tree.

## Graph

Graphs are mathematical structures that represent pairwise relationships between objects. A graph is an abstract data structure that represents the relationship between various objects.

A Graph is a pair V, E, where V is a set of Nodes called Vertices, and E is a collection of connections between Vertices called Edges or Links.

Definition:

  - `G = (V, E)`

  `V` is a set of Vertices or Nodes.(number of Vertices)
  `E` is a set of Edges or Links.(number of connections)



There are tree types of graphs: Directed, Undirected and Weighted.

#### Vocabulary

__Edges:__ Represent the connection between two Vertices.

__Vertices:__ Nodes in the graph.

__Path:__ A sequence of connected Vertices.

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
We visit the neighbors the the neighbors of these new Vertices and so on.

Time complexity : O(V + E)
Memory complexity is not good. We have to store a lot of references. O(N)

#### Depth First Search

- Internally this Algorithm uses a Stack.

It explores as far as possible along each branch before backtracking.

There are three main traversal orders that you’ll come across for graph traversal:

PreOrder : Each vertex is added to the visited list and added to the output list BEFORE getting added to the Stack.
PostOrder : Each vertex is added to the visited list and added to the output list AFTER it is popped off the Stack.
Reverse PostOrder (also known as Topological Sort): Which returns an output list that is exactly the reverse of the post-order list.

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
- Floyd-Warshall algorithm
- Bellman-Ford algorithm
- A* Search algorithm

## Dijkstra algorithm

- It was invented by computer scientist Edsger Dijkstra in 1956.
- This is the fastest know single source shortest path algorithm for arbitrary directed graphs with unbounded non-negative weights.

- It uses greedy method: Always pick the next closest vertex to the source.
- It uses priority queue lo store unvisited vertices by distance from s.
- It does not work with negative weights.

#### Difference between Unweighted Shortest Path and Dijkstra's Algorithm

- To represent weights in the adjacency list, each vertex contains the weights of the edges (in addition to their identifier).

- Instead of ordinary queue we use priority queue (distances are the priorities) and the vertex with the smallest distance is selected for processing.

- The distance to a vertex is calculated by the sum of the weights of the edges on the path from the source to that vertex.

- We update the distances in case the newly computed distance is smaller than the old distance which we have already computed.

Time Complexity : `O(V * Log(V) + E)`

__Pseudo code__

1 - Find the cheapest unvisited node reachable.

2 - Mark it as visited and keep track on which nodes you can visit from it.

3 - Repeat.

Dijkstra algorithm find the fastest path.

Breadth-first search find the path with the fewest segments.

## Bellman-Ford

The Bellman-Ford algorithm is an algorithm that computes shortest paths from a single source vertex to all of the other vertices in a weighted directed graph.


It was invented in 1958 by Bellman Ford respectively.


Slower than Dijkstra's but more robust. It can handle negative edge weight.

If the graph has negative edge costs, then Dijkstra's algorithm cannot work. The problem is that once a vertex `u` is declared known, it is possible that from some other unknown vertex `v` there is a path back t o `u` that is negative. In such case, taking a path from `s` to `v` back to `u` is better than going from `s` to `u` without using `v`.

Finding negative cycles can be useful in many types of application.

The Bellman-Ford algorithm, uses the principle of relaxation to find increasingly accurate path length.

Relaxation is the most important step in Bellman-Ford. It is what increases the accuracy of the distance to any given vertex. Relaxation works by continuously shortening the calculated distance between vertices comparing that distance with other known distances.

The detection of negative cycles is important, but the main contribution of this algorithm is in its ordering of relaxations. Dijkstra's algorithm is a greedy algorithm that selects the nearest vertex that has not been processed. Bellman-Ford, on the other hand, relaxes all of the edges.


Time Complexity : `O (V * E)`
