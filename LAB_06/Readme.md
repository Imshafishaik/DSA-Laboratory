LAB-06                         Advanced Algorithms and Programming                             Team - 23
--------------------------------------------------------------------------------------------------------

Team Members :- Shaik Shafi & Anshul Reddy


-------------------------Exercise 1 done by shafi-------------------------

Logic & Approach

A social network is modelled as an undirected graph where each user is a
vertex and each friendship is an edge. Two representations are implemented
simultaneously inside one SocialGraph class:
Adjacency Matrix: a 2D boolean array of size N×N. matrix[u][v] = True means
u and v are friends. Fast for checking if two specific users are friends (O(1)),
but wastes memory when friendships are sparse.
Adjacency List: a dictionary mapping each user to a set of their friends.
Memory-efficient for sparse graphs (most real social networks). Slower for
checking if two users are friends (O(degree)).
Both representations are kept in sync — every add_friendship and
remove_friendship updates both simultaneously.

Complexity Analysis Answers:

Q1. What is the time complexity of are_friends(u, v) in each representation?
Prove it.

Ans. Time complexity of are_friends(u, v):
Adjacency Matrix: O(1) - direct array index lookup matrix[u][v], no traversal
needed.
Adjacency List: O(degree(u)) in the worst case if using a list, O(1) average if
using a hash set (Python set). In the worst case (very high-degree node), it is
O(n).
Proof for matrix: accessing matrix[u][v] is a single memory read at offset u * n +
v. No loop, no comparison chain. Constant time regardless of n.


Q2. For a social network with 1 billion users where average user has 150
friends, which representation is more space-efficient? Calculate the exact
memory difference.

Ans. Memory comparison for 1 billion users, average degree 150:
Adjacency Matrix: stores N² bits -> 10⁹ × 10⁹ bits = 10¹⁸ bits = 125,000
terabytes. Completely impractical.
Adjacency List: stores 2 × |E| entries = 2 × (N × avg_degree / 2) = N × 150 =
150 × 10⁹ entries. At 8 bytes per integer -> ~1.2 terabytes. Manageable with
distributed storage.
The adjacency list uses roughly 100 million times less memory for this use
case.



Q3. If you need to frequently add/remove friendships, which representation
is better? Why?

Ans. For Add/remove friendships:
Adjacency List is better. Adding or removing a friendship requires
inserting/deleting from two sets - O(1) average with hash sets. With the matrix
you also update two cells (O(1)), so both are technically O(1), but the list has
better cache locality and does not require N² pre-allocated memory.


-------------------------Exercise 2 done by Anshul-------------------------

DFS explores as deep as possible along each branch before backtracking. In a social network this means: starting from a user, visit one of their friends, then one of that friend's friends, going as deep as possible before coming back. This naturally finds all users reachable from a starting point (a connected component), detects if a path exists, and finds the actual path. 

Recursive DFS: uses the call stack. Clean and readable but risks RecursionError on deep graphs (Python default stack limit ~1000). 

Iterative DFS: uses an explicit stack (a Python list). Same traversal order, no recursion limit, safe for any size. 

Connected components: run DFS from every unvisited user. Each DFS call discovers one complete component. 

Complexity Analysis Answers: 
 
Q1 What is the time and space complexity of DFS on an adjacency list representation? On adjacency matrix? 

Ans. Time and space complexity of DFS: 
Adjacency List: O(V + E) time — each vertex is visited once (O(V)) and each edge is examined once from each endpoint (O(E)). Space: O(V) for the visited set and stack. 
Adjacency Matrix: O(V²) time — for each vertex, scanning its entire row to find neighbors costs O(V), and this happens for all V vertices. Space: O(V) for visited and stack. 
The adjacency list is strictly better for sparse graphs (where E << V²). 
 
Q2. Why might recursive DFS cause problems in a social network with 1 million users? How would you solve it? 
 
Ans. use iterative DFS with an explicit stack (as implemented above), or increase the limit with sys.setrecursionlimit() (risky — can crash the Python process by exhausting OS stack memory). 