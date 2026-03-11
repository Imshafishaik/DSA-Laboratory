LAB-03                         Advanced Algorithms and Programming                             Team - 23
--------------------------------------------------------------------------------------------------------

Team Members :- Shaik Shafi & Anshul Reddy

-------------------------Exercise 1 done by shafi-------------------------

Logic Explanation:
The story content system utilizes a doubly linked list to create a swipeable
story feed. Each story is a StoryNode containing its information and pointers to
the next and Prev stories. The Story Feed manages the list with head, tail,
current viewing position, and size. New stories are added to the tail to maintain
chronological order. Navigation is simple: moving forward shifts the current
pointer to current.next, and moving backward shifts it to current.prev.

Complexity Analysis Answers

Q1. Compare forward/backward navigation complexity
----------------------------------------------------------
      Structure           Forward              Backward.  |
   Singly Linked List      O(1)                  O(n).    |
   Doubly Linked List      O(1)                  O(1).    |
----------------------------------------------------------

Explanation:
Singly linked lists only store a next pointer, so moving backward requires
traversing from the head.
Doubly linked lists store both next and previous pointers, allowing constant-
time backward traversal.


Q2. Time complexity of removing a node with pointer
O(1)
Explanation:
If we already have the pointer to the node, we only update:
prev.next = next
next.prev = prev
No traversal is required.


Q3. Extra memory required
A doubly linked list stores:
data + next pointer + prev pointer
A singly linked list stores:
data + next pointer
Thus, 1 extra pointer per node is required.


Q4. When bidirectional navigation is useful
Examples include:
• Social media feeds
• Browser history
• Music playlist navigation
• Image galleries
• Undo/redo systems
These systems frequently move both forward and backward, making doubly
linked lists beneficial.



