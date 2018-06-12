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

## Basic Operations on Linked List

- Add value to Head/Tail
- Add value at specific index
- Remove value
- Find value
- Create list from Linked List
- Reverse the Linked List

## Linked List vs Array

Linked List are preferable:
- You need Insertion / Deletion in the list to be extremely fast.
- You Insert / Delete items in the middle of the list.
- You can’t evaluate the size of the list, it needs to grow
or shrink throughout the execution.

Array are preferable over Linked List:
- You frequently need random, unordered access to the data.
- You need extreme performance to access the items.
- The number of items doesn't change during execution, so you can easily allocate contiguous space of computer memory.

## Stack
A stack is a simple data structure used for storing data.

The last element inserted is the first one to be deleted. Last in, First out (LIFO).


Linked List implementation of a Stack.


|Operation                   |Big O  |
|----------------------------|-------|
|Push value                  |O(1)   |
|Pop value                   |O(1)   |
|Size                        |O(1)   |


### Basic Operations on Stack

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

### Basic Operations on Queue

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

The number of nodes n in a full binary tree is (2^h + 1) - 1.

Since, there are h levels we need to add all nodes at each level [ 2^0 + 2^1 + 2^2 + ... + 2^h = (2^h + 1) - 1].

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

Worst case scenarios :

If the Tree become unbalanced then the operations running times can be reduced to O(n).


### Binary Search Tree Traversals:


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

### Heap property :

- A Binary Heap is a complete Binary Tree. Every level except possibly the last is completely filled.

### Heap ordering property :

- Min heap : Each node is greater than or equal to its parent(min value is root).

- Max heap : Each node is less than or equal to its parent(max value is root).





## Graph

Graphs are mathematical structures that represent pairwise relationships between objects. A graph is an abstract data structure that represents the relationship between various objects.

A Graph is a pair V, E, where V is a set of Nodes called Vertices, and E is a collection of connections between vertices called Edges or Arcs.


There are tree types of graphs: Directed, Undirected and Weighted.

#### Vocabulary

##### Edges :
Represent the connection between two vertices.
##### Vertices :
Nodes in the graph
##### Path :
A sequence of connected vertices.
##### Cycles :
A path that is cyclical.


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

#### Undirected Graph :
An undirected graph is a graph in which all the edges are bi-directional i.e. the edges do not point in any specific direction.

#### Directed Graph :
A directed graph is a graph in which all the edges are uni-directional i.e. the edges point in a single direction.

#### Weighted Graph :
In a weighted graph, each edge is assigned a weight or cost.

### Graph representation

There are three common way to represent graph:
  - Adjacency Matrix
  - Adjacency List
  - Edge List

### Adjacency Matrix

An adjacency matrix is a VxV binary matrix.

A binary matrix is a matrix in which the cells can have only one of two possible values. 0 or 1.(Undirected Graph)

For Directed Graph we use tree possible values. 0, 1 or -1.

Adjacency matrix provides constant time access O(1) to determine if there is an edge between two nodes.

Space complexity of the adjacency matrix is O(V**2).

Pro : Faster for dense Graph. Simpler for Weighted Graph.

Con : Uses more space.

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

### Graph Traversals:

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

1 - Find the cheapest unvisited node reachable.

2 - Mark it as visited and keep track on which nodes you can visit from it.

3 - Repeat.

Dijkstra algorithm find the fastest path.

Breadth-first search find the path with the fewest segments.
